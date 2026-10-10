#!/usr/bin/env python3
"""
anecdotes_commune.py — génère un dossier Markdown d'anecdotes pour une commune,
sans aucune IA : Wikipédia FR (sections utiles) + Wikidata (personnalités, films,
événements) + pistes de faits divers.

Aucune dépendance externe (bibliothèque standard uniquement). Python 3.8+.

Exemples :
    python anecdotes_commune.py Nantes
    python anecdotes_commune.py Saint-Denis --dept "Seine-Saint-Denis"
    python anecdotes_commune.py "Le Mans" --faits-divers --max-chars 5000
    python anecdotes_commune.py --titre "Aix-en-Provence"

Licences : texte Wikipédia = CC BY-SA 4.0 (citer la source, partage à l'identique) ;
données Wikidata = CC0.
"""

import argparse
import html
import http.client
import json
import re
import time
import threading
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = "ProjetAnecdotes/0.1 (contact: https://github.com/amaurylopin/anecdotes-contenu)"
WIKI_API = "https://fr.wikipedia.org/w/api.php"
SPARQL = "https://query.wikidata.org/sparql"

# Sections de l'article Wikipédia à conserver (titre de niveau 2 contenant l'un de ces mots)
SECTION_KEYWORDS = [
    "histoire", "toponymie", "personnalit", "cinéma", "tournage", "film",
    "légende", "anecdote", "événement", "fait divers", "catastrophe",
    "dans la fiction", "dans les arts", "littérature", "culture populaire",
]
# Sous-sections (niveau 3+) gardées même si leur section parente n'est pas retenue
STRONG_SUB_KEYWORDS = ["cinéma", "film", "tournage", "légende", "anecdote", "fait divers"]

# Mots-clés pour la recherche de pistes de faits divers / événements marquants
FAITS_DIVERS_KEYWORDS = [
    "incendie", "catastrophe", "affaire criminelle", "naufrage",
    "émeute", "épidémie", "bataille", "siège", "explosion",
]


# --------------------------------------------------------------------------- HTTP

MIN_INTERVAL = 0.1  # secondes entre deux requêtes, tous traitements confondus (≈ 10 requêtes/s max)
_rate_lock = threading.Lock()
_last_request = [0.0]


def throttle():
    with _rate_lock:
        wait = _last_request[0] + MIN_INTERVAL - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        _last_request[0] = time.monotonic()


def http_get(url, params, accept="application/json", timeout=60, retries=3):
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": UA, "Accept": accept})
    for attempt in range(retries):
        throttle()
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code in (429, 502, 503, 504) and attempt < retries - 1:
                wait = 3 * (attempt + 1)
                retry_after = err.headers.get("Retry-After") if err.headers else None
                if retry_after and retry_after.isdigit():
                    wait = min(int(retry_after), 60)
                time.sleep(wait)
                continue
            raise
        except (OSError, http.client.HTTPException, ValueError) as err:
            # URLError, TimeoutError, IncompleteRead, JSON tronqué...
            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            if isinstance(err, OSError):
                raise
            # Les appelants rattrapent OSError : on y convertit les autres erreurs réseau
            raise ConnectionError(f"{type(err).__name__}: {err}") from err


API_ERROR_LOG = None  # défini par le mode lot : fichier où sont notées les erreurs renvoyées par l'API
_log_lock = threading.Lock()
TRANSIENT_API_ERRORS = ("ratelimited", "maxlag", "readonly", "internal_api_error", "unknownerror",
                        "timeout", "cirrussearch")


def log_api_error(code, info, params):
    if API_ERROR_LOG is None:
        return
    with _log_lock:
        with open(API_ERROR_LOG, "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%d/%m %H:%M:%S')}\t{params.get('action')}/{params.get('list') or params.get('prop')}"
                     f"\t{code}\t{str(info)[:200]}\n")


def wiki(params):
    """Appel à l'API Wikipédia. L'API répond parfois HTTP 200 avec un corps d'erreur
    (limitation de débit, délai dépassé...) : c'est détecté, retenté, puis remonté en erreur."""
    last = "inconnu"
    max_attempts = 6
    for attempt in range(max_attempts):
        data = http_get(WIKI_API, {**params, "format": "json", "formatversion": 2})
        err = data.get("error") if isinstance(data, dict) else None
        if err is None and isinstance(data, dict) and "query" in data:
            return data
        if err is None:
            err = {"code": "reponse-sans-query", "info": str(list(data.keys()) if isinstance(data, dict) else data)}
        last = err.get("code", "inconnu")
        log_api_error(last, err.get("info", ""), params)
        if attempt < max_attempts - 1 and (last == "reponse-sans-query" or last.startswith(TRANSIENT_API_ERRORS)):
            time.sleep(min(60, 4 * 2 ** attempt))  # 4, 8, 16, 32, 60 s : ≈ 2 min au total
            continue
        break
    raise ConnectionError(f"API Wikipédia : {last}")


def sparql(query):
    data = http_get(SPARQL, {"query": query, "format": "json"},
                    accept="application/sparql-results+json", timeout=90, retries=2)
    return data["results"]["bindings"]


def val(row, key, default=""):
    return row.get(key, {}).get("value", default)


# --------------------------------------------------------------------------- Wikipédia

def fetch_page(title):
    data = wiki({
        "action": "query",
        "prop": "extracts|pageprops|coordinates",
        "coprimary": "primary",
        "explaintext": 1,
        "exsectionformat": "wiki",
        "redirects": 1,
        "ppprop": "wikibase_item",
        "titles": title,
    })
    pages = data.get("query", {}).get("pages", [])
    if not pages or pages[0].get("missing"):
        return None
    page = pages[0]
    coords = (page.get("coordinates") or [{}])[0]
    return {
        "title": page["title"],
        "text": page.get("extract", ""),
        "qid": page.get("pageprops", {}).get("wikibase_item"),
        "lat": coords.get("lat"),
        "lon": coords.get("lon"),
    }


def looks_like_commune(text):
    return "commune" in text[:700].lower()


def find_commune(name, dept=None, forced_title=None):
    if forced_title:
        return fetch_page(forced_title)
    candidates = []
    if dept:
        candidates.append(f"{name} ({dept})")
    candidates.append(name)
    for cand in candidates:
        page = fetch_page(cand)
        if page and looks_like_commune(page["text"]):
            return page
    # Repli : recherche plein texte
    data = wiki({
        "action": "query", "list": "search", "srlimit": 5, "srnamespace": 0,
        "srsearch": f"{name} commune {dept or ''} France".strip(),
    })
    for hit in data.get("query", {}).get("search", []):
        page = fetch_page(hit["title"])
        if page and looks_like_commune(page["text"]):
            return page
    return None


HEADING = re.compile(r"^(={2,6})\s*(.+?)\s*\1\s*$", re.M)


def parse_sections(text):
    matches = list(HEADING.finditer(text))
    intro = text[: matches[0].start()].strip() if matches else text.strip()
    sections = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append({
            "level": len(m.group(1)),
            "title": m.group(2).strip(),
            "text": text[m.end():end].strip(),
        })
    return intro, sections


def select_sections(sections, exclude=()):
    kept, in_kept_top = [], False
    for sec in sections:
        title = sec["title"].lower()
        if sec["level"] == 2:
            in_kept_top = (any(k in title for k in SECTION_KEYWORDS)
                           and not any(x in title for x in exclude))
            if in_kept_top:
                kept.append(sec)
        elif in_kept_top or any(k in title for k in STRONG_SUB_KEYWORDS):
            kept.append(sec)
    return [s for s in kept if s["text"]]


def trim(text, max_chars):
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    end = max(cut.rfind(". "), cut.rfind(".\n"))
    if end > max_chars * 0.5:
        cut = cut[: end + 1]
    return cut.rstrip() + " […]"


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


# --------------------------------------------------------------------------- Wikidata

WIKIDATA_API = "https://www.wikidata.org/w/api.php"


def year_of(date_str):
    m = re.match(r"\+?(-?\d{1,4})", date_str or "")
    return str(int(m.group(1))) if m else ""


def claim_year(claims, props):
    """Année de la première date trouvée parmi les propriétés données."""
    for prop in props:
        for claim in claims.get(prop, []):
            try:
                return year_of(claim["mainsnak"]["datavalue"]["value"]["time"])
            except KeyError:
                continue
    return ""


def ids_by_links(qid, props, limit, min_links=0):
    """Éléments liés à la commune via chaque propriété, triés par notoriété
    (nombre d'articles Wikipédia). Requêtes SPARQL volontairement minimales :
    seulement des identifiants, les libellés viennent ensuite de l'API."""
    found = {}
    for prop, rel in props:
        flt = f"FILTER(?links >= {min_links})" if min_links else ""
        query = f"""
        SELECT ?x ?links WHERE {{
          ?x wdt:{prop} wd:{qid}.
          ?x wikibase:sitelinks ?links.
          {flt}
        }} ORDER BY DESC(?links) LIMIT {limit}
        """
        try:
            rows = sparql(query)
        except (OSError, KeyError, ValueError) as err:
            print(f"  ! Wikidata {prop} indisponible : {err}")
            continue
        for row in rows:
            ident = val(row, "x").rsplit("/", 1)[-1]
            entry = found.setdefault(ident, {"links": int(val(row, "links", "0")), "rels": []})
            if rel and rel not in entry["rels"]:
                entry["rels"].append(rel)
        time.sleep(2)  # ménager Wikidata (limitation de débit)
    return found


def get_entities(ids):
    """Libellé, description et affirmations (dates) pour une liste d'identifiants."""
    ids = list(ids)
    out = {}
    for i in range(0, len(ids), 25):
        chunk = ids[i:i + 25]
        try:
            data = http_get(WIKIDATA_API, {
                "action": "wbgetentities", "ids": "|".join(chunk),
                "props": "labels|descriptions|claims", "languages": "fr",
                "languagefallback": 1, "format": "json",
            })
        except (OSError, ValueError) as err:
            print(f"  ! Wikidata (libellés) indisponible : {err}")
            continue
        for ident, ent in data.get("entities", {}).items():
            out[ident] = {
                "label": ent.get("labels", {}).get("fr", {}).get("value", ""),
                "desc": ent.get("descriptions", {}).get("fr", {}).get("value", ""),
                "claims": ent.get("claims", {}),
            }
        time.sleep(1)
    return out


def query_people(qid):
    found = ids_by_links(
        qid,
        [("P19", "né(e) ici"), ("P20", "mort(e) ici"), ("P551", "a résidé ici")],
        limit=30, min_links=10,
    )
    top = sorted(found.items(), key=lambda kv: -kv[1]["links"])[:25]
    ents = get_entities([ident for ident, _ in top])
    people = []
    for ident, info in top:
        ent = ents.get(ident)
        if not ent or not ent["label"]:
            continue
        people.append({
            "label": ent["label"],
            "desc": ent["desc"],
            "birth": claim_year(ent["claims"], ["P569"]),
            "death": claim_year(ent["claims"], ["P570"]),
            "links": info["links"],
            "rels": info["rels"],
        })
    return people


def query_films(qid):
    found = ids_by_links(
        qid, [("P915", "tourné ici"), ("P840", "se déroule ici")], limit=25,
    )
    top = sorted(found.items(), key=lambda kv: -kv[1]["links"])[:20]
    ents = get_entities([ident for ident, _ in top])
    films = []
    for ident, info in top:
        ent = ents.get(ident)
        if not ent or not ent["label"]:
            continue
        films.append({
            "label": ent["label"],
            "desc": ent["desc"],
            "year": claim_year(ent["claims"], ["P577"]),
            "links": info["links"],
            "rels": info["rels"],
        })
    return films


def query_events(qid):
    found = ids_by_links(qid, [("P276", "")], limit=25)
    top = sorted(found.items(), key=lambda kv: -kv[1]["links"])
    ents = get_entities([ident for ident, _ in top])
    events = []
    for ident, info in top:
        ent = ents.get(ident)
        if not ent or not ent["label"]:
            continue
        events.append({
            "label": ent["label"],
            "desc": ent["desc"],
            "year": claim_year(ent["claims"], ["P585", "P580"]),
            "links": info["links"],
        })

    def sort_key(e):
        try:
            return int(e["year"])
        except ValueError:
            return 99999

    return sorted(events, key=sort_key)


# --------------------------------------------------------------------------- Faits divers

def search_faits_divers(name, dept, own_title):
    seen, results = {own_title}, []
    place = f'"{name}"' + (f" {dept}" if dept else "")
    for kw in FAITS_DIVERS_KEYWORDS:
        try:
            data = wiki({
                "action": "query", "list": "search", "srnamespace": 0, "srlimit": 4,
                "srsearch": f"{place} {kw}",
            })
        except OSError:
            continue
        for hit in data.get("query", {}).get("search", []):
            title = hit["title"]
            if title in seen:
                continue
            seen.add(title)
            results.append({
                "title": title,
                "kw": kw,
                "snippet": strip_tags(hit.get("snippet", "")).strip(),
            })
        time.sleep(0.2)
    return results


# --------------------------------------------------------------------------- Lieux (mode « autour de moi »)

SKIP_SECTION = re.compile(
    r"notes|références|liens externes|voir aussi|bibliographie|galerie|annexes|"
    r"articles connexes|sources|filmographie|discographie")
EXCLUDED_TITLES = re.compile(
    r"^(Liste |Canton |Arrondissement |Communauté |Département |Aire d|Unité urbaine|"
    r"Circonscription|Histoire de |Géographie de |Démographie )")
UNITS = r"(?!\s*(?:m\b|mètres|km\b|habitants|personnes|euros|€|%|kg|hectares|ha\b|tonnes|places|lits|élèves|exemplaires|pièces))"
YEAR4 = re.compile(r"\b(1\d{3}|20[0-2]\d)\b" + UNITS)
YEAR3 = re.compile(r"\b(?:en|vers|dès|depuis|l'an) ([5-9]\d{2})\b" + UNITS)
SIECLE = re.compile(r"\b([IVX]{1,5})(?:e|er|ème)?\s+siècle")
EVENT = re.compile(
    r"\b(construit|édifi|bâti|érigé|fondé|inauguré|détruit|démoli|incendi|rasé|reconstruit|"
    r"assiégé|bombardé|exécuté|emprisonn|guillotiné|signé|installé|transformé|achevé|abandonné|"
    r"converti|démantel|comblé|déplacé|ouvert|fermé|vendu|légué|décapité|pendu|pillé|ravagé|"
    r"occupé|libéré|évacué|naufrag|inondé|effondr|explos)\w*", re.I)
TRACE = re.compile(
    r"(subsist|vestige|\btraces?\b|encore visible|\bvisibles?\b|il (?:ne )?reste|on peut encore|"
    r"emplacement|aujourd.hui|de nos jours|actuellement|occupé par|remplacé par|a laissé)", re.I)
ABBREV = re.compile(r"(?:\b(?:St|Ste|Mgr|Mme|MM|av|apr|env|vol|fig|etc|cf|Bd|Av)\.|\b[A-Z]\.)$")


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


GENERIC_TOKENS = {"saint", "sainte", "st", "ste", "le", "la", "les", "l", "sur", "sous", "en", "de", "du",
                  "des", "d", "aux", "au", "et", "les", "lez", "lès"}


def name_variants(name):
    """Formes sous lesquelles une commune peut être citée :
    « Le Tampon » s'écrit aussi « au Tampon », « La Baule-Escoublac » aussi « La Baule »."""
    full = norm(name)
    variants = {full}
    m = re.match(r"^(le|la|les|l) (.+)$", full)
    bases = [full]
    if m and len(m.group(2)) >= 4:
        variants.add(m.group(2))
        bases.append(m.group(2))
    for base in bases:
        tokens = base.split()
        for k in range(1, len(tokens)):
            prefix_tokens = tokens[:k]
            prefix = " ".join(prefix_tokens)
            if (len(prefix) >= 5 and prefix_tokens[-1] not in GENERIC_TOKENS
                    and not all(t in GENERIC_TOKENS for t in prefix_tokens)):
                variants.add(prefix)
    return variants


def mentions(variants, text):
    padded = f" {norm(text)} "
    return any(f" {v} " in padded for v in variants)


def roman_to_int(r):
    values = {"I": 1, "V": 5, "X": 10}
    total, prev = 0, 0
    for ch in reversed(r):
        v = values[ch]
        total += v if v >= prev else -v
        prev = max(prev, v)
    return total


def find_date(sentence):
    """(libellé, année de tri) de la première date trouvée, sinon None."""
    for pattern in (YEAR4, YEAR3):
        m = pattern.search(sentence)
        if m:
            return m.group(1), int(m.group(1))
    m = SIECLE.search(sentence)
    if m:
        n = roman_to_int(m.group(1))
        if 1 <= n <= 21:
            return m.group(0).strip(), (n - 1) * 100 + 50
    return None


def split_sentences(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?…])\s+(?=[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŒ«\"'(0-9])", text)
    merged = []
    for part in parts:
        if merged and ABBREV.search(merged[-1]):
            merged[-1] += " " + part
        else:
            merged.append(part)
    return [s.strip() for s in merged if s.strip()]


_geo_lock = threading.Lock()


def nearby_pages(lat, lon, radius, limit=300):
    # La géorecherche s'appuie sur le moteur de recherche de Wikipédia, vite saturé :
    # on les envoie une par une, même avec plusieurs traitements en parallèle.
    with _geo_lock:
        data = wiki({
            "action": "query", "list": "geosearch", "gscoord": f"{lat}|{lon}",
            "gsradius": min(radius, 10000), "gslimit": limit, "gsnamespace": 0,
        })
    return data.get("query", {}).get("geosearch", [])


def fetch_intros(titles):
    out = {}
    for i in range(0, len(titles), 20):
        chunk = titles[i:i + 20]
        data = wiki({
            "action": "query", "prop": "extracts", "exintro": 1, "explaintext": 1,
            "exlimit": 20, "titles": "|".join(chunk),
        })
        for p in data.get("query", {}).get("pages", []):
            if p.get("extract"):
                out[p["title"]] = p["extract"]
        time.sleep(0.2)
    return out


def analyse_lieu(place):
    """Fait(s) daté(s) + trace actuelle pour un lieu, à partir de son article Wikipédia."""
    page = fetch_page(place["title"])  # une erreur réseau remonte : la commune sera retentée
    if not page or not page["text"]:
        return None
    intro_text, sections = parse_sections(page["text"])
    texts = [intro_text] + [s["text"] for s in sections if not SKIP_SECTION.search(s["title"].lower())]

    sentences, seen = [], set()
    for text in texts:
        for s in split_sentences(text):
            if 40 <= len(s) <= 380 and s not in seen:
                seen.add(s)
                sentences.append(s)

    scored = []
    for idx, s in enumerate(sentences):
        date = find_date(s)
        if not date:
            continue
        score = 1 + (2 if EVENT.search(s) else 0) + (1 if 70 <= len(s) <= 300 else 0)
        if score >= 3:
            scored.append((-score, idx, date, s))
    scored.sort()
    top = scored[:3]
    faits = [{"date": d[0], "annee": d[1], "texte": s}
             for _, _, d, s in sorted(top, key=lambda t: t[2][1])]
    fact_texts = {f["texte"] for f in faits}

    trace = next((s for s in sentences if TRACE.search(s) and s not in fact_texts), None)
    if not faits and not trace:
        return None

    first = split_sentences(intro_text)
    url = "https://fr.wikipedia.org/wiki/" + urllib.parse.quote(page["title"].replace(" ", "_"))
    return {
        "titre": page["title"],
        "url": url,
        "lat": place["lat"],
        "lon": place["lon"],
        "distance_m": int(place.get("dist", 0)),
        "intro": first[0][:250] if first else "",
        "faits": faits,
        "trace": trace,
        "score": 2 * len(faits) + (2 if trace else 0) + (1 if any(EVENT.search(f["texte"]) for f in faits) else 0),
    }


def collect_lieux(page, commune_name, radius, max_lieux, strict, population=0):
    used_radius = radius
    raw = nearby_pages(page["lat"], page["lon"], radius)
    alerte = None
    if not raw and population >= 3000:
        # Commune étendue dont le point central est loin des lieux d'intérêt : on élargit à 10 km.
        used_radius = 10000
        raw = nearby_pages(page["lat"], page["lon"], used_radius)
        if not raw:
            alerte = "aucune page géolocalisée dans 10 km"
    nearby = [n for n in raw if n["title"] != page["title"] and not EXCLUDED_TITLES.match(n["title"])]
    intros = fetch_intros([n["title"] for n in nearby])
    if len(nearby) >= 4 and len(intros) < 0.5 * len(nearby):
        raise ConnectionError(f"introductions manquantes ({len(intros)} sur {len(nearby)})")
    variants = name_variants(commune_name)

    candidates = []
    for n in nearby:
        intro = intros.get(n["title"], "")
        if not intro:
            continue
        if re.search(r"\bné(?:e)? (?:le|en|à)\b", intro[:250]):
            continue  # article de personne
        if strict and not mentions(variants, intro[:800] + " " + n["title"]):
            continue  # lieu d'une commune voisine
        has_date = 1 if (YEAR4.search(intro) or SIECLE.search(intro)) else 0
        candidates.append((has_date, len(intro), n))
    candidates.sort(key=lambda c: (-c[0], -c[1]))

    lieux = []
    for _, _, place in candidates[: max_lieux * 2]:
        lieu = analyse_lieu(place)
        if lieu:
            lieux.append(lieu)
        time.sleep(0.1)
    lieux.sort(key=lambda l: -l["score"])
    lieux = lieux[:max_lieux]
    diag = {"pages_proches": len(raw), "introductions": len(intros),
            "citant_la_commune": len(candidates), "lieux_retenus": len(lieux), "rayon_m": used_radius}
    if alerte:
        diag["alerte"] = alerte
    return lieux, diag


def build_frise(all_sections, limit=15):
    """Événements datés tirés des sections « Histoire » de la commune."""
    texts, in_hist = [], False
    for sec in all_sections:
        if sec["level"] == 2:
            in_hist = "histoire" in sec["title"].lower()
        if in_hist:
            texts.append(sec["text"])
    scored, seen = [], set()
    for text in texts:
        for s in split_sentences(text):
            if not (40 <= len(s) <= 380) or s in seen:
                continue
            seen.add(s)
            date = find_date(s)
            if not date:
                continue
            score = 1 + (2 if EVENT.search(s) else 0) + (1 if 70 <= len(s) <= 300 else 0)
            if score >= 3:
                scored.append((-score, len(scored), date, s))
    scored.sort()
    top = sorted(scored[:limit], key=lambda t: t[2][1])
    return [{"date": d[0], "annee": d[1], "texte": s} for _, _, d, s in top]


def lieux_markdown(lieux, frise):
    out = []
    if frise:
        out += ["## Frise historique de la commune", ""]
        out += [f"- **{f['date']}** — {f['texte']}" for f in frise]
        out.append("")
    if lieux:
        out += ["## Lieux à découvrir (extraits automatiques de Wikipédia)", ""]
        for l in lieux:
            out += [f"### {l['titre']} ({l['distance_m'] / 1000:.1f} km du centre)", ""]
            if l["intro"]:
                out += [f"_{l['intro']}_", ""]
            for f in l["faits"]:
                out.append(f"- **{f['date']}** — {f['texte']}")
            if l["trace"]:
                out.append(f"- Aujourd'hui : {l['trace']}")
            out.append("")
    return out


# --------------------------------------------------------------------------- Markdown

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "commune"


def span(birth, death):
    if birth and death:
        return f" ({birth}–{death})"
    if birth:
        return f" (né(e) en {birth})"
    return ""


def build_markdown(page, intro, sections, people, films, events, faits_divers, max_chars, max_total,
                   lieux=(), frise=()):
    url = "https://fr.wikipedia.org/wiki/" + urllib.parse.quote(page["title"].replace(" ", "_"))
    out = [f"# {page['title']} — dossier d'anecdotes", ""]
    if intro:
        out += ["## Présentation", "", trim(intro, 1200), ""]

    out += lieux_markdown(lieux, frise)

    used = 0
    for sec in sections:
        room = max_total - used
        if room < 300:
            out += ["_(Sections Wikipédia suivantes omises : plafond --max-total atteint.)_", ""]
            break
        text = trim(sec["text"], min(max_chars, room))
        used += len(text)
        out += [f"{'#' * min(sec['level'], 4)} {sec['title']}", "", text, ""]

    if events:
        out += ["## Événements notables (Wikidata)", ""]
        for e in events:
            year = f"**{e['year']}** — " if e["year"] else ""
            desc = f" : {e['desc']}" if e["desc"] else ""
            out.append(f"- {year}{e['label']}{desc}")
        out.append("")

    if people:
        out += ["## Personnalités liées (Wikidata, par notoriété)", ""]
        for p in people:
            desc = f" — {p['desc']}" if p["desc"] else ""
            out.append(f"- **{p['label']}**{span(p['birth'], p['death'])}{desc} [{', '.join(p['rels'])}]")
        out.append("")

    if films:
        out += ["## Cinéma et fiction (Wikidata)", ""]
        for f in films:
            year = f" ({f['year']})" if f["year"] else ""
            desc = f" — {f['desc']}" if f["desc"] else ""
            out.append(f"- **{f['label']}**{year}{desc} [{', '.join(f['rels'])}]")
        out.append("")

    if faits_divers:
        out += ["## Pistes de faits divers et événements (à vérifier)", "",
                "_Résultats de recherche Wikipédia, bruités : à trier avant utilisation._", ""]
        for r in faits_divers:
            out.append(f"- **{r['title']}** ({r['kw']}) — {r['snippet']}")
        out.append("")

    out += [
        "---",
        f"Source : [Wikipédia]({url}) (texte sous licence CC BY-SA 4.0 ; auteurs dans l'historique "
        "de la page) et Wikidata (données CC0).",
        "",
    ]
    return "\n".join(out)


# --------------------------------------------------------------------------- Main

def histoire_extrait(all_sections, limit=1500):
    """Début des sections « Histoire » de la commune : texte de repli quand il n'y a pas de faits datés."""
    parts, in_hist = [], False
    for sec in all_sections:
        if sec["level"] == 2:
            in_hist = "histoire" in sec["title"].lower()
        if in_hist and sec["text"]:
            parts.append(sec["text"])
    return trim(re.sub(r"\s+", " ", " ".join(parts)).strip(), limit) if parts else ""


def generate(page, name, args, out_dir, stem, write_md=True, dept=None, extra=None):
    """Traite une commune déjà résolue : lieux, frise, Wikidata, puis écrit .json (+ .md)."""
    intro, all_sections = parse_sections(page["text"])

    people = films = events = []
    if page["qid"] and not args.no_wikidata:
        for label, fn in (("personnalités", query_people), ("films", query_films), ("événements", query_events)):
            try:
                result = fn(page["qid"])
            except (OSError, KeyError, ValueError) as err:
                print(f"  ! Wikidata ({label}) indisponible : {err}")
                result = []
            if fn is query_people:
                people = result
            elif fn is query_films:
                films = result
            else:
                events = result
            time.sleep(3)

    # La liste Wikidata remplace la section « Personnalités » de Wikipédia (évite le doublon)
    sections = select_sections(all_sections, exclude=("personnalit",) if people else ())

    lieux, frise, diag = [], build_frise(all_sections), {}
    if not args.no_lieux and page.get("lat") is not None:
        base_name = re.sub(r"\s*\(.*\)$", "", page["title"])
        population = (extra or {}).get("population") or 0
        lieux, diag = collect_lieux(page, base_name, args.rayon, args.max_lieux,
                                    not args.no_strict, population)

    faits_divers = search_faits_divers(name, dept, page["title"]) if args.faits_divers else []

    out_dir.mkdir(parents=True, exist_ok=True)
    md = ""
    if write_md:
        md = build_markdown(page, intro, sections, people, films, events, faits_divers,
                            args.max_chars, args.max_total, lieux, frise)
        (out_dir / f"{stem}.md").write_text(md, encoding="utf-8")

    wiki_url = "https://fr.wikipedia.org/wiki/" + urllib.parse.quote(page["title"].replace(" ", "_"))
    commune = {"titre": page["title"], "qid": page["qid"], "lat": page.get("lat"),
               "lon": page.get("lon"), "url": wiki_url}
    commune.update(extra or {})
    payload = {
        "commune": commune,
        "presentation": trim(re.sub(r"\s+", " ", intro).strip(), 800),
        "histoire_extrait": histoire_extrait(all_sections),
        "frise": frise,
        "lieux": lieux,
        "diagnostic_lieux": diag,
        "personnalites": people,
        "films": films,
        "evenements": events,
        "faits_divers_pistes": faits_divers,
        "licence": "Textes : Wikipédia (CC BY-SA 4.0), données : Wikidata (CC0)",
    }
    json_path = out_dir / f"{stem}.json"
    tmp_path = out_dir / f"{stem}.json.tmp"
    tmp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp_path.replace(json_path)  # écriture atomique : un .json présent est toujours complet
    return {"json": json_path, "md_len": len(md), "lieux": len(lieux), "frise": len(frise),
            "people": len(people), "films": len(films), "events": len(events)}


# --------------------------------------------------------------------------- Mode lot (toute la France)

def load_communes(out_dir):
    cache = out_dir / "_communes.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    print("Téléchargement de la liste officielle des communes (geo.api.gouv.fr)…")
    data = http_get("https://geo.api.gouv.fr/communes", {
        "fields": "nom,code,codeDepartement,population,centre", "format": "json",
    }, timeout=180)
    out_dir.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"  {len(data)} communes.")
    return data


def wikidata_titles(dept, out_dir):
    """code INSEE -> {qid, titre de l'article Wikipédia FR}, pour un département."""
    cache = out_dir / "_wikidata" / f"{dept}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    query = f"""
    SELECT ?insee ?c ?title WHERE {{
      ?c wdt:P374 ?insee.
      FILTER(STRSTARTS(?insee, "{dept}"))
      ?art schema:about ?c ; schema:isPartOf <https://fr.wikipedia.org/> ; schema:name ?title .
    }}
    """
    rows, last_err = None, None
    for attempt in range(3):
        try:
            rows = sparql(query)
            break
        except (OSError, KeyError, ValueError) as err:
            last_err = err
            time.sleep(20 * (attempt + 1))
    if rows is None:
        raise RuntimeError(f"Wikidata indisponible pour le département {dept} : {last_err}")
    mapping = {}
    for row in rows:
        mapping.setdefault(val(row, "insee"), {
            "qid": val(row, "c").rsplit("/", 1)[-1], "titre": val(row, "title"),
        })
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(mapping, ensure_ascii=False), encoding="utf-8")
    time.sleep(2)
    return mapping


def run_lot(args):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    global API_ERROR_LOG

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    API_ERROR_LOG = out_dir / "_erreurs_api.log"
    args.no_wikidata = not args.avec_wikidata
    args.faits_divers = False

    communes = load_communes(out_dir)
    if args.code_dept:
        communes = [c for c in communes if c.get("codeDepartement") == args.code_dept]
    communes = [c for c in communes if (c.get("population") or 0) >= args.min_pop]
    communes.sort(key=lambda c: -(c.get("population") or 0))  # les plus peuplées d'abord
    if args.limite:
        communes = communes[: args.limite]
    if not communes:
        raise SystemExit("Aucune commune ne correspond aux filtres.")

    todo = []
    for c in communes:
        path = out_dir / c["codeDepartement"] / f"{c['code']}-{slugify(c['nom'])}.json"
        if not path.exists():
            todo.append((c, path))
    print(f"{len(communes)} communes ciblées, {len(communes) - len(todo)} déjà faites, {len(todo)} à traiter.")
    if not todo:
        return

    mappings = {}
    for dept in sorted({c["codeDepartement"] for c, _ in todo}):
        print(f"  Titres Wikipédia du département {dept}…")
        try:
            mappings[dept] = wikidata_titles(dept, out_dir)
        except RuntimeError as err:
            print(f"  ! {err} — département ignoré pour cette passe (relancez la commande plus tard).")
    todo = [(c, p) for c, p in todo if c["codeDepartement"] in mappings]
    if not todo:
        raise SystemExit("Aucun département exploitable pour le moment, réessayez plus tard.")

    log_path = out_dir / "_erreurs.log"
    lock = threading.Lock()
    start = time.time()
    done = {"n": 0, "ok": 0, "err": 0}

    def work(item):
        c, path = item
        info = mappings[c["codeDepartement"]].get(c["code"])
        if not info:
            raise LookupError("pas d'article Wikipédia FR relié à ce code INSEE (Wikidata P374)")
        page = fetch_page(info["titre"])
        if not page or not page["text"]:
            raise LookupError(f"article « {info['titre']} » introuvable ou vide")
        page["qid"] = info["qid"]
        coords = (c.get("centre") or {}).get("coordinates")
        if coords and page.get("lat") is None:  # sinon on garde les coordonnées de l'article (le bourg)
            page["lon"], page["lat"] = coords[0], coords[1]
        extra = {"code_insee": c["code"], "departement": c["codeDepartement"],
                 "population": c.get("population")}
        if coords:
            extra["centre_geometrique"] = [coords[1], coords[0]]
        return generate(page, c["nom"], args, path.parent, path.stem, write_md=args.md, extra=extra)

    workers = max(1, min(args.workers, 4))
    executor = ThreadPoolExecutor(max_workers=workers)
    futures = {executor.submit(work, item): item for item in todo}
    try:
        for fut in as_completed(futures):
            c, _ = futures[fut]
            done["n"] += 1
            try:
                res = fut.result()
                done["ok"] += 1
                status = f"{res['lieux']} lieux, {res['frise']} faits de frise"
            except Exception as err:  # une commune en échec ne doit jamais arrêter le lot
                done["err"] += 1
                status = f"ERREUR : {err}"
                with lock:
                    with open(log_path, "a", encoding="utf-8") as fh:
                        fh.write(f"{c['code']}\t{c['nom']}\t{err}\n")
            elapsed = time.time() - start
            remaining = elapsed / done["n"] * (len(todo) - done["n"])
            print(f"[{done['n']}/{len(todo)}] {c['code']} {c['nom']} — {status} "
                  f"(reste ≈ {remaining / 3600:.1f} h)")
    except KeyboardInterrupt:
        print("\nInterruption demandée : arrêt des tâches en cours…")
        executor.shutdown(wait=False, cancel_futures=True)
        print("Relancez la même commande pour reprendre là où le lot s'est arrêté.")
        raise SystemExit(130)
    executor.shutdown()
    print(f"Terminé : {done['ok']} communes générées, {done['err']} erreurs"
          + (f" (voir {log_path})." if done["err"] else "."))


# --------------------------------------------------------------------------- Point d'entrée

def main():
    ap = argparse.ArgumentParser(description="Dossier d'anecdotes pour une commune (Wikipédia + Wikidata).")
    ap.add_argument("commune", nargs="?", help="Nom de la commune (ex. Nantes)")
    ap.add_argument("--dept", help="Département, pour lever une ambiguïté (ex. Loire-Atlantique)")
    ap.add_argument("--titre", help="Titre exact de l'article Wikipédia (court-circuite la recherche)")
    ap.add_argument("--out", default="contenu", help="Dossier de sortie (défaut : contenu)")
    ap.add_argument("--max-chars", type=int, default=1500, help="Taille max par section (défaut : 1500)")
    ap.add_argument("--max-total", type=int, default=12000,
                    help="Taille max cumulée des sections Wikipédia (défaut : 12000)")
    ap.add_argument("--faits-divers", action="store_true", help="Ajouter des pistes de faits divers (bruitées)")
    ap.add_argument("--no-wikidata", action="store_true", help="Ne pas interroger Wikidata")
    ap.add_argument("--no-lieux", action="store_true", help="Ne pas chercher les lieux autour de la commune")
    ap.add_argument("--rayon", type=int, default=5000, help="Rayon de recherche des lieux en mètres (max 10000)")
    ap.add_argument("--max-lieux", type=int, default=25, help="Nombre max de lieux conservés (défaut : 25)")
    ap.add_argument("--no-strict", action="store_true",
                    help="Garder aussi les lieux dont l'introduction ne cite pas la commune")
    lot = ap.add_argument_group("mode lot (toute la France)")
    lot.add_argument("--lot", action="store_true", help="Traiter toutes les communes de France")
    lot.add_argument("--code-dept", help="Limiter à un département par son code (ex. 44, 2A, 971)")
    lot.add_argument("--min-pop", type=int, default=0, help="Population minimale (défaut : 0 = toutes)")
    lot.add_argument("--limite", type=int, help="Ne traiter que les N communes les plus peuplées (test)")
    lot.add_argument("--workers", type=int, default=2, help="Traitements en parallèle, 1 à 4 (défaut : 2)")
    lot.add_argument("--md", action="store_true", help="En lot, écrire aussi les fichiers .md (par défaut : JSON seul)")
    lot.add_argument("--avec-wikidata", action="store_true",
                     help="En lot, ajouter personnalités/films/événements (beaucoup plus lent)")
    args = ap.parse_args()

    if args.lot:
        run_lot(args)
        return

    if not args.commune and not args.titre:
        ap.error("indiquez une commune, --titre ou --lot")
    name = args.commune or args.titre

    page = find_commune(name, args.dept, args.titre)
    if not page:
        raise SystemExit(f"Article de commune introuvable pour « {name} ». Essayez --dept ou --titre.")
    print(f"Article : {page['title']} (Wikidata : {page['qid']})")
    print("  Traitement (lieux autour de la commune, frise, Wikidata)…")

    res = generate(page, name, args, Path(args.out), slugify(page["title"]), write_md=True, dept=args.dept)
    print(f"OK : {res['json'].with_suffix('.md')} et {res['json'].name} ({res['md_len']} caractères, "
          f"{res['lieux']} lieux, {res['frise']} faits de frise, {res['people']} personnalités, "
          f"{res['films']} films, {res['events']} événements)")


if __name__ == "__main__":
    main()
