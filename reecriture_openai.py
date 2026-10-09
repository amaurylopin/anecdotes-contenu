#!/usr/bin/env python3
"""
reecriture_openai.py — réécriture par IA (OpenAI) des fiches communes, par ordre de population,
dans la limite d'un budget, avec reprise et contrôles qualité.

Prérequis : pilote_openai.py dans le MÊME dossier (ce script en réutilise le code) et la clé API dans
~/.openai_env (ligne OPENAI_API_KEY=...) ou dans la variable d'environnement OPENAI_API_KEY.

Usage :
  python3 reecriture_openai.py --simulation --limite 5     # aucun appel, aucun coût
  python3 reecriture_openai.py --limite 20                 # vrai test sur les 20 plus grandes communes
  python3 reecriture_openai.py                             # production jusqu'à épuisement du budget
  python3 reecriture_openai.py --bilan                     # état d'avancement et dépenses

Les fiches V1 ne sont jamais modifiées. Résultats : ~/anecdotes/contenu_ia/<dept>/<code>-<slug>.json
Relancer la même commande reprend là où le script s'est arrêté.
"""

import argparse
import json
import re
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pilote_openai as po

CONSIGNES_PROD = """Tu es un conteur d'histoire locale français : précis, vivant, jamais bavard.
Règles absolues :
1. Utilise UNIQUEMENT les SOURCES numérotées fournies. N'utilise AUCUNE connaissance extérieure : un fait, un nom, un chiffre ou une année que tu connais mais qui ne figure pas dans les sources doit être ignoré. N'écris aucune année absente des sources.
2. Chaque élément de chronologie, chaque anecdote et chaque lieu cite ses sources par identifiant (ex. "S3") dans les champs "sources".
3. N'écris JAMAIS d'identifiant de source dans les textes (pas de « (S2) », pas de « S3 »). Relis et corrige l'orthographe, les accords et la grammaire.
4. Une anecdote est un détail curieux, une légende, une tradition ou un fait surprenant rapporté par une source. Un simple fait historique n'est PAS une anecdote : place-le dans l'histoire. S'il n'y a aucune anecdote dans les sources, laisse la liste vide.
5. Statut d'une anecdote : "etabli" si la source l'affirme comme un fait ; "tradition_locale" ou "legende" si la source la présente comme telle ; "conteste" si la source signale un désaccord. En cas de doute, choisis "tradition_locale".
6. Si les sources ne permettent pas d'écrire un champ, laisse une chaîne vide ou une liste vide : n'invente jamais.
7. Pour "lieux", utilise UNIQUEMENT les noms de la liste LIEUX AUTORISÉS, écrits exactement comme dans la liste. "a_voir_aujourdhui" n'est rempli que si une source décrit une trace actuelle.
8. Accroche : UNE seule phrase (30 mots maximum) qui cite un fait précis tiré des sources (un nom, une date, un lieu). Interdits : « les pierres racontent », « garde la mémoire », « au fil des siècles » et toute image vague. Si aucune source ne permet une accroche précise, écris une phrase simple qui présente la commune.
9. Style : français, ton de conteur vivant et exact. Histoire de la commune ≤ 250 mots, histoire d'un lieu ≤ 120 mots, anecdote ≤ 60 mots. Pas de formule creuse ni de superlatif non sourcé."""

ACCROCHE_INTERDITE = re.compile(r"(?i)pierres?\s+(racont|gard|ont chang)|garde la m[ée]moire|au fil des si[èe]cles|m[ée]moire de la pierre")


class Registre:
    """Dépenses cumulées, sûres entre plusieurs traitements en parallèle et entre plusieurs lancements."""

    def __init__(self, dossier, plafond):
        self.dossier = Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.fichier = self.dossier / "depenses.json"
        self.journal = self.dossier / "appels.jsonl"
        self.plafond = plafond
        self.verrou = threading.Lock()
        self.reserve = 0.0
        self.total = 0.0
        self.nb = 0
        if self.fichier.exists():
            d = json.loads(self.fichier.read_text(encoding="utf-8"))
            self.total, self.nb = d.get("total_usd", 0.0), d.get("nb_appels", 0)

    def reserver(self, pire):
        with self.verrou:
            if self.total + self.reserve + pire > self.plafond:
                return False
            self.reserve += pire
            return True

    def annuler(self, pire):
        with self.verrou:
            self.reserve = max(0.0, self.reserve - pire)

    def regler(self, pire, modele, commune, tin, tout, cout):
        with self.verrou:
            self.reserve = max(0.0, self.reserve - pire)
            self.total = round(self.total + cout, 6)
            self.nb += 1
            with open(self.journal, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"date": time.strftime("%Y-%m-%d %H:%M:%S"), "modele": modele, "commune": commune,
                                     "tokens_entree": tin, "tokens_sortie": tout, "cout_usd": round(cout, 6)},
                                    ensure_ascii=False) + "\n")
            tmp = self.fichier.with_suffix(".tmp")
            tmp.write_text(json.dumps({"total_usd": self.total, "nb_appels": self.nb}), encoding="utf-8")
            tmp.replace(self.fichier)

    @property
    def restant(self):
        return self.plafond - self.total


class CacheGeo:
    """Commune qui contient des coordonnées (API officielle geo.api.gouv.fr), avec cache sur disque."""

    def __init__(self, fichier, actif=True):
        self.fichier = Path(fichier)
        self.actif = actif
        self.verrou = threading.Lock()
        self.data = {}
        self.nouveaux = 0
        if self.fichier.exists():
            try:
                self.data = json.loads(self.fichier.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self.data = {}

    @staticmethod
    def interroger(lat, lon):
        """Code INSEE de la commune au point donné ; None si l'API est injoignable ; '' si hors commune."""
        url = f"https://geo.api.gouv.fr/communes?lat={lat}&lon={lon}&fields=code&format=json"
        for essai in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "pilote-anecdotes/0.1"})
                with urllib.request.urlopen(req, timeout=15) as rep:
                    liste = json.load(rep)
                return liste[0]["code"] if liste else ""
            except (OSError, ValueError, KeyError, IndexError):
                time.sleep(1 + essai)
        return None

    def commune_de(self, lat, lon):
        if not self.actif:
            return None
        cle = f"{round(float(lat), 4)},{round(float(lon), 4)}"
        with self.verrou:
            if cle in self.data:
                return self.data[cle]
        code = self.interroger(lat, lon)
        if code is not None:
            with self.verrou:
                self.data[cle] = code
                self.nouveaux += 1
                if self.nouveaux % 50 == 0:
                    self.sauver()
        return code

    def sauver(self):
        tmp = self.fichier.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data), encoding="utf-8")
        tmp.replace(self.fichier)


def lieux_de_la_commune(d, geo):
    """Écarte les lieux situés dans une autre commune. En cas de doute (API injoignable, hors commune), on garde."""
    code = (d.get("commune") or {}).get("code_insee")
    lieux = sorted(d.get("lieux") or [], key=lambda l: -l.get("score", 0))[:14]
    if not code:
        return lieux, 0
    gardes, ecartes = [], 0
    for l in lieux:
        if l.get("lat") is None or l.get("lon") is None:
            gardes.append(l)
            continue
        c = geo.commune_de(l["lat"], l["lon"])
        if c and c != code:
            ecartes += 1
            continue
        gardes.append(l)
    return gardes, ecartes


def appeler_modele(cle, modele, dossier_txt, max_sortie, registre, commune, correction=None):
    contenu = dossier_txt + (f"\n\nCORRECTION DEMANDÉE : ta réponse précédente contenait des défauts : {correction}. "
                             "Réécris-la en les supprimant, sans rien ajouter qui ne soit dans les sources." if correction else "")
    messages = [{"role": "system", "content": CONSIGNES_PROD}, {"role": "user", "content": contenu}]
    p_in, p_out = po.prix_modele(modele)
    pire = (po.estimer_tokens(CONSIGNES_PROD + contenu) * p_in + max_sortie * p_out) / 1_000_000
    if not registre.reserver(pire):
        raise po.ArretBudget(f"Budget atteint : dépensé {registre.total:.4f} $ sur {registre.plafond:g} $.")
    corps = {"model": modele, "messages": messages, "max_completion_tokens": max_sortie,
             "response_format": {"type": "json_schema",
                                 "json_schema": {"name": "fiche_commune", "strict": True, "schema": po.SCHEMA}}}
    try:
        rep = po.appeler_api(_CLE_API[0], corps)
    except Exception:
        registre.annuler(pire)
        raise
    usage = rep.get("usage", {})
    tin, tout = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
    cout = po.cout_appel(modele, tin, tout)
    registre.regler(pire, modele, commune, tin, tout, cout)
    choix = rep["choices"][0]
    message = choix.get("message", {})
    res = {"tokens_entree": tin, "tokens_sortie": tout, "cout": cout, "sortie": None, "erreur": None}
    if message.get("refusal"):
        res["erreur"] = "refus du modèle : " + po.masquer(message["refusal"])[:200]
    elif choix.get("finish_reason") == "length":
        res["erreur"] = "réponse tronquée (max_completion_tokens atteint)"
    else:
        try:
            res["sortie"] = json.loads(message.get("content") or "")
        except ValueError:
            res["erreur"] = "réponse non conforme (JSON invalide)"
    return res


def appeler_modele_factice(cle, modele, dossier_txt, max_sortie, registre, commune, correction=None):
    tin = po.estimer_tokens(CONSIGNES_PROD + dossier_txt)
    tout = 900
    cout = po.cout_appel(modele, tin, tout)
    pire = cout
    registre.reserver(pire)
    registre.regler(pire, modele, commune, tin, tout, cout)
    noms = re.findall(r"LIEUX AUTORISÉS \(noms exacts\) : (.*)", dossier_txt)
    lieux = [{"nom": n.strip(), "histoire": "(simulation)", "anecdotes": [], "a_voir_aujourdhui": "", "sources": ["S1"]}
             for n in (noms[0].split("|") if noms and "(aucun)" not in noms[0] else [])]
    sortie = {"accroche": "(simulation)", "histoire": {"recit": "(simulation)", "chronologie": []}, "lieux": lieux}
    return {"tokens_entree": tin, "tokens_sortie": tout, "cout": cout, "sortie": sortie, "erreur": None}


_CLE_API = [""]


def lister_problemes(res, sources, lieux_ok):
    if res["erreur"]:
        return [res["erreur"]], None
    c = po.verifier(res["sortie"], sources, lieux_ok)
    pb = []
    if c["identifiants_dans_texte"]:
        pb.append("identifiants de sources (S1, S2…) écrits dans les textes")
    if c["sources_inconnues"]:
        pb.append("sources inexistantes citées : " + ", ".join(c["sources_inconnues"]))
    if c["annees_hors_dossier"]:
        pb.append("années absentes des sources : " + ", ".join(c["annees_hors_dossier"]))
    if ACCROCHE_INTERDITE.search(res["sortie"].get("accroche", "")):
        pb.append("accroche vague (« les pierres racontent », « au fil des siècles »…) : cite un fait précis")
    return pb, c


def chemin_sortie(sortie, x):
    return Path(sortie) / x["chemin"].parent.name / x["chemin"].name


def ecrire(chemin, enreg):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tmp = chemin.with_suffix(".tmp")
    tmp.write_text(json.dumps(enreg, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(chemin)


def traiter(x, ctx):
    d = json.loads(Path(x["chemin"]).read_text(encoding="utf-8"))
    d = dict(d)
    d["lieux"], nb_ecartes = lieux_de_la_commune(d, ctx["geo"])
    dossier_txt, sources, lieux_ok = po.construire_dossier(d)
    c = d.get("commune", {})
    base = {"commune": {k: c.get(k) for k in ("titre", "code_insee", "departement", "population", "lat", "lon", "url")},
            "modele": ctx["modele"], "genere_le": time.strftime("%Y-%m-%d %H:%M:%S"),
            "lieux_ecartes_autre_commune": nb_ecartes,
            "licence": "Textes d'origine : Wikipédia (CC BY-SA 4.0), réécrits par IA à partir des sources listées."}
    chemin = chemin_sortie(ctx["sortie"], x)
    pauvre = len(sources) < 3 or (not d.get("frise") and len(d.get("histoire_extrait", "")) < 300 and not d.get("lieux"))
    if pauvre:
        ecrire(chemin, {**base, "statut_qualite": "insuffisant", "contenu_insuffisant": True})
        return {"statut": "insuffisant", "cout": 0.0, "essais": 0}
    generer = ctx["generer"]
    res = generer(ctx["cle"], ctx["modele"], dossier_txt, ctx["max_sortie"], ctx["registre"], x["titre"])
    cout, essais = res["cout"], 1
    problemes, controles = lister_problemes(res, sources, lieux_ok)
    if problemes and not ctx["stop"].is_set():
        res2 = generer(ctx["cle"], ctx["modele"], dossier_txt, ctx["max_sortie"], ctx["registre"], x["titre"],
                       correction="; ".join(problemes))
        cout += res2["cout"]
        essais = 2
        pb2, c2 = lister_problemes(res2, sources, lieux_ok)
        if res2["sortie"] is not None or res["sortie"] is None:
            res, problemes, controles = res2, pb2, c2
    if res["sortie"] is None:
        ecrire(chemin, {**base, "statut_qualite": "echec", "problemes": problemes, "essais": essais,
                        "cout_usd": round(cout, 6)})
        return {"statut": "echec", "cout": cout, "essais": essais}
    par_nom = {po.norm(l["titre"]): l for l in lieux_ok}
    gardes = []
    for l in res["sortie"].get("lieux", []):
        ref = par_nom.get(po.norm(l.get("nom", "")))
        if ref:  # coordonnées de la fiche V1 ; les lieux hors liste sont écartés
            l.update({"lat": ref["lat"], "lon": ref["lon"], "url": ref["url"]})
            gardes.append(l)
    statut = "ok" if not problemes else "a_relire"
    ecrire(chemin, {**base, "statut_qualite": statut, "problemes": problemes, "essais": essais,
                    "tokens": {"entree": res["tokens_entree"], "sortie": res["tokens_sortie"]},
                    "cout_usd": round(cout, 6), "accroche": res["sortie"].get("accroche", ""),
                    "histoire": res["sortie"].get("histoire", {}), "lieux": gardes, "sources": sources,
                    "controles": controles})
    return {"statut": statut, "cout": cout, "essais": essais}


def bilan(sortie, registre):
    comptes, cout = {}, 0.0
    for p in Path(sortie).glob("[0-9]*/*.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        comptes[d.get("statut_qualite", "?")] = comptes.get(d.get("statut_qualite", "?"), 0) + 1
        cout += d.get("cout_usd", 0) or 0
    print(f"Fiches réécrites : {sum(comptes.values())}  " + ", ".join(f"{k} : {v}" for k, v in sorted(comptes.items())))
    print(f"Dépensé : {registre.total:.4f} $ sur {registre.plafond:g} $ (reste {registre.restant:.4f} $), {registre.nb} appels")
    if comptes.get("ok") or comptes.get("a_relire"):
        n = comptes.get("ok", 0) + comptes.get("a_relire", 0)
        print(f"Coût moyen par fiche réécrite : {cout / n:.5f} $")


def main():
    ap = argparse.ArgumentParser(description="Réécriture par IA des fiches communes, budget plafonné, avec reprise.")
    ap.add_argument("--source", default=str(Path.home() / "anecdotes" / "contenu"), help="Dossier des fiches V1")
    ap.add_argument("--sortie", default=str(Path.home() / "anecdotes" / "contenu_ia"), help="Dossier des fiches réécrites")
    ap.add_argument("--plafond", type=float, default=4.0, help="Plafond de dépense cumulée, en dollars (défaut : 4,0)")
    ap.add_argument("--modele", default="gpt-5.4-nano")
    ap.add_argument("--workers", type=int, default=2, help="Appels en parallèle (1 à 4)")
    ap.add_argument("--limite", type=int, help="Ne traiter que les N premières communes à faire (test)")
    ap.add_argument("--max-sortie", type=int, default=5000, help="Tokens de sortie maximum par appel")
    ap.add_argument("--prix", action="append", default=[], help="modele=entree,sortie ($/million de tokens)")
    ap.add_argument("--refaire-echecs", action="store_true", help="Retenter les fiches marquées en échec")
    ap.add_argument("--simulation", action="store_true", help="Aucun appel API ni coût ; écrit dans <sortie>_simulation")
    ap.add_argument("--bilan", action="store_true", help="Afficher l'état d'avancement et les dépenses")
    ap.add_argument("--oui", action="store_true", help="Ne pas demander de confirmation")
    args = ap.parse_args()

    for p in args.prix:
        nom, valeurs = p.split("=", 1)
        entree, sortie = valeurs.split(",")
        po.PRIX[nom.strip()] = (float(entree), float(sortie))
    po.prix_modele(args.modele)

    sortie = args.sortie + ("_simulation" if args.simulation else "")
    registre = Registre(sortie, args.plafond)
    if args.bilan:
        bilan(sortie, registre)
        return

    if not args.simulation:
        cle = po.charger_cle()
        _CLE_API[0] = cle
        disponibles = {m["id"] for m in po.requete("GET", "/models", cle).get("data", [])}
        if args.modele not in disponibles:
            proches = sorted(i for i in disponibles if i.startswith("gpt") and ("nano" in i or "mini" in i))
            sys.exit(f"Modèle indisponible pour votre clé : {args.modele}. Proches : {', '.join(proches[:15])}")
    else:
        cle = ""

    print("Lecture des fiches V1…")
    index = sorted(po.indexer(args.source), key=lambda x: -x["pop"])
    if not index:
        sys.exit(f"Aucune fiche trouvée dans {args.source}.")

    def deja_fait(x):
        p = chemin_sortie(sortie, x)
        if not p.exists():
            return False
        if args.refaire_echecs:
            try:
                return json.loads(p.read_text(encoding="utf-8")).get("statut_qualite") != "echec"
            except (OSError, ValueError):
                return False
        return True

    a_faire = [x for x in index if not deja_fait(x)]
    if args.limite:
        a_faire = a_faire[: args.limite]
    print(f"{len(index)} fiches V1, {len(index) - len([x for x in index if not deja_fait(x)])} déjà réécrites, "
          f"{len(a_faire)} à traiter (par population décroissante).")
    print(f"Modèle {args.modele}, prix {po.PRIX[args.modele]} $/M tokens (à vérifier sur la page officielle). "
          f"Budget restant : {registre.restant:.4f} $ — le script s'arrête tout seul quand il est épuisé.")
    if not a_faire:
        return
    if not args.simulation and not args.oui:
        if input("Lancer ? [o/N] ").strip().lower() not in ("o", "oui", "y", "yes"):
            sys.exit("Abandon.")

    ctx = {"cle": cle, "modele": args.modele, "max_sortie": args.max_sortie, "registre": registre, "sortie": sortie,
           "generer": appeler_modele_factice if args.simulation else appeler_modele, "stop": threading.Event(),
           "geo": CacheGeo(Path(sortie) / "_geo_cache.json", actif=not args.simulation)}
    compteur = {"n": 0}
    verrou = threading.Lock()

    def travail(x):
        if ctx["stop"].is_set():
            return
        try:
            r = traiter(x, ctx)
        except (po.ArretBudget, po.ArretApi) as err:
            ctx["stop"].set()
            with verrou:
                print(f"\nARRÊT : {po.masquer(err)}")
            return
        except Exception as err:  # une commune en erreur ne doit pas arrêter les autres
            with verrou:
                print(f"  ! {x['titre']} : {po.masquer(err)}")
            return
        with verrou:
            compteur["n"] += 1
            print(f"[{compteur['n']}] {x['code']} {x['titre']} — {r['statut']}"
                  + (f" ({r['essais']} essais)" if r["essais"] > 1 else "")
                  + f" {r['cout']:.5f} $ | total {registre.total:.4f} $ / {registre.plafond:g} $")

    try:
        with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 4))) as ex:
            list(ex.map(travail, a_faire))
    except KeyboardInterrupt:
        ctx["stop"].set()
        print("\nInterruption : les fiches terminées sont conservées. Relancez la même commande pour reprendre.")
    ctx["geo"].sauver()
    print()
    bilan(sortie, registre)


if __name__ == "__main__":
    main()
