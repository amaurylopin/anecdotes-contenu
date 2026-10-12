#!/usr/bin/env python3
"""Mise à jour non destructive des métadonnées des communes modifiées.

Exécuter avec --from/--to dans GitHub Actions ou --code 76259.
Ne réécrit jamais les autres entrées de l'index.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

CODE = re.compile(r"^(?:[0-9]{5}|2[AB][0-9]{3})$")
PATH = re.compile(r"^communes/((?:[0-9]{5}|2[AB][0-9]{3}))\.json$")

def codes_from_diff(start: str, end: str) -> set[str]:
    if not start or start == "0" * 40:
        # Premier push : pas de parent Git utilisable, forcer une liste explicite.
        return set()
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", start, end, "--", "communes/"],
        check=True, capture_output=True, text=True)
    return {m.group(1) for line in result.stdout.splitlines() if (m := PATH.fullmatch(line))}

def sync(index_file: Path, communes_dir: Path, codes: set[str], timestamp: str) -> list[str]:
    if not index_file.is_file():
        raise ValueError("index.json absent : refus de régénérer une base incomplète")
    obj = json.loads(index_file.read_text(encoding="utf-8"))
    entries = obj.get("communes")
    if not isinstance(entries, dict) or len(entries) < 1000:
        raise ValueError("Index incomplet ou structure inattendue : aucune écriture")
    updated = []
    for code in sorted(codes):
        if not CODE.fullmatch(code):
            raise ValueError(f"Code INSEE refusé : {code!r}")
        file = communes_dir / (code + ".json")
        if not file.is_file():
            raise FileNotFoundError(f"Fiche absente : {file}")
        content = file.read_bytes()
        place = json.loads(content)
        if str(place.get("insee", "")).upper() != code or str(place.get("id", "")).upper() != code:
            raise ValueError(f"Code INSEE incohérent : {code}")
        articles = place.get("anecdotes")
        if not isinstance(articles, list):
            raise ValueError(f"Liste d'anecdotes invalide : {code}")
        digest = hashlib.sha256(content).hexdigest()
        old = entries.get(code) or {}
        # Conserver les champs additionnels si présents dans l'index.
        new = dict(old)
        new["name"] = place["name"]
        new["count"] = len(articles)
        new["written"] = sum(1 for story in articles if story.get("category") != "politique")
        if (old.get("revision") != digest or any(old.get(k) != new[k] for k in ("name", "count", "written"))):
            new["updated"] = timestamp
            new["revision"] = digest
            entries[code] = new
            updated.append(code)
    if updated:
        temp = index_file.with_suffix(".json.tmp")
        try:
            temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            check = json.loads(temp.read_text(encoding="utf-8"))
            assert len(check["communes"]) == len(entries)
            temp.replace(index_file)
        finally:
            temp.unlink(missing_ok=True)
    return updated

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="start")
    parser.add_argument("--to", dest="end")
    parser.add_argument("--code", action="append", default=[], help="Code INSEE à contrôler explicitement")
    parser.add_argument("--index", type=Path, default=Path("index.json"))
    parser.add_argument("--communes", type=Path, default=Path("communes"))
    args = parser.parse_args()
    codes = set(args.code)
    if args.start or args.end:
        if not (args.start and args.end):
            parser.error("--from et --to sont indissociables")
        codes |= codes_from_diff(args.start, args.end)
    if not codes:
        print("Aucun code INSEE à contrôler, aucun changement")
        return
    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    changed = sync(args.index, args.communes, codes, stamp)
    print(f"Vérifiées : {len(codes)} ; index actualisé : {len(changed)} ; INSEE : {', '.join(changed[:50])}")
    if len(changed) > 50:
        print(f"Et {len(changed) - 50} autres communes.")

if __name__ == "__main__":
    main()
