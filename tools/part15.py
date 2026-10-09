import json, os
from urllib.parse import quote
W="https://fr.wikipedia.org/wiki/"
def wk(t): return quote(t.replace(" ","_"),safe="_(),-.")
def A(cat,title,label,teaser,lead,body,wiki,more=None,timeline=None,lat=None,lon=None,links=None,access=None,protection=None,status=None):
    w=wk(wiki)
    a={"category":cat,"title":title,"label":label}
    if status: a["status"]=status
    a.update({"teaser":teaser,"lead":lead,"text":lead,"body":body,"more":more or [],"timeline":timeline,"links":links,"wiki":w,"source":W+w,"lat":lat,"lon":lon,"access":access,"protection":protection})
    return a
def L(kind,title,url,note): return {"kind":kind,"title":title,"url":url,"note":note}
def T(*p): return [{"year":y,"text":t} for y,t in p]

# ---------------------------------------------------------------- PAU

tourcoing=[
A("politique","Doriane Becue, l'héritière de Gérald Darmanin","2014-2026 · Hôtel de ville",
 "Gérald Darmanin a été maire de Tourcoing avant d'entrer au gouvernement. Sa successeure, Doriane Becue, a été réélue en mars 2026 avec 55,43 % des voix, face à La France insoumise.",
 "Doriane Becue, divers droite, maire de Tourcoing depuis 2020, a été réélue au second tour des municipales de mars 2026 avec 55,43 % des voix.",
 ["Gérald Darmanin, élu maire en 2014, quitte la mairie en 2017 pour devenir ministre de l'Action et des Comptes publics. Réélu maire en 2020, il la quitte de nouveau quelques semaines plus tard, nommé ministre de l'Intérieur ; son adjointe Doriane Becue lui succède.",
  "En mars 2026, elle obtient 47,64 % au premier tour, puis 12 785 voix au second, devant La France insoumise d'Émilie Croës (24,94 %) et le Rassemblement national de Bastien Verbrugghe (19,64 %). Sa liste détient 42 des 53 sièges. Moins de 36 % des inscrits ont voté."],
 "Gérald Darmanin"),
A("histoire","La bataille de Tourcoing, victoire de 1794","18 mai 1794 · Tourcoing",
 "Le 18 mai 1794, l'armée républicaine bat près de Tourcoing les troupes autrichiennes et britanniques du duc d'York, qui manque d'être capturé. La victoire écarte la menace d'invasion par le Nord.",
 "Le 18 mai 1794, l'armée du Nord de la République remporte la bataille de Tourcoing contre une coalition austro-britannique qui tentait d'encercler ses troupes autour de Lille.",
 ["Au printemps 1794, les coalisés veulent couper l'armée française en Flandre. Les généraux Souham et Moreau, en l'absence de Pichegru, lancent une contre-attaque sur des colonnes ennemies trop dispersées.",
  "Le duc d'York, fils du roi George III, échappe de peu à la capture. Un mois plus tard, la victoire de Fleurus confirme le reflux des coalisés hors de France."],
 "Bataille de Tourcoing"),
]

calais=[
A("politique","Natacha Bouchart réélue face au député RN","2008-2026 · Hôtel de ville",
 "En 2008, Natacha Bouchart met fin à 37 ans de mairie communiste à Calais. En mars 2026, elle est réélue dès le premier tour avec 60,06 %, devant le député RN Marc de Fleurian.",
 "Natacha Bouchart, divers droite, maire de Calais depuis 2008, a été réélue au premier tour des municipales de mars 2026 avec 60,06 % des voix.",
 ["Elle prend la ville en 2008 au communiste Jacky Hénin, alors que le PCF dirigeait Calais depuis 1971. Sénatrice du Pas-de-Calais, elle s'est fait connaître nationalement par ses prises de position sur la présence des migrants.",
  "En mars 2026, sa liste obtient 15 412 voix, contre 7 031 à celle du député Rassemblement national Marc de Fleurian (27,40 %), élu dans la circonscription en 2024. Elle détient 41 sièges."],
 "Natacha Bouchart"),
A("histoire","Les six bourgeois de Calais et Rodin","1347-1895 · Hôtel de ville",
 "En 1347, après onze mois de siège, six notables de Calais se livrent au roi d'Angleterre, la corde au cou, pour sauver la ville. Rodin immortalise leur sacrifice en 1889.",
 "En août 1347, au terme d'un siège de onze mois par le roi d'Angleterre Édouard III, six bourgeois de Calais se livrent au vainqueur pour épargner leurs concitoyens ; leur geste inspire à Auguste Rodin un célèbre groupe sculpté.",
 ["Selon le chroniqueur Jean Froissart, Édouard III exige que six notables lui soient remis en chemise, la corde au cou, avec les clés de la ville. Eustache de Saint-Pierre se porte volontaire le premier. La reine Philippa de Hainaut obtient leur grâce. Calais reste anglaise jusqu'en 1558.",
  "En 1884, la ville commande à Rodin un monument. Il représente les six hommes sans piédestal héroïque, accablés et marchant vers la mort, ce qui déroute le conseil municipal. Le bronze est inauguré en 1895 devant l'hôtel de ville ; d'autres exemplaires se trouvent à Londres, Paris et Tokyo."],
 "Les Bourgeois de Calais",
 lat=50.9510,lon=1.8536),
A("histoire","La « Jungle » de Calais, démantelée en 2016","2015-2016 · Lande de Calais",
 "Au plus fort de la crise migratoire, près de 7 000 personnes vivent dans un bidonville à la sortie de Calais, espérant passer en Angleterre. L'État le démantèle en octobre 2016.",
 "La « Jungle » de Calais, campement de migrants installé sur une lande à l'est de la ville, a abrité jusqu'à plusieurs milliers de personnes avant son démantèlement en octobre 2016.",
 ["Depuis la fermeture du centre de Sangatte en 2002, des exilés venus d'Afghanistan, du Soudan, d'Érythrée ou de Syrie se regroupent à Calais pour tenter de rejoindre le Royaume-Uni, cachés dans des camions ou le tunnel sous la Manche. En 2015, l'État les concentre sur une lande où se forme un bidonville avec écoles, échoppes et lieux de culte.",
  "Fin octobre 2016, les autorités évacuent le camp et répartissent ses occupants dans des centres d'accueil en France. Les tentatives de passage se sont ensuite déplacées vers les traversées en petites embarcations, souvent meurtrières."],
 "Jungle de Calais"),
]

cities=[("59599","Tourcoing","Nord",50.7239,3.1612,tourcoing),
        ("62193","Calais","Pas-de-Calais",50.9513,1.8587,calais)]
idx=json.load(open('index.json'))
for insee,name,dept,lat,lon,arts in cities:
    path=f"communes/{insee}.json"
    if os.path.exists(path):
        p=json.load(open(path)); have={a.get("wiki") for a in p["anecdotes"]}
        p["anecdotes"]+=[a for a in arts if a.get("wiki") not in have]
    else:
        p={"id":insee,"insee":insee,"name":name,"dept":dept,"kind":"commune","lat":lat,"lon":lon,"anecdotes":arts}
    json.dump(p,open(path,'w'),ensure_ascii=False,indent=1)
    idx["communes"][insee]={"name":name,"count":len(p["anecdotes"]),"updated":"2026-10-07"}
    print(name,len(p["anecdotes"]))
json.dump(idx,open('index.json','w'),ensure_ascii=False,indent=1)
print(sum(v["count"] for v in idx["communes"].values()),"articles",len(idx["communes"]),"communes")
