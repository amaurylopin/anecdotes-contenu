import json
W="https://fr.wikipedia.org/wiki/"
def A(cat,title,label,teaser,lead,body,wiki,more=None,timeline=None,lat=None,lon=None,links=None,source=None):
    return {"category":cat,"title":title,"label":label,"teaser":teaser,"lead":lead,"text":lead,"body":body,"more":more or [],"timeline":timeline,"links":links,"wiki":wiki,"source":source or (W+wiki),"lat":lat,"lon":lon,"access":None,"protection":None}
L=lambda kind,title,url,note=None:{"kind":kind,"title":title,"url":url,"note":note}

# ============ NANTES, suite ============
nantes=[
A("patrimoine","L'île Feydeau, les maisons qui penchent","XVIIIe siècle · Entre Loire et Erdre comblées",
 "Les hôtels des armateurs ont été bâtis sur des pieux de chêne plantés dans la vase. Deux siècles plus tard, les façades penchent visiblement, et les escaliers montent de travers.",
 "L'île Feydeau, ancienne île de la Loire lotie à partir de 1723, aligne les hôtels particuliers des armateurs nantais enrichis par le commerce colonial et la traite.",
 ["Les terrains, gagnés sur le fleuve, sont vendus à des négociants qui y font construire des immeubles de rapport avec balcons de fer forgé et mascarons sculptés : têtes de divinités marines, visages grimaçants, et quelques visages africains qui rappellent l'origine des fortunes. Les fondations reposent sur des pieux de chêne enfoncés dans la vase ; en séchant après les comblements des années 1930, le sol s'est tassé.",
  "Le résultat est spectaculaire allée Turenne et rue Kervégan : les façades penchent, les linteaux sont de travers, certains escaliers ont jusqu'à quinze centimètres de dénivelé par étage. Les immeubles sont surveillés et régulièrement confortés.",
  "Jules Verne est né au 4 rue Olivier-de-Clisson, sur l'île. Le quartier a été piétonnisé et restauré dans les années 2010."],
 "%C3%8Ele_Feydeau_(Nantes)",lat=47.2122,lon=-1.5565),
A("patrimoine","Le musée Dobrée et le cœur d'Anne de Bretagne","XVe-XIXe siècle · Place Jean-V",
 "Un manoir médiéval, un palais néoroman construit par un collectionneur, et dans une vitrine, un reliquaire d'or contenant le cœur d'une reine. Volé en 2018, retrouvé dans un sac de ferraille.",
 "Le musée Dobrée, rouvert en 2024 après douze ans de travaux, conserve le reliquaire du cœur d'Anne de Bretagne, pièce la plus précieuse du patrimoine nantais.",
 ["Thomas Dobrée, fils d'armateur, consacre sa fortune à une collection de manuscrits, d'émaux et d'objets d'art, et se fait bâtir à partir de 1862 un palais d'inspiration romane, accolé au manoir de la Touche, résidence des évêques au XVe siècle. Il lègue le tout au département à sa mort en 1895.",
  "Le reliquaire, en or, orné d'une couronne et d'une inscription, a été réalisé en 1514 pour recueillir le cœur d'Anne de Bretagne, dont le corps repose à Saint-Denis. Dans la nuit du 13 au 14 avril 2018, il est dérobé par effraction. Il est retrouvé huit jours plus tard, caché dans un sac au domicile d'un receleur en Seine-Saint-Denis, légèrement déformé mais intact.",
  "Le musée, agrandi d'un bâtiment contemporain, a rouvert en mai 2024 et retrace l'histoire de la Loire-Atlantique de la préhistoire à nos jours."],
 "Mus%C3%A9e_Dobr%C3%A9e",lat=47.2140,lon=-1.5640),
A("gastronomie","Le muscadet, le vin le plus bu de France dans les années 1970","Depuis le XVIIe siècle · Vignoble nantais",
 "Planté après l'hiver terrible de 1709, le melon de Bourgogne a donné le vin blanc qui accompagnait les huîtres de tout le pays. Puis il s'est effondré, et renaît aujourd'hui en crus communaux.",
 "Le muscadet, produit sur 8 000 hectares autour de Nantes, est le vin blanc du vignoble nantais ; son cépage unique, le melon de Bourgogne, a été planté après le gel de 1709 qui détruisit les vignes de la région.",
 ["Le grand hiver de 1709 tue les ceps ; les Hollandais, qui achètent le vin nantais pour en faire de l'eau-de-vie, poussent à replanter un cépage résistant venu de Bourgogne. Le muscadet est né. L'élevage « sur lie », qui laisse le vin au contact de ses levures jusqu'au printemps, lui donne sa fraîcheur perlante.",
  "Dans les années 1960 et 1970, il devient le blanc le plus vendu en France, synonyme de plateau de fruits de mer, puis souffre de la surproduction et d'une image bon marché ; le vignoble perd la moitié de sa surface en trente ans.",
  "Depuis 2011, dix crus communaux (Clisson, Gorges, Le Pallet, Goulaine, Monnières-Saint-Fiacre…) imposent des rendements bas et un élevage long ; ces muscadets de garde se vieillissent dix ans et ont redonné au vin ses lettres de noblesse."],
 "Muscadet",lat=47.1200,lon=-1.3500),
A("nature","L'île de Versailles, un jardin japonais sur l'Erdre","1983 · Quartier Hauts-Pavés – Saint-Félix",
 "Une île artificielle créée avec les déblais du canal, devenue entrepôt de bois puis blanchisserie, transformée en jardin japonais pour le centenaire du jumelage avec Niigata.",
 "L'île de Versailles, sur l'Erdre, est un jardin japonais public ouvert en 1983, à dix minutes du centre de Nantes.",
 ["L'île naît au XIXe siècle des déblais du creusement du canal Saint-Félix. Elle accueille des entrepôts de bois, des tanneries et des blanchisseuses qui lavaient le linge des Nantais dans l'Erdre. Désaffectée, elle est réaménagée à l'occasion du jumelage avec Niigata : cascade, bambous, érables, pierres, bassins à carpes et maison de thé.",
  "On y accède à pied par une passerelle depuis le quai de Versailles ; des bateaux de promenade sur l'Erdre y font escale.",
  "C'est l'un des rares jardins japonais français conçus avec un paysagiste japonais, et un lieu de pique-nique très fréquenté en été."],
 "%C3%8Ele_de_Versailles",lat=47.2232,lon=-1.5530),
A("insolite","Vingt mille logements en vingt ans","1958-1975 · Dervallières, Bellevue, Malakoff",
 "Le Sillon de Bretagne, à Saint-Herblain, est une barre de 300 mètres et seize étages, l'une des plus longues de France. Elle fait partie des grands ensembles qui ont logé les Nantais chassés des taudis du centre.",
 "Entre 1958 et 1975, Nantes et ses communes voisines bâtissent les grands ensembles qui logent les habitants des taudis du centre, les rapatriés d'Algérie et les ouvriers des chantiers.",
 ["Les Dervallières, Bellevue, Malakoff, le Breil et la Boissière sortent de terre en quelques années, sur les modèles de l'urbanisme de dalle. Le Sillon de Bretagne, achevé en 1974 à Saint-Herblain, est le plus spectaculaire : 300 mètres de long, seize étages, près de 900 logements, visible depuis la Loire.",
  "Ces quartiers, d'abord très demandés pour leur confort moderne, se paupérisent à partir des années 1980 avec la crise industrielle. Ils ont été inscrits en politique de la ville et font l'objet de démolitions-reconstructions depuis les années 2000 : à Malakoff et au Breil, des barres ont été remplacées par des immeubles plus petits.",
  "Le Sillon de Bretagne, réhabilité en 2010, a été l'un des premiers grands ensembles de France à viser une performance énergétique."],
 "Sillon_de_Bretagne",lat=47.2440,lon=-1.6020),
]

# ============ RENNES ============
rennes=[
A("politique","Nathalie Appéré, la maire qui a fait de Rennes un laboratoire","Depuis 2014 · Hôtel de ville",
 "Élue en 2014, réélue en 2020 et 2026, elle préside aussi l'Agence nationale de l'habitat. Rennes est à gauche sans interruption depuis 1977.",
 "Nathalie Appéré est maire de Rennes depuis avril 2014 et présidente de Rennes Métropole.",
 ["Ancienne députée d'Ille-et-Vilaine et adjointe d'Edmond Hervé puis de Daniel Delaveau, elle succède à ce dernier en 2014. Ses mandats portent sur la deuxième ligne de métro, ouverte en 2022, la densification du centre et l'accueil d'une population étudiante de 70 000 personnes.",
  "Elle préside l'Agence nationale de l'habitat depuis 2017 et a été l'une des voix du Parti socialiste sur le logement. En mars 2026, elle est réélue pour un troisième mandat.",
  "Rennes est dirigée par la gauche depuis 1977 et l'élection d'Edmond Hervé, qui restera maire vingt-sept ans et sera mis en cause, puis relaxé pénalement mais déclaré coupable sans peine, dans l'affaire du sang contaminé en tant qu'ancien secrétaire d'État à la Santé."],
 "Nathalie_App%C3%A9r%C3%A9",lat=48.1113,lon=-1.6800),
A("faits_divers","Le Parlement de Bretagne en flammes, une fusée de détresse","4 février 1994 · Place du Parlement",
 "Lors d'une manifestation de marins-pêcheurs, une fusée de détresse met le feu à la charpente du Parlement de Bretagne. Le bâtiment du XVIIe siècle brûle toute la nuit sous les caméras.",
 "Dans la nuit du 4 au 5 février 1994, le Parlement de Bretagne, siège de la cour d'appel, est ravagé par un incendie déclenché lors d'une manifestation de marins-pêcheurs.",
 ["Les pêcheurs protestent contre l'effondrement des cours du poisson. En fin de manifestation, des affrontements éclatent place du Parlement ; des fusées de détresse sont tirées, dont l'une se loge dans la toiture en bois du bâtiment construit au XVIIe siècle par Salomon de Brosse. Le feu couve, puis embrase la charpente ; les secours, gênés par les manifestants et par la configuration des lieux, ne parviennent pas à le maîtriser.",
  "Les peintures du XVIIe siècle de la Grand'Chambre sont sauvées par des pompiers qui les décrochent sous les flammes ; une partie des plafonds est détruite. Quatre manifestants seront condamnés.",
  "La restauration, décidée aussitôt, dure jusqu'en 1999 et coûte plus de 300 millions de francs. Le Parlement se visite aujourd'hui ; la cour d'appel y siège toujours."],
 "Parlement_de_Bretagne",lat=48.1127,lon=-1.6780),
A("histoire","L'incendie de 1720 : Rennes brûle une semaine","22-29 décembre 1720 · Centre-ville",
 "Un menuisier ivre, une bougie, et neuf cents maisons de bois détruites en sept jours. La ville est reconstruite en pierre selon un plan en damier : c'est le Rennes que l'on voit aujourd'hui.",
 "Du 22 au 29 décembre 1720, un incendie détruit le cœur de Rennes : neuf cents maisons, 32 rues, huit mille personnes sans abri.",
 ["Le feu part, selon la tradition, de l'atelier d'un menuisier ivre rue Tristin, dans un quartier de maisons à pans de bois serrées. Le vent, le gel qui a figé les puits et l'absence de pompes efficaces font le reste : il brûle pendant sept jours. On dénombre peu de morts, mais le centre est anéanti.",
  "La reconstruction est confiée à l'ingénieur Isaac Robelin puis à Jacques Gabriel, premier architecte du roi : rues droites et larges, îlots réguliers, façades de granit et de tuffeau à l'identique, interdiction du pan de bois. C'est ce plan en damier qui donne au centre de Rennes son allure classique, unique en Bretagne.",
  "Les maisons à pans de bois qui subsistent autour de la place des Lices et de la rue du Chapitre sont celles des quartiers épargnés par le feu."],
 "Incendie_de_Rennes",lat=48.1113,lon=-1.6800),
A("personnalites","Dreyfus rejugé à Rennes, et gracié dix jours après","Août-septembre 1899 · Lycée de Rennes",
 "Le second procès du capitaine se tient dans la salle des fêtes du lycée, sous les yeux de la presse mondiale. Il est de nouveau condamné, avec circonstances atténuantes, avant d'être gracié.",
 "Du 7 août au 9 septembre 1899, le conseil de guerre de Rennes rejuge le capitaine Alfred Dreyfus, après la cassation de sa condamnation de 1894.",
 ["La ville est choisie pour son calme supposé et sa garnison. Le procès se tient dans la salle des fêtes du lycée, devenu lycée Émile-Zola. Plus de quatre cents journalistes du monde entier s'installent à Rennes ; des incidents éclatent entre dreyfusards et antidreyfusards. Le 14 août, l'avocat de Dreyfus, Fernand Labori, est blessé d'un coup de revolver dans le dos en se rendant à l'audience ; son agresseur n'est jamais retrouvé.",
  "Le 9 septembre, le conseil de guerre le condamne de nouveau, par cinq voix contre deux, à dix ans de détention, avec des « circonstances atténuantes » absurdes pour un crime de trahison. L'émotion internationale est immense.",
  "Dix jours plus tard, le président Émile Loubet le gracie ; Dreyfus accepte pour sortir de prison, tout en continuant à réclamer la révision. Il sera réhabilité en 1906 et réintégré dans l'armée."],
 "Affaire_Dreyfus",lat=48.1140,lon=-1.6830),
]

# ============ BORDEAUX ============
bordeaux=[
A("politique","Juppé, Premier ministre devenu maire pendant vingt-quatre ans","1995-2019 · Hôtel de ville",
 "Premier ministre de Chirac, condamné en 2004 dans l'affaire des emplois fictifs de la mairie de Paris, exilé un an à Montréal, revenu et réélu : Alain Juppé a transformé Bordeaux de 1995 à 2019.",
 "Alain Juppé a été maire de Bordeaux de 1995 à 2004 puis de 2006 à 2019, avant de rejoindre le Conseil constitutionnel.",
 ["Il hérite d'une ville noire de suie et vidée de son centre, après les quarante-huit ans de Jacques Chaban-Delmas. Il lance le nettoyage des façades, le tramway ouvert en 2003, la reconquête des quais et le classement UNESCO du Port de la Lune en 2007. La population du centre remonte, les prix de l'immobilier aussi.",
  "En janvier 2004, il est condamné à dix-huit mois de prison avec sursis et un an d'inéligibilité pour prise illégale d'intérêts dans l'affaire des emplois fictifs du RPR payés par la mairie de Paris, où il avait été adjoint aux finances. Il démissionne, part enseigner un an à Montréal, puis se représente en 2006 et l'emporte avec 56 % des voix.",
  "Candidat à la primaire de la droite en 2016, battu par François Fillon, il quitte la mairie en mars 2019 pour le Conseil constitutionnel. Son successeur, Nicolas Florian, est battu l'année suivante par l'écologiste Pierre Hurmic."],
 "Alain_Jupp%C3%A9",lat=44.8378,lon=-0.5792,
 timeline=[{"year":"1995","text":"Premier ministre et élu maire de Bordeaux."},{"year":"2003","text":"Ouverture du tramway."},{"year":"2004","text":"Condamné, démissionne, part à Montréal."},{"year":"2006","text":"Réélu maire."},{"year":"2007","text":"Port de la Lune classé UNESCO."},{"year":"2019","text":"Conseil constitutionnel."}]),
A("faits_divers","L'incendie du 5-7, 146 morts dans une boîte de nuit","1er novembre 1970 · Saint-Laurent-du-Pont (Isère)",
 "",
 "",
 [""],
 "x"),
A("histoire","Bordeaux, capitale de la France trois fois","1870, 1914, 1940 · Grand Théâtre et préfecture",
 "Quand Paris est menacé, le gouvernement descend à Bordeaux : en 1870 devant les Prussiens, en 1914 devant la Marne, en 1940 devant les panzers. C'est là que Pétain a demandé l'armistice.",
 "Bordeaux a été trois fois le siège du gouvernement français : en 1870-1871, en septembre 1914 et en juin 1940.",
 ["En 1870, après Sedan, la Délégation de Tours se replie à Bordeaux ; l'Assemblée nationale y siège au Grand Théâtre en février 1871 et c'est là que sont débattues les conditions de paix avec la Prusse. En septembre 1914, devant l'avancée allemande, le gouvernement de Viviani s'installe de nouveau à Bordeaux ; il y reste jusqu'en décembre, après la victoire de la Marne.",
  "Le 14 juin 1940, le gouvernement Reynaud arrive de Tours. Les ministères s'installent dans les lycées et les hôtels. Le 16 juin, Reynaud démissionne ; Pétain forme un gouvernement et demande l'armistice. C'est aussi depuis Bordeaux que le Massilia part pour Casablanca avec des parlementaires qui voulaient continuer la guerre.",
  "Une plaque au Grand Théâtre et une autre rue Vital-Carles rappellent ces épisodes. La ville, loin du front et reliée au port, était le refuge naturel d'un pouvoir chassé de Paris."],
 "Bordeaux",lat=44.8412,lon=-0.5750),
A("personnalites","Montaigne, maire de Bordeaux pendant la peste","1581-1585 · Hôtel de ville",
 "L'auteur des Essais a été maire de la ville quatre ans. Quand la peste frappe en 1585, il est à la campagne et n'y revient pas : on le lui reproche encore.",
 "Michel de Montaigne a été maire de Bordeaux de 1581 à 1585, élu alors qu'il voyageait en Italie et ne demandait rien.",
 ["Il accepte sur ordre d'Henri III, dans une ville déchirée entre catholiques et protestants, et conduit une magistrature de conciliation, négociant entre le maréchal de Matignon, gouverneur, et Henri de Navarre, futur Henri IV, qu'il reçoit dans son château.",
  "En juin 1585, la peste éclate à Bordeaux et tue un tiers de la population. Montaigne, dont le mandat s'achève, se trouve hors de la ville ; il écrit aux jurats pour demander où les rejoindre, ne reçoit pas de réponse claire et ne revient pas. Ses contempteurs y ont vu une fuite, ses défenseurs le respect d'un mandat déjà expiré.",
  "Il consacre à l'épisode des pages des Essais sur la peur et la mort. Son cœur est au château de Montaigne, son corps au musée d'Aquitaine, à Bordeaux."],
 "Michel_de_Montaigne",lat=44.8395,lon=-0.5760),
]
bordeaux=[a for a in bordeaux if a["wiki"]!="x"]

def write(insee,name,dept,lat,lon,arts,replace_cats=None):
    import os
    path=f"communes/{insee}.json"
    if os.path.exists(path):
        p=json.load(open(path))
        have={a.get("wiki") for a in p["anecdotes"]}
        p["anecdotes"]+= [a for a in arts if a.get("wiki") not in have]
    else:
        p={"id":f"{name.lower()}-{insee}","insee":insee,"name":name,"dept":dept,"kind":"commune","lat":lat,"lon":lon,"anecdotes":arts}
    json.dump(p,open(path,'w'),ensure_ascii=False,indent=1)
    return len(p["anecdotes"])

idx=json.load(open('index.json'))
for insee,name,dept,lat,lon,arts in [
    ("44109","Nantes","Loire-Atlantique",47.2184,-1.5536,nantes),
    ("35238","Rennes","Ille-et-Vilaine",48.1113,-1.6800,rennes),
    ("33063","Bordeaux","Gironde",44.8378,-0.5792,bordeaux)]:
    n=write(insee,name,dept,lat,lon,arts)
    idx["communes"][insee]={"name":name,"count":n,"updated":"2026-10-07"}
    print(name,n)
json.dump(idx,open('index.json','w'),ensure_ascii=False,indent=1)
