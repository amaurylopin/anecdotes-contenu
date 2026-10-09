import glob, json, os, sys, time, urllib.request
sys.path.insert(0, os.path.expanduser("~/anecdotes"))
import anecdotes_commune as a

def commune_au_point(lat, lon):
    url = f"https://geo.api.gouv.fr/communes?lat={lat}&lon={lon}&fields=code&format=json"
    for essai in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "diag-anecdotes"}), timeout=15) as r:
                liste = json.load(r)
            return liste[0]["code"] if liste else ""
        except Exception:
            time.sleep(1 + essai)
    return None

def diagnostiquer(slug):
    fichiers = glob.glob(os.path.expanduser(f"~/anecdotes/contenu/*/*-{slug}.json"))
    if not fichiers:
        print(f"{slug} : fiche introuvable"); return
    d = json.load(open(fichiers[0], encoding="utf-8")); c = d["commune"]
    code, nom = c["code_insee"], c["titre"]
    brut = a.nearby_pages(c["lat"], c["lon"], 5000)
    pages = [n for n in brut if n["title"] != nom and not a.EXCLUDED_TITLES.match(n["title"])][:80]
    dedans = [n["title"] for n in pages if commune_au_point(n["lat"], n["lon"]) == code]
    intros = a.fetch_intros(dedans[:20]) if dedans else {}
    variantes = a.name_variants(a.re.sub(r"\s*\(.*\)$", "", nom))
    citant = [t for t in dedans if a.mentions(variantes, intros.get(t, "")[:800] + " " + t)]
    print(f"\n{nom} : {len(brut)} pages proches, {len(pages)} testées, {len(dedans)} DANS la commune (selon l'API officielle), dont {len(citant)} citent son nom")
    print("  pages dans la commune :", dedans-[:12])

for slug in sys.argv[1:]:
    diagnostiquer(slug)
