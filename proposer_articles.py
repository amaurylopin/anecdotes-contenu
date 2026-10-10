#!/usr/bin/env python3
"""
proposer_articles.py — transforme les fiches réécrites par IA (contenu_ia) en PROPOSITIONS d'articles au format
de l'application (communes/<code INSEE>.json), sans jamais modifier communes/ ni index.json.

Règles de sécurité :
  - Les communes qui ont déjà du contenu travaillé (au moins un article hors « politique ») sont PROTÉGÉES :
    aucune proposition n'est écrite pour elles.
  - Seules les fiches au statut « ok » sont utilisées.
  - Tout est écrit dans ~/anecdotes/propositions/ ; rien n'entre dans communes/ sans une étape de relecture séparée.

Usage :
  python3 proposer_articles.py --limite 30           # 30 premières fiches IA (ordre alphabétique des fichiers)
  python3 proposer_articles.py --codes 30189,38185   # communes précises
  python3 proposer_articles.py                       # toutes les fiches IA disponibles
Aucune dépendance externe (bibliothèque standard).
"""

import argparse
import glob
import json
import os
import re
import time
from collections import Counter
from pathlib import Path

ANNEE = re.compile(r"\b(1\d{3}|20[0-2]\d)\b")
SEPARATEUR_PHRASES = re.compile(r"(?<=[.!?])\s+(?=[A-ZÉÈÀÂÊÎÔÛ«\"“(0-9])")


ABREVIATIONS = re.compile(r"(?:\b(?:apr|av|St|Ste|Mgr|Mme|MM|env|cf|vol|fig|etc)\.|\bM\.)$")


def phrases(texte):
    morceaux = [p.strip() for p in SEPARATEUR_PHRASES.split(re.sub(r"[ \t]+", " ", texte).strip()) if p.strip()]
    sortie = []
    for m in morceaux:
        if sortie and ABREVIATIONS.search(sortie[-1]):  # « apr. J.-C. », « St. », « M. » ne terminent pas une phrase
            sortie[-1] += " " + m
        else:
            sortie.append(m)
    return sortie


def paragraphes(texte, cible=450):
    """Découpe un texte en paragraphes : sauts de ligne existants, sinon groupes de phrases d'environ 450 caractères."""
    blocs = [b.strip() for b in re.split(r"\n\s*\n|\n", texte or "") if b.strip()]
    if len(blocs) > 1:
        return blocs
    sortie, courant = [], ""
    for ph in phrases(texte or ""):
        if courant and len(courant) + len(ph) > cible:
            sortie.append(courant)
            courant = ph
        else:
            courant = (courant + " " + ph).strip()
    if courant:
        sortie.append(courant)
    return sortie


VERBES_FONDATION = r"(?:construi|constructi|fondati|inaugurati|édificati|bâti|bâtit|édifi|érig|fond|élev|inaugur|ouvr|ouvert|achev|consacr|mise? en service|réalis|creus|posée?)\w*"
ANNEE_FONDATION = re.compile(VERBES_FONDATION + r"[^.]{0,90}?\b(1\d{3}|20[0-2]\d)\b", re.I)
VERBE_FONDATION = re.compile(r"\b" + VERBES_FONDATION, re.I)
EXCLUS = re.compile(r"(?i)^(lycée|collège|école|groupe scolaire|gare|stade|piscine|gymnase|centre commercial|"
                    r"zone d.activit|hôpital|clinique|centre hospitalier|caserne|salle des fêtes|complexe sportif)\b")


PRONOM_INITIAL = re.compile(r"(?i)^(ses|sa|son|elle|elles|il|ils|cette|cet|ce|ces|leur|leurs|celle|celui)\b")


PATRIMOINE = re.compile(r"(?i)\b(église|chapelle|château|abbaye|cathédrale|cocathédrale|basilique|monastère|couvent|prieuré|"
                        r"tour|porte|pont|remparts?|fort|citadelle|donjon|hôtel particulier|hôtel de ville|halle|théâtre|"
                        r"opéra|musée|moulin|fontaine|manoir|palais|arènes|amphithéâtre|aqueduc|phare|beffroi|bastide|"
                        r"temple|synagogue|collégiale|commanderie)\b")
MIN_PATRIMOINE = 110  # un édifice patrimonial court est gardé s'il donne une date de construction


def annee_fondation(texte):
    """Année liée à un verbe de construction, de fondation ou d'inauguration ; None si le texte n'en donne pas."""
    m = ANNEE_FONDATION.search(texte or "")
    return int(m.group(1)) if m else None


def meilleur_teaser(texte, maxi=230):
    """Phrase la plus informative : une année ET un verbe de fondation ; à défaut la première phrase."""
    ph = phrases(texte)
    # Une phrase qui commence par un pronom (« Ses limites… », « Elle est… ») ne se comprend pas isolément
    autonomes = [p for p in ph if not PRONOM_INITIAL.match(p)]
    choix = next((p for p in autonomes if ANNEE.search(p) and VERBE_FONDATION.search(p)),
                 ph[0] if ph else (texte or "")[:maxi])
    return choix if len(choix) <= maxi else choix[:maxi].rsplit(" ", 1)[0] + "…"


def premiere_annee(*textes):
    for t in textes:
        m = ANNEE.search(t or "")
        if m:
            return m.group(1)
    return ""


def titre_page(url):
    return (url or "").rsplit("/wiki/", 1)[-1] if "/wiki/" in (url or "") else None


def article(categorie, titre, label, teaser, paragraphes_corps, plus, url, lat, lon, marqueur):
    corps = [p for p in paragraphes_corps if p]
    lead = corps[0] if corps else ""
    art = {
        "category": categorie, "title": titre, "label": label, "teaser": teaser, "lead": lead, "text": lead,
        "body": corps, "more": plus, "timeline": None, "wiki": titre_page(url), "source": url or None,
        "lat": lat, "lon": lon, "access": None, "protection": None,
    }
    if marqueur:
        art["auto"] = True
    return art


def score_lieu(lieu, an):
    s = 2 if lieu.get("a_voir_aujourdhui") else 0
    s += len(lieu.get("anecdotes", []))
    s += 1 if an and an < 1800 else 0
    s += min(len(lieu.get("histoire", "")), 800) / 400
    return s


def articles_depuis_fiche(fiche, marqueur=True, max_lieux=4, min_caracteres=220, inclure_modernes=False, rejets=None):
    c = fiche["commune"]
    nom = c.get("titre", "")
    nom_court = re.sub(r"\s*\(.*\)$", "", nom)
    arts = []
    recit = (fiche.get("histoire") or {}).get("recit", "") or ""
    if len(recit) >= 200:
        paras = paragraphes(recit)
        annees = sorted({int(m.group(1)) for d in (fiche.get("histoire") or {}).get("chronologie", [])
                         for m in [ANNEE.search(d.get("date", ""))] if m})
        label = (f"{annees[0]}-{annees[-1]} · {nom_court}" if len(annees) >= 2
                 else f"{annees[0]} · {nom_court}" if annees else nom_court)
        arts.append(article("histoire", f"{nom_court} : son histoire", label, fiche.get("accroche", "") or (phrases(paras[0])[:1] or [""])[0],
                            paras, [], c.get("url"), c.get("lat"), c.get("lon"), marqueur))
    candidats = []
    for lieu in fiche.get("lieux", []):
        hist = lieu.get("histoire", "") or ""
        nom_lieu = re.sub(r"\s*\(.*\)$", "", lieu.get("nom", ""))
        raison = None
        if lieu.get("lat") is None or lieu.get("lon") is None:
            raison = "sans coordonnées"
        elif len(hist) < min_caracteres or len(phrases(hist)) < 2:
            court_ok = (PATRIMOINE.search(nom_lieu) and len(hist) >= MIN_PATRIMOINE and annee_fondation(hist) is not None)
            if not court_ok:
                raison = "trop court"
        elif EXCLUS.match(nom_lieu):
            raison = "équipement courant (lycée, gare, stade…)"
        an = annee_fondation(hist)
        if not raison and an and an >= 1950 and not inclure_modernes:
            raison = "construction récente (≥ 1950)"
        if raison:
            if rejets is not None:
                rejets[raison] = rejets.get(raison, 0) + 1
            continue
        candidats.append((score_lieu(lieu, an), an, lieu))
    candidats.sort(key=lambda c: -c[0])
    if rejets is not None and len(candidats) > max_lieux:
        rejets["au-delà du plafond"] = rejets.get("au-delà du plafond", 0) + len(candidats) - max_lieux
    for _, an, lieu in candidats[:max_lieux]:
        hist = lieu.get("histoire", "") or ""
        paras = paragraphes(hist)
        if lieu.get("a_voir_aujourdhui"):
            paras.append("À voir aujourd'hui : " + lieu["a_voir_aujourdhui"].strip())
        plus = [a["texte"] for a in lieu.get("anecdotes", []) if a.get("texte")]
        nom_lieu = re.sub(r"\s*\(.*\)$", "", lieu.get("nom", ""))
        arts.append(article("patrimoine", nom_lieu, f"{an} · {nom_lieu}" if an else nom_lieu,
                            meilleur_teaser(hist), paras, plus, lieu.get("url"),
                            lieu.get("lat"), lieu.get("lon"), marqueur))
    return arts


def main():
    racine = Path.home() / "anecdotes"
    ap = argparse.ArgumentParser(description="Propositions d'articles à partir des fiches IA, sans toucher à communes/.")
    ap.add_argument("--ia", default=str(racine / "contenu_ia"))
    ap.add_argument("--communes", default=str(racine / "communes"))
    ap.add_argument("--sortie", default=str(racine / "propositions"))
    ap.add_argument("--codes", help="Codes INSEE séparés par des virgules")
    ap.add_argument("--limite", type=int, help="Nombre maximal de fiches IA traitées")
    ap.add_argument("--sans-marqueur", action="store_true", help='Ne pas ajouter le champ "auto": true')
    ap.add_argument("--max-lieux", type=int, default=4, help="Nombre maximal d'articles de patrimoine par commune (défaut : 4)")
    ap.add_argument("--min-caracteres", type=int, default=220, help="Longueur minimale du texte d'un lieu (défaut : 220)")
    ap.add_argument("--inclure-modernes", action="store_true", help="Garder aussi les constructions postérieures à 1950")
    args = ap.parse_args()

    protegees = {}
    for p in glob.glob(os.path.join(args.communes, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        n = sum(1 for a in d.get("anecdotes", []) if a.get("category") != "politique")
        if n:
            protegees[d.get("insee") or d.get("id")] = (d.get("name", ""), n)
    print(f"{len(protegees)} communes protégées (contenu existant hors politique).")

    voulus = set(args.codes.split(",")) if args.codes else None
    fichiers = sorted(glob.glob(os.path.join(args.ia, "[0-9]*", "*.json")))
    sortie = Path(args.sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    stats = Counter()
    rejets = {}
    categories = Counter()
    ignorees_protegees, sans_article = [], []
    for chemin in fichiers:
        if args.limite and stats["lues"] >= args.limite:
            break
        try:
            fiche = json.load(open(chemin, encoding="utf-8"))
        except (OSError, ValueError):
            stats["illisibles"] += 1
            continue
        insee = fiche.get("commune", {}).get("code_insee")
        if voulus and insee not in voulus:
            continue
        stats["lues"] += 1
        if fiche.get("statut_qualite") != "ok":
            stats["statut_" + str(fiche.get("statut_qualite"))] += 1
            continue
        if insee in protegees:
            ignorees_protegees.append(f"{protegees[insee][0]} ({protegees[insee][1]} articles existants)")
            continue
        arts = articles_depuis_fiche(fiche, marqueur=not args.sans_marqueur, max_lieux=args.max_lieux,
                                     min_caracteres=args.min_caracteres, inclure_modernes=args.inclure_modernes, rejets=rejets)
        if not arts:
            sans_article.append(fiche["commune"].get("titre", insee))
            continue
        existant = {}
        pe = os.path.join(args.communes, f"{insee}.json")
        if os.path.exists(pe):
            try:
                existant = json.load(open(pe, encoding="utf-8"))
            except (OSError, ValueError):
                existant = {}
        c = fiche["commune"]
        prop = {"insee": insee, "name": c.get("titre", ""), "dept": existant.get("dept"),
                "meta": {"source_fiche": os.path.relpath(chemin, args.ia), "modele": fiche.get("modele"),
                         "genere_le": fiche.get("genere_le"), "propose_le": time.strftime("%Y-%m-%d"),
                         "existe_dans_communes": bool(existant)},
                "anecdotes": arts}
        tmp = sortie / f"{insee}.json.tmp"
        tmp.write_text(json.dumps(prop, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(sortie / f"{insee}.json")
        stats["propositions"] += 1
        categories.update(a["category"] for a in arts)

    lignes = ["# Rapport des propositions", "",
              f"- Fiches IA lues : {stats['lues']}", f"- Propositions écrites : {stats['propositions']}",
              f"- Communes protégées ignorées : {len(ignorees_protegees)}",
              f"- Fiches sans article exploitable : {len(sans_article)}",
              "- Articles proposés par catégorie : " + (", ".join(f"{k} {v}" for k, v in sorted(categories.items())) or "aucun"), ""]
    if rejets:
        lignes.append("- Lieux écartés : " + ", ".join(f"{k} {v}" for k, v in sorted(rejets.items(), key=lambda x: -x[1])))
    autres = {k: v for k, v in stats.items() if k.startswith("statut_") or k == "illisibles"}
    if autres:
        lignes.append("- Fiches non utilisées : " + ", ".join(f"{k} {v}" for k, v in autres.items()))
    if ignorees_protegees:
        lignes += ["", "## Communes protégées (aucune proposition)", ""] + [f"- {x}" for x in ignorees_protegees[:50]]
    if sans_article:
        lignes += ["", "## Sans article exploitable", ""] + [f"- {x}" for x in sans_article[:50]]
    (sortie / "_rapport.md").write_text("\n".join(lignes), encoding="utf-8")
    print("\n".join(lignes))
    print(f"\nPropositions dans : {sortie}")


if __name__ == "__main__":
    main()
