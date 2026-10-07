import json
W="https://fr.wikipedia.org/wiki/"
def A(cat,title,label,teaser,lead,body,wiki,more=None,timeline=None,lat=None,lon=None,links=None):
    return {"category":cat,"title":title,"label":label,"teaser":teaser,"lead":lead,"text":lead,"body":body,"more":more or [],"timeline":timeline,"links":links,"wiki":wiki,"source":W+wiki,"lat":lat,"lon":lon,"access":None,"protection":None}
L=lambda kind,title,url,note=None:{"kind":kind,"title":title,"url":url,"note":note}

rennes=[
A("politique","Edmond Hervé, vingt-sept ans de mairie et le sang contaminé","1977-2008 · Hôtel de ville",
 "Il a fait basculer Rennes à gauche en 1977 et y est resté vingt-sept ans. Secrétaire d'État à la Santé dans les années 1980, il a été le seul des trois ministres jugés pour le sang contaminé à être déclaré coupable, et dispensé de peine.",
 "Edmond Hervé a été maire de Rennes de 1977 à 2008 et secrétaire d'État à la Santé de 1983 à 1986.",
 ["Universitaire, il prend la mairie à 35 ans et engage la transformation de Rennes : zones d'activité autour de Citroën et de l'électronique, université, et surtout le métro VAL, décidé contre l'avis général pour une ville de 200 000 habitants, ouvert en 2002 et devenu rentable. La métropole a doublé de population en quarante ans.",
  "En 1999, il comparaît devant la Cour de justice de la République avec Laurent Fabius et Georgina Dufoix dans l'affaire du sang contaminé, pour la période 1984-1985 où des hémophiles ont été transfusés avec des produits non chauffés. Fabius et Dufoix sont relaxés ; Hervé est déclaré coupable d'homicide involontaire pour deux victimes, mais dispensé de peine, la Cour relevant la médiatisation excessive qui avait nui à sa défense.",
  "Il reste maire jusqu'en 2008, puis sénateur. Rennes n'a pas changé de bord depuis : Daniel Delaveau, puis Nathalie Appéré."],
 "Edmond_Herv%C3%A9",
 timeline=[{"year":"1977","text":"Élu maire, bascule de Rennes à gauche."},{"year":"1983","text":"Secrétaire d'État à la Santé."},{"year":"1999","text":"Déclaré coupable et dispensé de peine, affaire du sang contaminé."},{"year":"2002","text":"Ouverture du métro VAL."},{"year":"2008","text":"Fin de son dernier mandat."}]),
A("insolite","La plus petite ville du monde à avoir un métro","2002 · Toute la ville",
 "Quand Rennes décide son métro automatique, elle compte 200 000 habitants. Tout le monde prédit un gouffre financier. Vingt ans plus tard, le réseau transporte 150 000 voyageurs par jour et une deuxième ligne a ouvert.",
 "Le métro de Rennes, mis en service le 15 mars 2002, a fait de la ville la plus petite au monde dotée d'un métro à son ouverture.",
 ["Le choix du VAL, métro automatique sans conducteur développé pour Lille, est contesté : trop cher, surdimensionné, inadapté. La ligne a, de Kennedy à La Poterie, coûte environ 400 millions d'euros. Elle atteint pourtant sa fréquentation prévue dès la première année et dépasse aujourd'hui les 130 000 voyageurs quotidiens.",
  "La ligne b, ouverte en septembre 2022 après dix ans de travaux et un chantier compliqué par le sous-sol granitique, dessert la gare, l'université de Villejean et le sud-est. Ses stations ont été confiées à des artistes, et le matériel Cityval est une première mondiale.",
  "Le réseau fonctionne entièrement sans conducteur, avec des rames toutes les minutes en heure de pointe."],
 "M%C3%A9tro_de_Rennes",lat=48.1053,lon=-1.6744),
A("patrimoine","Les maisons à pans de bois rescapées du grand feu","XVe-XVIIe siècle · Place du Champ-Jacquet, rue du Chapitre",
 "Deux cent quatre-vingts maisons de bois ont survécu à l'incendie de 1720. Celles du Champ-Jacquet penchent de façon spectaculaire, celles de la rue du Chapitre sont les plus anciennes de la ville.",
 "Rennes conserve environ 280 maisons à pans de bois, épargnées par l'incendie de 1720 qui détruisit le centre.",
 ["Les plus anciennes, rue Saint-Guillaume et rue du Chapitre, datent du XVe et du XVIe siècle ; la maison dite de Du Guesclin, rue Saint-Guillaume, abrite un restaurant depuis des générations. Place du Champ-Jacquet, un alignement de maisons du XVIIe siècle penche nettement vers l'avant, leurs encorbellements ayant travaillé avec le temps.",
  "La couleur n'est pas d'origine : les colombages étaient autrefois peints ou enduits, et les teintes vives actuelles résultent de campagnes de restauration des années 1980 et 1990, guidées par des analyses de pigments anciens.",
  "Le quartier a été protégé en secteur sauvegardé en 1966, l'un des premiers de France après le Vieux Lyon."],
 "Rennes",lat=48.1120,lon=-1.6790),
A("gastronomie","Le marché des Lices, le samedi matin obligatoire","Depuis 1622 · Place des Lices",
 "Trois cents producteurs, douze mille visiteurs chaque samedi, et une galette-saucisse qu'on mange debout. C'est l'un des plus grands marchés de France, sur l'ancien champ de tournois.",
 "Le marché des Lices se tient chaque samedi matin place des Lices, à Rennes, depuis le XVIIe siècle.",
 ["La place doit son nom aux tournois médiévaux qui s'y tenaient ; Du Guesclin y aurait combattu. Le marché y est installé par ordonnance en 1622. Il compte aujourd'hui près de 300 commerçants et producteurs, sous deux halles métalliques de 1871 et en plein air, et attire plus de 10 000 personnes par semaine.",
  "La galette-saucisse, saucisse grillée roulée dans une galette de blé noir froide, sans beurre ni rien d'autre, se mange debout en faisant la queue ; c'est le rituel du samedi et le symbole de la ville, repris dans les tribunes du Stade rennais.",
  "Le marché est aussi connu pour ses producteurs de légumes du bassin rennais et pour ses fleuristes, installés sous la halle sud."],
 "March%C3%A9_des_Lices",lat=48.1122,lon=-1.6836),
A("faits_divers","La tuerie de la rue du Chapitre reste sans coupable ?","À vérifier",
 "","",[""],"x"),
]
rennes=[a for a in rennes if a["wiki"]!="x"]

bordeaux=[
A("politique","Chaban-Delmas, quarante-huit ans maire de Bordeaux","1947-1995 · Hôtel de ville",
 "Compagnon de la Libération à 29 ans, général à 30, Premier ministre de Pompidou, président de l'Assemblée nationale, candidat malheureux à la présidentielle de 1974 : il a été maire de Bordeaux pendant quarante-huit ans.",
 "Jacques Chaban-Delmas a dirigé Bordeaux de 1947 à 1995, record de longévité pour une grande ville française.",
 ["Résistant, délégué militaire national du général de Gaulle, nommé général de brigade à trente ans, il prend la mairie en 1947 et ne la quittera qu'à 80 ans. Il construit le Bordeaux d'après-guerre : le quartier du Lac, le pont d'Aquitaine, la Cité Mériadeck, l'usine Ford à Blanquefort. Ses adversaires lui reprochent d'avoir laissé le centre historique se couvrir de suie et se vider.",
  "Premier ministre de Georges Pompidou de 1969 à 1972, il lance le projet de « nouvelle société » et des réformes sociales, avant d'être écarté. Candidat à la présidentielle en 1974, il est éliminé au premier tour avec 15 % des voix, distancé par Valéry Giscard d'Estaing : c'est l'un des grands ratages politiques de la Ve République, aggravé par la révélation qu'il ne payait pas d'impôt sur le revenu, légalement, grâce à l'avoir fiscal.",
  "Il préside l'Assemblée nationale à trois reprises et laisse la mairie à Alain Juppé en 1995. Le pont levant de Bordeaux, ouvert en 2013, porte son nom."],
 "Jacques_Chaban-Delmas",lat=44.8378,lon=-0.5792,
 timeline=[{"year":"1944","text":"Général de brigade à 30 ans, délégué militaire national."},{"year":"1947","text":"Élu maire de Bordeaux."},{"year":"1969","text":"Premier ministre."},{"year":"1974","text":"Éliminé au premier tour de la présidentielle."},{"year":"1995","text":"Quitte la mairie après 48 ans."}]),
A("histoire","Les Chartrons, le quartier des négociants du vin","XVIIe-XIXe siècle · Quai des Chartrons",
 "Des marchands anglais, irlandais, hollandais et allemands, souvent protestants, se sont installés hors les murs et ont fait la fortune du vin de Bordeaux. Leurs chais occupent encore les rez-de-chaussée.",
 "Le quartier des Chartrons, le long de la Garonne au nord du centre, a été pendant trois siècles le cœur du négoce du vin de Bordeaux.",
 ["Les négociants étrangers, exclus de la ville intra-muros parce que protestants pour beaucoup, s'installent à partir du XVIIe siècle sur le site d'un ancien couvent de chartreux, d'où le nom. Ils achètent le vin aux châteaux, l'élèvent dans leurs chais, le mettent en bouteille et l'exportent vers l'Angleterre, les Pays-Bas et l'Europe du Nord. Les familles Barton, Johnston, Schröder, Lawton deviennent une aristocratie à part, la « noblesse du bouchon ».",
  "Les hôtels particuliers du cours Xavier-Arnozan et les chais voûtés du quai témoignent de cette prospérité, nourrie aussi par le commerce colonial et la traite, dont Bordeaux fut le deuxième port français après Nantes.",
  "Le quartier s'est effondré avec la crise du négoce dans les années 1970, puis s'est embourgeoisé depuis 2000 : brocantes, galeries, restaurants, et la Cité du Vin ouverte en 2016 à quelques centaines de mètres."],
 "Chartrons",lat=44.8530,lon=-0.5680),
A("patrimoine","Le miroir d'eau, 3 450 m² et un ingénieur têtu","2006 · Place de la Bourse",
 "La plus grande étendue d'eau réfléchissante du monde a été installée face à la façade du XVIIIe siècle contre l'avis des Monuments historiques. Elle est devenue l'image de Bordeaux.",
 "Le miroir d'eau, inauguré en 2006 quai de la Douane, face à la place de la Bourse, alterne deux centimètres d'eau et un brouillard artificiel toutes les quelques minutes.",
 ["L'idée vient du paysagiste Michel Corajoud, chargé de réaménager les quais après le départ des hangars et des voies ferrées. Les Monuments historiques s'inquiètent de l'ajout devant une façade classée de Gabriel ; l'ingénieur fontainier Jean-Max Llorca met au point le système, 800 mètres cubes d'eau filtrée en circuit fermé, qui permet de le vider en quelques minutes.",
  "L'effet, le reflet parfait de la place de la Bourse sur une pellicule d'eau, est devenu la photo la plus prise de Bordeaux et a été copié à Nantes, Lyon et à l'étranger.",
  "Il fonctionne de mai à octobre et s'arrête l'hiver pour éviter le gel. Les enfants s'y baignent, officiellement à leurs risques."],
 "Miroir_d%27eau",lat=44.8412,lon=-0.5695),
A("personnalites","Montesquieu, président au Parlement de Bordeaux","1689-1755 · La Brède et Bordeaux",
 "Avant « L'Esprit des lois », il a été magistrat à Bordeaux pendant dix ans, charge achetée puis revendue parce qu'elle l'ennuyait. Il était aussi viticulteur et vendait son vin aux Anglais.",
 "Charles-Louis de Secondat, baron de La Brède et de Montesquieu, né en 1689 au château de La Brède près de Bordeaux, fut président à mortier au Parlement de Bordeaux de 1716 à 1726.",
 ["Il hérite de la charge de son oncle, siège au Parlement, s'y ennuie et finit par la vendre pour financer ses voyages et son travail. Il est en revanche un propriétaire attentif de ses vignes de La Brède, qu'il vend aux négociants anglais, et tient une correspondance précise sur les prix du vin.",
  "Membre de l'Académie de Bordeaux, il y présente des mémoires scientifiques avant de publier les « Lettres persanes » en 1721, anonymement, puis « L'Esprit des lois » en 1748, où il expose la séparation des pouvoirs qui inspirera les constitutions américaine et françaises.",
  "Le château de La Brède, où il écrivait dans une bibliothèque en berceau, se visite ; son cœur est conservé à Bordeaux, à l'église Saint-Sulpice-et-Sainte-Croix."],
 "Montesquieu",lat=44.6800,lon=-0.5290),
]

idx=json.load(open('index.json'))
for insee,arts in [("35238",rennes),("33063",bordeaux)]:
    p=json.load(open(f'communes/{insee}.json'))
    have={a.get("wiki") for a in p["anecdotes"]}
    p["anecdotes"]+=[a for a in arts if a.get("wiki") not in have]
    json.dump(p,open(f'communes/{insee}.json','w'),ensure_ascii=False,indent=1)
    idx["communes"][insee]["count"]=len(p["anecdotes"])
    print(p["name"],len(p["anecdotes"]))
for k in ("44109","13055"):
    idx["communes"][k]["count"]=len(json.load(open(f'communes/{k}.json'))["anecdotes"])
json.dump(idx,open('index.json','w'),ensure_ascii=False,indent=1)
