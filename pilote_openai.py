#!/usr/bin/env python3
"""
pilote_openai.py — pilote de réécriture par IA (API OpenAI) sur 10 communes, budget plafonné.

Il lit les fiches V1 déjà générées (~/anecdotes/contenu), construit pour chaque commune un dossier de
sources numérotées, demande à l'IA de réécrire en ton de conteur SANS rien ajouter, vérifie le résultat
automatiquement, mesure tokens et coûts, puis écrit un rapport et une projection pour toute la France.

Sécurité : la clé API n'est lue que dans la variable d'environnement OPENAI_API_KEY ou dans le fichier
~/.openai_env (ligne OPENAI_API_KEY=...). Elle n'est jamais affichée ni écrite.

Étapes conseillées :
  1) python3 pilote_openai.py --simulation          (aucun appel, aucun coût : montre le plan)
  2) python3 pilote_openai.py --lister-modeles      (vérifie les noms de modèles disponibles)
  3) python3 pilote_openai.py                       (vrai pilote, avec confirmation)

Aucune dépendance externe (bibliothèque standard, Python 3.9+).
"""

import argparse
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"

# Dollars par million de tokens (entrée, sortie). À VÉRIFIER sur la page officielle de tarification :
# on peut les corriger avec --prix modele=entree,sortie
PRIX = {
    "gpt-5.4-nano": (0.20, 1.25),
    "gpt-5.4-mini": (0.75, 4.50),
    "gpt-4.1-nano": (0.10, 0.40),
}
# Hypothèse de répartition des communes pour la projection (A grandes/riches, B moyennes, C petites)
PALIERS = {"A": 1000, "B": 4000, "C": 30000}
TAILLE_MAX_SOURCE = 420  # caractères par source, pour borner les tokens d'entrée

CONSIGNES = """Tu es un conteur d'histoire locale français : précis, vivant, jamais bavard.
Règles absolues :
1. Utilise UNIQUEMENT les SOURCES numérotées fournies. N'ajoute aucun fait, nom, date, chiffre ou lien absent des sources.
2. Chaque élément de chronologie, chaque anecdote et chaque lieu cite ses sources par identifiant (ex. "S3").
3. N'écris JAMAIS d'identifiant de source dans les textes (pas de « (S2) », pas de « S3 ») : ils vont uniquement dans les champs "sources". Relis et corrige l'orthographe, les accords et la grammaire.
4. Une anecdote est un détail curieux, une légende, une tradition ou un fait surprenant rapporté par une source. Un simple fait historique n'est PAS une anecdote : place-le dans l'histoire. S'il n'y a aucune anecdote dans les sources, laisse la liste vide.
5. Statut d'une anecdote : "etabli" si la source l'affirme comme un fait ; "tradition_locale" ou "legende" si la source la présente comme telle ; "conteste" si la source signale un désaccord. En cas de doute, choisis "tradition_locale".
6. Si les sources ne permettent pas d'écrire un champ, laisse une chaîne vide ou une liste vide : n'invente jamais.
7. Pour "lieux", utilise UNIQUEMENT les noms de la liste LIEUX AUTORISÉS, écrits exactement comme dans la liste. "a_voir_aujourdhui" n'est rempli que si une source décrit une trace actuelle.
8. Style : français, ton de conteur vivant et exact. Histoire de la commune ≤ 250 mots, histoire d'un lieu ≤ 120 mots, anecdote ≤ 60 mots. Pas de formule creuse ni de superlatif non sourcé."""

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["accroche", "histoire", "lieux"],
    "properties": {
        "accroche": {"type": "string"},
        "histoire": {
            "type": "object",
            "additionalProperties": False,
            "required": ["recit", "chronologie"],
            "properties": {
                "recit": {"type": "string"},
                "chronologie": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["date", "texte", "sources"],
                        "properties": {
                            "date": {"type": "string"},
                            "texte": {"type": "string"},
                            "sources": {"type": "array", "items": {"type": "string"}},
                        },
                    },
                },
            },
        },
        "lieux": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["nom", "histoire", "anecdotes", "a_voir_aujourdhui", "sources"],
                "properties": {
                    "nom": {"type": "string"},
                    "histoire": {"type": "string"},
                    "anecdotes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["texte", "statut", "sources"],
                            "properties": {
                                "texte": {"type": "string"},
                                "statut": {"type": "string",
                                           "enum": ["etabli", "tradition_locale", "legende", "conteste"]},
                                "sources": {"type": "array", "items": {"type": "string"}},
                            },
                        },
                    },
                    "a_voir_aujourdhui": {"type": "string"},
                    "sources": {"type": "array", "items": {"type": "string"}},
                },
            },
        },
    },
}


class ArretBudget(Exception):
    pass


class ArretApi(Exception):
    pass


# --------------------------------------------------------------------------- clé et réseau

_CLE = [""]


def masquer(texte):
    texte = str(texte)
    if _CLE[0]:
        texte = texte.replace(_CLE[0], "***")
    return re.sub(r"sk-[A-Za-z0-9_\-]{10,}", "sk-***", texte)


def charger_cle():
    cle = os.environ.get("OPENAI_API_KEY", "").strip()
    if not cle:
        fichier = Path.home() / ".openai_env"
        if fichier.exists():
            for ligne in fichier.read_text(encoding="utf-8").splitlines():
                ligne = ligne.strip()
                if ligne.startswith("export "):
                    ligne = ligne[7:]
                if ligne.startswith("OPENAI_API_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("'\"")
    if not cle:
        sys.exit("Clé introuvable. Mettez OPENAI_API_KEY=... dans ~/.openai_env (chmod 600) "
                 "ou dans la variable d'environnement OPENAI_API_KEY.")
    _CLE[0] = cle
    return cle


def requete(methode, chemin, cle, corps=None, timeout=180):
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(
        API + chemin, data=donnees, method=methode,
        headers={"Authorization": f"Bearer {cle}", "Content-Type": "application/json",
                 "User-Agent": "pilote-anecdotes/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as rep:
        return json.load(rep)


def appeler_api(cle, corps_base, efforts=("minimal", "low", None)):
    """POST /chat/completions avec adaptation automatique du paramètre de raisonnement et reprises."""
    corps = dict(corps_base)
    i, essais_429, essais_5xx = 0, 0, 0
    while True:
        if efforts[i]:
            corps["reasoning_effort"] = efforts[i]
        else:
            corps.pop("reasoning_effort", None)
        try:
            return requete("POST", "/chat/completions", cle, corps)
        except urllib.error.HTTPError as err:
            texte = masquer(err.read().decode("utf-8", "replace"))
            if err.code == 401:
                raise ArretApi("Clé refusée (401) : clé invalide, révoquée ou sans accès.")
            if err.code == 429:
                if "insufficient_quota" in texte:
                    raise ArretApi("Crédit épuisé ou quota insuffisant (insufficient_quota).")
                essais_429 += 1
                if essais_429 > 4:
                    raise ArretApi("Trop de refus 429 (limite de débit) : réessayez plus tard.")
                time.sleep(min(60, 5 * 2 ** essais_429))
                continue
            if err.code == 400 and "reasoning_effort" in texte and i < len(efforts) - 1:
                i += 1
                continue
            if err.code >= 500 and essais_5xx < 3:
                essais_5xx += 1
                time.sleep(5 * essais_5xx)
                continue
            raise ArretApi(f"Erreur API {err.code} : {texte[:300]}")
        except OSError as err:
            essais_5xx += 1
            if essais_5xx > 3:
                raise ArretApi(f"Réseau indisponible : {masquer(err)}")
            time.sleep(5 * essais_5xx)


# --------------------------------------------------------------------------- budget

def prix_modele(modele):
    if modele not in PRIX:
        sys.exit(f"Prix inconnu pour « {modele} » : ajoutez --prix {modele}=ENTREE,SORTIE "
                 "(dollars par million de tokens, voir la page officielle de tarification).")
    return PRIX[modele]


class Registre:
    """Dépenses cumulées du pilote, conservées sur disque : le plafond tient même après plusieurs lancements."""

    def __init__(self, chemin, plafond):
        self.chemin = Path(chemin)
        self.plafond = plafond
        self.data = {"total_usd": 0.0, "appels": []}
        if self.chemin.exists():
            self.data = json.loads(self.chemin.read_text(encoding="utf-8"))

    @property
    def total(self):
        return self.data["total_usd"]

    def peut_depenser(self, pire_cas):
        return self.total + pire_cas <= self.plafond

    def enregistrer(self, modele, commune, tin, tout, cout):
        self.data["total_usd"] = round(self.total + cout, 6)
        self.data["appels"].append({"date": time.strftime("%Y-%m-%d %H:%M:%S"), "modele": modele,
                                    "commune": commune, "tokens_entree": tin, "tokens_sortie": tout,
                                    "cout_usd": round(cout, 6)})
        tmp = self.chemin.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(self.chemin)


def cout_appel(modele, tin, tout):
    p_in, p_out = prix_modele(modele)
    return (tin * p_in + tout * p_out) / 1_000_000


# --------------------------------------------------------------------------- sélection et dossiers

def indexer(source):
    for chemin in sorted(Path(source).glob("[0-9]*/*.json")):
        try:
            d = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        c = d.get("commune", {})
        yield {
            "chemin": chemin, "titre": c.get("titre", ""), "code": c.get("code_insee", chemin.stem.split("-")[0]),
            "dept": str(c.get("departement", "")), "pop": c.get("population") or 0,
            "nb_lieux": len(d.get("lieux", [])), "nb_frise": len(d.get("frise", [])),
            "hist": len(d.get("histoire_extrait", "")),
        }


def choisir_communes(index, n, graine=42):
    rng = random.Random(graine)
    ok = [x for x in index if x["nb_frise"] >= 1 or x["hist"] >= 300]
    deja = set()

    def tirer(filtre, k, etiquette):
        pool = [x for x in ok if filtre(x) and x["code"] not in deja]
        rng.shuffle(pool)
        pris = pool[:k]
        for x in pris:
            deja.add(x["code"])
            x["strate"] = etiquette
        return pris

    choix = []
    choix += tirer(lambda x: x["pop"] >= 100_000 and x["nb_lieux"] >= 10, 2, "grande")
    choix += tirer(lambda x: 10_000 <= x["pop"] < 50_000 and x["nb_lieux"] >= 1, 3, "moyenne")
    choix += tirer(lambda x: 0 < x["pop"] < 2_000, 3, "petite")
    choix += tirer(lambda x: x["dept"].startswith(("97", "98")), 1, "outre-mer")
    choix += tirer(lambda x: x["nb_lieux"] == 0 and x["hist"] >= 300, 1, "sans lieux")
    # Complément si une strate est vide : on reprend n'importe quelles communes avec du contenu
    if len(choix) < n:
        choix += tirer(lambda x: True, n - len(choix), "autre")
    return choix[:n]


def coupe(texte, n=TAILLE_MAX_SOURCE):
    texte = re.sub(r"\s+", " ", str(texte)).strip()
    return texte if len(texte) <= n else texte[:n].rsplit(" ", 1)[0] + " […]"


def construire_dossier(d):
    """Sources numérotées S1… tirées de la fiche V1."""
    sources = []

    def ajouter(texte):
        if texte and str(texte).strip():
            sources.append(coupe(texte))
            return f"S{len(sources)}"
        return None

    c = d.get("commune", {})
    ajouter(d.get("presentation"))
    ajouter(d.get("histoire_extrait"))
    for f in (d.get("frise") or [])[:12]:
        ajouter(f"{f.get('date', '')} : {f.get('texte', '')}")
    lieux = sorted(d.get("lieux") or [], key=lambda l: -l.get("score", 0))[:8]
    lieux_ok = [{"titre": l.get("titre", ""), "lat": l.get("lat"), "lon": l.get("lon"), "url": l.get("url")}
                for l in lieux if l.get("titre")]
    for l in lieux:
        nom = l.get("titre", "")
        ajouter(f"Lieu « {nom} » : {l.get('intro', '')}")
        for f in (l.get("faits") or [])[:3]:
            ajouter(f"Lieu « {nom} », {f.get('date', '')} : {f.get('texte', '')}")
        if l.get("trace"):
            ajouter(f"Lieu « {nom} », aujourd'hui : {l['trace']}")
    texte = [f"COMMUNE : {c.get('titre', '')} (code INSEE {c.get('code_insee', '')}, "
             f"{c.get('population') or 'population inconnue'} habitants)", "SOURCES :"]
    texte += [f"[S{i}] {s}" for i, s in enumerate(sources, 1)]
    texte.append("LIEUX AUTORISÉS (noms exacts) : " + (" | ".join(l["titre"] for l in lieux_ok) or "(aucun)"))
    return "\n".join(texte), sources, lieux_ok


# --------------------------------------------------------------------------- génération et contrôles

def estimer_tokens(texte):
    return int(len(texte) / 3) + 50  # prudent : le français compte ~3,5 caractères par token


def generer(cle, modele, dossier_txt, max_sortie, registre, commune):
    messages = [{"role": "system", "content": CONSIGNES}, {"role": "user", "content": dossier_txt}]
    p_in, p_out = prix_modele(modele)
    pire = (estimer_tokens(CONSIGNES + dossier_txt) * p_in + max_sortie * p_out) / 1_000_000
    if not registre.peut_depenser(pire):
        raise ArretBudget(f"Plafond atteint : dépensé {registre.total:.4f} $, "
                          f"pire cas de l'appel suivant {pire:.4f} $, plafond {registre.plafond:g} $.")
    corps = {"model": modele, "messages": messages, "max_completion_tokens": max_sortie,
             "response_format": {"type": "json_schema",
                                 "json_schema": {"name": "fiche_commune", "strict": True, "schema": SCHEMA}}}
    rep = appeler_api(cle, corps)
    usage = rep.get("usage", {})
    tin, tout = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
    cout = cout_appel(modele, tin, tout)
    registre.enregistrer(modele, commune, tin, tout, cout)
    choix = rep["choices"][0]
    message = choix.get("message", {})
    res = {"tokens_entree": tin, "tokens_sortie": tout, "cout": cout, "sortie": None, "erreur": None}
    if message.get("refusal"):
        res["erreur"] = "refus du modèle : " + masquer(message["refusal"])[:200]
    elif choix.get("finish_reason") == "length":
        res["erreur"] = "réponse tronquée (max_completion_tokens atteint)"
    else:
        try:
            res["sortie"] = json.loads(message.get("content") or "")
        except ValueError:
            res["erreur"] = "réponse non conforme (JSON invalide)"
    return res


def norm(s):
    """Minuscules sans accents ; toute ponctuation (apostrophes droites ou typographiques, traits d'union) devient un espace."""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())


def textes_sortie(sortie):
    t = [sortie.get("accroche", ""), sortie["histoire"].get("recit", "")]
    t += [c.get("texte", "") for c in sortie["histoire"].get("chronologie", [])]
    for l in sortie.get("lieux", []):
        t += [l.get("histoire", ""), l.get("a_voir_aujourdhui", "")]
        t += [a.get("texte", "") for a in l.get("anecdotes", [])]
    return " ".join(t)


def verifier(sortie, sources, lieux_ok=None):
    """Contrôles automatiques : sources citées, affirmations sans source, années et noms absents du dossier."""
    ids = {f"S{i}" for i in range(1, len(sources) + 1)}
    cites, sans_source = [], 0
    for c in sortie["histoire"].get("chronologie", []):
        cites += c.get("sources", [])
        sans_source += 0 if c.get("sources") else 1
    for l in sortie.get("lieux", []):
        cites += l.get("sources", [])
        for a in l.get("anecdotes", []):
            cites += a.get("sources", [])
            sans_source += 0 if a.get("sources") else 1
    corpus = " ".join(sources)
    texte = textes_sortie(sortie)
    annees = sorted(set(re.findall(r"\b(1\d{3}|20[0-2]\d)\b", texte)) - set(re.findall(r"\b(1\d{3}|20[0-2]\d)\b", corpus)))
    mots_dossier = set(norm(corpus).split())
    noms = re.findall(r"(?<=[a-zà-ÿ,] )([A-ZÉÈÀÂÊÎÔÛ][A-Za-zà-ÿ'’\-]{3,})", texte)
    noms_hors = sorted({n for n in noms if norm(n) not in mots_dossier and not set(norm(n).split()) <= mots_dossier})
    autorises = {norm(l["titre"]) for l in (lieux_ok or [])}
    hors_liste = [l.get("nom", "") for l in sortie.get("lieux", []) if norm(l.get("nom", "")) not in autorises]
    return {
        "lieux_hors_liste": hors_liste[:10],
        "identifiants_dans_texte": len(re.findall(r"\bS\d{1,3}\b", texte)),
        "sources_inconnues": sorted(set(cites) - ids),
        "affirmations_sans_source": sans_source,
        "annees_hors_dossier": annees,
        "noms_hors_dossier": noms_hors[:15],
        "nb_lieux": len(sortie.get("lieux", [])),
        "nb_anecdotes": sum(len(l.get("anecdotes", [])) for l in sortie.get("lieux", [])),
    }


class ClientFactice:
    """Mode simulation : aucune requête, sortie fabriquée à partir du dossier, tokens estimés."""

    @staticmethod
    def generer(modele, dossier_txt, max_sortie, registre, commune):
        tin = estimer_tokens(CONSIGNES + dossier_txt)
        tout = min(max_sortie, 900)
        cout = cout_appel(modele, tin, tout)
        registre.enregistrer(modele, commune, tin, tout, cout)
        sortie = {"accroche": "(simulation)", "histoire": {"recit": "(simulation)", "chronologie": []}, "lieux": []}
        return {"tokens_entree": tin, "tokens_sortie": tout, "cout": cout, "sortie": sortie, "erreur": None}


# --------------------------------------------------------------------------- rapport

def rapport(chemin, resultats, registre, args, modeles):
    lignes = ["# Rapport du pilote OpenAI", "",
              f"Modèles : {', '.join(modeles)} — plafond {args.plafond:.2f} $ — dépensé au total : {registre.total:.4f} $", "",
              "## Détail par commune et modèle", "",
              "| Commune | Strate | Modèle | Tokens entrée | Tokens sortie | Coût ($) | Lieux | Anecdotes | Sans source | Lieux hors liste | Id dans texte | Années hors dossier | Noms hors dossier | Remarque |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in resultats:
        v = r.get("controles") or {}
        lignes.append(f"| {r['commune']} | {r['strate']} | {r['modele']} | {r['tokens_entree']} | {r['tokens_sortie']} | "
                      f"{r['cout']:.5f} | {v.get('nb_lieux', '')} | {v.get('nb_anecdotes', '')} | "
                      f"{v.get('affirmations_sans_source', '')} | {len(v.get('lieux_hors_liste', []))} | "
                      f"{v.get('identifiants_dans_texte', '')} | {', '.join(v.get('annees_hors_dossier', []))} | "
                      f"{', '.join(v.get('noms_hors_dossier', [])[:6])} | {r.get('erreur') or ''} |")
    lignes += ["", "## Projection pour la France (indicative : échantillon très petit)", "",
               f"Hypothèse : {PALIERS['A']} communes de palier A (grandes), {PALIERS['B']} de palier B (moyennes), "
               f"{PALIERS['C']} de palier C (petites). L'API Batch réduirait ces coûts d'environ moitié.", "",
               "| Modèle | Coût moyen A | Coût moyen B | Coût moyen C | Projection totale ($) |", "|---|---|---|---|---|"]
    if not any(r["strate"] == "petite" for r in resultats):
        lignes.insert(-2, "**Attention : aucune vraie petite commune (< 2 000 habitants) dans l'échantillon, "
                          "le palier C est donc surestimé.**")
        lignes.insert(-2, "")
    tier = {"grande": "A", "moyenne": "B"}
    for m in modeles:
        moy = {}
        for t in "ABC":
            vals = [r["cout"] for r in resultats if r["modele"] == m and not r.get("erreur")
                    and tier.get(r["strate"], "C") == t]
            moy[t] = sum(vals) / len(vals) if vals else None
        if all(moy[t] is not None for t in "ABC"):
            total = sum(moy[t] * PALIERS[t] for t in "ABC")
            lignes.append(f"| {m} | {moy['A']:.4f} | {moy['B']:.4f} | {moy['C']:.4f} | {total:.0f} |")
        else:
            lignes.append(f"| {m} | " + " | ".join(f"{moy[t]:.4f}" if moy[t] is not None else "n/d" for t in "ABC")
                          + " | n/d (échantillon incomplet) |")
    lignes += ["", "## Extraits à relire", ""]
    vus = set()
    for r in resultats:
        if r.get("sortie") and r["commune"] not in vus and len(vus) < 3:
            vus.add(r["commune"])
            s = r["sortie"]
            premiere = next((a["texte"] for l in s.get("lieux", []) for a in l.get("anecdotes", [])), "(aucune anecdote)")
            lignes += [f"### {r['commune']} ({r['modele']})", "", f"**Accroche** : {s.get('accroche', '')}", "",
                       f"**Récit** : {coupe(s['histoire'].get('recit', ''), 500)}", "", f"**Première anecdote** : {premiere}", ""]
    Path(chemin).write_text("\n".join(lignes), encoding="utf-8")


# --------------------------------------------------------------------------- programme

def main():
    ap = argparse.ArgumentParser(description="Pilote de réécriture par IA (OpenAI), budget plafonné.")
    ap.add_argument("--source", default=str(Path.home() / "anecdotes" / "contenu"), help="Dossier des fiches V1")
    ap.add_argument("--sortie", default=str(Path.home() / "anecdotes" / "pilote_openai"), help="Dossier de sortie")
    ap.add_argument("--plafond", type=float, default=2.0, help="Plafond de dépense cumulée du pilote, en dollars")
    ap.add_argument("--modeles", default="gpt-5.4-nano,gpt-5.4-mini",
                    help="Deux modèles séparés par une virgule : le premier traite toutes les communes, le second les premières")
    ap.add_argument("--n", type=int, default=10, help="Nombre de communes du pilote")
    ap.add_argument("--comparer", type=int, default=4, help="Nombre de communes passées aussi au second modèle")
    ap.add_argument("--max-sortie", type=int, default=6000, help="Tokens de sortie maximum par appel")
    ap.add_argument("--prix", action="append", default=[], help="modele=entree,sortie ($/million de tokens)")
    ap.add_argument("--simulation", action="store_true", help="Aucun appel API : montre le plan et le coût estimé")
    ap.add_argument("--lister-modeles", action="store_true", help="Liste les modèles disponibles pour votre clé")
    ap.add_argument("--oui", action="store_true", help="Ne pas demander de confirmation")
    args = ap.parse_args()

    for p in args.prix:
        nom, valeurs = p.split("=", 1)
        entree, sortie = valeurs.split(",")
        PRIX[nom.strip()] = (float(entree), float(sortie))

    if args.lister_modeles:
        cle = charger_cle()
        ids = sorted(m["id"] for m in requete("GET", "/models", cle).get("data", []))
        print("\n".join(i for i in ids if i.startswith(("gpt", "o1", "o3", "o4"))))
        return

    modeles = [m.strip() for m in args.modeles.split(",") if m.strip()][:2]
    for m in modeles:
        prix_modele(m)

    cle = None if args.simulation else charger_cle()
    if cle:
        disponibles = {m["id"] for m in requete("GET", "/models", cle).get("data", [])}
        manquants = [m for m in modeles if m not in disponibles]
        if manquants:
            proches = sorted(i for i in disponibles if i.startswith("gpt") and ("nano" in i or "mini" in i))
            sys.exit(f"Modèle(s) indisponible(s) pour votre clé : {', '.join(manquants)}.\n"
                     f"Modèles proches : {', '.join(proches[:15])}\nRelancez avec --modeles NOM1,NOM2 "
                     "(et --prix NOM=ENTREE,SORTIE si le prix n'est pas connu).")

    sortie = Path(args.sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    chemin_registre = sortie / ("depenses_simulation.json" if args.simulation else "depenses.json")
    if args.simulation and chemin_registre.exists():
        chemin_registre.unlink()
    registre = Registre(chemin_registre, args.plafond)

    print("Lecture des fiches V1…")
    index = list(indexer(args.source))
    if not index:
        sys.exit(f"Aucune fiche trouvée dans {args.source}.")
    choix = choisir_communes(index, args.n)
    taches = []  # (commune, strate, modele, dossier_txt, sources, chemin_fiche)
    pire_total = 0.0
    for rang, x in enumerate(choix):
        d = json.loads(Path(x["chemin"]).read_text(encoding="utf-8"))
        dossier_txt, sources, lieux_ok = construire_dossier(d)
        for j, m in enumerate(modeles):
            if j == 1 and rang >= args.comparer:
                continue
            taches.append((x["titre"], x["strate"], m, dossier_txt, sources, x, lieux_ok))
            p_in, p_out = prix_modele(m)
            pire_total += (estimer_tokens(CONSIGNES + dossier_txt) * p_in + args.max_sortie * p_out) / 1_000_000

    print(f"\nPlan : {len(choix)} communes, {len(taches)} appels, modèles {', '.join(modeles)}")
    for x in choix:
        print(f"  - {x['titre']} ({x['strate']}, {x['pop']} hab., {x['nb_lieux']} lieux, {x['nb_frise']} faits de frise)")
    print("Prix supposés ($/M tokens entrée/sortie) : " + ", ".join(f"{m} {PRIX[m]}" for m in modeles)
          + "  <- à vérifier sur la page officielle de tarification")
    print(f"Coût maximal théorique : {pire_total:.3f} $ — plafond : {args.plafond:.2f} $ — déjà dépensé : {registre.total:.4f} $")
    if not args.simulation and not args.oui:
        if input("Lancer le pilote ? [o/N] ").strip().lower() not in ("o", "oui", "y", "yes"):
            sys.exit("Abandon.")

    resultats = []
    try:
        for commune, strate, modele, dossier_txt, sources, x, lieux_ok in taches:
            print(f"  {commune} / {modele}…", end=" ", flush=True)
            if args.simulation:
                res = ClientFactice.generer(modele, dossier_txt, args.max_sortie, registre, commune)
            else:
                res = generer(cle, modele, dossier_txt, args.max_sortie, registre, commune)
            res.update({"commune": commune, "strate": strate, "modele": modele})
            if res["sortie"]:
                res["controles"] = verifier(res["sortie"], sources, lieux_ok)
                par_nom = {norm(l["titre"]): l for l in lieux_ok}
                gardes = []
                for l in res["sortie"].get("lieux", []):
                    ref = par_nom.get(norm(l.get("nom", "")))
                    if ref:  # on rattache les coordonnées de la fiche V1 ; les lieux inventés sont écartés
                        l.update({"lat": ref["lat"], "lon": ref["lon"], "url": ref["url"]})
                        gardes.append(l)
                res["sortie"]["lieux"] = gardes
                if not args.simulation:
                    nom = f"{x['code']}-{re.sub(r'[^a-z0-9]+', '-', norm(commune))}.{modele}.json"
                    (sortie / nom).write_text(json.dumps({"commune": commune, "modele": modele, "sources": sources,
                                                          "resultat": res["sortie"], "controles": res["controles"]},
                                                         ensure_ascii=False, indent=1), encoding="utf-8")
            resultats.append(res)
            print(f"{res['tokens_entree']} + {res['tokens_sortie']} tokens, {res['cout']:.5f} $"
                  + (f"  ! {res['erreur']}" if res["erreur"] else ""))
    except (ArretBudget, ArretApi) as err:
        print(f"\nARRÊT : {masquer(err)}")
    finally:
        if resultats:
            rapport(sortie / ("rapport_simulation.md" if args.simulation else "rapport.md"),
                    resultats, registre, args, modeles)
            print(f"\nRapport : {sortie / ('rapport_simulation.md' if args.simulation else 'rapport.md')}")
        print(f"Dépensé au total par le pilote : {registre.total:.4f} $ (plafond {args.plafond:.2f} $)")


if __name__ == "__main__":
    main()
