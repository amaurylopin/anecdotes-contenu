import json, sys, os
for code in sys.argv[1:]:
    p = os.path.expanduser(f"~/anecdotes/propositions/{code}.json")
    if not os.path.exists(p):
        print(f"\n##### {code} : pas de proposition (commune protégée ou fiche non retenue)"); continue
    d = json.load(open(p, encoding="utf-8"))
    print(f"\n##### {d['name']} ({d['insee']}) — {len(d['anecdotes'])} articles proposés")
    for a in d["anecdotes"]:
        print(f"\n[{a['category']}] {a['title']}  |  {a['label']}  |  ({a['lat']}, {a['lon']})")
        print("  teaser :", a["teaser"])
        print("  body[0] :", a["body"][0][:260] + ("…" if len(a["body"][0]) > 260 else ""))
        print(f"  {len(a['body'])} paragraphes, 'more' : {len(a['more'])}")
