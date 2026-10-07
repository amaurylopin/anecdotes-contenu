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

# ---------------------------------------------------------------- ROUBAIX
roubaix=[
A("politique","David Guiraud, maire insoumis de Roubaix","2026 · Hôtel de ville",
 "En mars 2026, le député insoumis David Guiraud remporte Roubaix avec 53,19 % des voix au second tour, dans une ville où moins de quatre électeurs sur dix se sont déplacés.",
 "David Guiraud, La France insoumise, député du Nord, est maire de Roubaix depuis mars 2026, élu au second tour d'une quadrangulaire avec 53,19 % des voix.",
 ["Arrivé en tête du premier tour avec 46,64 %, David Guiraud obtient au second 9 723 voix, devant Alexandre Garcin, divers droite (25,55 %), Karim Amrouni, union de la gauche (11,30 %), et le Rassemblement national (9,97 %). Sa liste détient 41 des 53 sièges.",
  "La participation n'atteint que 37,48 %. Roubaix fait partie, avec Saint-Denis, des villes gagnées par La France insoumise en 2026."],
 "David Guiraud"),
A("faits_divers","Le gang de Roubaix, en 1996","Mars 1996 · Rue Henri-Carette",
 "En 1996, un groupe de jeunes convertis revenus de la guerre de Bosnie multiplie les braquages et pose une voiture piégée à Lille. Le RAID donne l'assaut à leur repaire de Roubaix le 29 mars.",
 "Le gang de Roubaix, groupe islamiste armé formé de jeunes de la région revenus de Bosnie, commet début 1996 des braquages et une tentative d'attentat, avant que la police ne donne l'assaut à sa planque, à Roubaix, le 29 mars 1996.",
 ["Ses membres, dont plusieurs Français convertis, ont combattu aux côtés des musulmans bosniaques. De retour dans le Nord, ils attaquent des supermarchés et des fourgons à l'arme de guerre. Le 28 mars 1996, une voiture piégée est découverte près du commissariat de Lille, à la veille d'un sommet du G7.",
  "Le lendemain, les policiers du RAID encerclent une maison de la rue Henri-Carette, à Roubaix. Après une fusillade, la maison prend feu ; quatre membres du gang meurent. Le chef présumé, Christophe Caze, est tué en Belgique dans sa fuite. Le carnet d'adresses retrouvé sur lui mettra les enquêteurs sur la piste de réseaux djihadistes internationaux.",
  "L'affaire est considérée par les spécialistes comme l'une des premières manifestations en France du djihadisme de retour de zones de combat."],
 "Gang de Roubaix"),
A("patrimoine","La Piscine, un musée dans un bassin Art déco","1932-2001 · Musée La Piscine",
 "Fermée en 1985 pour des raisons de sécurité, la piscine Art déco de Roubaix est devenue en 2001 un musée d'art et d'industrie. Les sculptures sont disposées autour du bassin.",
 "La Piscine, musée d'Art et d'Industrie André-Diligent, occupe depuis 2001 l'ancienne piscine municipale de Roubaix, construite en 1932 dans le style Art déco.",
 ["La piscine, dessinée par l'architecte Albert Baert, est conçue comme un équipement d'hygiène pour les ouvriers du textile, avec bains-douches et vitrail en forme de soleil levant. Elle ferme en 1985, la voûte menaçant de s'effondrer.",
  "La ville décide d'y installer ses collections de beaux-arts et de textiles. Le bassin, conservé et partiellement rempli d'eau, est entouré de sculptures, et le vitrail se reflète dans l'eau. Le musée rappelle le passé de Roubaix, capitale mondiale de la laine au début du XXe siècle."],
 "La Piscine (musée)",
 lat=50.6914,lon=3.1675,access="Musée fermé le lundi"),
A("sport","Paris-Roubaix et ses pavés","Depuis 1896 · Vélodrome de Roubaix",
 "Depuis 1896, la course cycliste Paris-Roubaix traverse les chemins pavés du Nord et s'achève sur le vélodrome de Roubaix. On la surnomme « l'Enfer du Nord ».",
 "Paris-Roubaix, course cycliste d'un jour créée en 1896, se termine sur le vélodrome de Roubaix après une trentaine de secteurs pavés.",
 ["Deux industriels roubaisiens, Théodore Vienne et Maurice Perez, lancent l'épreuve pour faire connaître leur nouveau vélodrome. Les coureurs y parcourent plus de 250 kilomètres, dont plus de cinquante sur des pavés, comme ceux de la tranchée d'Arenberg.",
  "Après la Première Guerre mondiale, des journalistes découvrent une région dévastée et parlent d'« Enfer du Nord », surnom resté attaché à la course. Le vainqueur reçoit un pavé en trophée. Les douches du vélodrome, où chaque cabine porte une plaque au nom d'un vainqueur, font partie de la légende."],
 "Paris-Roubaix"),
]

# ---------------------------------------------------------------- DUNKERQUE
dunkerque=[
A("politique","Patrice Vergriete réélu dès le premier tour","2014-2026 · Hôtel de ville",
 "Maire depuis 2014, Patrice Vergriete a été réélu dès le premier tour en mars 2026 avec 64,47 % des voix, devant une liste d'extrême droite.",
 "Patrice Vergriete, divers centre, maire de Dunkerque depuis 2014, a été réélu au premier tour des municipales de mars 2026 avec 64,47 % des voix.",
 ["Urbaniste de formation, il fait de la gratuité totale des bus de l'agglomération, en 2018, la mesure phare de son action, en septembre 2018.",
  "En mars 2026, sa liste obtient 20 127 voix, devant celle d'Adrien Nave, classée à l'extrême droite (21,24 %), les écologistes (7,11 %) et La France insoumise (5,17 %). Elle détient 45 des 53 sièges."],
 "Patrice Vergriete"),
A("histoire","Opération Dynamo, le miracle de Dunkerque","26 mai-4 juin 1940 · Plages de Malo",
 "Fin mai 1940, encerclés par les Allemands, plus de 330 000 soldats alliés sont évacués des plages de Dunkerque vers l'Angleterre, par des navires de guerre et une flottille de bateaux civils.",
 "Du 26 mai au 4 juin 1940, l'opération Dynamo permet d'évacuer de Dunkerque vers l'Angleterre plus de 330 000 soldats britanniques et français, pris au piège par l'offensive allemande.",
 ["La percée allemande dans les Ardennes coupe les armées alliées en deux. Le corps expéditionnaire britannique et une partie de l'armée française reculent vers Dunkerque, dernier port disponible. Hitler arrête ses blindés pendant deux jours, un répit décisif.",
  "Destroyers, ferries, chalutiers et petits bateaux de plaisance, les « little ships », embarquent les soldats depuis le port et les plages de Malo-les-Bains, sous les bombardements. Les troupes françaises qui tiennent le périmètre permettent le rembarquement ; environ 35 000 d'entre elles sont faites prisonnières. La ville est détruite en grande partie."],
 "Bataille de Dunkerque",
 links=[L("film","« Dunkerque » (2017), de Christopher Nolan","https://fr.wikipedia.org/wiki/Dunkerque_(film,_2017)","Tourné en partie sur la plage de Malo-les-Bains")]),
A("insolite","Le carnaval et le jet de harengs","Février-mars · Place Jean-Bart",
 "Chaque hiver, le carnaval de Dunkerque culmine avec le lancer de harengs saurs depuis le balcon de l'hôtel de ville, devant des milliers de carnavaleux déguisés.",
 "Le carnaval de Dunkerque, né des fêtes que les armateurs offraient aux pêcheurs avant leur départ pour l'Islande, se tient chaque année de janvier à mars et culmine avec le jet de harengs.",
 ["Au XVIIe siècle, avant de partir plusieurs mois pêcher la morue au large de l'Islande, les marins reçoivent un banquet et une fête, la « foye ». La tradition devient un carnaval où les participants défilent en « bandes », costumés, au son des fifres et des tambours.",
  "Le temps fort est le rigodon final autour de la statue du corsaire Jean Bart, né à Dunkerque en 1650, et le lancer de harengs saurs emballés dans du plastique, jetés par le maire et les élus depuis le balcon de l'hôtel de ville."],
 "Carnaval de Dunkerque"),
]

# ---------------------------------------------------------------- BOULOGNE-SUR-MER
boulognesurmer=[
A("politique","Frédéric Cuvillier réélu face au député RN","2008-2026 · Hôtel de ville",
 "Ancien ministre des Transports et de la Mer, le socialiste Frédéric Cuvillier a été réélu dès le premier tour en mars 2026 avec 53,94 %, devant le député RN Antoine Golliot.",
 "Frédéric Cuvillier (PS), maire de Boulogne-sur-Mer depuis 2008, a été réélu au premier tour des municipales de mars 2026 avec 53,94 % des voix.",
 ["Député du Pas-de-Calais, il est ministre délégué aux Transports, à la Mer et à la Pêche de 2012 à 2014 dans les gouvernements Ayrault et Valls.",
  "En mars 2026, sa liste obtient 6 947 voix, contre 4 225 à celle du député Rassemblement national Antoine Golliot (32,81 %) et 13,25 % à la liste divers gauche de Baptiste Legrand. Elle détient 34 sièges."],
 "Frédéric Cuvillier"),
A("histoire","Le camp de Boulogne et la première Légion d'honneur","1803-1805 · Colonne de la Grande Armée",
 "Napoléon rassemble à Boulogne près de 200 000 hommes pour envahir l'Angleterre. L'invasion n'a jamais lieu, mais il y remet en 1804 les premières croix de la Légion d'honneur à ses soldats.",
 "De 1803 à 1805, Boulogne-sur-Mer accueille le camp de la Grande Armée que Napoléon prépare pour envahir l'Angleterre ; le 16 août 1804, il y distribue la Légion d'honneur aux soldats.",
 ["Le Premier consul, puis empereur, fait construire des centaines de barges et entraîner des troupes le long de la côte, face à Douvres. Faute de maîtrise de la Manche, l'invasion est abandonnée à l'été 1805 ; l'armée part vers l'Autriche et remporte la bataille d'Austerlitz.",
  "Le 16 août 1804, sur le plateau de Terlincthun, Napoléon remet les insignes de la Légion d'honneur à des milliers de soldats. Une colonne de la Grande Armée, haute de plus de 50 mètres et surmontée de sa statue, commémore l'épisode."],
 "Camp de Boulogne"),
A("nature","Nausicaá et le premier port de pêche français","Port de Boulogne-sur-Mer",
 "Boulogne-sur-Mer est le premier port de pêche de France en volume débarqué et transformé. La ville abrite aussi Nausicaá, l'un des plus grands aquariums d'Europe.",
 "Boulogne-sur-Mer est le premier centre français de transformation des produits de la mer, et accueille depuis 1991 Nausicaá, centre national de la mer.",
 ["Le port débarque et transforme chaque année des dizaines de milliers de tonnes de poissons, dont une grande partie arrive par camion de toute l'Europe pour y être filetée, fumée ou conditionnée. Le hareng a longtemps fait sa richesse.",
  "Nausicaá, ouvert en 1991 sur le front de mer, a été agrandi en 2018 avec un bassin de 10 000 mètres cubes reproduisant la haute mer, où nagent raies manta et requins."],
 "Nausicaá (centre national de la mer)"),
]

cities=[("59512","Roubaix","Nord",50.6942,3.1746,roubaix),
        ("59183","Dunkerque","Nord",51.0344,2.3768,dunkerque),
        ("62160","Boulogne-sur-Mer","Pas-de-Calais",50.7264,1.6147,boulognesurmer)]
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
