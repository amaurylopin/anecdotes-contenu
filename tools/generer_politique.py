#!/usr/bin/env python3
"""
generer_politique.py — Phase 1 : une anecdote « politique » (municipales 2026)
pour chaque commune de France absente du dépôt anecdotes-contenu.

Double vérification, sans recherche web :
  source 1 : résultats officiels du ministère de l'Intérieur (fichiers data.gouv.fr, tours 1 et 2) ;
  source 2 : Répertoire national des élus (RNE, fichier des maires, data.gouv.fr).
Une fiche n'est générée que si le maire inscrit au RNE est bien la tête de la liste
arrivée en tête, avec une prise de fonction postérieure au 15 mars 2026.
Tout le reste est écarté et listé dans le rapport, avec son motif.

Autres données : liste des communes, département et coordonnées (geo.api.gouv.fr),
titre de l'article Wikipédia FR de chaque commune (Wikidata, propriété P374 = code INSEE).

Utilisation (depuis la racine du dépôt cloné) :
  1. Vérifier la lecture des fichiers, sans rien écrire :
       python3 tools/generer_politique.py --t1 T1.csv --t2 T2.csv --rne elus-maires.csv --inspect
  2. Générer un département pour contrôler le résultat :
       python3 tools/generer_politique.py --t1 T1.csv --t2 T2.csv --rne elus-maires.csv --dept 01
  3. Tout générer, un commit par département (aucun push) :
       python3 tools/generer_politique.py --t1 T1.csv --t2 T2.csv --rne elus-maires.csv --commit

Les fichiers --t1, --t2 et --rne peuvent être des chemins locaux ou des URL.
Si la détection automatique des colonnes échoue, --mapping mapping.json permet de
forcer le nom des colonnes (voir MAPPING_EXEMPLE plus bas).
Aucune dépendance hors bibliothèque standard Python 3.9+.
"""
import argparse, csv, io, json, os, re, subprocess, sys, unicodedata, urllib.request, urllib.parse
from collections import defaultdict

UA = {"User-Agent": "anecdotes-contenu/generer_politique (contact: depot GitHub amaurylopin/anecdotes-contenu)"}
GEO_URL = ("https://geo.api.gouv.fr/communes?fields=nom,code,departement,centre,population"
           "&format=json&geometry=centre")
SPARQL = """SELECT ?insee ?article WHERE {
  ?c wdt:P374 ?insee .
  ?article schema:about ?c ; schema:isPartOf <https://fr.wikipedia.org/> .
}"""
WIKI = "https://fr.wikipedia.org/wiki/"
DATE_T1, DATE_T2 = "15 mars 2026", "22 mars 2026"
CATS = {"histoire", "faits_divers", "politique", "personnalites", "patrimoine",
        "insolite", "gastronomie", "sport", "legende", "nature"}
MAPPING_EXEMPLE = {
    "commune": {"code": "Code commune", "libelle": "Libellé commune", "inscrits": "Inscrits",
                "votants": "Votants", "exprimes": "Exprimés"},
    "liste": {"liste": "Libellé de liste", "nuance": "Nuance liste", "nom": "Nom tête de liste",
              "prenom": "Prénom tête de liste", "voix": "Voix", "sieges": "Sièges au CM"},
}
DOM = {"ZA": "971", "ZB": "972", "ZC": "973", "ZD": "974", "ZM": "976",
       "ZS": "975", "ZN": "988", "ZP": "987", "ZW": "986"}

# ---------------------------------------------------------------- utilitaires
def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9%/]+", " ", s).strip()

def same_person(nom1, pre1, nom2, pre2):
    n1, n2 = norm(nom1).replace(" ", ""), norm(nom2).replace(" ", "")
    p1, p2 = norm(pre1).split(), norm(pre2).split()
    return bool(n1) and n1 == n2 and bool(p1) and bool(p2) and p1[0] == p2[0]

def num(v):
    v = str(v or "").replace("\u202f", "").replace("\xa0", "").replace(" ", "").replace(",", ".")
    try: return float(v)
    except ValueError: return None

def fr_int(n): return f"{int(n):,}".replace(",", " ")
def fr_pct(p): return f"{p:.2f}".replace(".", ",") + " %"
def wk(title): return urllib.parse.quote(title.replace(" ", "_"), safe="_(),-.")

def fetch(src, cache=None):
    """Lit un chemin local ou télécharge une URL (avec cache facultatif)."""
    if cache and os.path.exists(cache): return open(cache, "rb").read()
    if re.match(r"https?://", src):
        req = urllib.request.Request(src, headers=UA)
        data = urllib.request.urlopen(req, timeout=300).read()
    else:
        data = open(src, "rb").read()
    if cache:
        os.makedirs(os.path.dirname(cache), exist_ok=True); open(cache, "wb").write(data)
    return data

def read_table(src, cache=None):
    raw = fetch(src, cache)
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try: text = raw.decode(enc); break
        except UnicodeDecodeError: continue
    sample = text[:20000]
    delim = max([";", "\t", ","], key=lambda d: sample.splitlines()[0].count(d) if sample else 0)
    rows = list(csv.reader(io.StringIO(text), delimiter=delim))
    rows = [r for r in rows if any(c.strip() for c in r)]
    return rows[0], rows[1:]

def insee_from(dept, code):
    code, dept = str(code).strip(), str(dept or "").strip().upper()
    if re.fullmatch(r"\d[\dAB]\d{3}", code): return code
    dept = DOM.get(dept, dept)
    if not dept or not code.isdigit(): return None
    if len(dept) == 3: return dept + code.zfill(3)[-2:]
    return dept.zfill(2) + code.zfill(3)

# ---------------------------------------------------------------- résultats ministère
COMMUNE_PAT = {
    "dept": r"^code (du )?dep", "code": r"^code (de la )?commune|^code insee|^commune code",
    "libelle": r"^libelle (de la )?commune|^nom (de la )?commune",
    "inscrits": r"^inscrits$", "votants": r"^votants$", "exprimes": r"^exprimes$",
}
LISTE_PAT = {
    "liste": r"^libelle (de )?(la )?liste$|^liste$|^libelle de liste|^nom (de la )?liste",
    "liste_abr": r"libelle abrege",
    "nuance": r"nuance",
    "nom": r"^nom( (de la )?tete de liste| candidat)?$",
    "prenom": r"^prenom( (de la )?tete de liste| candidat)?$",
    "sexe": r"^sexe",
    "voix": r"^voix$",
    "sieges": r"^sieges?( au)?( (cm|conseil municipal))?$|^sieges?( /)? elu|^elus?$|sieges au cm",
    "panneau": r"panneau",
}

def classify(name, pats):
    n = norm(name)
    for k, p in pats.items():
        if re.search(p, n): return k
    return None

def parse_results(src, mapping=None, label="T1", cache=None):
    head, rows = read_table(src, cache)
    info = {"format": None, "colonnes_commune": {}, "colonnes_liste": {}}
    cidx = {}
    if mapping:
        for k, col in mapping.get("commune", {}).items():
            if col in head: cidx[k] = head.index(col)
    for i, h in enumerate(head):
        k = classify(h, COMMUNE_PAT)
        if k and k not in cidx and not re.search(r"\d+$", h.strip()): cidx[k] = i
    info["colonnes_commune"] = {k: head[i] for k, i in cidx.items()}

    # Format A : en-têtes numérotés (« Voix 1 », « Voix 2 »…)
    numbered = defaultdict(dict)
    for i, h in enumerate(head):
        m = re.match(r"^(.*?)[\s_]*(\d+)$", h.strip())
        if not m: continue
        k = None
        if mapping:
            for kk, col in mapping.get("liste", {}).items():
                if norm(m.group(1)) == norm(col): k = kk
        k = k or classify(m.group(1), LISTE_PAT)
        if k: numbered[int(m.group(2))][k] = i
    blocks_spec = None
    if len(numbered) >= 2 and all("voix" in v for v in numbered.values()):
        info["format"] = "A (colonnes numérotées)"
        blocks_spec = [numbered[n] for n in sorted(numbered)]
    else:
        # Format B (fichiers 2020) : un bloc de colonnes nommé une fois, répété ensuite sans en-tête
        first, spec = None, {}
        for i, h in enumerate(head):
            k = classify(h, LISTE_PAT) if i not in cidx.values() else None
            if mapping:
                for kk, col in mapping.get("liste", {}).items():
                    if h == col: k = kk
            if k and k not in spec:
                spec[k] = i; first = i if first is None else first
        if "voix" not in spec:
            raise SystemExit(f"[{label}] Colonne « Voix » introuvable. En-tête : {head}\n"
                             f"Utilisez --mapping (exemple : {json.dumps(MAPPING_EXEMPLE, ensure_ascii=False)})")
        L = len(head) - first
        codes = [insee_from(r[cidx["dept"]] if "dept" in cidx else "", r[cidx["code"]]) for r in rows[:200]]
        if len(set(codes)) < len(codes) * 0.9 and max(len(r) for r in rows[:200]) <= len(head):
            info["format"] = "C (une ligne par liste)"
        else:
            info["format"] = f"B (bloc de {L} colonnes répété)"
        blocks_spec = ("B", first, L, {k: i - first for k, i in spec.items()})
    info["colonnes_liste"] = ({k: head[i] for k, i in blocks_spec[0].items()}
                              if isinstance(blocks_spec, list) else
                              {k: head[blocks_spec[1] + o] for k, o in blocks_spec[3].items()})

    out = {}
    def blk(row, spec):
        g = lambda k: row[spec[k]].strip() if k in spec and spec[k] < len(row) else ""
        voix = num(g("voix"))
        if voix is None or (not g("nom") and not g("liste")): return None
        return {"liste": g("liste") or g("liste_abr"), "nuance": g("nuance"), "nom": g("nom"),
                "prenom": g("prenom"), "sexe": g("sexe"), "voix": voix, "sieges": num(g("sieges"))}
    for r in rows:
        if "code" not in cidx or cidx["code"] >= len(r): continue
        insee = insee_from(r[cidx["dept"]] if "dept" in cidx else "", r[cidx["code"]])
        if not insee: continue
        c = out.setdefault(insee, {"libelle": r[cidx["libelle"]] if "libelle" in cidx else "",
                                   "inscrits": num(r[cidx["inscrits"]]) if "inscrits" in cidx else None,
                                   "votants": num(r[cidx["votants"]]) if "votants" in cidx else None,
                                   "exprimes": num(r[cidx["exprimes"]]) if "exprimes" in cidx else None,
                                   "listes": []})
        if isinstance(blocks_spec, list):
            for spec in blocks_spec:
                b = blk(r, spec)
                if b: c["listes"].append(b)
        else:
            _, first, L, rel = blocks_spec
            start = first
            while start < len(r):
                b = blk(r, {k: start + o for k, o in rel.items()})
                if b: c["listes"].append(b)
                start += L
    info["communes"] = len(out)
    return out, info

# ---------------------------------------------------------------- RNE
RNE_PAT = {"code": r"^code (de la )?commune$", "dept": r"^code (du )?departement$",
           "nom": r"^nom (de l )?elu", "prenom": r"^prenom (de l )?elu",
           "sexe": r"^code sexe|^sexe", "debut": r"debut (de la )?fonction"}

def parse_rne(src, cache=None):
    head, rows = read_table(src, cache)
    idx = {}
    for i, h in enumerate(head):
        k = classify(h, RNE_PAT)
        if k and k not in idx: idx[k] = i
    missing = {"code", "nom", "prenom", "debut"} - set(idx)
    if missing: raise SystemExit(f"[RNE] colonnes manquantes {missing}. En-tête : {head}")
    out = {}
    for r in rows:
        insee = insee_from(r[idx["dept"]] if "dept" in idx else "", r[idx["code"]])
        d = r[idx["debut"]].strip()
        m = re.match(r"(\d{2})/(\d{2})/(\d{4})", d) or re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
        iso = (f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if "/" in d else d[:10]) if m else ""
        out[insee] = {"nom": r[idx["nom"]].strip(), "prenom": r[idx["prenom"]].strip(),
                      "sexe": r[idx["sexe"]].strip().upper()[:1] if "sexe" in idx else "", "debut": iso}
    return out, {k: head[i] for k, i in idx.items()}

# ---------------------------------------------------------------- référentiels
def load_geo(cache):
    data = json.loads(fetch(GEO_URL, cache))
    return {c["code"]: c for c in data}

def load_wikidata(cache):
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(SPARQL)
    data = json.loads(fetch(url, cache))
    out = defaultdict(set)
    for b in data["results"]["bindings"]:
        title = urllib.parse.unquote(b["article"]["value"].split("/wiki/", 1)[1]).replace("_", " ")
        out[b["insee"]["value"]].add(title)
    return out

# ---------------------------------------------------------------- rédaction
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]
def fr_date(iso):
    y, m, d = iso.split("-"); return f"{int(d)}{'er' if d == '01' else ''} {MOIS[int(m) - 1]} {y}"

VOY = "AEIOUYÂÀÉÈÊÎÏÔÛaeiouyâàéèêîïôûh"
def de(c):
    if c.startswith("Le "): return "du " + c[3:]
    if c.startswith("Les "): return "des " + c[4:]
    return ("d'" if c[0] in VOY else "de ") + c
def a_(c):
    if c.startswith("Le "): return "au " + c[3:]
    if c.startswith("Les "): return "aux " + c[4:]
    return "à " + c
def cap(n): return n.title() if n.isupper() else n

def title_for(full, commune, f):
    for t in (f"{full}, {'élue' if f else 'élu'} maire {de(commune)}", f"{full}, maire {de(commune)}",
              f"{full}, maire depuis mars 2026", f"{full.split()[-1]}, maire {de(commune)}"):
        if 4 <= len(t.split()) <= 9: return t
    return None

def write_anecdote(geo, res1, res2, rne, wiki):
    commune = geo["nom"]
    tour2 = bool(res2 and res2["listes"])
    res = res2 if tour2 else res1
    listes = sorted(res["listes"], key=lambda l: -l["voix"])
    win = listes[0]
    f = (rne.get("sexe") == "F") or norm(win.get("sexe")) in ("f", "feminin")
    full = f"{cap(rne['prenom'])} {cap(rne['nom'])}"
    exp = res["exprimes"] or sum(l["voix"] for l in listes)
    pct = 100 * win["voix"] / exp if exp else None
    tour_txt, date = ("au second tour", DATE_T2) if tour2 else ("dès le premier tour", DATE_T1)
    seul = len(listes) == 1
    liste = f"« {win['liste']} »" if win["liste"] else "sa liste"
    sieges = f" et {int(win['sieges'])} sièges au conseil municipal" if win["sieges"] else ""
    total = sum(int(l["sieges"] or 0) for l in listes)
    title = title_for(full, commune, f)
    if not title or pct is None: return None, "titre ou score impossible à construire"

    if seul:
        teaser = (f"Seule liste en présence le {date}, celle de {full} recueille {fr_int(win['voix'])} voix ; "
                  f"{'elle' if f else 'il'} devient maire {de(commune)}.")
    else:
        teaser = (f"Le {date}, la liste de {full} l'emporte {tour_txt} {a_(commune)} avec "
                  f"{fr_pct(pct)} des suffrages exprimés{sieges}.")
    if len(teaser) > 220:
        teaser = f"Le {date}, {full} remporte {tour_txt} l'élection municipale {de(commune)} avec {fr_pct(pct)}."
    lead = (f"{full} a été {'élue' if f else 'élu'} maire {de(commune)} après les élections municipales de mars 2026, "
            + (f"sa liste {liste}, seule en présence, ayant été élue dès le premier tour." if seul else
               f"sa liste {liste} ayant obtenu {fr_pct(pct)} des suffrages exprimés {tour_txt}."))
    p1 = (f"{'Seule liste candidate, elle' if seul else 'La liste ' + liste + ' arrive en tête'} "
          f"{'a recueilli' if seul else 'avec'} {fr_int(win['voix'])} voix le {date}"
          + ((f" et obtient les {total} sièges du conseil municipal." if seul else
              f" et obtient {int(win['sieges'])} des {total} sièges du conseil municipal.") if win["sieges"] and total else "."))
    if not seul:
        def sg(l): return f" et {int(l['sieges'])} siège{'s' if l['sieges'] > 1 else ''}" if l["sieges"] else ""
        adv = listes[1:4]
        if len(adv) == 1:
            l = adv[0]
            p1 += (f" La liste concurrente, conduite par {cap(l['prenom'])} {cap(l['nom'])}, recueille "
                   f"{fr_pct(100 * l['voix'] / exp)} des voix{sg(l)}.")
        else:
            parts = [f"{cap(l['prenom'])} {cap(l['nom'])} ({fr_pct(100 * l['voix'] / exp)}"
                     + (f", {int(l['sieges'])} siège{'s' if l['sieges'] > 1 else ''})" if l["sieges"] else ")") for l in adv]
            p1 += " Les autres listes étaient conduites par " + ", ".join(parts[:-1]) + " et " + parts[-1] + "."
        if len(listes) > 4:
            n = len(listes) - 4
            p1 += f" {n} autre{'s' if n > 1 else ''} liste{'s' if n > 1 else ''} {'étaient' if n > 1 else 'était'} en lice."
    p2 = ""
    if res["inscrits"] and res["votants"]:
        part = 100 * res["votants"] / res["inscrits"]
        p2 = (f"Sur {fr_int(res['inscrits'])} électeurs inscrits, {fr_int(res['votants'])} ont voté, "
              f"soit une participation de {fr_pct(part)}. ")
    p2 += (f"Le conseil municipal nouvellement élu a désigné {full} maire le {fr_date(rne['debut'])}, "
           f"selon le Répertoire national des élus.")
    a = {"category": "politique", "title": title, "label": f"2026 · {commune}", "teaser": teaser,
         "lead": lead, "text": lead, "body": [p1, p2], "more": [], "timeline": None, "links": None,
         "wiki": wk(wiki), "source": WIKI + wk(wiki), "lat": None, "lon": None,
         "access": None, "protection": None}
    return a, None

def check(a):
    pb = []
    if a["category"] not in CATS: pb.append("catégorie")
    if not 4 <= len(a["title"].split()) <= 9: pb.append("titre")
    if len(a["teaser"]) > 220: pb.append("teaser")
    if a["lead"] != a["text"]: pb.append("lead")
    if not 2 <= len(a["body"]) <= 4: pb.append("body")
    if a["source"] != WIKI + a["wiki"]: pb.append("source")
    return pb

# ---------------------------------------------------------------- programme principal
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--t1", required=True); ap.add_argument("--t2", required=True); ap.add_argument("--rne", required=True)
    ap.add_argument("--repo", default="."); ap.add_argument("--cache", default=".cache-generation")
    ap.add_argument("--mapping"); ap.add_argument("--dept", nargs="*", help="limiter à ces départements (ex. 01 2A 971)")
    ap.add_argument("--inspect", action="store_true", help="afficher la lecture des fichiers sans rien écrire")
    ap.add_argument("--commit", action="store_true", help="un commit par département (pas de push)")
    ap.add_argument("--date", default=None, help="date « updated » de l'index (défaut : aujourd'hui)")
    args = ap.parse_args()
    mapping = json.load(open(args.mapping)) if args.mapping else None
    C = lambda n: os.path.join(args.cache, n)

    r1, i1 = parse_results(args.t1, mapping, "T1", C("t1.csv") if args.t1.startswith("http") else None)
    r2, i2 = parse_results(args.t2, mapping, "T2", C("t2.csv") if args.t2.startswith("http") else None)
    rne, irne = parse_rne(args.rne, C("rne.csv") if args.rne.startswith("http") else None)
    if args.inspect:
        for lab, info, res in (("Tour 1", i1, r1), ("Tour 2", i2, r2)):
            print(f"== {lab} : format {info['format']}, {info['communes']} communes")
            print("   colonnes commune :", info["colonnes_commune"]); print("   colonnes liste   :", info["colonnes_liste"])
            k = next(iter(res)); print("   exemple", k, json.dumps(res[k], ensure_ascii=False)[:400])
        print("== RNE :", len(rne), "maires ; colonnes", irne)
        k = next(iter(rne)); print("   exemple", k, rne[k]); return

    geo = load_geo(C("geo.json")); wd = load_wikidata(C("wikidata.json"))
    idx_path = os.path.join(args.repo, "index.json"); index = json.load(open(idx_path))
    known = set(index["communes"])
    from datetime import date as _d
    today = args.date or _d.today().isoformat()
    report, per_dept = [], defaultdict(list)

    for insee in sorted(geo):
        g = geo[insee]; dcode = g.get("departement", {}).get("code") or insee[:2]
        if args.dept and dcode not in args.dept: continue
        def skip(motif): report.append((insee, g["nom"], dcode, "écartée", motif))
        if insee in known: report.append((insee, g["nom"], dcode, "déjà présente", "")); continue
        res1, res2, m = r1.get(insee), r2.get(insee), rne.get(insee)
        if not res1 or not res1["listes"]: skip("absente des résultats du ministère (tour 1)"); continue
        if not m: skip("maire absent du RNE"); continue
        if not m["debut"] or m["debut"] < "2026-03-15": skip(f"RNE non à jour (prise de fonction {m['debut'] or 'inconnue'})"); continue
        res = res2 if res2 and res2["listes"] else res1
        win = max(res["listes"], key=lambda l: l["voix"])
        if not same_person(win["nom"], win["prenom"], m["nom"], m["prenom"]):
            skip(f"maire RNE ({m['prenom']} {m['nom']}) différent de la tête de liste ({win['prenom']} {win['nom']})"); continue
        titles = wd.get(insee, set())
        if len(titles) != 1: skip(f"article Wikipédia de la commune {'introuvable' if not titles else 'ambigu'}"); continue
        a, err = write_anecdote(g, res1, res2, m, next(iter(titles)))
        if err: skip(err); continue
        pb = check(a)
        if pb: skip("contrôle de format : " + ", ".join(pb)); continue
        c = g.get("centre", {}).get("coordinates", [None, None])
        fiche = {"id": insee, "insee": insee, "name": g["nom"], "dept": g.get("departement", {}).get("nom", ""),
                 "kind": "commune", "lat": c[1], "lon": c[0], "anecdotes": [a]}
        s = json.dumps(fiche, ensure_ascii=False, indent=1); assert json.loads(s) == fiche
        open(os.path.join(args.repo, "communes", f"{insee}.json"), "w", encoding="utf-8").write(s + "\n")
        index["communes"][insee] = {"name": g["nom"], "count": 1, "updated": today}
        per_dept[dcode].append(insee); report.append((insee, g["nom"], dcode, "générée", ""))

    json.dump(index, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(idx_path, "a").write("\n")
    with open(os.path.join(args.repo, "rapport-generation.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter=";"); w.writerow(["insee", "commune", "departement", "statut", "motif"]); w.writerows(report)
    st = defaultdict(int)
    for r in report: st[r[3]] += 1
    print("Bilan :", dict(st)); motifs = defaultdict(int)
    for r in report:
        if r[3] == "écartée": motifs[r[4].split(" (")[0]] += 1
    for k, v in sorted(motifs.items(), key=lambda x: -x[1]): print(f"  écartées — {k} : {v}")

    if args.commit:
        git = lambda *a: subprocess.run(["git", "-C", args.repo, *a], check=True)
        for d in sorted(per_dept):
            git("add", *[f"communes/{i}.json" for i in per_dept[d]])
            git("commit", "-qm", f"Phase 1 · département {d} : {len(per_dept[d])} communes (politique 2026)")
        git("add", "index.json"); git("commit", "-qm", f"index.json : {len(index['communes'])} communes")
        print("Commits créés. Vérifiez puis poussez : git push origin main")

if __name__ == "__main__":
    main()
