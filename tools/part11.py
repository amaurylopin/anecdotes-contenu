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

# ---------------------------------------------------------------- TROYES
troyes=[
A("politique","François Baroin, maire de Troyes depuis 1995","1995-2026 · Hôtel de ville",
 "Élu maire à 30 ans, ancien ministre de l'Économie et président de l'Association des maires de France, François Baroin a été réélu en mars 2026, pour la première fois au second tour.",
 "François Baroin, divers droite, maire de Troyes depuis 1995, a été réélu au second tour des municipales de mars 2026 avec 56,94 % des voix.",
 ["Fils de Michel Baroin, ancien grand maître du Grand Orient et proche de Jacques Chirac, il devient maire de Troyes en 1995, à 30 ans. Il est successivement ministre de l'Outre-mer, brièvement de l'Intérieur en 2007, du Budget, puis de l'Économie et des Finances en 2011-2012. Il préside l'Association des maires de France de 2014 à 2021.",
  "Réélu dès le premier tour en 2020, il n'obtient que 48,55 % le 15 mars 2026. Au second tour, sa liste l'emporte avec 7 106 voix, devant celle de la gauche menée par Charline Briot (22,05 %) et celle du Rassemblement national de Pierre Brochet (21,00 %). Elle détient 39 des 49 sièges."],
 "François Baroin"),
A("faits_divers","Patrick Henry et « La France a peur »","1976-1977 · Troyes",
 "En 1976, un enfant de 7 ans est enlevé à la sortie de l'école à Troyes. Son ravisseur, Patrick Henry, sauvé de la peine de mort par Robert Badinter, devient le symbole du combat pour l'abolition.",
 "Le 30 janvier 1976, Philippe Bertrand, 7 ans, est enlevé à la sortie de son école à Troyes ; son corps est retrouvé le 17 février sous le lit d'une chambre louée par Patrick Henry, 22 ans.",
 ["Le ravisseur réclame une rançon d'un million de francs à la famille. Interrogé par la télévision pendant l'enquête, Patrick Henry, d'abord relâché faute de preuves, déclare que le coupable mérite la mort. Le soir de son arrestation, le 18 février, Roger Gicquel ouvre le journal de TF1 par une phrase restée célèbre : « La France a peur ».",
  "Au procès, en janvier 1977 devant la cour d'assises de l'Aube, l'opinion réclame la peine capitale. Défendu par Robert Bocquillon et Robert Badinter, qui fait du procès celui de la guillotine, Patrick Henry est condamné le 20 janvier 1977 à la réclusion criminelle à perpétuité. Badinter, devenu garde des Sceaux, fera voter l'abolition en 1981.",
  "Libéré conditionnellement en 2001, Patrick Henry est arrêté en Espagne l'année suivante avec plusieurs kilos de cannabis et réincarcéré. Remis en liberté pour raisons médicales en 2017, il meurt le 3 décembre 2017."],
 "Affaire Patrick Henry",
 timeline=T(("1976","Enlèvement et meurtre de Philippe Bertrand, arrestation de Patrick Henry."),("1977","Condamné à perpétuité, évitant la peine de mort."),("1981","Abolition de la peine de mort."),("2001","Libération conditionnelle."),("2017","Mort de Patrick Henry."))),
A("histoire","Les foires de Champagne et Chrétien de Troyes","XIIe-XIIIe siècles · Centre historique",
 "Au XIIe siècle, Troyes accueille deux des grandes foires de Champagne, où se croisent marchands flamands et italiens. C'est à la cour de Champagne que Chrétien de Troyes invente les romans de la Table ronde.",
 "Aux XIIe et XIIIe siècles, Troyes est l'un des grands carrefours commerciaux d'Europe grâce aux foires de Champagne, et la cour des comtes de Champagne en fait un centre littéraire.",
 ["Les comtes de Champagne organisent un cycle de foires réparties entre Troyes, Provins, Lagny et Bar-sur-Aube. Les draps de Flandre y sont échangés contre les épices et les soieries apportées par les Italiens ; la « livre de Troyes » sert d'unité de poids pour l'or et l'argent, et l'once troy est encore utilisée aujourd'hui sur les marchés des métaux précieux.",
  "À la cour de la comtesse Marie de Champagne, Chrétien de Troyes écrit vers 1170-1190 « Lancelot ou le Chevalier de la charrette » et « Perceval ou le Conte du Graal », qui fondent la légende arthurienne en langue française. Le centre de Troyes a conservé ses maisons à pans de bois, reconstruites après le grand incendie de 1524."],
 "Foires de Champagne"),
A("gastronomie","L'andouillette de Troyes et ses cinq A","XVIe siècle · Troyes",
 "Spécialité troyenne, l'andouillette de porc est tirée à la main en lanières. Elle est défendue par l'Association amicale des amateurs d'authentiques andouillettes, l'AAAAA.",
 "L'andouillette de Troyes, préparée avec des lanières de chaudins et d'estomac de porc, est la spécialité charcutière de la ville depuis au moins le XVIe siècle.",
 ["La tradition rapporte qu'en 1562, des soldats royaux entrés dans le quartier Saint-Denis se seraient gavés d'andouillettes au point de ne plus pouvoir combattre. Plus sûrement, la charcuterie troyenne est réputée depuis la Renaissance.",
  "Sa recette impose que les boyaux soient coupés en lanières puis « tirés » à la main dans l'enveloppe. Créée par des critiques gastronomiques en 1970, l'AAAAA décerne son diplôme aux andouillettes qu'elle juge conformes ; celle de Troyes en est la référence."],
 "Andouillette"),
]

# ---------------------------------------------------------------- CHALON
chalon=[
A("politique","Gilles Platret et les menus de substitution","2014-2026 · Hôtel de ville",
 "En 2015, le maire de Chalon supprime les menus sans porc dans les cantines. La justice administrative annule la décision jusqu'au Conseil d'État en 2020. Il est réélu dès le premier tour en 2026 avec 61,48 %.",
 "Gilles Platret, Les Républicains puis divers droite, maire de Chalon-sur-Saône depuis 2014, a été réélu au premier tour des municipales de mars 2026 avec 61,48 % des voix.",
 ["En 2015, au nom de la laïcité, il met fin aux menus de substitution servis les jours de porc dans les cantines scolaires de la ville. La Ligue de défense judiciaire des musulmans attaque la décision. Le tribunal administratif de Dijon l'annule en 2017, estimant que l'intérêt des enfants n'a pas été pris en compte ; la cour administrative d'appel de Lyon confirme, puis le Conseil d'État rejette le pourvoi de la ville le 11 décembre 2020.",
  "Le débat devient national, plusieurs maires de droite et d'extrême droite revendiquant la même mesure. En mars 2026, la liste de Gilles Platret obtient 8 486 voix, contre 26,20 % à celle de Clément Mugnier, divers gauche, et 10,58 % à La France insoumise. Elle détient 36 des 43 sièges."],
 "Gilles Platret"),
A("personnalites","Nicéphore Niépce, l'inventeur de la photographie","1765-1833 · Musée Nicéphore-Niépce",
 "Né à Chalon en 1765, Nicéphore Niépce réalise vers 1827 la plus ancienne photographie conservée, une vue prise de sa fenêtre après des heures de pose. Chalon lui consacre un musée.",
 "Nicéphore Niépce, né à Chalon-sur-Saône le 7 mars 1765, est l'inventeur de la photographie : il obtient les premières images fixées durablement par la lumière dans sa propriété de Saint-Loup-de-Varennes, près de la ville.",
 ["Inventeur touche-à-tout, il met au point avec son frère Claude un moteur à combustion interne, le pyréolophore, breveté en 1807. Il cherche ensuite à fixer les images de la chambre noire, en utilisant du bitume de Judée qui durcit à la lumière.",
  "Vers 1827, depuis une fenêtre de sa maison du Gras, il obtient une vue des toits, après une exposition de plusieurs heures : c'est la plus ancienne photographie conservée, aujourd'hui à l'université du Texas. En 1829, il s'associe avec Louis Daguerre, qui poursuivra ses travaux après sa mort, en 1833.",
  "Le musée Nicéphore-Niépce, sur les quais de la Saône, conserve ses appareils et une importante collection de photographies."],
 "Nicéphore Niépce",
 timeline=T(("1765","Naissance à Chalon-sur-Saône."),("1807","Brevet du pyréolophore."),("1827","Point de vue du Gras, plus ancienne photographie conservée."),("1829","Association avec Daguerre."),("1833","Mort à Saint-Loup-de-Varennes.")),
 access="Musée Nicéphore-Niépce, quai des Messageries"),
A("sport","L'Élan chalonnais, champion de France en 2012","2012 · Colisée",
 "En 2012, le club de basket de Chalon réussit le doublé coupe de France et championnat, puis dispute une finale européenne. Il est de nouveau sacré champion de France en 2017.",
 "L'Élan sportif chalonnais, club de basket-ball de Chalon-sur-Saône, a été champion de France en 2012 et en 2017.",
 ["En 2012, l'équipe entraînée par Grégor Beugnot remporte la coupe de France puis le championnat, en battant Le Mans en finale. La même saison, elle atteint la finale de l'EuroChallenge, la troisième coupe d'Europe.",
  "Le club, qui joue au Colisée, gagne un second titre de champion de France en 2017. Pour une ville de 45 000 habitants, ces sacres font de Chalon l'une des places fortes du basket français."],
 "Élan sportif chalonnais"),
]

# ---------------------------------------------------------------- MACON
macon=[
A("politique","Jean-Patrick Courtois réélu à Mâcon","2026 · Hôtel de ville",
 "Le centriste Jean-Patrick Courtois, ancien sénateur, a été réélu maire de Mâcon en mars 2026 avec 48,28 % des voix au second tour, devant la liste de gauche d'Émile Blondet.",
 "Jean-Patrick Courtois, divers centre, maire sortant de Mâcon, a été réélu au second tour des municipales de mars 2026 avec 48,28 % des voix.",
 ["Ancien sénateur de Saône-et-Loire, il arrive en tête du premier tour avec 44,69 %. Au second, sa liste obtient 4 435 voix, contre 3 593 à celle d'Émile Blondet, divers gauche (39,11 %), et 1 158 à celle de Baptiste Delcroix, soutenue par l'UDR (12,61 %).",
  "Sa liste détient 29 des 39 sièges du conseil municipal. La participation n'a atteint que 47,84 %."],
 "Jean-Patrick Courtois"),
A("insolite","Lamartine, 0,26 % à la présidentielle de 1848","Décembre 1848 · Mâcon",
 "Le poète mâconnais Lamartine, héros de la révolution de février 1848, se présente à la première élection présidentielle au suffrage universel. Il recueille moins de 18 000 voix.",
 "Alphonse de Lamartine, né à Mâcon le 21 octobre 1790, poète des « Méditations », a dirigé de fait le gouvernement provisoire de 1848 avant d'être écrasé à l'élection présidentielle de décembre 1848.",
 ["Ses « Méditations poétiques », publiées en 1820 avec « Le Lac », en font l'une des voix majeures du romantisme. Député, il se rallie à la République et, en février 1848, proclame le nouveau régime à l'hôtel de ville de Paris. Ministre des Affaires étrangères du gouvernement provisoire, il refuse le drapeau rouge et défend le drapeau tricolore devant la foule.",
  "Mais sa popularité s'effondre après les journées de juin. Le 10 décembre 1848, Louis-Napoléon Bonaparte est élu président avec près de 75 % des voix ; Lamartine n'obtient qu'environ 0,26 %. Ruiné, il passe la fin de sa vie à écrire pour payer ses dettes et meurt en 1869. Il repose à Saint-Point, près de Mâcon ; sa ville natale lui consacre un musée à l'hôtel Senecé."],
 "Alphonse de Lamartine",
 timeline=T(("1790","Naissance à Mâcon."),("1820","« Méditations poétiques »."),("1848","Membre du gouvernement provisoire ; candidat malheureux à la présidentielle."),("1869","Mort à Paris."))),
A("patrimoine","Le vieux Saint-Vincent, cathédrale rasée à la Révolution","XIIe-XIXe siècles · Quartier Saint-Vincent",
 "De l'ancienne cathédrale de Mâcon, détruite après la Révolution, il ne reste que deux tours et le porche. Une nouvelle cathédrale a été bâtie à côté au XIXe siècle.",
 "Le vieux Saint-Vincent est le vestige de l'ancienne cathédrale de Mâcon, démolie après la Révolution, dont subsistent le narthex et les deux tours octogonales.",
 ["Mâcon perd son évêché à la Révolution, qui supprime le diocèse. L'édifice est vendu comme bien national puis démoli à partir de 1799 ; seuls la façade, ses deux tours et le porche roman, orné d'un tympan du Jugement dernier mutilé, sont conservés.",
  "Une nouvelle église Saint-Vincent, de style néoclassique, est construite à proximité au XIXe siècle. Le vieux Saint-Vincent accueille aujourd'hui des expositions."],
 "Vieux Saint-Vincent de Mâcon",
 protection="Monument historique classé"),
]

# ---------------------------------------------------------------- AUXERRE
auxerre=[
A("politique","Mathieu Debain bat le maire sortant à Auxerre","1971-2026 · Hôtel de ville",
 "Dans une quadrangulaire, le centriste Mathieu Debain a battu en mars 2026 le maire sortant Crescent Marault avec 33,80 % des voix. Auxerre a longtemps été la ville de Jean-Pierre Soisson.",
 "Mathieu Debain, divers centre, est maire d'Auxerre depuis mars 2026, élu au second tour d'une quadrangulaire avec 33,80 % des voix.",
 ["Jean-Pierre Soisson, maire de 1971 à 1998, a été plusieurs fois ministre, dont ministre du Travail du gouvernement Rocard au titre de l'« ouverture » de 1988. Le socialiste Guy Férez lui succède de 2001 à 2020, puis le centriste Crescent Marault.",
  "En mars 2026, quatre listes se maintiennent au second tour. Mathieu Debain obtient 3 922 voix, devant la liste d'union de la gauche de Mani Cambefort (27,73 %), le maire sortant (23,96 %) et le Rassemblement national (14,52 %). Avec la prime majoritaire, sa liste détient 27 des 39 sièges."],
 "Auxerre"),
A("faits_divers","Les disparues de l'Yonne et Émile Louis","1977-2004 · Auxerre",
 "Entre 1977 et 1979, sept jeunes femmes handicapées disparaissent autour d'Auxerre. Il faut plus de vingt ans pour que le chauffeur de car Émile Louis soit condamné à perpétuité.",
 "Entre 1977 et 1979, sept jeunes femmes déficientes mentales, pensionnaires d'institutions de l'Yonne, disparaissent près d'Auxerre ; le chauffeur de car Émile Louis, qui les transportait, est condamné à perpétuité en 2004 pour leurs meurtres.",
 ["Les disparitions sont d'abord classées comme des fugues, faute de plaintes des familles et d'intérêt des institutions. En 1984, le gendarme Christian Jambert rédige un rapport mettant en cause Émile Louis, sans suite. Le gendarme est retrouvé mort en 1997 ; la thèse du suicide sera mise en doute après l'exhumation de son corps en 2004.",
  "L'association de défense des handicapés de l'Yonne relance l'affaire. Arrêté en décembre 2000, Émile Louis avoue et conduit les enquêteurs à deux corps, avant de se rétracter. Le 25 novembre 2004, la cour d'assises de l'Yonne le condamne à la réclusion criminelle à perpétuité ; la peine est confirmée en appel en 2006. Il meurt en détention en 2013.",
  "L'affaire a montré les défaillances de la justice et des services sociaux, et la vulnérabilité des personnes placées en institution."],
 "Affaire des disparues de l'Yonne",
 status="Émile Louis, condamné à perpétuité en 2004, peine confirmée en appel en 2006, est mort en 2013."),
A("sport","Guy Roux, 44 ans sur le banc auxerrois","1961-2005 · Stade de l'Abbé-Deschamps",
 "Arrivé en 1961 dans un club amateur, Guy Roux en fait un champion de France en 1996. Il entraîne l'AJ Auxerre pendant 44 ans.",
 "Guy Roux a entraîné l'AJ Auxerre de 1961 à 2005, faisant de ce club d'une ville de 35 000 habitants un champion de France et un habitué des coupes d'Europe.",
 ["Recruté à 22 ans comme entraîneur-joueur d'un club de division d'honneur, il le conduit jusqu'en première division en 1980. Il bâtit un centre de formation d'où sortent notamment Basile Boli, Éric Cantona et Djibril Cissé.",
  "En 1996, Auxerre réussit le doublé coupe de France et championnat. Le club remporte quatre coupes de France sous sa direction, en 1994, 1996, 2003 et 2005. Réputé pour sa gestion économe, Guy Roux devient l'une des figures les plus populaires du football français, jusqu'à sa marionnette dans « Les Guignols de l'info »."],
 "Guy Roux",
 timeline=T(("1961","Arrive à l'AJ Auxerre, en amateur."),("1980","Montée en première division."),("1996","Doublé coupe-championnat."),("2005","Dernière coupe de France et départ."))),
A("patrimoine","Le Christ à cheval de la crypte d'Auxerre","XIe siècle · Cathédrale Saint-Étienne",
 "Dans la crypte romane de la cathédrale d'Auxerre, une fresque montre le Christ à cheval, entouré de quatre anges cavaliers. C'est une représentation unique dans l'art chrétien.",
 "La cathédrale Saint-Étienne d'Auxerre, gothique, conserve sous son chœur une crypte du XIe siècle ornée d'une fresque du Christ à cheval, sans équivalent connu.",
 ["La crypte appartient à la cathédrale romane élevée au début du XIe siècle. Sa voûte est peinte d'un Christ en majesté chevauchant un cheval blanc, inspiré de l'Apocalypse, entouré de quatre anges eux aussi à cheval.",
  "Au-dessus, la cathédrale gothique est construite à partir de 1215 ; son chœur conserve d'importants vitraux du XIIIe siècle, et sa façade, jamais terminée, n'a qu'une seule tour achevée."],
 "Cathédrale Saint-Étienne d'Auxerre",
 lat=47.7978,lon=3.5728,access="Crypte et trésor en visite payante",protection="Monument historique classé"),
]

# ---------------------------------------------------------------- COLMAR
colmar=[
A("politique","Éric Straumann face à son ancien suppléant","2020-2026 · Hôtel de ville",
 "Élu en 2020 après les 25 ans de Gilbert Meyer, Éric Straumann a été réélu en mars 2026 avec 37,70 % des voix, devant Yves Hemedinger, qui lui avait succédé à l'Assemblée.",
 "Éric Straumann, divers droite, maire de Colmar depuis 2020, a été réélu au second tour des municipales de mars 2026 avec 37,70 % des voix.",
 ["Gilbert Meyer dirige Colmar de 1995 à 2020. Député du Haut-Rhin, Éric Straumann l'emporte en 2020 et laisse son siège de député à son suppléant, Yves Hemedinger.",
  "En mars 2026, les deux hommes s'affrontent. Au second tour, Éric Straumann obtient 7 323 voix, contre 6 144 à Yves Hemedinger (31,63 %), 17,17 % à l'union de la gauche et 13,51 % à l'extrême droite. Sa liste détient 34 sièges. L'abstention dépasse 54 %."],
 "Éric Straumann"),
A("personnalites","Bartholdi, le Colmarien de la statue de la Liberté","1834-1904 · Musée Bartholdi",
 "Né à Colmar en 1834, Auguste Bartholdi a sculpté la statue de la Liberté de New York et le Lion de Belfort. Une réplique de 12 mètres de sa Liberté accueille les visiteurs à l'entrée nord de la ville.",
 "Frédéric Auguste Bartholdi, né à Colmar le 2 août 1834, est l'auteur de « La Liberté éclairant le monde », inaugurée à New York le 28 octobre 1886.",
 ["Fils d'une famille aisée de Colmar, il se forme à Paris à la peinture et à la sculpture. Après l'annexion de l'Alsace par l'Allemagne en 1871, il met son art au service de la mémoire nationale : le Lion de Belfort, achevé en 1880, célèbre la résistance de la ville pendant le siège.",
  "La statue de la Liberté, offerte par la France aux États-Unis, est montée sur une structure conçue par Gustave Eiffel. Sa maison natale, rue des Marchands, abrite le musée Bartholdi. En 2004, Colmar a installé une réplique de la statue, haute de douze mètres, sur un rond-point à l'entrée de la ville."],
 "Auguste Bartholdi",
 timeline=T(("1834","Naissance à Colmar."),("1880","Achèvement du Lion de Belfort."),("1886","Inauguration de la statue de la Liberté à New York."),("1904","Mort à Paris.")),
 access="Musée Bartholdi, rue des Marchands"),
A("patrimoine","Le retable d'Issenheim, chef-d'œuvre d'Unterlinden","1512-1516 · Musée Unterlinden",
 "Peint pour soigner l'âme des malades du « mal des ardents », le retable d'Issenheim de Grünewald montre un Christ supplicié couvert de plaies. Il est exposé à Colmar depuis la Révolution.",
 "Le retable d'Issenheim, peint par Matthias Grünewald et sculpté par Nicolas de Haguenau entre 1512 et 1516, est conservé au musée Unterlinden de Colmar.",
 ["Il a été commandé pour le couvent des Antonins d'Issenheim, qui soignaient les malades de l'ergotisme, une intoxication due à un champignon du seigle qui provoquait gangrènes et brûlures. Le Christ de la Crucifixion, couvert de plaies, renvoyait les malades à leur propre souffrance.",
  "Ses panneaux mobiles s'ouvraient selon les fêtes du calendrier. Saisi à la Révolution et transporté à Colmar, le retable est devenu la pièce maîtresse du musée Unterlinden, installé dans un ancien couvent de dominicaines et agrandi en 2015 par les architectes Herzog et de Meuron."],
 "Retable d'Issenheim",
 access="Musée Unterlinden, fermé le mardi"),
A("insolite","La Petite Venise et le Château ambulant","Quartier de la Krutenau · Colmar",
 "Les maisons à colombages de la Petite Venise, au bord de la Lauch, sont souvent citées comme l'une des inspirations du « Château ambulant » de Hayao Miyazaki, sorti en 2004.",
 "La Petite Venise, quartier de Colmar traversé par la Lauch, est l'un des sites les plus photographiés d'Alsace ; elle est souvent présentée comme une source d'inspiration du film d'animation « Le Château ambulant ».",
 ["Le quartier était celui des maraîchers, qui transportaient leurs légumes en barques à fond plat jusqu'au marché couvert. Ses maisons à pans de bois colorées, restaurées à partir des années 1970, attirent aujourd'hui de très nombreux visiteurs, surtout pendant les marchés de Noël.",
  "Le studio Ghibli s'est inspiré de villes d'Alsace pour les décors du « Château ambulant », et Colmar en revendique une part, ce qui attire de nombreux visiteurs japonais."],
 "Petite Venise (Colmar)",
 links=[L("film","« Le Château ambulant » (2004), de Hayao Miyazaki","https://fr.wikipedia.org/wiki/Le_Ch%C3%A2teau_ambulant","Des décors inspirés des villes alsaciennes")]),
]

# ---------------------------------------------------------------- BELFORT
belfort=[
A("politique","Chevènement, le ministre qui démissionnait","1983-2026 · Hôtel de ville",
 "Maire de Belfort pendant vingt ans, Jean-Pierre Chevènement a quitté trois fois le gouvernement par désaccord. Damien Meslot, maire depuis 2014, a été réélu en 2026 avec 53,41 %.",
 "Damien Meslot, Les Républicains, maire de Belfort depuis 2014, a été réélu au second tour des municipales de mars 2026 avec 53,41 % des voix ; la ville a été dirigée de 1983 à 2007 par Jean-Pierre Chevènement, avec une interruption.",
 ["Jean-Pierre Chevènement, cofondateur du CERES au Parti socialiste, devient maire de Belfort en 1983. Ministre de la Recherche, de l'Éducation nationale, de la Défense puis de l'Intérieur, il démissionne trois fois : en 1983 contre le tournant de la rigueur, en 1991 contre la participation à la guerre du Golfe, en 2000 contre le processus de Matignon sur la Corse. On lui prête la formule selon laquelle un ministre, ça ferme sa gueule ou ça démissionne.",
  "Candidat à l'élection présidentielle de 2002, il obtient 5,33 %, un score souvent cité parmi les causes de l'élimination de Lionel Jospin au premier tour. Il quitte la mairie en 2007.",
  "En mars 2026, Damien Meslot obtient 6 732 voix au second tour, devant Florian Chauche, divers gauche (27,90 %), Bastien Faudot (9,56 %) et le Rassemblement national (9,12 %). Sa liste détient 33 des 43 sièges."],
 "Jean-Pierre Chevènement"),
A("histoire","Le Lion de Belfort, 103 jours de siège","1870-1880 · Citadelle",
 "Assiégée par les Prussiens pendant 103 jours en 1870-1871, Belfort ne se rend que sur ordre du gouvernement. Elle reste française, et Bartholdi sculpte à flanc de rocher un lion de 22 mètres.",
 "Du 3 novembre 1870 au 18 février 1871, la garnison du colonel Denfert-Rochereau tient Belfort face à l'armée prussienne ; la ville reste française à la paix, ce que commémore le Lion de Belfort de Bartholdi.",
 ["Après la défaite de Sedan, la place forte de Belfort est encerclée. Le colonel Pierre Philippe Denfert-Rochereau, avec quelque 17 000 hommes, résiste aux bombardements pendant plus de trois mois. Il ne quitte la ville, avec les honneurs de la guerre, que sur ordre du gouvernement, après l'armistice.",
  "Au traité de Francfort, l'Alsace est annexée, mais Belfort reste française : son arrondissement devient le Territoire de Belfort, le plus petit département hors Île-de-France. Bartholdi sculpte au pied de la citadelle un lion de grès rose de 22 mètres de long et 11 mètres de haut, achevé en 1880 ; une réplique en cuivre se trouve place Denfert-Rochereau, à Paris."],
 "Lion de Belfort",
 lat=47.6370,lon=6.8657,access="Terrasse du Lion accessible, billet couplé avec la citadelle",protection="Monument historique classé"),
A("histoire","Alstom Belfort, la ville du TGV menacée","2016 · Usine Alstom",
 "En septembre 2016, Alstom annonce le transfert de la production de son usine de Belfort, berceau des locomotives du TGV. Un mois plus tard, l'État commande quinze rames pour sauver le site.",
 "L'usine Alstom de Belfort, qui a construit les motrices des premiers TGV, a failli fermer en 2016, avant que l'État n'intervienne par des commandes publiques.",
 ["Les ateliers de construction ferroviaire de Belfort, nés au XIXe siècle de l'installation de l'Alsacienne de constructions mécaniques, fondatrice d'Alstom, après l'annexion de l'Alsace, produisent des locomotives depuis plus d'un siècle, dont les motrices du TGV.",
  "En septembre 2016, Alstom annonce le transfert de l'activité vers Reichshoffen, faute de commandes. À quelques mois de l'élection présidentielle, le gouvernement réagit : l'État et la SNCF commandent quinze rames TGV, destinées notamment à des lignes Intercités. Le site est maintenu, mais l'épisode reste un symbole de la fragilité de l'industrie française."],
 "Alstom"),
]

# ---------------------------------------------------------------- CHARLEVILLE
charleville=[
A("politique","Boris Ravignon réélu dès le premier tour","2014-2026 · Hôtel de ville",
 "Maire depuis 2014, Boris Ravignon a été réélu dès le premier tour en mars 2026 avec 65,91 % des voix, dans une ville marquée par une abstention de plus de 52 %.",
 "Boris Ravignon, divers droite, maire de Charleville-Mézières depuis 2014, a été réélu au premier tour des municipales de mars 2026 avec 65,91 % des voix.",
 ["Ancien conseiller de Nicolas Sarkozy à l'Élysée, il prend la mairie en 2014 et préside aussi l'agglomération Ardenne Métropole.",
  "En mars 2026, sa liste obtient 7 993 voix, loin devant l'union de la gauche de Damien Lerouge (20,15 %) et l'union de l'extrême droite de Romain Petitfils (9,77 %). Elle détient 37 des 43 sièges. La commune de Charleville-Mézières est née en 1966 de la fusion de Charleville, Mézières et trois autres communes."],
 "Boris Ravignon"),
A("faits_divers","Le procès Fourniret à Charleville-Mézières","2008 · Palais de justice",
 "En 2008, la cour d'assises des Ardennes juge à Charleville le tueur en série Michel Fourniret et sa femme Monique Olivier. Il est condamné à la perpétuité réelle, elle à la perpétuité.",
 "Le 28 mai 2008, la cour d'assises des Ardennes, à Charleville-Mézières, condamne Michel Fourniret à la réclusion criminelle à perpétuité incompressible pour sept meurtres de jeunes filles commis entre 1987 et 2001.",
 ["Originaire de Sedan, Michel Fourniret est arrêté en Belgique en 2003 après une tentative d'enlèvement. Sa femme, Monique Olivier, finit par révéler ses crimes, commis en France et en Belgique, dont celui d'Isabelle Laville, 17 ans, enlevée à Auxerre en 1987. Le procès, ouvert en mars 2008, dure deux mois.",
  "Monique Olivier est condamnée à la perpétuité pour complicité dans quatre de ces meurtres. Michel Fourniret meurt en détention en mai 2021, sans avoir été jugé pour d'autres crimes qu'il avait fini par avouer, dont le meurtre d'Estelle Mouzin, 9 ans, disparue en 2003.",
  "En décembre 2023, la cour d'assises des Hauts-de-Seine condamne de nouveau Monique Olivier à la réclusion criminelle à perpétuité, avec une période de sûreté de vingt ans, pour sa complicité dans les enlèvements et meurtres d'Estelle Mouzin, de Joanna Parrish et de Marie-Angèle Domèce. Les corps d'Estelle Mouzin et de Marie-Angèle Domèce n'ont jamais été retrouvés."],
 "Michel Fourniret",
 status="Michel Fourniret, condamné à la perpétuité incompressible en 2008, est mort en 2021. Monique Olivier a été condamnée à la perpétuité en 2008, puis de nouveau en décembre 2023."),
A("personnalites","Arthur Rimbaud, le poète qui fuyait Charleville","1854-1891 · Musée Rimbaud",
 "Né à Charleville en 1854, Arthur Rimbaud fugue plusieurs fois vers Paris, écrit toute son œuvre avant vingt et un ans, puis part trafiquer en Afrique. Il repose au cimetière de sa ville natale.",
 "Arthur Rimbaud, né à Charleville le 20 octobre 1854, a écrit l'essentiel de son œuvre entre quinze et vingt ans avant de renoncer à la poésie ; il est enterré à Charleville.",
 ["Élève brillant du collège de Charleville, il étouffe dans sa ville, qu'il juge « supérieurement idiote » dans une lettre de 1870. Il fugue à plusieurs reprises, envoie « Le Bateau ivre » à Verlaine et le rejoint à Paris en 1871. Leur liaison tumultueuse s'achève à Bruxelles en 1873, quand Verlaine lui tire dessus.",
  "Après « Une saison en enfer » et les « Illuminations », il cesse d'écrire et voyage, jusqu'à devenir négociant à Harar, en Éthiopie. Amputé d'une jambe, il meurt à Marseille le 10 novembre 1891. Le musée Rimbaud occupe le Vieux Moulin, sur la Meuse, à quelques pas de la maison où il a vécu."],
 "Arthur Rimbaud",
 timeline=T(("1854","Naissance à Charleville."),("1871","« Le Bateau ivre », départ pour Paris."),("1873","« Une saison en enfer » ; Verlaine lui tire dessus."),("1880","Installation à Harar."),("1891","Mort à Marseille, inhumé à Charleville.")),
 access="Musée Arthur-Rimbaud, quai Arthur-Rimbaud"),
A("patrimoine","La place Ducale, sœur de la place des Vosges","1606-1628 · Centre-ville",
 "Charleville a été fondée en 1606 par Charles de Gonzague, qui lui a donné son nom. Sa place Ducale, bordée d'arcades, rappelle la place des Vosges à Paris, construite à la même époque.",
 "La place Ducale de Charleville, construite au début du XVIIe siècle, est le cœur de la ville nouvelle fondée en 1606 par Charles de Gonzague, duc de Nevers et de Rethel.",
 ["Le prince veut créer une capitale pour sa principauté souveraine d'Arches. L'architecte Clément Métezeau dessine une ville en damier autour d'une grande place à arcades, aux façades de brique et de pierre ocre, sur le modèle de la place Royale, l'actuelle place des Vosges, à laquelle travaille son frère Louis.",
  "Charleville est aussi la capitale mondiale de la marionnette : depuis 1961, elle accueille le Festival mondial des théâtres de marionnettes, et l'École nationale supérieure des arts de la marionnette s'y est installée en 1987."],
 "Place Ducale",
 lat=49.7735,lon=4.7206,protection="Monument historique classé"),
]

# ---------------------------------------------------------------- EPINAL
epinal=[
A("politique","Épinal, la ville de Philippe Séguin","1983-2026 · Hôtel de ville",
 "Philippe Séguin, figure du « non » à Maastricht et président de l'Assemblée, a dirigé Épinal de 1983 à 1997. En mars 2026, Benoît Jourdain a battu le maire sortant avec 39,93 % des voix.",
 "Benoît Jourdain, divers droite, est maire d'Épinal depuis mars 2026, élu au second tour avec 39,93 % des voix face au maire sortant Patrick Nardin.",
 ["Philippe Séguin, gaulliste social, devient maire d'Épinal en 1983. Ministre des Affaires sociales de 1986 à 1988, il mène en 1992 la campagne contre le traité de Maastricht et débat à la télévision avec François Mitterrand. Président de l'Assemblée nationale de 1993 à 1997, puis premier président de la Cour des comptes à partir de 2004, il meurt en fonctions le 7 janvier 2010.",
  "Michel Heinrich lui succède en 1997 jusqu'en 2020, puis Patrick Nardin. En mars 2026, deux listes de droite s'affrontent. Benoît Jourdain, deuxième au premier tour, l'emporte au second avec 4 270 voix contre 4 015 au maire sortant (37,55 %) ; la gauche obtient 13,01 % et le Rassemblement national 9,51 %."],
 "Philippe Séguin"),
A("patrimoine","Les images d'Épinal, depuis 1796","1796 · Imagerie d'Épinal",
 "Depuis 1796, l'imagerie fondée par Jean-Charles Pellerin produit à Épinal des estampes coloriées au pochoir. Elles ont donné une expression : une « image d'Épinal », vision naïve et embellie.",
 "L'Imagerie d'Épinal, fondée en 1796 par Jean-Charles Pellerin, a diffusé dans toute la France des images populaires coloriées, à l'origine de l'expression « image d'Épinal ».",
 ["Cartier de métier, Jean-Charles Pellerin imprime des gravures sur bois coloriées au pochoir : saints, soldats, scènes de la vie quotidienne et surtout l'épopée napoléonienne, qui contribue à la légende de l'Empereur. Vendues par des colporteurs, ces images entrent dans les foyers les plus modestes.",
  "L'expression « image d'Épinal » en est venue à désigner une représentation simpliste et idéalisée de la réalité. L'Imagerie, toujours en activité, se visite, et le Musée de l'Image présente les collections."],
 "Imagerie d'Épinal",
 access="Imagerie et Musée de l'Image, quai de Dogneville"),
A("histoire","La basilique Saint-Maurice et les reliques de saint Goëry","XIe-XIIIe siècles · Vieille ville",
 "Épinal est née autour d'un monastère fondé vers 980 par l'évêque de Metz. Sa basilique Saint-Maurice, mêlant roman et gothique, abrite les reliques de saint Goëry.",
 "La basilique Saint-Maurice d'Épinal, élevée du XIe au XIIIe siècle, est le principal monument de la ville, née à la fin du Xe siècle autour d'un monastère.",
 ["Vers 980, l'évêque de Metz Thierry de Hamelant fonde un monastère sur les bords de la Moselle et y fait transférer les reliques de saint Goëry, évêque de Metz au VIIe siècle. Une ville se forme autour, protégée par un château.",
  "La basilique combine une tour-porche romane et un chœur gothique de style champenois. Sa fête, la Saint-Nicolas, réunit chaque décembre des milliers de personnes dans les rues de la ville."],
 "Basilique Saint-Maurice d'Épinal",
 lat=48.1736,lon=6.4507,access="Entrée libre en dehors des offices",protection="Monument historique classé"),
]

cities=[("10387","Troyes","Aube",48.2973,4.0744,troyes),
        ("71076","Chalon-sur-Saône","Saône-et-Loire",46.7806,4.8539,chalon),
        ("71270","Mâcon","Saône-et-Loire",46.3069,4.8287,macon),
        ("89024","Auxerre","Yonne",47.7986,3.5674,auxerre),
        ("68066","Colmar","Haut-Rhin",48.0794,7.3585,colmar),
        ("90010","Belfort","Territoire de Belfort",47.6380,6.8628,belfort),
        ("08105","Charleville-Mézières","Ardennes",49.7719,4.7161,charleville),
        ("88160","Épinal","Vosges",48.1724,6.4496,epinal)]
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
