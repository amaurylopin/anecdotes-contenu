#!/usr/bin/env python3
"""
appliquer_propositions.py — ajoute les articles AUTOMATIQUES (dossier propositions/) aux fichiers
communes/<code INSEE>.json de l'application, sans jamais modifier ni supprimer un article existant.

Garde-fous :
  - SIMULATION par défaut : rien n'est écrit sans l'option --appliquer.
  - Une commune qui possède au moins un article HORS « politique » et NON automatique est PROTÉGÉE : ignorée.
  - Seuls les articles marqués "auto": true (ajoutés par un lancement précédent) peuvent être remplacés ;
    tous les autres articles (politique, articles soignés) sont conservés tels quels, dans le même ordre.
  - index.json : on ne met à jour (count, updated) que les communes qui y figurent déjà ; aucune entrée n'est ajoutée.
  - Chaque article est validé (champs attendus, paragraphes non vides, coordonnées numériques) avant écriture.
  - Les fichiers sont écrits de façon atomique ; git permet de revenir en arrière (git revert).

Usage :
  python3 appliquer_propositions.py                 # simulation sur toutes les propositions
  python3 appliquer_propositions.py --appliquer     # écrit dans communes/ et index.json
  python3 appliquer_propositions.py --codes 13005,01053 --appliquer
Aucune dépendance externe (bibliothèque standard).
"""

import argparse
import glob
import json
import os
import time
from collections import Counter
from pathlib import Path

CLES = ["category", "title", "label", "teaser", "lead", "text", "body", "more", "timeline", "wiki", "source",
        "lat", "lon", "access", "protection"]
CATEGORIES = {"histoire", "faits_divers", "personnalites", "patrimoine", "insolite", "gastronomie", "sport",
              "legende", "nature", "politique"}


def article_valide(a):
    """Retourne None si l'article est valide, sinon la raison du refus."""
    manquantes = [k for k in CLES if k not in a]
    if manquantes:
        return "champs manquants : " + ", ".join(manquantes)
    if a["category"] not in CATEGORIES:
        return f"catégorie inconnue : {a['category']}"
    if not a["title"] or not a["teaser"] or not a["lead"]:
        return "titre, teaser ou lead vide"
    if not isinstance(a["body"], list) or not a["body"] or not all(isinstance(p, str) and p.strip() for p in a["body"]):
        return "body vide ou invalide"
    if not isinstance(a["more"], list):
        return "more invalide"
    for k in ("lat", "lon"):
        if a[k] is not None and not isinstance(a[k], (int, float)):
            return f"{k} non numérique"
    return None


def lire_json(chemin):
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def ecrire_json(chemin, data, fin_de_ligne):
    chemin = Path(chemin)
    tmp = chemin.with_suffix(chemin.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + ("\n" if fin_de_ligne else ""), encoding="utf-8")
    tmp.replace(chemin)


def main():
    racine = Path.home() / "anecdotes"
    ap = argparse.ArgumentParser(description="Ajoute les articles automatiques aux fichiers communes/, sans rien écraser.")
    ap.add_argument("--propositions", default=str(racine / "propositions"))
    ap.add_argument("--communes", default=str(racine / "communes"))
    ap.add_argument("--index", default=str(racine / "index.json"))
    ap.add_argument("--codes", help="Codes INSEE séparés par des virgules")
    ap.add_argument("--limite", type=int, help="Nombre maximal de communes traitées")
    ap.add_argument("--appliquer", action="store_true", help="Écrire réellement (sans cette option : simulation)")
    args = ap.parse_args()

    voulus = set(args.codes.split(",")) if args.codes else None
    fichiers = sorted(p for p in glob.glob(os.path.join(args.propositions, "*.json")) if not os.path.basename(p).startswith("_"))
    index_data, index_fin = None, True
    if os.path.exists(args.index):
        brut = Path(args.index).read_text(encoding="utf-8")
        index_data, index_fin = json.loads(brut), brut.endswith("\n")
    aujourdhui = time.strftime("%Y-%m-%d")

    stats = Counter()
    ajoutes = Counter()
    refus = []
    exemples = []
    modifiees = []
    for chemin in fichiers:
        if args.limite and stats["traitees"] >= args.limite:
            break
        try:
            prop = lire_json(chemin)
        except (OSError, ValueError):
            stats["proposition illisible"] += 1
            continue
        insee = prop.get("insee")
        if voulus and insee not in voulus:
            continue
        stats["traitees"] += 1
        fichier = os.path.join(args.communes, f"{insee}.json")
        if not os.path.exists(fichier):
            stats["commune absente de communes/"] += 1
            continue
        brut = Path(fichier).read_text(encoding="utf-8")
        commune = json.loads(brut)
        existants = commune.get("anecdotes", [])
        soignes = [a for a in existants if not a.get("auto")]
        if any(a.get("category") != "politique" for a in soignes):
            stats["protégée (contenu soigné)"] += 1
            continue
        nouveaux, invalides = [], 0
        for a in prop.get("anecdotes", []):
            raison = article_valide(a)
            if raison:
                invalides += 1
                refus.append(f"{prop.get('name', insee)} : {a.get('title', '?')} — {raison}")
            else:
                nouveaux.append(a)
        if not nouveaux:
            stats["aucun article valide"] += 1
            continue
        resultat = soignes + nouveaux
        remplaces = len(existants) - len(soignes)
        stats["modifiées"] += 1
        stats["anciens articles automatiques remplacés"] += remplaces
        ajoutes.update(a["category"] for a in nouveaux)
        modifiees.append(insee)
        if len(exemples) < 8:
            exemples.append(f"{commune.get('name', insee)} ({insee}) : {len(soignes)} article(s) conservé(s) + {len(nouveaux)} automatique(s)")
        if args.appliquer:
            commune["anecdotes"] = resultat
            ecrire_json(fichier, commune, brut.endswith("\n"))
            if index_data is not None and insee in index_data.get("communes", {}):
                index_data["communes"][insee]["count"] = len(resultat)
                index_data["communes"][insee]["updated"] = aujourdhui
                stats["entrées d'index mises à jour"] += 1
            elif index_data is not None:
                stats["absentes de index.json (non ajoutées)"] += 1

    if args.appliquer and index_data is not None and stats["entrées d'index mises à jour"]:
        ecrire_json(args.index, index_data, index_fin)

    titre = "APPLICATION RÉELLE" if args.appliquer else "SIMULATION (rien n'est écrit ; ajoutez --appliquer pour appliquer)"
    lignes = [titre, "", f"Propositions examinées : {stats['traitees']}"]
    for k in ("modifiées", "protégée (contenu soigné)", "commune absente de communes/", "aucun article valide",
              "proposition illisible", "anciens articles automatiques remplacés", "entrées d'index mises à jour",
              "absentes de index.json (non ajoutées)"):
        if stats[k]:
            lignes.append(f"- {k} : {stats[k]}")
    lignes.append("- articles ajoutés par catégorie : " + (", ".join(f"{k} {v}" for k, v in sorted(ajoutes.items())) or "aucun"))
    if exemples:
        lignes += ["", "Exemples :"] + [f"  {e}" for e in exemples]
    if refus:
        lignes += ["", f"Articles refusés à la validation ({len(refus)}) :"] + [f"  {r}" for r in refus[:15]]
    print("\n".join(lignes))
    if args.appliquer and modifiees:
        journal = Path(args.propositions) / "_application.txt"
        journal.write_text("\n".join(lignes) + "\n\nCommunes modifiées :\n" + "\n".join(modifiees) + "\n", encoding="utf-8")
        print(f"\nJournal : {journal}")
        print("Vérifiez avec :  git status --short | head   puis   git diff --stat | tail -3")


if __name__ == "__main__":
    main()
