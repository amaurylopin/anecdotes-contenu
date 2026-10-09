import json
W="https://fr.wikipedia.org/wiki/"
def A(cat,title,label,teaser,lead,body,wiki,more=None,timeline=None,lat=None,lon=None,links=None,source=None):
    return {"category":cat,"title":title,"label":label,"teaser":teaser,"lead":lead,"text":lead,"body":body,"more":more or [],"timeline":timeline,"links":links,"wiki":wiki,"source":source or (W+wiki),"lat":lat,"lon":lon,"access":None,"protection":None}
L=lambda kind,title,url,note=None:{"kind":kind,"title":title,"url":url,"note":note}

new=[
# ===== FAITS DIVERS (suite) =====
A("faits_divers","La cour d'assises prise en otage, en direct à la télévision","19-20 décembre 1985 · Palais de justice, place Aristide-Briand",
 "Jugé pour vol à main armée, Georges Courtois sort une arme en pleine audience avec deux complices, retient 34 personnes, dont les jurés, et exige que les caméras de FR3 filment la salle. Pendant 34 heures, la France regarde.",
 "Le 19 décembre 1985, trois détenus, Georges Courtois, Patrick Thiolet et Abdelkarim Khalki, prennent en otage la cour d'assises de Nantes pendant le procès des deux premiers. L'affaire dure 34 heures et se termine à l'aéroport.",
 ["Courtois, « voleur professionnel » comme il se présente, licencié en droit et poète à ses heures, attend ce moment depuis deux ans. Des armes et des grenades ont été introduites dans le palais ; Khalki, qui n'était pas jugé, surgit dans la salle. Les otages sont les magistrats, les jurés, des avocats, le public. Courtois exige une équipe de FR3 : l'interrogatoire des jurés par l'accusé, filmé et diffusé, est resté une scène unique dans l'histoire judiciaire française. Khalki, revolver et grenade en main, menace de tout faire sauter.",
  "Robert Broussard et le RAID d'Ange Mancini négocient. Les otages sont libérés par vagues ; le 20 décembre à 15 h 15, les trois hommes sortent avec quatre derniers otages, dont le président de la cour Dominique Bailhache et Mancini lui-même, et gagnent l'aéroport en voiture. Ils se rendent à 20 h 30, sans qu'aucun otage ait été blessé. Une jurée, prise en otage, rendra visite à Courtois en prison pendant dix ans.",
  "Jugés en 1988 à Nantes, sous haute surveillance, les trois hommes sont lourdement condamnés. Courtois, libéré dans les années 2000, a publié ses mémoires et participé en 2017 au documentaire de France 3 sur l'affaire."],
 "Georges_Courtois",lat=47.2128,lon=-1.5541,
 links=[L("documentaire","« Prise d'otages en direct à la cour d'assises » (France 3, 2017)","https://www.ina.fr/recherche?q=Courtois+prise+d%27otages+Nantes+1985","Avec Georges Courtois lui-même ; archives INA"),
        L("vidéo","Les images de FR3 dans la salle d'audience (INA, 19 décembre 1985)","https://www.ina.fr/recherche?q=Courtois+cour+d%27assises+Nantes")]),
A("faits_divers","Août 1955 : un ouvrier tué, la ville en état de siège","19 août 1955 · Chantiers de Nantes, préfecture",
 "Deux mois de grève dans la métallurgie, des affrontements place Royale, un maçon de 25 ans tué d'une balle devant la préfecture. Les grèves de 1955 à Nantes ont obtenu les augmentations que le patronat refusait.",
 "À l'été 1955, les ouvriers des chantiers navals et de la métallurgie de Nantes et Saint-Nazaire mènent une grève dure pour les salaires. Le 19 août, à Nantes, les affrontements avec les CRS font un mort, Jean Rigollet, 25 ans.",
 ["Le conflit part de Saint-Nazaire en juin, pour une augmentation de 22 % : les salaires de l'Ouest sont nettement inférieurs à ceux de la région parisienne. Les ouvriers des Chantiers de Bretagne et de Dubigeon suivent, puis toute la métallurgie nantaise. Les manifestations se succèdent dans le centre ; le 17 août, la préfecture est assiégée, des pavés volent, des grenades répondent.",
  "Le 19 août, lors d'une nouvelle manifestation, un maçon, Jean Rigollet, est tué par balle près de la préfecture ; une cinquantaine de personnes sont blessées. Le gouvernement envoie des renforts ; la ville est quadrillée. Les obsèques réunissent une foule immense. Les accords signés fin août accordent une partie des hausses demandées.",
  "Les grèves de 1955 ont forgé le mouvement ouvrier nantais, qui jouera un rôle de premier plan en mai 1968 : la ville est alors dirigée pendant une semaine par un comité central de grève, épisode resté comme la « commune de Nantes »."],
 "Gr%C3%A8ves_de_1955_%C3%A0_Nantes_et_Saint-Nazaire",lat=47.2127,lon=-1.5546),
A("faits_divers","Marcel Redureau, quinze ans, sept morts, jugé à Nantes","1913-1914 · Cour d'assises de Nantes",
 "Le 30 septembre 1913, au Landreau, un valet de ferme de quinze ans tue à la serpe toute la famille de son maître, sept personnes. Jugé à Nantes, il échappe à la mort grâce à son âge. André Gide en fera un livre.",
 "L'affaire Redureau, l'un des crimes les plus célèbres de l'Ouest, a été jugée par la cour d'assises de la Loire-Inférieure, à Nantes, en mars 1914.",
 ["Marcel Redureau, quinze ans, est domestique chez les Mabit, viticulteurs de Bas-Briacé, au Landreau, dans le vignoble nantais. Un soir de vendanges, réprimandé par son patron, il le tue d'un coup de serpe, puis assassine la femme, les enfants, la grand-mère et la servante : sept morts. Il se cache chez ses parents et avoue le lendemain, sans pouvoir expliquer son geste.",
  "La presse nationale se passionne pour « le petit valet du Landreau ». Mineur, il ne peut être condamné à mort : la cour d'assises de Nantes le condamne en 1914 à vingt ans de détention. Il meurt de tuberculose en 1916, à dix-sept ans, à la colonie pénitentiaire.",
  "André Gide, fasciné par l'absence de mobile, publie en 1930 « L'Affaire Redureau », recueil des pièces du dossier, dans sa collection « Ne jugez pas »."],
 "Affaire_Marcel_Redureau",
 links=[L("livre","« L'Affaire Redureau » d'André Gide (1930)","https://fr.wikipedia.org/wiki/L%27Affaire_Redureau","Collection « Ne jugez pas », Gallimard")]),
A("faits_divers","Mai 68 : la semaine où Nantes s'est gouvernée seule","24-31 mai 1968 · Préfecture, bourse du travail",
 "Pendant une semaine, un comité central de grève a contrôlé la circulation, l'essence, les prix et le ravitaillement de la ville, tandis que le préfet restait enfermé. Les journaux ont parlé de « commune de Nantes ».",
 "En mai 1968, Nantes est la ville de France où la grève est allée le plus loin : du 24 au 31 mai, un comité central de grève installé à la bourse du travail remplace de fait les autorités.",
 ["Tout commence tôt : Sud-Aviation, à Bouguenais, est la première usine occupée de France, le 14 mai, avec le directeur séquestré. Les étudiants, les ouvriers et les paysans, menés par un syndicalisme libertaire et le Mouvement de défense des exploitations familiales, convergent. Le 24 mai, les manifestants assiègent la préfecture ; le préfet ne sort plus.",
  "Le comité central de grève organise des barrages aux entrées de la ville, délivre des bons d'essence, fixe les prix dans les marchés, fait fonctionner les écoles pour les enfants de grévistes et édite un journal. Les paysans approvisionnent directement les quartiers populaires. Ce fonctionnement dure une semaine, jusqu'au reflux de la grève après le discours de De Gaulle du 30 mai.",
  "L'épisode a été étudié comme une expérience d'autogestion unique dans le pays ; une plaque et des expositions l'ont rappelé pour le cinquantenaire, en 2018."],
 "Mai_68_%C3%A0_Nantes"),

# ===== PERSONNALITES (suite) =====
A("personnalites","Jacques Vaché, l'ami de Breton, mort à l'hôtel de France","1895-1919 · Place Graslin",
 "Dandy, dessinateur, soldat interprète, il meurt à vingt-trois ans d'une surdose d'opium dans une chambre de l'hôtel de France, place Graslin. André Breton dira que le surréalisme vient de lui.",
 "Jacques Vaché, né à Lorient en 1895 et élevé à Nantes, est mort le 6 janvier 1919 à l'hôtel de France, place Graslin. André Breton, qui l'avait rencontré à l'hôpital de Nantes en 1916, l'a désigné comme l'inspirateur du surréalisme.",
 ["Élève du lycée de Nantes, Vaché anime avec des amis le groupe des « Sârs », qui publie une revue satirique, dessine, s'habille en dandy et cultive une ironie glaciale qu'il appelle « l'umour », sans h. Mobilisé, blessé, il est soigné en 1916 à l'hôpital de la rue du Bocage, où Breton, interne, fait sa connaissance. Les deux hommes échangent des lettres : les « Lettres de guerre », publiées en 1919, sont son seul livre.",
  "Le 6 janvier 1919, il est retrouvé mort dans sa chambre d'hôtel avec un ami, tous deux victimes d'une dose excessive d'opium. Accident ou suicide mis en scène, la question n'a jamais été tranchée ; Breton a toujours penché pour la seconde hypothèse.",
  "Nantes l'a tardivement reconnu : une plaque sur l'hôtel de France, une rue à son nom sur l'Île de Nantes, et le Lieu unique lui a consacré une exposition. Breton écrira que Nantes est « peut-être, avec Paris, la seule ville de France où j'ai l'impression que peut m'arriver quelque chose qui en vaut la peine »."],
 "Jacques_Vach%C3%A9",lat=47.2129,lon=-1.5625,
 timeline=[{"year":"1895","text":"Naissance à Lorient ; enfance et lycée à Nantes."},{"year":"1916","text":"Rencontre André Breton à l'hôpital de Nantes."},{"year":"1919","text":"Mort à l'hôtel de France, place Graslin."},{"year":"1919","text":"Publication des « Lettres de guerre »."}]),
A("personnalites","Claude Cahun, née Lucy Schwob rue de Rennes","1894-1954 · 6, rue de Rennes",
 "Photographe, écrivaine, résistante à Jersey, elle a inventé l'autoportrait travesti un demi-siècle avant tout le monde. Petite-nièce de Marcel Schwob, fille du directeur du Phare de la Loire, elle est née à Nantes.",
 "Claude Cahun, née Lucy Schwob à Nantes le 25 octobre 1894, est l'une des figures les plus singulières du surréalisme, redécouverte dans les années 1990.",
 ["Sa famille dirige « Le Phare de la Loire », grand journal républicain de Nantes ; son oncle est l'écrivain Marcel Schwob. Elle grandit rue de Rennes, puis au lycée de Nantes, où elle subit l'antisémitisme au moment de l'affaire Dreyfus. Avec sa compagne Suzanne Malherbe, dite Marcel Moore, qui est aussi sa demi-sœur par alliance, elle s'installe à Paris en 1920 et fréquente Breton et Bataille.",
  "Ses autoportraits, où elle apparaît crâne rasé, en haltérophile, en poupée, en bouddha, interrogent le genre et l'identité avec un demi-siècle d'avance. Elle publie « Aveux non avenus » en 1930. En 1937, le couple s'installe à Jersey ; sous l'Occupation, elles mènent une campagne de tracts contre les soldats allemands, sont arrêtées en 1944 et condamnées à mort, peine non exécutée avant la Libération.",
  "Oubliée après sa mort en 1954, elle est redécouverte par les historiens de l'art et les études de genre ; ses œuvres sont au Musée d'arts de Nantes, qui lui a consacré une exposition, et dans les plus grands musées du monde."],
 "Claude_Cahun",lat=47.2200,lon=-1.5590,
 timeline=[{"year":"1894","text":"Naissance à Nantes, rue de Rennes."},{"year":"1920","text":"Installation à Paris avec Marcel Moore."},{"year":"1930","text":"« Aveux non avenus »."},{"year":"1944","text":"Arrêtée à Jersey, condamnée à mort par l'occupant."},{"year":"1954","text":"Mort à Jersey."}]),
A("personnalites","Claire Bretécher, de Nantes aux Frustrés","1940-2020 · Née à Nantes",
 "La dessinatrice d'Agrippine et des Frustrés, « la meilleure sociologue de l'année » selon Roland Barthes, a grandi dans une famille nantaise catholique et bourgeoise qu'elle n'a cessé de croquer.",
 "Claire Bretécher est née à Nantes le 17 avril 1940 et y a passé son enfance avant de partir pour Paris à vingt ans.",
 ["Élevée dans un milieu qu'elle décrira comme étouffant, elle enseigne brièvement le dessin à Nantes, puis monte à Paris où elle débute chez Spirou et Pilote. En 1972, elle cofonde L'Écho des savanes avec Gotlib et Mandryka, premier journal de bande dessinée pour adultes.",
  "Les « Frustrés », publiés dans Le Nouvel Observateur à partir de 1973, croquent les intellectuels de gauche parisiens avec une cruauté affectueuse qui fait d'elle, selon Roland Barthes, « la meilleure sociologue de l'année ». Elle est la première autrice de bande dessinée à s'autoéditer, pour garder ses droits. Agrippine, l'adolescente ingrate, naît en 1988 et reste son personnage le plus célèbre.",
  "Elle a aussi peint, discrètement, des portraits exposés après sa mort en 2020. Le Musée d'arts de Nantes lui a consacré une rétrospective."],
 "Claire_Bret%C3%A9cher",
 timeline=[{"year":"1940","text":"Naissance à Nantes."},{"year":"1972","text":"Cofonde L'Écho des savanes."},{"year":"1973","text":"Les Frustrés dans Le Nouvel Observateur."},{"year":"1988","text":"Création d'Agrippine."},{"year":"2020","text":"Mort à Paris."}]),
A("personnalites","Waldeck-Rousseau, l'homme de la loi de 1901","1846-1904 · Né rue Voltaire",
 "Né à Nantes dans une famille républicaine, il a été le président du Conseil qui a gracié Dreyfus, légalisé les associations par la loi de 1901 et imposé l'État face aux congrégations.",
 "Pierre Waldeck-Rousseau, né à Nantes le 2 décembre 1846, a dirigé le gouvernement de 1899 à 1902, le plus long de la IIIe République jusqu'alors.",
 ["Son père, René Waldeck-Rousseau, avocat et maire de Nantes en 1870-1871, fut député sous la IIe République. Pierre devient avocat à Nantes puis à Rennes, député d'Ille-et-Vilaine en 1879, et ministre de l'Intérieur à 35 ans sous Gambetta. Il fait voter en 1884 la loi qui légalise les syndicats, qui porte son nom.",
  "Appelé en juin 1899 en pleine affaire Dreyfus, il forme un gouvernement de « défense républicaine » qui va des radicaux au socialiste Millerand, fait gracier le capitaine après le procès de Rennes, et fait adopter la loi du 1er juillet 1901 sur la liberté d'association, qui régit encore toutes les associations françaises et a servi d'instrument contre les congrégations religieuses non autorisées.",
  "Malade, il se retire en 1902 et meurt en 1904. Un lycée de Nantes et une place portent son nom ; une statue le représente place Waldeck-Rousseau."],
 "Pierre_Waldeck-Rousseau",
 timeline=[{"year":"1846","text":"Naissance à Nantes."},{"year":"1884","text":"Loi Waldeck-Rousseau sur les syndicats."},{"year":"1899","text":"Président du Conseil, grâce de Dreyfus."},{"year":"1901","text":"Loi sur les associations."},{"year":"1904","text":"Mort à Corbeil."}]),

# ===== INSOLITE (suite) =====
A("insolite","Le pont transbordeur, 70 mètres au-dessus de la Loire","1903-1958 · Entre le quai de la Fosse et l'île",
 "Pendant 55 ans, une nacelle suspendue à une poutre métallique de 141 mètres a transporté les Nantais d'une rive à l'autre sans gêner les navires. Démoli en 1958, il manque encore à beaucoup.",
 "Le pont transbordeur de Nantes, inauguré en 1903, reliait le quai de la Fosse à l'île Sainte-Anne, à côté de l'actuelle grue Titan. Il a été démonté en 1958.",
 ["Conçu par Ferdinand Arnodin, l'ingénieur de celui de Rochefort et de Marseille, il se composait de deux pylônes de 75 mètres, d'un tablier suspendu à 50 mètres au-dessus de l'eau et d'une nacelle de 50 tonnes qui faisait la traversée en une minute et demie, voitures, chevaux et piétons compris. C'était la solution pour franchir le fleuve sans interrompre le trafic des grands voiliers et des cargos vers le port.",
  "Avec le déclin du port de Nantes au profit de Saint-Nazaire et le comblement des bras de la Loire, il est jugé inutile et dangereux ; une structure similaire vient d'ailleurs de s'effondrer à Rouen. Il est démoli en 1958 malgré des protestations.",
  "Depuis les années 1990, des associations militent pour sa reconstruction sur le même site ; la ville a préféré le pont Anne-de-Bretagne élargi. Il ne subsiste en France qu'un seul transbordeur, à Rochefort, et des maquettes au Musée d'histoire de Nantes."],
 "Pont_transbordeur_de_Nantes",lat=47.2063,lon=-1.5680),
A("insolite","Élue « ville la plus agréable d'Europe » par Time","2004 · Toute la ville",
 "En 2004, le magazine Time place Nantes en tête de son classement des villes européennes où il fait bon vivre. La ville n'a jamais cessé de citer ce titre, et les Nantais de s'en moquer un peu.",
 "Le 29 août 2004, l'hebdomadaire américain Time désigne Nantes comme « la ville la plus agréable d'Europe » dans un dossier consacré aux villes de taille moyenne.",
 ["Le magazine salue une ville sortie de son déclin industriel des années 1980, la fermeture des chantiers navals en 1987 ayant été suivie d'une reconversion vers les services et la culture : tramway, Lieu unique, universités, et un centre-ville rendu aux piétons. Le titre arrive au milieu du mandat de Jean-Marc Ayrault, qui en fait un argument.",
  "Depuis, Nantes figure régulièrement en tête des classements français sur la qualité de vie et l'attractivité, et sa population a augmenté de près de 50 000 habitants entre 2004 et 2024. L'envers du titre, c'est la hausse des loyers et la saturation des transports, que les Nantais mettent volontiers sur le compte des « néo-Nantais ».",
  "Le classement de Time est devenu une blague locale : on le cite à chaque jour de pluie."],
 "Nantes"),
]
p=json.load(open('communes/44109.json'))
# Coordonnées manquantes sur quelques fiches patrimoine existantes
coords={"Passage_Pommeraye":(47.2130,-1.5590),"Cours_des_50-Otages":(47.2168,-1.5555),"Le_Lieu_unique":(47.2155,-1.5455),"Th%C3%A9%C3%A2tre_Graslin":(47.2127,-1.5622),"Jardin_des_plantes_de_Nantes":(47.2203,-1.5424),"Tour_Bretagne":(47.2170,-1.5577),"M%C3%A9morial_de_l'abolition_de_l'esclavage":(47.2113,-1.5618),"Mémorial_de_l'abolition_de_l'esclavage":(47.2113,-1.5618)}
for a in p["anecdotes"]:
    w=a.get("wiki") or ""
    if (a.get("lat") is None) and w in coords: a["lat"],a["lon"]=coords[w]
p["anecdotes"]+=new
json.dump(p,open('communes/44109.json','w'),ensure_ascii=False,indent=1)
idx=json.load(open('index.json')); idx["communes"]["44109"]["count"]=len(p["anecdotes"]); json.dump(idx,open('index.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(p["anecdotes"]),Counter(a["category"] for a in p["anecdotes"]))
