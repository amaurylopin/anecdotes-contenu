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

# ---------------------------------------------------------------- BOURGES
bourges=[
A("politique","Yann Galut réélu, Bourges reste à gauche","2020-2026 · Hôtel de ville",
 "Élu en 2020 dans une ville longtemps dirigée par la droite, le socialiste Yann Galut a été réélu en mars 2026 avec 53,40 % des voix et 38 sièges sur 49.",
 "Yann Galut (PS), maire de Bourges depuis 2020, a été réélu au second tour des municipales de mars 2026 avec 53,40 % des voix.",
 ["Ancien député du Cher de 1997 à 2002 et de 2012 à 2017, Yann Galut prend Bourges en 2020 à la tête d'une liste de rassemblement de la gauche et des écologistes. La ville avait été dirigée par Serge Lepeltier, maire de 1995 à 2014 et ministre de l'Écologie de 2004 à 2005, puis par Pascal Blanc.",
  "En mars 2026, sa liste devance au second tour celle de Philippe Mercier, divers droite (34,25 %), et celle du Rassemblement national conduite par Ugo Iannuzzi (12,35 %)."],
 "Yann Galut"),
A("personnalites","Jacques Cœur, l'argentier de Charles VII","1400-1456 · Palais Jacques-Cœur",
 "Fils d'un pelletier de Bourges, Jacques Cœur devient le plus riche marchand du royaume et finance la reconquête de Charles VII. Il finit disgracié, évadé, puis mort sur une île grecque.",
 "Jacques Cœur, né à Bourges vers 1400, a été l'argentier du roi Charles VII et l'un des plus grands marchands de son temps ; son palais de Bourges est un chef-d'œuvre du gothique civil.",
 ["Charles VII, chassé de Paris pendant la guerre de Cent Ans, a fait de Bourges sa capitale, au point d'être surnommé le « roi de Bourges ». Jacques Cœur, fils d'un marchand de fourrures de la ville, y bâtit une fortune dans le commerce avec l'Orient, à partir de Montpellier, avec ses propres galées. Argentier du roi à partir de 1439, il finance la reconquête de la Normandie.",
  "Sa richesse lui vaut des ennemis. Arrêté en 1451, accusé notamment d'avoir empoisonné Agnès Sorel, maîtresse du roi, il est condamné en 1453 et ses biens sont confisqués. Il s'évade en 1454, gagne Rome et meurt en 1456 dans l'île de Chios, au cours d'une expédition contre les Turcs.",
  "Son palais, construit entre 1443 et 1451, porte sa devise, « À vaillans cœurs riens impossible », et ses emblèmes, des cœurs et des coquilles Saint-Jacques."],
 "Jacques Cœur",
 timeline=T(("1400","Naissance à Bourges, vers cette date."),("1439","Argentier de Charles VII."),("1451","Arrêté et accusé de l'empoisonnement d'Agnès Sorel."),("1454","Évasion vers Rome."),("1456","Mort à Chios.")),
 lat=47.0828,lon=2.3958,access="Palais Jacques-Cœur, Centre des monuments nationaux",protection="Monument historique classé"),
A("patrimoine","La cathédrale Saint-Étienne et sa tour de Beurre","1195-XVIe siècle · Place Étienne-Dolet",
 "Commencée en 1195, la cathédrale de Bourges n'a pas de transept, un plan rare pour une grande cathédrale gothique. Sa tour nord a été reconstruite grâce à des dispenses de jeûne pendant le Carême.",
 "La cathédrale Saint-Étienne de Bourges, édifiée à partir de 1195, est inscrite depuis 1992 au patrimoine mondial de l'Unesco pour son architecture gothique et ses vitraux du XIIIe siècle.",
 ["Son plan, sans transept, crée un vaisseau continu de cinq nefs étagées, dont la largeur et la lumière surprennent. Les vitraux du chœur, posés au début du XIIIe siècle, comptent parmi les ensembles les mieux conservés de cette époque.",
  "La tour nord s'effondre en 1506. Pour la reconstruire, l'archevêché vend aux fidèles des dispenses autorisant la consommation de beurre pendant le Carême : l'ouvrage, achevé au XVIe siècle, est resté la « tour de Beurre »."],
 "Cathédrale Saint-Étienne de Bourges",
 lat=47.0822,lon=2.3995,access="Entrée libre en dehors des offices ; tour et crypte en visite payante",protection="Monument historique classé, patrimoine mondial de l'Unesco"),
A("histoire","Avaricum, la ville gauloise prise par César","52 av. J.-C. · Avaricum",
 "En 52 av. J.-C., César assiège Avaricum, la capitale des Bituriges. Selon son propre récit, sur 40 000 habitants, 800 seulement parviennent à s'échapper.",
 "Au printemps 52 av. J.-C., pendant la révolte de Vercingétorix, les légions de Jules César assiègent et prennent Avaricum, l'actuelle Bourges, capitale du peuple gaulois des Bituriges.",
 ["Vercingétorix pratique la politique de la terre brûlée et veut incendier Avaricum, mais les Bituriges le supplient d'épargner leur ville, protégée par des marais et un rempart. César l'investit et fait construire une terrasse d'assaut, malgré le froid et la faim de ses troupes.",
  "Après près d'un mois de siège, les Romains prennent la ville sous une pluie battante. César écrit dans « La Guerre des Gaules » que ses soldats n'épargnent ni les vieillards, ni les femmes, ni les enfants. Quelques mois plus tard, Vercingétorix remporte la victoire de Gergovie, avant de capituler à Alésia."],
 "Siège d'Avaricum"),
A("patrimoine","Le Printemps de Bourges, festival depuis 1977","Depuis 1977 · Centre-ville",
 "Créé en 1977 par Alain Meilland et Daniel Colling, le Printemps de Bourges ouvre chaque printemps la saison des festivals et révèle de jeunes talents.",
 "Le Printemps de Bourges, festival de chanson et de musiques actuelles, se tient chaque année en avril depuis 1977.",
 ["Alain Meilland et Daniel Colling lancent le festival en 1977 pour donner une scène à la chanson française, dans une ville qui n'a pas de tradition rock. Il s'ouvre ensuite à toutes les musiques actuelles.",
  "Son dispositif de repérage, les « Inouïs », permet chaque année à de jeunes groupes de jouer devant les professionnels. Le festival investit les salles et les rues du centre pendant près d'une semaine."],
 "Printemps de Bourges"),
]

# ---------------------------------------------------------------- CHATEAUROUX
chateauroux=[
A("politique","Gil Avérous réélu au premier tour à Châteauroux","2014-2026 · Hôtel de ville",
 "Maire depuis 2014, Gil Avérous a été réélu dès le premier tour en mars 2026 avec 68,24 % des voix.",
 "Gil Avérous, divers droite, maire de Châteauroux depuis 2014, a été réélu au premier tour des municipales de mars 2026 avec 68,24 % des voix.",
 ["Élu en 2014, il préside aussi l'agglomération Châteauroux Métropole. En mars 2026, sa liste obtient 10 033 voix, loin devant celle d'Éric Domenge-Abeau, divers gauche (13,01 %), et celle du Rassemblement national menée par Mylène Wunsch (11,84 %), arrivée deuxième à Châteauroux aux législatives de 2024.",
  "Sa liste détient 38 des 43 sièges du conseil municipal, avec une participation de 53,67 %."],
 "Gil Avérous"),
A("insolite","Quand l'US Air Force vivait à Châteauroux","1951-1967 · Base de Déols",
 "Pendant seize ans, des milliers de militaires américains et leurs familles ont vécu à Châteauroux. Ils y ont apporté le jazz, le rock'n'roll, le Coca-Cola et les jeans.",
 "De 1951 à 1967, l'armée de l'air américaine a occupé à Déols, aux portes de Châteauroux, l'une de ses principales bases en France, dans le cadre de l'OTAN.",
 ["Au début de la guerre froide, les États-Unis installent en France des bases logistiques loin de la frontière allemande. Châteauroux-Déols devient un grand dépôt de l'US Air Force : des milliers d'Américains s'installent dans la ville et ses environs, avec leurs écoles, leurs magasins et leurs clubs.",
  "La ville découvre avant le reste du pays les voitures américaines, le jazz, le rock et les jeans. Le jeune Gérard Depardieu, qui grandit à Châteauroux, fréquente les soldats et revend leurs cigarettes et leur whisky.",
  "Après la décision du général de Gaulle, en 1966, de retirer la France du commandement intégré de l'OTAN, les Américains quittent la base en 1967. L'aéroport de Châteauroux-Centre occupe aujourd'hui une partie du site."],
 "Base aérienne de Châteauroux-Déols"),
A("personnalites","Gérard Depardieu, l'enfant de Châteauroux","1948 · Châteauroux",
 "Né à Châteauroux en 1948, Gérard Depardieu a quitté l'école à treize ans avant de devenir l'un des acteurs les plus célèbres du cinéma français. Il a été condamné en première instance en 2025 pour agressions sexuelles.",
 "Gérard Depardieu, né à Châteauroux le 27 décembre 1948, a tourné plus de deux cents films ; il fait l'objet depuis plusieurs années de procédures judiciaires pour violences sexuelles.",
 ["Fils d'un tôlier, troisième de six enfants, il grandit dans un quartier populaire de Châteauroux, quitte l'école à treize ans et vit de petits trafics avant de partir pour Paris, où il suit des cours de théâtre. Révélé par « Les Valseuses » en 1974, il enchaîne « Le Dernier Métro », « Danton », « Jean de Florette » et « Cyrano de Bergerac », qui lui vaut le prix d'interprétation à Cannes en 1990 et le César du meilleur acteur.",
  "Le 13 mai 2025, le tribunal correctionnel de Paris le condamne à dix-huit mois de prison avec sursis pour l'agression sexuelle de deux femmes sur le tournage des « Volets verts » en 2021 ; il fait appel, et le procès en appel est fixé du 16 au 20 novembre 2026. Il est par ailleurs renvoyé devant la cour criminelle départementale de Paris pour viols sur la comédienne Charlotte Arnould, ce qu'il conteste en affirmant que la relation était consentie ; il a fait appel de ce renvoi."],
 "Gérard Depardieu",
 status="Condamné en première instance le 13 mai 2025 (appel jugé du 16 au 20 novembre 2026) ; renvoyé devant la cour criminelle pour viols, renvoi contesté en appel. Présumé innocent dans les deux dossiers tant qu'aucune décision définitive n'est intervenue.",
 timeline=T(("1948","Naissance à Châteauroux."),("1974","« Les Valseuses »."),("1990","« Cyrano de Bergerac », prix d'interprétation à Cannes."),("2025","Condamné en première instance pour agressions sexuelles ; appel."))),
]

# ---------------------------------------------------------------- NEVERS
nevers=[
A("politique","Denis Thuriot conserve Nevers de 316 voix","2014-2026 · Hôtel de ville",
 "Maire depuis 2014, Denis Thuriot a été réélu en mars 2026 avec 44,79 % des voix, 316 de plus que la liste de gauche de Wilfried Séjeau.",
 "Denis Thuriot, divers centre, maire de Nevers depuis 2014, a été réélu au second tour des municipales de mars 2026 avec 44,79 % des voix.",
 ["Ancien socialiste, avocat, Denis Thuriot prend la mairie en 2014 sans étiquette, puis se rapproche d'Emmanuel Macron. En mars 2026, il arrive en tête du premier tour avec 34,49 %, puis l'emporte au second avec 4 951 voix, contre 4 635 à la liste citoyenne et de gauche unie de Wilfried Séjeau (41,93 %) et 1 467 à celle de Xavier Morel, divers droite (13,27 %).",
  "Sa liste obtient 29 des 39 sièges du conseil municipal."],
 "Denis Thuriot"),
A("personnalites","Pierre Bérégovoy, la mort d'un Premier ministre","1er mai 1993 · Bords du canal",
 "Maire de Nevers et ancien Premier ministre, Pierre Bérégovoy se tire une balle dans la tête le 1er mai 1993, au bord d'un canal près de la ville, un mois après la défaite de la gauche.",
 "Pierre Bérégovoy, maire de Nevers depuis 1983 et Premier ministre d'avril 1992 à mars 1993, s'est donné la mort le 1er mai 1993 près de Nevers.",
 ["Ancien cheminot et ajusteur, devenu l'un des hommes de confiance de François Mitterrand, il est ministre des Finances avant de diriger le gouvernement. Dans son discours de politique générale, il promet de lutter contre la corruption.",
  "En février 1993, la presse révèle qu'il a reçu en 1986 de Roger-Patrice Pelat, homme d'affaires proche de Mitterrand, un prêt sans intérêt d'un million de francs pour acheter un appartement à Paris. Il n'est pas poursuivi, mais l'affaire le touche profondément. Après la déroute de la gauche aux législatives de mars 1993, il quitte Matignon.",
  "Le 1er mai 1993, il se tue avec l'arme de son garde du corps au bord du canal de la Jonction. Aux obsèques, à Nevers, François Mitterrand accuse ceux qui ont, selon lui, livré l'honneur d'un homme aux chiens."],
 "Pierre Bérégovoy",
 timeline=T(("1925","Naissance à Déville-lès-Rouen."),("1983","Élu maire de Nevers."),("1984","Ministre de l'Économie et des Finances."),("1992","Premier ministre."),("1993","Mort le 1er mai près de Nevers."))),
A("personnalites","Bernadette Soubirous repose à Nevers","1866-1879 · Espace Bernadette",
 "La voyante de Lourdes a passé les treize dernières années de sa vie au couvent Saint-Gildard de Nevers. Son corps, exposé dans une châsse de verre, attire des pèlerins du monde entier.",
 "Bernadette Soubirous, témoin des apparitions de Lourdes en 1858, est entrée en 1866 chez les sœurs de la Charité de Nevers, au couvent Saint-Gildard, où elle est morte le 16 avril 1879.",
 ["Pour échapper à la curiosité des foules de Lourdes, la jeune femme rejoint la maison mère des sœurs de la Charité, à Nevers, en juillet 1866. Elle y vit comme religieuse, souvent malade, et y meurt de la tuberculose à 35 ans.",
  "Son corps est exhumé trois fois, en 1909, 1919 et 1925, dans le cadre de la procédure de canonisation ; les témoins le décrivent comme bien conservé. Canonisée en 1933, elle repose depuis 1925 dans une châsse de verre dans la chapelle du couvent, le visage et les mains recouverts d'une fine couche de cire."],
 "Bernadette Soubirous",
 access="Espace Bernadette, chapelle ouverte tous les jours"),
A("patrimoine","Le bleu de Nevers, une faïence venue d'Italie","XVIe siècle · Centre-ville",
 "À la fin du XVIe siècle, des faïenciers italiens appelés par le duc de Nevers, un Gonzague de Mantoue, fondent une tradition qui fera de la ville l'une des capitales de la faïence française.",
 "La faïence de Nevers est née à la fin du XVIe siècle, lorsque le duc Louis de Gonzague, d'origine italienne, attire dans sa ville des céramistes venus d'Albisola, près de Gênes.",
 ["Les frères Conrade introduisent la technique de la faïence émaillée. Au XVIIe siècle, les ateliers nivernais créent le « bleu de Nevers », un fond bleu profond orné de motifs blancs ou jaunes, inspiré des porcelaines chinoises et persanes.",
  "Pendant la Révolution, Nevers produit des « faïences patriotiques », assiettes illustrées de slogans et de symboles révolutionnaires. Le musée de la Faïence et des Beaux-Arts, installé près de la Loire, conserve l'une des plus riches collections de cette production."],
 "Faïence de Nevers"),
]

# ---------------------------------------------------------------- VICHY
vichy=[
A("politique","Vichy, de Claude Malhuret à Frédéric Aguilera","1989-2026 · Hôtel de ville",
 "Fondateur de Médecins sans frontières devenu maire, Claude Malhuret a dirigé Vichy pendant vingt-huit ans. Son successeur, Frédéric Aguilera, a été réélu dès le premier tour en 2026.",
 "Frédéric Aguilera, divers droite, maire de Vichy depuis 2017, a été réélu dès le premier tour des municipales de mars 2026 ; sa liste compte Claude Malhuret, son prédécesseur.",
 ["Médecin, président de Médecins sans frontières de 1978 à 1986, Claude Malhuret devient secrétaire d'État aux Droits de l'homme dans le gouvernement de Jacques Chirac en 1986, puis maire de Vichy en 1989. Élu sénateur en 2014, il cède la mairie en 2017 à Frédéric Aguilera, en raison de la limitation du cumul des mandats.",
  "Frédéric Aguilera est réélu au premier tour en 2020 avec 74,10 % des voix, puis de nouveau au premier tour en mars 2026. Il préside aussi l'agglomération Vichy Communauté. Claude Malhuret figure en quinzième position sur sa liste et a été réélu conseiller municipal."],
 "Claude Malhuret"),
A("histoire","10 juillet 1940, la République abdique au casino","10 juillet 1940 · Grand Casino",
 "Le 10 juillet 1940, réunis dans le théâtre du Grand Casino de Vichy, 569 parlementaires votent les pleins pouvoirs au maréchal Pétain. Quatre-vingts s'y opposent.",
 "Le 10 juillet 1940, dans la salle de l'Opéra du Grand Casino de Vichy, l'Assemblée nationale vote les pleins pouvoirs constituants au maréchal Philippe Pétain, ce qui met fin à la IIIe République.",
 ["Après la défaite et l'armistice du 22 juin 1940, le gouvernement cherche une ville de la zone libre capable de l'accueillir. Vichy, station thermale, offre des centaines de chambres d'hôtel et un réseau téléphonique moderne. Les ministères s'installent dans les hôtels ; Pétain loge à l'hôtel du Parc.",
  "Le vote donne 569 voix pour, 80 contre et une vingtaine d'abstentions. Dès le lendemain, Pétain se proclame chef de l'État français. Vichy reste le siège du régime de collaboration jusqu'en août 1944, lorsque les Allemands emmènent Pétain à Sigmaringen.",
  "La ville porte depuis ce nom comme une marque. Une plaque rend hommage aux « 80 » parlementaires qui ont refusé les pleins pouvoirs."],
 "Vote des pleins pouvoirs constituants à Philippe Pétain",
 lat=46.1265,lon=3.4224),
A("patrimoine","Napoléon III et la reine des villes d'eaux","1861-1866 · Parc des Sources",
 "Entre 1861 et 1866, Napoléon III vient cinq fois prendre les eaux à Vichy. Il fait tracer des parcs, bâtir des chalets et transforme la station, inscrite au patrimoine mondial en 2021.",
 "Les séjours de Napoléon III à Vichy, de 1861 à 1866, ont fait de la station thermale l'une des plus fréquentées d'Europe ; Vichy est inscrite depuis 2021 au patrimoine mondial avec les grandes villes d'eaux d'Europe.",
 ["L'empereur, qui souffre de calculs, vient suivre des cures. Il fait endiguer l'Allier, aménager des parcs à l'anglaise et construire des chalets, dont certains subsistent le long du boulevard des États-Unis. La gare et le casino suivent, et la bonne société afflue.",
  "La Belle Époque ajoute le Grand Casino, l'Opéra et les galeries couvertes du parc des Sources. En 2021, l'Unesco inscrit Vichy, avec dix autres stations comme Spa, Baden-Baden ou Bath, sur la liste des « grandes villes d'eaux d'Europe »."],
 "Napoléon III",
 protection="Patrimoine mondial de l'Unesco (Grandes villes d'eaux d'Europe)"),
]

# ---------------------------------------------------------------- MONTLUCON
montlucon=[
A("politique","Philippe Perche bat le maire sortant à Montluçon","2020-2026 · Hôtel de ville",
 "À 38 ans, Philippe Perche a battu en mars 2026 le maire sortant Frédéric Laporte, lui aussi divers droite, avec 47,85 % des voix au second tour.",
 "Philippe Perche, divers droite, est maire de Montluçon depuis mars 2026, élu au second tour d'une triangulaire avec 47,85 % des voix.",
 ["Longtemps communiste, Montluçon est dirigée par Pierre Goldberg de 1977 à 2001, puis par Daniel Dugléry, à droite, jusqu'en 2020. Frédéric Laporte, Les Républicains, lui succède en 2020.",
  "En mars 2026, deux listes de droite s'affrontent. Au second tour, Philippe Perche obtient 5 296 voix, contre 3 105 au maire sortant (28,06 %) et 2 666 à la liste d'union de la gauche de Pierre Mothet (24,09 %). Sa liste détient 29 des 39 sièges."],
 "Montluçon"),
A("personnalites","Marx Dormoy, le ministre assassiné par la Cagoule","1888-1941 · Montluçon",
 "Maire de Montluçon, ministre de l'Intérieur du Front populaire, Marx Dormoy démantèle la Cagoule en 1937. En 1941, d'anciens cagoulards le tuent avec une bombe placée sous son lit.",
 "Marx Dormoy, maire socialiste de Montluçon à partir de 1926, ministre de l'Intérieur de 1936 à 1938, a été assassiné le 26 juillet 1941 à Montélimar, où le régime de Vichy l'avait assigné à résidence.",
 ["Fils de Jean Dormoy, premier maire socialiste de Montluçon à la fin du XIXe siècle, il devient maire à son tour en 1926. En novembre 1936, après le suicide de Roger Salengro, Léon Blum le nomme ministre de l'Intérieur.",
  "En 1937, sa police met au jour la Cagoule, une organisation secrète d'extrême droite qui prépare un coup d'État et a commis plusieurs assassinats ; des dépôts d'armes sont saisis et ses dirigeants arrêtés.",
  "Le 10 juillet 1940, il fait partie des 80 parlementaires qui refusent les pleins pouvoirs à Pétain. Arrêté, puis assigné à résidence à Montélimar, il est tué dans la nuit du 25 au 26 juillet 1941 par une bombe déposée dans sa chambre d'hôtel par d'anciens cagoulards."],
 "Marx Dormoy",
 timeline=T(("1888","Naissance à Montluçon."),("1926","Maire de Montluçon."),("1936","Ministre de l'Intérieur."),("1937","Démantèlement de la Cagoule."),("1941","Assassiné à Montélimar."))),
A("patrimoine","Le château des ducs de Bourbon et le MuPop","XVe siècle · Vieux Montluçon",
 "Au sommet de la vieille ville, le château des ducs de Bourbon domine le MuPop, ouvert en 2013 et consacré aux musiques populaires, de la vielle à la guitare électrique.",
 "Le château des ducs de Bourbon, qui domine Montluçon, a été bâti aux XIVe et XVe siècles et a longtemps abrité le musée des musiques populaires de la ville.",
 ["Les ducs de Bourbon, maîtres du Bourbonnais, font de Montluçon l'une de leurs places fortes. Le château, remanié au XVe siècle, conserve son logis et sa tour d'angle, avec une vue sur la vallée du Cher et la ville industrielle née au XIXe siècle avec le canal de Berry et les usines métallurgiques.",
  "Le Bourbonnais a été un grand centre de fabrication de vielles à roue. En 2013, la ville a ouvert au pied du château le MuPop, qui présente plusieurs milliers d'instruments, des cornemuses du Centre aux guitares électriques."],
 "Château des ducs de Bourbon (Montluçon)",
 access="MuPop, horaires à consulter"),
]

# ---------------------------------------------------------------- AURILLAC
aurillac=[
A("politique","Patrick Casagrande élu au premier tour à Aurillac","2014-2026 · Hôtel de ville",
 "La droite a repris Aurillac dès le premier tour en mars 2026 : Patrick Casagrande a battu la liste de gauche, sur laquelle figurait le maire sortant Pierre Mathonier, avec 61,47 % des voix.",
 "Patrick Casagrande, divers droite, est maire d'Aurillac depuis mars 2026, élu au premier tour avec 61,47 % des voix.",
 ["Le socialiste Pierre Mathonier dirigeait la ville depuis 2014. En mars 2026, la gauche se présente derrière Valérie Rueda, arrivée en deuxième position aux législatives de 2024, avec le maire sortant sur sa liste.",
  "La liste de Patrick Casagrande obtient 6 452 voix contre 4 045 (38,53 %) et 29 des 35 sièges, avec une participation de près de 66 %, élevée pour une municipale."],
 "Aurillac"),
A("personnalites","Gerbert d'Aurillac, le pape de l'an mil","999 · Abbaye Saint-Géraud",
 "Formé chez les moines d'Aurillac, Gerbert devient en 999 le pape Sylvestre II. Savant, il aurait diffusé en Occident les chiffres venus du monde arabe, ce qui lui valut une réputation de sorcier.",
 "Gerbert d'Aurillac, moine formé à l'abbaye Saint-Géraud d'Aurillac, a été pape de 999 à 1003 sous le nom de Sylvestre II, premier pape français.",
 ["Né en Auvergne vers 950, il étudie dans l'abbaye bénédictine d'Aurillac, puis en Catalogne, au contact des savoirs mathématiques et astronomiques du monde arabe. Écolâtre à Reims, il enseigne l'arithmétique avec un abaque et les chiffres indo-arabes, encore inconnus en Occident.",
  "Précepteur du futur empereur Otton III, il devient archevêque de Reims, puis de Ravenne, et enfin pape en 999. Sa science lui vaut, après sa mort, une légende de pacte avec le diable. Sa statue, œuvre de David d'Angers, se dresse depuis 1851 sur la place qui porte son nom."],
 "Sylvestre II",
 timeline=T(("950","Naissance en Auvergne, vers cette date."),("972","Écolâtre à Reims."),("991","Archevêque de Reims."),("999","Élu pape sous le nom de Sylvestre II."),("1003","Mort à Rome."))),
A("personnalites","Paul Doumer, le président assassiné","1857-1932 · Aurillac",
 "Né à Aurillac dans une famille modeste, Paul Doumer devient président de la République en 1931. Un an plus tard, il est abattu par un émigré russe lors d'une vente de livres à Paris.",
 "Paul Doumer, né à Aurillac le 22 mars 1857, président de la République de 1931 à 1932, est mort le 7 mai 1932 après avoir été blessé par balles la veille à Paris.",
 ["Fils d'un ouvrier poseur de voies, il devient professeur de mathématiques, puis journaliste et député radical. Gouverneur général de l'Indochine de 1897 à 1902, il y lance de grands travaux, dont le pont qui porte son nom à Hanoï. Il perd quatre fils pendant la Première Guerre mondiale.",
  "Élu président de la République en mai 1931, il assiste le 6 mai 1932 à une vente de livres d'écrivains anciens combattants, à l'hôtel Salomon de Rothschild, lorsqu'un émigré russe, Paul Gorgulov, tire sur lui. Il meurt le lendemain. L'assassin est condamné à mort et exécuté."],
 "Paul Doumer",
 timeline=T(("1857","Naissance à Aurillac."),("1897","Gouverneur général de l'Indochine."),("1931","Élu président de la République."),("1932","Assassiné à Paris."))),
A("patrimoine","Le Festival de théâtre de rue d'Aurillac","Depuis 1986 · Rues et places",
 "Chaque mois d'août depuis 1986, Aurillac devient pendant quatre jours la capitale du théâtre de rue, avec des centaines de compagnies officielles et indépendantes dans les rues.",
 "Le Festival international de théâtre de rue d'Aurillac, créé en 1986 par Michel Crespin, réunit chaque été les arts de la rue dans toute la ville.",
 ["Michel Crespin, figure des arts de la rue, fonde le festival en 1986 pour réunir des compagnies jouant hors des salles. Il programme une sélection officielle, à laquelle s'ajoutent des centaines de compagnies « de passage », qui jouent sur les trottoirs, dans les cours et les parcs.",
  "La préfecture du Cantal, d'environ 25 000 habitants, accueille alors plusieurs dizaines de milliers de spectateurs. Aurillac est aussi connue pour une autre tradition : la fabrication de parapluies, dont elle assure l'essentiel de la production française."],
 "Festival international de théâtre de rue d'Aurillac"),
]

# ---------------------------------------------------------------- LE PUY-EN-VELAY
lepuy=[
A("politique","Le Puy-en-Velay, la ville de Laurent Wauquiez","2008-2026 · Hôtel de ville",
 "Laurent Wauquiez a dirigé la ville de 2008 à 2016 avant de présider la région. Son successeur, Michel Chapuis, a été réélu dès le premier tour en mars 2026 avec 56,47 % des voix.",
 "Michel Chapuis, divers droite, maire du Puy-en-Velay depuis 2016, a été réélu au premier tour des municipales de mars 2026 avec 56,47 % des voix.",
 ["Laurent Wauquiez, élu maire en 2008, est plusieurs fois ministre sous Nicolas Sarkozy, puis préside la région Auvergne-Rhône-Alpes de 2016 à 2024 et le parti Les Républicains de 2017 à 2019. Il quitte la mairie en 2016 et laisse la place à Michel Chapuis, qui est réélu dès le premier tour en 2020.",
  "En mars 2026, la liste de Michel Chapuis devance celle d'union de la gauche de Laurent Johanny (33,82 %) et celle de La France insoumise (9,71 %). Elle obtient 27 des 33 sièges."],
 "Laurent Wauquiez"),
A("patrimoine","La cathédrale du Puy, départ du chemin de Compostelle","Xe-XIIe siècles · Haute ville",
 "Depuis que l'évêque Godescalc partit du Puy vers Compostelle en 951, la cathédrale est le point de départ de la via Podiensis, la voie la plus fréquentée du chemin en France.",
 "La cathédrale Notre-Dame du Puy, au sommet de la vieille ville, est le point de départ de la via Podiensis, l'un des quatre grands chemins de Saint-Jacques-de-Compostelle en France.",
 ["En 951, l'évêque du Puy, Godescalc, se rend à Saint-Jacques-de-Compostelle : c'est le premier pèlerinage d'un non-Espagnol attesté par les sources. La cathédrale, avec sa façade polychrome et son grand escalier, devient un sanctuaire marial très fréquenté, autour d'une Vierge noire, brûlée en 1794 et remplacée depuis.",
  "La pierre des fièvres, une dalle sur laquelle les malades venaient s'allonger, est encore visible. Chaque matin, les pèlerins reçoivent une bénédiction avant de partir sur le GR 65 vers Conques et les Pyrénées. La cathédrale est inscrite depuis 1998 au patrimoine mondial au titre des chemins de Compostelle."],
 "Cathédrale Notre-Dame du Puy-en-Velay",
 lat=45.0458,lon=3.8850,access="Entrée libre ; bénédiction des pèlerins chaque matin",protection="Monument historique classé, patrimoine mondial de l'Unesco"),
A("insolite","Notre-Dame-de-France, fondue dans des canons russes","1860 · Rocher Corneille",
 "La statue rouge qui domine Le Puy est faite avec 213 canons pris aux Russes à Sébastopol et offerts par Napoléon III. On peut monter à l'intérieur, jusqu'à sa couronne.",
 "La statue de Notre-Dame-de-France, inaugurée en 1860 sur le rocher Corneille, a été coulée avec le métal de 213 canons russes pris pendant le siège de Sébastopol.",
 ["Un prédicateur, le père Combalot, lance une souscription pour élever une statue de la Vierge sur le rocher volcanique qui domine la ville. Napoléon III, vainqueur de la guerre de Crimée, offre 213 canons pris à Sébastopol en 1855.",
  "La statue, haute de près de 16 mètres, est assemblée à partir de pièces de fonte et peinte en rouge. Un escalier intérieur permet de monter jusqu'à la hauteur de la tête, d'où l'on voit la ville, la cathédrale et la chapelle Saint-Michel d'Aiguilhe, perchée sur son piton voisin."],
 "Notre-Dame-de-France (Le Puy-en-Velay)",
 lat=45.0466,lon=3.8858,access="Visite payante, horaires selon la saison"),
A("gastronomie","La lentille verte du Puy, première AOC légumière","1996 · Plateau du Velay",
 "Cultivée sur les sols volcaniques du Velay, la lentille verte du Puy est en 1996 le premier légume sec à obtenir une appellation d'origine contrôlée.",
 "La lentille verte du Puy, cultivée autour du Puy-en-Velay, est le premier légume sec à avoir obtenu une appellation d'origine contrôlée, en 1996, devenue appellation d'origine protégée européenne en 2008.",
 ["Le climat sec de l'été et les sols volcaniques du Velay donnent une lentille petite, à peau fine et marbrée de bleu, qui cuit vite et se tient à la cuisson.",
  "L'appellation, qui couvre quelques centaines d'exploitations de Haute-Loire, impose une zone de culture, l'absence d'irrigation et d'engrais azotés. Le Puy est aussi connu pour sa dentelle aux fuseaux et pour la verveine du Velay, une liqueur verte ou jaune."],
 "Lentille verte du Puy"),
]

# ---------------------------------------------------------------- RODEZ
rodez=[
A("politique","Stéphane Mazars bat Christian Teyssèdre à Rodez","2008-2026 · Hôtel de ville",
 "Maire depuis 2008, Christian Teyssèdre a été battu en mars 2026 par le député Stéphane Mazars, qui l'emporte avec 49,12 % des voix au second tour.",
 "Stéphane Mazars, divers centre, député de l'Aveyron, est maire de Rodez depuis mars 2026, élu au second tour avec 49,12 % des voix.",
 ["Christian Teyssèdre, socialiste devenu soutien d'Emmanuel Macron, dirigeait Rodez depuis 2008. Stéphane Mazars, avocat au barreau de Rodez, élu député en 2017 sous l'étiquette La République en marche et réélu depuis, se présente contre lui en 2026.",
  "Après la fusion de sa liste avec celle de Sarah Vidal, divers gauche (18,36 % au premier tour), il obtient au second tour 4 547 voix, contre 3 635 au maire sortant (39,27 %) et 1 075 à la liste d'union de la gauche de Florian Monteillet (11,61 %). Sa liste détient 26 des 35 sièges."],
 "Stéphane Mazars"),
A("faits_divers","L'affaire Fualdès, le crime qui passionna la France","19 mars 1817 · Rue des Hebdomadiers",
 "Dans la nuit du 19 mars 1817, l'ancien procureur Antoine Fualdès est égorgé dans une maison de Rodez, son corps jeté dans l'Aveyron. Deux procès, deux exécutions et une France entière captivée.",
 "Le 20 mars 1817, le corps d'Antoine-Bernardin Fualdès, ancien procureur impérial de Rodez, est retrouvé dans l'Aveyron ; l'enquête conclut qu'il a été égorgé la veille au soir dans une maison mal famée de la ville, la maison Bancal.",
 ["Selon l'accusation, Fualdès a été attiré dans la maison Bancal, rue des Hebdomadiers, puis tué sur une table, tandis que des joueurs de vielle jouaient dans la rue pour couvrir ses cris. Son filleul Bernard-Charles Bastide-Gramont et le beau-frère de celui-ci, le banquier Joseph Jausion, sont accusés : ils auraient voulu se débarrasser d'un créancier.",
  "Le procès de Rodez, en 1817, est annulé pour vice de forme. Rejugés à Albi en 1818, Bastide et Jausion sont condamnés à mort et exécutés le 3 juin 1818. Les témoignages changeants de Clarisse Manson, une jeune femme qui affirme avoir assisté au crime, font le tour de la presse.",
  "L'affaire, l'une des premières à être suivie jour après jour par les journaux de tout le pays, inspire des complaintes, des gravures et des pièces de théâtre. Le doute sur la culpabilité réelle des condamnés persiste chez certains historiens."],
 "Affaire Fualdès"),
A("personnalites","Pierre Soulages, le peintre de l'outrenoir","1919-2022 · Musée Soulages",
 "Né à Rodez en 1919, Pierre Soulages a inventé l'outrenoir, une peinture où la lumière naît du noir. Sa ville lui a consacré en 2014 un musée qui conserve plus de 500 de ses œuvres.",
 "Pierre Soulages, né à Rodez le 24 décembre 1919 et mort le 25 octobre 2022, est l'un des peintres français les plus reconnus du XXe siècle ; le musée Soulages de Rodez a ouvert en 2014.",
 ["Enfant, il est fasciné par les statues-menhirs du Rouergue et par l'abbatiale de Conques, dont il dessinera les vitraux dans les années 1980. Installé à Paris après la guerre, il s'impose dans l'abstraction avec des toiles sombres aux larges traits.",
  "En 1979, il découvre que le noir, travaillé en reliefs et en stries, renvoie la lumière : il appelle cette peinture « outrenoir ». Il fait don à sa ville, avec son épouse Colette, de plus de 500 œuvres et documents. Le musée, dessiné par l'agence catalane RCR Arquitectes, est inauguré le 30 mai 2014."],
 "Pierre Soulages",
 timeline=T(("1919","Naissance à Rodez."),("1979","Invention de l'outrenoir."),("1994","Achèvement des vitraux de Conques."),("2014","Ouverture du musée Soulages à Rodez."),("2022","Mort à Nîmes.")),
 lat=44.3497,lon=2.5726,access="Musée Soulages, horaires à consulter"),
A("patrimoine","La cathédrale de Rodez, clocher de 87 mètres","1277-1542 · Place d'Armes",
 "Bâtie en grès rose pendant près de trois siècles, la cathédrale Notre-Dame de Rodez porte un clocher de 87 mètres. Sa façade occidentale, sans portail, ressemble à un rempart.",
 "La cathédrale Notre-Dame de Rodez, construite de 1277 à 1542 en grès rose, est dominée par un clocher de 87 mètres achevé au début du XVIe siècle.",
 ["Sa façade ouest, presque aveugle, faisait partie des fortifications de la ville : elle n'a pas de grand portail, contrairement aux cathédrales gothiques du Nord.",
  "Le clocher, élevé de 1513 à 1526 après un incendie, superpose des étages de plus en plus ornés jusqu'à une statue de la Vierge. À l'intérieur, le jubé et les stalles de bois sculpté du XVe siècle ont été conservés."],
 "Cathédrale Notre-Dame de Rodez",
 lat=44.3510,lon=2.5743,access="Entrée libre en dehors des offices",protection="Monument historique classé"),
]

cities=[("18033","Bourges","Cher",47.0810,2.3988,bourges),
        ("36044","Châteauroux","Indre",46.8103,1.6913,chateauroux),
        ("58194","Nevers","Nièvre",46.9908,3.1590,nevers),
        ("03310","Vichy","Allier",46.1277,3.4259,vichy),
        ("03185","Montluçon","Allier",46.3401,2.6033,montlucon),
        ("15014","Aurillac","Cantal",44.9264,2.4397,aurillac),
        ("43157","Le Puy-en-Velay","Haute-Loire",45.0434,3.8853,lepuy),
        ("12202","Rodez","Aveyron",44.3506,2.5750,rodez)]
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
