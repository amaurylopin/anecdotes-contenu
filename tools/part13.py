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

# ---------------------------------------------------------------- PARIS
paris=[
A("politique","Emmanuel Grégoire, maire de Paris face à Rachida Dati","1977-2026 · Hôtel de Ville",
 "En mars 2026, l'ancien premier adjoint d'Anne Hidalgo bat Rachida Dati avec 50,52 % des voix. La gauche garde Paris, qu'elle dirige depuis 2001, après Jacques Chirac et Jean Tiberi.",
 "Emmanuel Grégoire, socialiste, à la tête d'une liste d'union de la gauche et des écologistes, est maire de Paris depuis mars 2026, élu au second tour avec 50,52 % des voix.",
 ["Jacques Chirac devient en 1977 le premier maire de Paris élu depuis 1871 et le reste jusqu'à son élection à l'Élysée en 1995 ; Jean Tiberi lui succède. En 2001, le socialiste Bertrand Delanoë fait basculer la capitale. Le 5 octobre 2002, pendant la première Nuit blanche, il est poignardé dans l'Hôtel de Ville par un homme hostile aux homosexuels et aux politiques, et survit. Anne Hidalgo lui succède en 2014.",
  "Le scrutin de mars 2026 est le premier organisé après la réforme du mode d'élection à Paris, Lyon et Marseille. Emmanuel Grégoire arrive en tête du premier tour avec 37,98 %, devant Rachida Dati, maire du 7e arrondissement et ancienne garde des Sceaux (25,46 %).",
  "Au second tour, malgré la fusion de la liste Dati avec celle de Pierre-Yves Bournazel, il obtient 428 143 voix, contre 351 825 à Rachida Dati (41,52 %) et 67 464 à Sophia Chikirou, La France insoumise (7,96 %). Sa liste détient 103 des 163 sièges du Conseil de Paris."],
 "Emmanuel Grégoire"),
A("faits_divers","13 novembre 2015, la nuit des attentats","13 novembre 2015 · Bataclan et terrasses",
 "Le 13 novembre 2015, trois commandos djihadistes frappent le Stade de France, des terrasses de l'Est parisien et le Bataclan. 130 personnes sont tuées. Salah Abdeslam est condamné en 2022 à la perpétuité incompressible.",
 "Le soir du 13 novembre 2015, des attaques coordonnées revendiquées par l'État islamique tuent 130 personnes à Saint-Denis et à Paris, dont 90 dans la salle de concert du Bataclan : ce sont les attentats les plus meurtriers commis en France depuis la Seconde Guerre mondiale.",
 ["À 21 h 20, un premier kamikaze se fait exploser aux abords du Stade de France pendant un match France-Allemagne. Un commando mitraille ensuite les terrasses de bars et de restaurants des 10e et 11e arrondissements, tandis qu'un autre prend d'assaut le Bataclan pendant un concert des Eagles of Death Metal. L'assaut de la BRI met fin à la prise d'otages peu après minuit.",
  "L'état d'urgence est déclaré. Le coordinateur présumé, Abdelhamid Abaaoud, est tué le 18 novembre lors de l'assaut du RAID à Saint-Denis.",
  "Le procès, dit V13, se tient de septembre 2021 à juin 2022 devant une cour d'assises spéciale, avec près de 2 600 parties civiles. Le 29 juin 2022, Salah Abdeslam, seul membre survivant des commandos, est condamné à la réclusion criminelle à perpétuité incompressible ; il n'a pas fait appel."],
 "Attentats du 13 novembre 2015 en France",
 status="Salah Abdeslam : condamnation à la perpétuité incompressible du 29 juin 2022, devenue définitive en l'absence d'appel."),
A("faits_divers","Le vol de la Joconde en 1911","21 août 1911 · Musée du Louvre",
 "Le 21 août 1911, un vitrier italien décroche la Joconde et sort du Louvre avec le tableau sous sa blouse. On ne la retrouve qu'en 1913, à Florence. Apollinaire est un temps soupçonné.",
 "Le 21 août 1911, « La Joconde » de Léonard de Vinci est volée au musée du Louvre par Vincenzo Peruggia, un ouvrier italien qui y avait travaillé ; elle est retrouvée à Florence en décembre 1913.",
 ["Peruggia, qui avait participé à la pose de vitres de protection, se cache dans le musée un lundi de fermeture, décroche le tableau, le sort de son cadre et quitte le Louvre en le dissimulant. La disparition n'est remarquée que le lendemain.",
  "L'enquête piétine. Le poète Guillaume Apollinaire est incarcéré quelques jours pour une affaire de statuettes volées au Louvre, et Pablo Picasso est interrogé. Pendant deux ans, le tableau reste caché dans la chambre de Peruggia, à Paris.",
  "En décembre 1913, Peruggia tente de le vendre à un antiquaire de Florence, qui prévient la police. Il affirme avoir voulu rendre l'œuvre à l'Italie. Le retentissement du vol a largement contribué à la célébrité mondiale du tableau."],
 "Vol de La Joconde"),
A("patrimoine","Notre-Dame, l'incendie et la renaissance","15 avril 2019 · Île de la Cité",
 "Le 15 avril 2019, un incendie détruit la charpente de Notre-Dame et fait tomber la flèche de Viollet-le-Duc devant des millions de téléspectateurs. La cathédrale rouvre en décembre 2024.",
 "Le soir du 15 avril 2019, un incendie ravage la toiture de la cathédrale Notre-Dame de Paris ; la flèche s'effondre, mais la structure et les tours sont sauvées par les pompiers.",
 ["Le feu se déclare vers 18 h 20 dans les combles, pendant des travaux de restauration. La charpente médiévale, surnommée « la forêt », brûle entièrement. À 19 h 50, la flèche dessinée par Viollet-le-Duc au XIXe siècle s'effondre. Les pompiers de Paris parviennent à sauver le beffroi nord, et la couronne d'épines est évacuée.",
  "L'enquête écarte la piste criminelle et privilégie un accident, mégot ou défaillance électrique, sans en établir la cause exacte. Une souscription réunit plus de 800 millions d'euros de dons. La flèche est reconstruite à l'identique et la cathédrale rouvre au culte et au public le 7 décembre 2024."],
 "Incendie de Notre-Dame de Paris",
 lat=48.8530,lon=2.3499,access="Entrée libre",protection="Monument historique classé, patrimoine mondial de l'Unesco"),
]

# ---------------------------------------------------------------- VERSAILLES
versailles=[
A("politique","François de Mazières réélu dès le premier tour","2008-2026 · Hôtel de ville",
 "Maire de Versailles depuis 2008, François de Mazières a été réélu dès le premier tour en mars 2026 avec 64,56 % des voix, très loin devant l'union des droites.",
 "François de Mazières, divers droite, maire de Versailles depuis 2008, a été réélu au premier tour des municipales de mars 2026 avec 64,56 % des voix.",
 ["Ancien président de la Cité de l'architecture et du patrimoine, il a aussi été député des Yvelines de 2012 à 2022.",
  "En mars 2026, sa liste obtient 20 626 voix, devant l'union des droites d'Olivier de La Faire (15,49 %) et plusieurs listes de gauche sous les 6 %. Elle détient 46 des 53 sièges."],
 "François de Mazières"),
A("faits_divers","L'affaire du collier de la reine","1785 · Château de Versailles",
 "En 1785, une aventurière fait croire au cardinal de Rohan que Marie-Antoinette veut un collier de diamants hors de prix. L'escroquerie éclabousse la reine, pourtant innocente, à quatre ans de la Révolution.",
 "L'affaire du collier, révélée en août 1785, est une escroquerie montée par Jeanne de La Motte, qui convainc le cardinal de Rohan d'acheter pour Marie-Antoinette un collier de diamants que la reine n'a jamais commandé.",
 ["Les joailliers Boehmer et Bassenge cherchent à vendre un collier extravagant, conçu pour Madame du Barry. Jeanne de La Motte, se disant proche de la reine, persuade le cardinal de Rohan, en disgrâce, qu'il pourra regagner la faveur royale en servant d'intermédiaire. Une rencontre nocturne est même organisée dans les jardins de Versailles avec une jeune femme déguisée en reine.",
  "Rohan remet le collier, qui est aussitôt dépecé et ses diamants vendus à Londres. Quand les joailliers réclament leur paiement à la reine, le scandale éclate : le cardinal est arrêté en habits pontificaux le 15 août 1785, dans la galerie des Glaces.",
  "En 1786, le parlement de Paris acquitte Rohan et condamne Jeanne de La Motte à être fouettée et marquée au fer. L'opinion retient surtout la réputation d'une reine dépensière, ce qui pèse sur la monarchie."],
 "Affaire du collier de la reine"),
A("histoire","La galerie des Glaces, de 1871 à 1919","1871-1919 · Galerie des Glaces",
 "Le 18 janvier 1871, l'Empire allemand est proclamé dans la galerie des Glaces. Le 28 juin 1919, l'Allemagne vaincue y signe le traité de Versailles, au même endroit.",
 "La galerie des Glaces du château de Versailles a été le théâtre de la proclamation de l'Empire allemand en 1871 puis de la signature du traité de paix de 1919.",
 ["Pendant le siège de Paris, le roi de Prusse Guillaume Ier est proclamé empereur d'Allemagne dans la galerie, le 18 janvier 1871, en présence de Bismarck. Le choix du lieu, symbole de la puissance de Louis XIV, est vécu comme une humiliation par la France.",
  "Clemenceau impose la même salle pour la signature du traité de paix, le 28 juin 1919, cinq ans jour pour jour après l'attentat de Sarajevo. Le traité retire à l'Allemagne l'Alsace-Moselle et ses colonies, et lui impose de lourdes réparations, que l'historiographie a souvent associées à la montée du nazisme."],
 "Traité de Versailles",
 lat=48.8049,lon=2.1204,access="Château de Versailles, fermé le lundi",protection="Monument historique classé, patrimoine mondial de l'Unesco"),
]

# ---------------------------------------------------------------- SAINT-DENIS
saintdenis=[
A("politique","Bally Bagayoko, l'insoumis qui conquiert Saint-Denis","2025-2026 · Hôtel de ville",
 "En mars 2026, l'insoumis Bally Bagayoko bat dès le premier tour le maire socialiste Mathieu Hanotin. La France insoumise remporte sa première ville de plus de 100 000 habitants.",
 "Bally Bagayoko, La France insoumise, est maire de Saint-Denis depuis mars 2026, élu au premier tour avec 50,77 % des voix contre le maire sortant Mathieu Hanotin.",
 ["Bastion communiste pendant des décennies, Saint-Denis est dirigée depuis 2020 par le socialiste Mathieu Hanotin. Au 1er janvier 2025, elle fusionne avec Pierrefitte-sur-Seine pour former une commune nouvelle d'environ 150 000 habitants, la plus peuplée de la Seine-Saint-Denis.",
  "Ancien basketteur et ancien adjoint au maire, Bally Bagayoko obtient 13 506 voix au premier tour, contre 8 698 à Mathieu Hanotin (32,70 %). Sa liste détient 47 des 59 sièges. C'est la première ville de plus de 100 000 habitants gagnée par La France insoumise."],
 "Saint-Denis (Seine-Saint-Denis)"),
A("faits_divers","L'assaut du RAID rue du Corbillon","18 novembre 2015 · Rue du Corbillon",
 "Cinq jours après les attentats du 13 Novembre, le RAID donne l'assaut à un immeuble du centre de Saint-Denis. Abdelhamid Abaaoud, coordinateur présumé des attaques, est tué.",
 "Le 18 novembre 2015 à l'aube, le RAID donne l'assaut à un appartement du 8 rue du Corbillon, à Saint-Denis, où se cachent Abdelhamid Abaaoud et un complice, qui préparaient un nouvel attentat.",
 ["Le 13 novembre, trois kamikazes s'étaient fait exploser aux abords du Stade de France, à Saint-Denis, tuant un passant. Grâce à un témoignage, les enquêteurs localisent Abaaoud dans un appartement de la ville. L'assaut, lancé vers 4 h 20, dure plusieurs heures ; plus de 5 000 munitions sont tirées.",
  "Abaaoud, sa cousine et un troisième homme sont tués, l'un d'eux en déclenchant une ceinture explosive. L'homme qui avait hébergé les terroristes, Jawad Bendaoud, est jugé ; d'abord relaxé en 2018, il est condamné en appel en 2019 à quatre ans de prison pour recel de malfaiteurs terroristes."],
 "Assaut de Saint-Denis"),
A("patrimoine","La basilique de Saint-Denis, nécropole des rois","XIIe siècle · Basilique",
 "Quarante-trois rois et trente-deux reines ont été inhumés à Saint-Denis. En 1793, les révolutionnaires ouvrent les tombeaux et jettent les dépouilles dans des fosses communes.",
 "La basilique de Saint-Denis, reconstruite au XIIe siècle par l'abbé Suger, est considérée comme le premier grand édifice gothique ; elle a servi de nécropole aux rois de France pendant plus de mille ans.",
 ["Suger, conseiller de Louis VI et de Louis VII, fait reconstruire le chœur à partir de 1140 avec de grandes baies vitrées et des voûtes sur croisées d'ogives : c'est l'acte de naissance de l'architecture gothique.",
  "De Dagobert à Louis XVIII, la plupart des rois de France y sont inhumés. En 1793, la Convention ordonne la destruction des tombeaux ; les corps sont jetés dans des fosses. Sous la Restauration, les ossements sont rassemblés dans un ossuaire de la crypte, où reposent aussi les restes de Louis XVI et de Marie-Antoinette."],
 "Basilique Saint-Denis",
 lat=48.9356,lon=2.3597,access="Nécropole royale, Centre des monuments nationaux",protection="Monument historique classé"),
]

# ---------------------------------------------------------------- MONTREUIL
montreuil=[
A("politique","Patrice Bessac réélu dès le premier tour à Montreuil","1984-2026 · Hôtel de ville",
 "Maire depuis 2014, l'ancien communiste Patrice Bessac a été réélu dès le premier tour en mars 2026 avec 57,72 % des voix, devant La France insoumise.",
 "Patrice Bessac, union de la gauche, maire de Montreuil depuis 2014, a été réélu au premier tour des municipales de mars 2026 avec 57,72 % des voix.",
 ["Montreuil a été dirigée par le communiste Jean-Pierre Brard de 1984 à 2008, puis par l'écologiste Dominique Voynet, ancienne ministre de l'Environnement et candidate à l'élection présidentielle, de 2008 à 2014.",
  "En mars 2026, la liste de Patrice Bessac obtient 17 834 voix, devant celle de La France insoumise menée par Sayna Shahryari (22,56 %) et celle des Républicains (8,89 %). Elle détient 45 sièges."],
 "Patrice Bessac"),
A("insolite","Méliès invente le studio de cinéma à Montreuil","1897 · Studio de Montreuil",
 "En 1897, Georges Méliès construit dans sa propriété de Montreuil un atelier vitré : c'est le premier studio de cinéma. Il y tourne « Le Voyage dans la Lune » en 1902.",
 "Georges Méliès fait construire en 1897, dans sa propriété de Montreuil-sous-Bois, un atelier de prise de vues entièrement vitré, considéré comme le premier studio de cinéma au monde.",
 ["Illusionniste, propriétaire du théâtre Robert-Houdin à Paris, Méliès assiste en 1895 à la première projection des frères Lumière. Il se lance dans le cinéma et, pour contrôler la lumière et les décors, bâtit à Montreuil un studio de 17 mètres de long, avec des machineries de théâtre.",
  "Il y tourne plusieurs centaines de films, dont « Le Voyage dans la Lune » (1902), avec sa fusée plantée dans l'œil de la Lune. Ruiné par la concurrence, il détruit une grande partie de ses films et finit marchand de jouets à la gare Montparnasse. Le studio a été démoli, mais une plaque et une salle de cinéma, le Méliès, rappellent son souvenir."],
 "Georges Méliès",
 links=[L("film","« Le Voyage dans la Lune » (1902), de Georges Méliès","https://fr.wikipedia.org/wiki/Le_Voyage_dans_la_Lune","Tourné dans le studio de Montreuil"),
        L("film","« Hugo Cabret » (2011), de Martin Scorsese","https://fr.wikipedia.org/wiki/Hugo_Cabret","Un hommage à Méliès et à ses dernières années")]),
]

# ---------------------------------------------------------------- BOULOGNE-BILLANCOURT
boulogne=[
A("politique","Pierre-Christophe Baguet réélu face à la droite dissidente","2007-2026 · Hôtel de ville",
 "Maire depuis 2007, Pierre-Christophe Baguet a été réélu en mars 2026 avec 52,13 % des voix, face à une liste de droite concurrente menée par Antoine de Jerphanion.",
 "Pierre-Christophe Baguet, Les Républicains, maire de Boulogne-Billancourt depuis 2007, a été réélu au second tour des municipales de mars 2026 avec 52,13 % des voix.",
 ["Ancien député des Hauts-de-Seine, il succède en 2007 à Jean-Pierre Fourcade, ancien ministre de l'Économie et des Finances de Valéry Giscard d'Estaing.",
  "En mars 2026, il obtient 47,02 % au premier tour, puis 19 168 voix au second, contre 12 389 à Antoine de Jerphanion, divers droite (33,69 %), et 14,18 % à l'union de la gauche de Pauline Rapilly-Ferniot. Sa liste détient 42 des 55 sièges."],
 "Pierre-Christophe Baguet"),
A("histoire","Renault Billancourt, la forteresse ouvrière","1898-1992 · Île Seguin",
 "Louis Renault construit sa première voiture à Billancourt en 1898. Bombardée en 1942, nationalisée en 1945, l'usine devient le symbole de la classe ouvrière jusqu'à sa fermeture en 1992.",
 "Les usines Renault de Billancourt, nées en 1898 dans le jardin familial de Louis Renault, ont été pendant près d'un siècle le principal site industriel de la région parisienne.",
 ["Louis Renault assemble sa première voiturette en 1898 et fonde avec ses frères une entreprise qui couvre bientôt l'île Seguin. Pendant l'Occupation, l'usine travaille pour l'armée allemande : le 3 mars 1942, un bombardement de la RAF la vise et fait plusieurs centaines de morts parmi les habitants de Boulogne. Louis Renault, accusé de collaboration, meurt en prison en 1944 avant d'être jugé ; l'entreprise est nationalisée en 1945.",
  "Avec plus de 30 000 salariés à son apogée, Billancourt est le cœur des grandes grèves de 1936, 1947 et 1968. La formule attribuée à Jean-Paul Sartre, « il ne faut pas désespérer Billancourt », en fait le symbole du monde ouvrier. Le site ferme en 1992 ; l'île Seguin accueille aujourd'hui la Seine musicale."],
 "Usine Renault de Boulogne-Billancourt"),
]

cities=[("75056","Paris","Paris",48.8566,2.3522,paris),
        ("78646","Versailles","Yvelines",48.8049,2.1204,versailles),
        ("93066","Saint-Denis","Seine-Saint-Denis",48.9362,2.3574,saintdenis),
        ("93048","Montreuil","Seine-Saint-Denis",48.8638,2.4485,montreuil),
        ("92012","Boulogne-Billancourt","Hauts-de-Seine",48.8397,2.2399,boulogne)]
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
