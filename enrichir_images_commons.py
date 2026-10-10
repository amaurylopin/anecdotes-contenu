#!/usr/bin/env python3
"""Anecdotes: validate actual Wikimedia Commons file metadata without downloading photos.

Dry run by default. --apply writes only JSONs with verified Commons references.
Never pushes to Git, never guesses an image, author, or license.
"""
import argparse
import copy
import html
import json
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

API = 'https://commons.wikimedia.org/w/api.php'
ALLOWED = {
    'CC0', 'CC0 1.0', 'CC BY 3.0', 'CC BY 4.0',
    'CC BY-SA 3.0', 'CC BY-SA 4.0', 'Public domain', 'PD', 'Domaine public',
}

def text_plain(value):
    value = re.sub(r'<[^>]+>', ' ', value or '')
    return re.sub(r'\s+', ' ', html.unescape(value)).strip()

def license_name(md):
    raw = text_plain(md.get('LicenseShortName', {}).get('value', ''))
    match = re.search(r'CC\s*BY(?:-SA)?\s*(?:3\.0|4\.0)', raw, re.I)
    if match:
        return re.sub(r'\s+', ' ', match.group(0).upper().replace('BY-SA', 'BY-SA'))
    if raw.upper() in ('CC0', 'CC0 1.0'):
        return 'CC0 1.0'
    if raw in ('PD', 'Public domain', 'Domaine public'):
        return 'Domaine public'
    return None

def fetch_metadata(names, opener=urllib.request.urlopen):
    results = {}
    for start in range(0, len(names), 25):
        batch = names[start:start+25]
        params = urllib.parse.urlencode({
            'action':'query', 'format':'json', 'formatversion':'2',
            'prop':'imageinfo', 'iiprop':'extmetadata|url',
            'redirects':'1', 'titles':'|'.join('File:'+n for n in batch),
        })
        request = urllib.request.Request(API+'?'+params, headers={'User-Agent':'AnecdotesImageAudit/1.0 (non-commercial educational metadata checker)'})
        with opener(request, timeout=25) as response:
            data = json.load(response)
        for page in data.get('query',{}).get('pages',[]):
            title = page.get('title','')
            results[title.removeprefix('File:')] = page.get('imageinfo',[None])[0] if page.get('imageinfo') else None
        # Map aliases/normalized titles back to requested keys through Commons redirects
        by_key = {re.sub(r'[ _]+',' ',k).casefold():v for k,v in results.items()}
        for name in batch:
            if name not in results:
                results[name] = by_key.get(re.sub(r'[ _]+',' ',name).casefold())
    return results

def references(doc):
    for anecdote in doc.get('anecdotes', []):
        if not isinstance(anecdote,dict): continue
        for field in ('image','images'):
            val = anecdote.get(field)
            if isinstance(val,dict): yield anecdote, field, 0, val
            elif isinstance(val,list):
                for i,obj in enumerate(val):
                    if isinstance(obj,dict): yield anecdote, field, i, obj

def process(root, apply=False, metadata=None):
    paths = sorted(root.glob('*.json')) if root.is_dir() else [root]
    docs = {}
    allnames = []
    for path in paths:
        try:
            doc = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(doc,dict): continue
            refs = list(references(doc))
            if refs:
                docs[path] = doc
                for _,_,_,img in refs:
                    n=img.get('commons')
                    if isinstance(n,str) and n.strip():
                        allnames.append(n.removeprefix('File:').replace('_',' ').strip())
        except (OSError, ValueError) as e:
            print('ERROR:',path,e,file=sys.stderr)
    names = sorted(set(allnames))
    print(f'Communes avec images : {len(docs)} | références Commons différentes : {len(names)}')
    if metadata is None:
        metadata = fetch_metadata(names)
    normalized = {re.sub(r'[ _]+',' ',k).casefold():v for k,v in metadata.items()}
    updated = 0; images = 0; unresolved = 0
    for path,doc in docs.items():
        old=copy.deepcopy(doc)
        for anecdote, field, n, img in references(doc):
            raw=img.get('commons')
            if not isinstance(raw,str) or not raw.strip():
                unresolved += 1
                print('SKIP sans nom Commons:', path, anecdote.get('title',''))
                continue
            name=raw.removeprefix('File:').replace('_',' ').strip()
            meta=normalized.get(re.sub(r'[ _]+',' ',name).casefold())
            if not meta:
                unresolved += 1
                print('SKIP introuvable sur Commons:', path, name)
                continue
            md=meta.get('extmetadata',{})
            license_value=license_name(md)
            if license_value not in ALLOWED:
                unresolved += 1
                print('SKIP licence non validée:', path, name, text_plain(md.get('LicenseShortName',{}).get('value','')))
                continue
            source=meta.get('descriptionurl')
            if not isinstance(source,str) or not source.startswith('https://commons.wikimedia.org/wiki/File:'):
                unresolved += 1
                print('SKIP page source manquante:', path, name)
                continue
            img['page'] = source
            img['license'] = license_value
            if not img.get('alt'):
                img['alt'] = img.get('caption') or anecdote.get('title') or name
            if not img.get('credit'):
                author=text_plain(md.get('Artist',{}).get('value',''))
                img['credit']=(author[:180] or 'Auteur indiqué sur Wikimedia Commons')
            images += 1
        if old!=doc:
            updated+=1
            print(('UPDATE' if apply else 'DRY-RUN'), path)
            if apply:
                content=json.dumps(doc,ensure_ascii=False,indent=2)+'\n'
                # atomic write in same directory, safe against interruption
                with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=path.parent,delete=False) as out:
                    out.write(content);tmp=Path(out.name)
                tmp.replace(path)
    print(f'BILAN: {images} images vérifiées via Commons; {unresolved} non vérifiées; {updated} fichiers à modifier; écriture={apply}')
    return 0 if unresolved==0 else 2

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('path',type=Path)
    p.add_argument('--apply',action='store_true',help='modifier les JSON en place après validation Wikimedia')
    a=p.parse_args()
    if not a.path.exists():p.error('chemin inexistant')
    try:sys.exit(process(a.path,a.apply))
    except Exception as e:
        print('ERREUR réseau ou API Wikimedia:',e,file=sys.stderr)
        sys.exit(3)
