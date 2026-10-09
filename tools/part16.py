# part16 : intégration des livraisons IA.txt (lots 13 à 34) et des lots 11-12.
# Entrées : IA.txt et lot-11.md / lot-12.md ; la section « Lot 2 » (lignes 4258-5457) est volontairement ignorée.
import json,re
T=open('/mnt/user-data/uploads/IA.txt',encoding='utf-8').read().replace('\r\n','\n')
L=T.split('\n')
dec=json.JSONDecoder()
starts=[0];acc=0
for l in L: acc+=len(l)+1; starts.append(acc)
lineof=lambda p: T.count('\n',0,p)+1
SKIP=(4258,5457)
# 1) toutes les valeurs JSON de premier niveau (début de ligne)
vals=[];p=0
pat=re.compile(r'(?m)^[ \t]*[\{\[]')
while True:
    m=pat.search(T,p)
    if not m: break
    s=m.end()-1
    try:
        o,e=dec.raw_decode(T,s); vals.append((lineof(s),o)); p=e
    except Exception: p=m.end()
heads=[i+1 for i,l in enumerate(L) if l.lstrip().startswith('#')]
fulls={}
for ln,o in vals:
    if SKIP[0]<=ln<=SKIP[1]: continue
    if isinstance(o,dict) and 'anecdotes' in o and 'insee' in o:
        fulls.setdefault(o['insee'],[]).append((ln,o))
ops=[]
for i,l in enumerate(L):
    ln=i+1
    m=re.match(r'^#+\s*(Remplacer|À fusionner) dans communes/(\w{5})\.json(.*)$',l.strip())
    if not m: continue
    nxt=min([h for h in heads if h>ln]+[len(L)+1])
    items=[o for vl,o in vals if ln<vl<nxt]
    ops.append((ln,m.group(1),m.group(2),m.group(3).strip(),items))

import json,re,os,glob

R='/home/claude/repo'
CATS={"histoire","faits_divers","politique","personnalites","patrimoine","insolite","gastronomie","sport","legende","nature"}
idx=json.load(open(f'{R}/index.json'))
def load(i): return json.load(open(f'{R}/communes/{i}.json'))
def save(o): open(f"{R}/communes/{o['insee']}.json",'w').write(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
log=[];changed={}
# lots 11-12 (mes livraisons)
mine={}
for f in ['/mnt/user-data/outputs/lot-11.md','/mnt/user-data/outputs/lot-12.md']:
    for b in re.findall(r'```json\n(.*?)\n```',open(f).read(),re.S):
        o=json.loads(b)
        if 'anecdotes' in o: mine[o['insee']]=(os.path.basename(f),o)
new={k:('IA.txt',v[-1][1]) for k,v in fulls.items()}
new.update(mine)

# --- corrections avant intégration
W='https://fr.wikipedia.org/wiki/'
def fixart(ins,a):
    if ins=='30189' and a['wiki']=='N%C3%AAmes': a['wiki']='N%C3%AEmes'
    a['source']=W+a['wiki']
    return a
for ins,(src,o) in list(new.items()):
    arts=[fixart(ins,a) for a in o['anecdotes']]
    if ins=='94017': arts=[a for a in arts if not (a['category']=='faits_divers' and a['wiki']=='Champigny-sur-Marne')]
    if ins=='93055':
        for a in arts:
            if a['category']=='insolite' and a['wiki']=='Pantin': a['wiki']='Canal_de_l%27Ourcq'; a['source']=W+a['wiki']
    o['anecdotes']=arts
for ln,kind,ins,rest,items in ops:
    for it in items:
        for a in (it if isinstance(it,list) else [it]): fixart(ins,a)

for ins,(src,o) in new.items():
    if os.path.exists(f'{R}/communes/{ins}.json'):
        cur=load(ins); w={a['wiki'] for a in cur['anecdotes']}
        add=[a for a in o['anecdotes'] if a['wiki'] not in w]
        cur['anecdotes']+=add; save(cur); log.append(f'FUSION {ins} +{len(add)}')
    else:
        save(o)
    changed[ins]=src
for ln,kind,ins,rest,items in ops:
    flat=[]
    for it in items: flat+= it if isinstance(it,list) else [it]
    cur=load(ins); ws=[a['wiki'] for a in cur['anecdotes']]
    if kind=='Remplacer':
        m=re.search(r'wiki\s*:\s*([^)\s—]+)',rest); target=m.group(1).replace('\\_','_') if m else None
        if ins=="30189": target="N%C3%AEmes"
        a=flat[0]
        if target in ws: i=ws.index(target); how='wiki'
        else:
            pol=[k for k,x in enumerate(cur['anecdotes']) if x['category']==a['category']]
            i=pol[0] if pol else None; how='repli catégorie'
        if i is None: cur['anecdotes'].append(a); log.append(f'REMPL {ins} cible {target} introuvable -> ajout')
        else:
            old=cur['anecdotes'][i]['wiki']; cur['anecdotes'][i]=a
            if how!='wiki': log.append(f'REMPL {ins} cible {target} absente, remplacé {old} ({how})')
    else:
        for a in flat:
            if a['wiki'] in ws: log.append(f'DOUBLON ignoré {ins} {a["wiki"]}')
            else: cur['anecdotes'].append(a); ws.append(a['wiki'])
    # doublons de wiki après remplacement
    neww={a['wiki'] for a in flat}
    seen=set();ded=[]
    for a in cur['anecdotes']:
        if a['wiki'] in seen and a['wiki'] in neww: log.append(f'DOUBLON retiré {ins} {a["wiki"]}'); continue
        seen.add(a['wiki']); ded.append(a)
    cur['anecdotes']=ded; save(cur); changed.setdefault(ins,'IA.txt (audit)')
# validation
errs=[]
for ins in changed:
    o=load(ins)
    if not any(a['category']=='politique' for a in o['anecdotes']): errs.append((ins,'pas de politique'))
    for a in o['anecdotes']:
        t=a.get('title','')
        if a.get('category') not in CATS: errs.append((ins,'cat',a.get('category')))
        if not 4<=len(t.split())<=9: errs.append((ins,'titre',len(t.split()),t))
        if t.endswith('.'): errs.append((ins,'point',t))
        if len(a.get('teaser',''))>220: errs.append((ins,'teaser',len(a['teaser']),t))
        if not 2<=len(a.get('body',[]))<=4: errs.append((ins,'body',len(a.get('body',[])),t))
        if a.get('category')=='personnalites' and not (a.get('timeline') and 3<=len(a['timeline'])<=5): errs.append((ins,'timeline',t))
        if a.get('lead')!=a.get('text'): errs.append((ins,'lead!=text',t))
        if a.get('source')!='https://fr.wikipedia.org/wiki/'+a.get('wiki',''): errs.append((ins,'source',t))
    pols=[a['title'] for a in o['anecdotes'] if a['category']=='politique']
    if len(pols)>1: log.append(f'PLUSIEURS POLITIQUE {ins}: {pols}')
for ins in changed:
    o=load(ins); idx['communes'][ins]={'name':o['name'],'count':len(o['anecdotes']),'updated':'2026-10-08'}
open(f'{R}/index.json','w').write(json.dumps(idx,ensure_ascii=False,indent=1)+'\n')
print('communes touchées',len(changed),'| index',len(idx['communes']))
print('\n'.join(log)); print('ERREURS',len(errs))
for e in errs: print(e)

# --- contrôle limité aux articles nouveaux
newarts=[]
for ins,(src,o) in new.items(): newarts+= [(ins,a) for a in o['anecdotes']]
for ln,kind,ins,rest,items in ops:
    for it in items: newarts+= [(ins,a) for a in (it if isinstance(it,list) else [it])]
print('--- articles nouveaux :',len(newarts))
for ins,a in newarts:
    t=a.get('title','');pb=[]
    if a.get('category') not in CATS: pb.append('cat')
    if not 4<=len(t.split())<=9: pb.append(f'titre {len(t.split())} mots')
    if len(a.get('teaser',''))>220: pb.append(f"teaser {len(a['teaser'])}")
    if not 2<=len(a.get('body',[]))<=4: pb.append('body')
    if a.get('category')=='personnalites' and not (a.get('timeline') and 3<=len(a['timeline'])<=5): pb.append('timeline')
    if a.get('lead')!=a.get('text'): pb.append('lead!=text')
    if a.get('source')!='https://fr.wikipedia.org/wiki/'+a.get('wiki',''): pb.append('source: '+str(a.get('source'))[:60])
    if pb: print(ins,t[:60],pb)
