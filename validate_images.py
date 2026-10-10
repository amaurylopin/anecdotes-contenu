#!/usr/bin/env python3
"""Audit local, en lecture seule, des références d'images des fiches Anecdotes.

Usage: python3 validate_images.py /root/anecdotes/communes [--strict] [--report images_qa.csv]
Aucun téléchargement ni écriture dans le dépôt ; rapport optionnel hors dépôt.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ALLOWED = {'CC0 1.0', 'CC BY 3.0', 'CC BY 4.0', 'CC BY-SA 3.0', 'CC BY-SA 4.0', 'Domaine public'}
IMAGE_KEYS = ('image', 'images')

def check(ref, file, title, slot):
    problems=[]
    if not isinstance(ref, dict):
        return [('ERROR',file,title,slot,'Référence image non objet')]
    commons=ref.get('commons')
    page=ref.get('page')
    url=ref.get('url')
    if not any(isinstance(x,str) and x.strip() for x in (commons,page,url)):
        problems.append(('ERROR',file,title,slot,'Ni commons, ni page, ni url'))
    if commons is not None and (not isinstance(commons,str) or not commons.strip() or '/' in commons.replace('File:','')):
        problems.append(('ERROR',file,title,slot,'Nom Commons invalide (fichier attendu, pas URL/chemin)'))
    for key in ('page','url'):
        value=ref.get(key)
        if value is not None and (not isinstance(value,str) or urlsplit(value).scheme != 'https' or not urlsplit(value).netloc):
            problems.append(('ERROR',file,title,slot,f'{key} doit être une URL HTTPS absolue'))
    for key in ('caption','credit'):
        if not isinstance(ref.get(key),str) or not ref[key].strip():
            problems.append(('ERROR',file,title,slot,f'{key} manquant'))
    if 'alt' not in ref or not isinstance(ref.get('alt'),str) or not ref['alt'].strip():
        problems.append(('WARN',file,title,slot,'alt absent (à renseigner progressivement)'))
    license_value=ref.get('license')
    if license_value is None:
        problems.append(('WARN',file,title,slot,'license absent, vérifier le crédit et la page source'))
    elif license_value not in ALLOWED:
        problems.append(('WARN',file,title,slot,f'licence non reconnue: {license_value!r}; revue humaine nécessaire'))
    if not isinstance(ref.get('page'),str):
        problems.append(('WARN',file,title,slot,'lien vers la page de licence/source manquant'))
    return problems

def audit(root):
    files=sorted(root.glob('*.json')) if root.is_dir() else [root]
    rows=[]; stats={'files':0,'anecdotes':0,'images':0,'errors':0,'warnings':0}
    for path in files:
        try:
            doc=json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(doc,dict) or not isinstance(doc.get('anecdotes'),list):
                rows.append(('ERROR',str(path),'','', 'anecdotes absent ou invalide'))
                continue
        except Exception as e:
            rows.append(('ERROR',str(path),'','',f'JSON invalide: {e}'))
            continue
        stats['files']+=1
        for item in doc['anecdotes']:
            stats['anecdotes']+=1
            title=item.get('title','') if isinstance(item,dict) else ''
            if not isinstance(item,dict):
                rows.append(('ERROR',str(path),str(title),'','anecdote invalide'))
                continue
            for key in IMAGE_KEYS:
                value=item.get(key)
                if value is None: continue
                refs=[value] if key=='image' else value
                if not isinstance(refs,list):
                    rows.append(('ERROR',str(path),title,key,'images doit être une liste'))
                    continue
                for n,ref in enumerate(refs):
                    stats['images']+=1
                    rows.extend(check(ref,str(path),title,f'{key}[{n}]'))
    stats['errors']=sum(r[0]=='ERROR' for r in rows)
    stats['warnings']=sum(r[0]=='WARN' for r in rows)
    return stats,rows

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',type=Path)
    p.add_argument('--strict',action='store_true',help='sortie 1 si avertissement également')
    p.add_argument('--report',type=Path)
    args=p.parse_args()
    if not args.root.exists(): p.error('chemin inexistant')
    stats,rows=audit(args.root)
    for level,file,title,slot,reason in rows:
        print(f'{level}: {file} :: {title} :: {slot} :: {reason}')
    print('BILAN:',json.dumps(stats,ensure_ascii=False))
    if args.report:
        with args.report.open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(['niveau','fichier','anecdote','placement','problème']);w.writerows(rows)
    return 1 if stats['errors'] or (args.strict and stats['warnings']) else 0
if __name__=='__main__':sys.exit(main())
