#!/usr/bin/env python3
"""
ajouter_articles.py — ajoute des articles RELUS à un fichier communes/<code INSEE>.json, sans jamais modifier ni supprimer
un article existant.

  python3 ajouter_articles.py nantes_nouveaux_articles.json                 # simulation
  python3 ajouter_articles.py nantes_nouveaux_articles.json --appliquer     # écrit communes/44109.json et index.json

Garde-fous : simulation par défaut ; un article dont le titre existe déjà est ignoré ; les articles existants restent
intacts et dans le même ordre ; les nouveaux sont ajoutés à la suite ; index.json : seul le compteur de la commune est mis à jour.
"""
import argparse, json, os, sys, time
from pathlib import Path

def main():
    racine = Path.home() / "anecdotes"
    ap = argparse.ArgumentParser()
    ap.add_argument("fichier")
    ap.add_argument("--communes", default=str(racine / "communes"))
    ap.add_argument("--index", default=str(racine / "index.json"))
    ap.add_argument("--appliquer", action="store_true")
    a = ap.parse_args()
    nouveau = json.loads(Path(a.fichier).read_text(encoding="utf-8"))
    insee = nouveau["insee"]
    chemin = Path(a.communes) / f"{insee}.json"
    if not chemin.exists():
        sys.exit(f"{chemin} introuvable : rien à faire.")
    brut = chemin.read_text(encoding="utf-8")
    commune = json.loads(brut)
    existants = commune["anecdotes"]
    titres = {x["title"] for x in existants}
    ajoutes = [x for x in nouveau["anecdotes"] if x["title"] not in titres]
    ignores = [x["title"] for x in nouveau["anecdotes"] if x["title"] in titres]
    print(("APPLICATION RÉELLE" if a.appliquer else "SIMULATION (rien n'est écrit)") + f" — {commune['name']} ({insee})")
    print(f"  articles existants : {len(existants)} (conservés tels quels)")
    print(f"  articles ajoutés   : {len(ajoutes)}")
    for x in ajoutes: print(f"    + [{x['category']}] {x['title']}")
    for t in ignores: print(f"    = déjà présent, ignoré : {t}")
    if not a.appliquer or not ajoutes:
        return
    commune["anecdotes"] = existants + ajoutes
    tmp = chemin.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(commune, ensure_ascii=False, indent=1) + ("\n" if brut.endswith("\n") else ""), encoding="utf-8")
    tmp.replace(chemin)
    if os.path.exists(a.index):
        brut_i = Path(a.index).read_text(encoding="utf-8")
        idx = json.loads(brut_i)
        if insee in idx.get("communes", {}):
            idx["communes"][insee]["count"] = len(commune["anecdotes"])
            idx["communes"][insee]["updated"] = time.strftime("%Y-%m-%d")
            Path(a.index).write_text(json.dumps(idx, ensure_ascii=False, indent=1) + ("\n" if brut_i.endswith("\n") else ""), encoding="utf-8")
            print("  index.json : compteur mis à jour")
    print("Vérifiez avec : git diff --stat communes/%s.json index.json" % insee)

if __name__ == "__main__":
    main()
