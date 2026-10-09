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

# ---------------------------------------------------------------- LE MANS
lemans=[
A("politique","Stéphane Le Foll réélu maire du Mans","2018-2026 · Hôtel de ville",
 "Ancien ministre de l'Agriculture et porte-parole du gouvernement de François Hollande, Stéphane Le Foll a été réélu maire du Mans en mars 2026 avec 50,06 % des voix au second tour.",
 "Stéphane Le Foll (PS), maire du Mans depuis 2018, a été réélu au second tour des municipales de mars 2026 avec 50,06 % des voix.",
 ["Proche de François Hollande, il est ministre de l'Agriculture de 2012 à 2017 et porte-parole du gouvernement à partir de 2014. Il succède en 2018 à Jean-Claude Boulard, maire depuis 1989, mort en cours de mandat.",
  "En mars 2026, il arrive en tête du premier tour avec 43,59 %, puis obtient au second 21 739 voix dans une quadrangulaire, face à la députée Marietta Karamanli, divers gauche (21,58 %), au Rassemblement national (16,21 %) et à la droite d'Olivier Sasso. Sa liste détient 42 des 55 sièges."],
 "Stéphane Le Foll"),
A("faits_divers","Le crime des sœurs Papin","2 février 1933 · Rue Bruyère",
 "Le 2 février 1933, deux domestiques, Christine et Léa Papin, massacrent leur patronne et sa fille dans une maison bourgeoise du Mans. L'affaire fascine Lacan et inspire « Les Bonnes » de Genet.",
 "Le 2 février 1933, au Mans, Christine et Léa Papin, employées de maison depuis six ans chez la famille Lancelin, tuent Mme Lancelin et sa fille Geneviève avec une violence extrême.",
 ["Les deux sœurs sont décrites comme des domestiques modèles. Ce soir-là, après une panne de fer à repasser qui aurait déclenché une réprimande, elles attaquent leurs patronnes, leur arrachent les yeux et les frappent à mort. On les retrouve couchées ensemble dans leur chambre.",
  "Au procès, en septembre 1933, Christine est condamnée à mort, peine commuée en travaux forcés ; elle meurt en 1937 à l'asile de Rennes. Léa est condamnée à dix ans de travaux forcés.",
  "Le crime alimente les débats sur la lutte des classes et la folie à deux. Le psychanalyste Jacques Lacan lui consacre un article, et Jean Genet s'en inspire pour sa pièce « Les Bonnes », créée en 1947."],
 "Affaire des sœurs Papin",
 links=[L("film","« Les Blessures assassines » (2000), de Jean-Pierre Denis","https://fr.wikipedia.org/wiki/Les_Blessures_assassines","Avec Sylvie Testud dans le rôle de Christine Papin")]),
A("faits_divers","1955, la catastrophe des 24 Heures du Mans","11 juin 1955 · Circuit des 24 Heures",
 "Le 11 juin 1955, la Mercedes de Pierre Levegh s'envole dans la tribune des 24 Heures. Plus de 80 spectateurs sont tués : c'est l'accident le plus meurtrier de l'histoire du sport automobile.",
 "Le 11 juin 1955, pendant les 24 Heures du Mans, la Mercedes du pilote français Pierre Levegh percute une Austin-Healey, décolle et se désintègre dans la foule ; le pilote et plus de 80 spectateurs sont tués.",
 ["Vers 18 h 30, Mike Hawthorn, en tête sur sa Jaguar, ralentit brusquement pour rentrer aux stands. L'Austin-Healey de Lance Macklin fait un écart et la Mercedes de Levegh, lancée à près de 240 km/h, la heurte. La voiture, en magnésium, explose et projette des débris sur les spectateurs massés le long de la ligne droite.",
  "La course n'est pas arrêtée, pour éviter que la foule ne gêne l'arrivée des secours ; Mercedes retire ses voitures dans la nuit. Plusieurs pays suspendent les courses automobiles, et la Suisse interdit les compétitions sur circuit pour des décennies. Le circuit est réaménagé, la sécurité des tribunes renforcée."],
 "Catastrophe des 24 Heures du Mans 1955"),
]

# ---------------------------------------------------------------- LAVAL
laval=[
A("politique","Florian Bercault réélu dès le premier tour à Laval","2020-2026 · Hôtel de ville",
 "Élu en 2020 à la tête d'une union de la gauche, Florian Bercault a été réélu dès le premier tour en mars 2026 avec 54,49 % des voix.",
 "Florian Bercault, union de la gauche, maire de Laval depuis 2020, a été réélu au premier tour des municipales de mars 2026 avec 54,49 % des voix.",
 ["En mars 2026, sa liste « Laval à venir » obtient 9 700 voix, devant celle de Samia Soultani-Vigneron, divers droite (31,40 %), et celle du Rassemblement national (8,62 %).",
  "Elle détient 34 des 43 sièges du conseil municipal, avec une participation de 56,83 %."],
 "Laval (Mayenne)"),
A("personnalites","Le Douanier Rousseau, peintre lavallois","1844-1910 · Vieux-Château",
 "Né à Laval en 1844, Henri Rousseau, employé de l'octroi de Paris, apprend seul à peindre. Moqué par la critique, il devient le maître des peintres naïfs, admiré par Picasso.",
 "Henri Rousseau, dit le Douanier Rousseau, né à Laval le 21 mai 1844, est un peintre autodidacte devenu la figure de référence de l'art naïf.",
 ["Fils d'un ferblantier, il travaille à l'octroi de Paris, d'où son surnom, et commence à peindre en amateur vers quarante ans. Il expose au Salon des indépendants à partir de 1886, sous les moqueries.",
  "Ses jungles luxuriantes, peuplées de fauves, qu'il n'a jamais vues que dans les jardins et serres de Paris, séduisent les avant-gardes. En 1908, Picasso organise en son honneur un banquet resté célèbre au Bateau-Lavoir. Le musée d'Art naïf de Laval, installé au Vieux-Château, lui rend hommage."],
 "Henri Rousseau",
 timeline=T(("1844","Naissance à Laval."),("1886","Premier Salon des indépendants."),("1908","Banquet donné par Picasso."),("1910","Mort à Paris.")),
 access="Musée d'Art naïf, Vieux-Château"),
A("personnalites","Alfred Jarry et Ambroise Paré, deux Lavallois","XVIe-XIXe siècles · Laval",
 "Laval a vu naître le chirurgien Ambroise Paré, qui renonce à cautériser les plaies à l'huile bouillante, et Alfred Jarry, l'auteur d'« Ubu roi ».",
 "Ambroise Paré, père de la chirurgie moderne, est né vers 1510 près de Laval, et Alfred Jarry, créateur d'Ubu, y est né le 8 septembre 1873.",
 ["Barbier devenu chirurgien des rois, Ambroise Paré découvre sur les champs de bataille que les plaies par arme à feu guérissent mieux sans huile bouillante et invente la ligature des artères lors des amputations. Il sert quatre rois de France.",
  "Alfred Jarry écrit « Ubu roi », créé à Paris en 1896, d'abord pour se moquer d'un professeur du lycée de Rennes. Le premier mot de la pièce provoque un scandale. Il meurt à 34 ans, en 1907, ruiné par l'absinthe."],
 "Alfred Jarry"),
]

# ---------------------------------------------------------------- CHARTRES
chartres=[
A("politique","Ladislas Vergne détrône Jean-Pierre Gorges","2001-2026 · Hôtel de ville",
 "Maire depuis 2001, Jean-Pierre Gorges a été battu en mars 2026 par Ladislas Vergne, lui aussi divers droite, élu avec 51,08 % des voix au second tour.",
 "Ladislas Vergne, divers droite, est maire de Chartres depuis mars 2026, élu au second tour avec 51,08 % des voix contre le maire sortant Jean-Pierre Gorges.",
 ["Jean-Pierre Gorges, ancien député d'Eure-et-Loir, dirigeait Chartres depuis 2001 et présidait l'agglomération. En mars 2026, deux listes de droite s'affrontent : celle de Ladislas Vergne arrive en tête du premier tour avec 39,78 %, contre 30,19 % au maire sortant.",
  "Au second tour, Ladislas Vergne obtient 7 553 voix, contre 4 420 à Jean-Pierre Gorges (29,89 %) et 2 813 à la liste d'union de la gauche (19,02 %). Sa liste détient 30 des 39 sièges."],
 "Chartres"),
A("histoire","Jean Moulin, préfet à Chartres en 1940","17 juin 1940 · Préfecture d'Eure-et-Loir",
 "Le 17 juin 1940, le préfet d'Eure-et-Loir refuse de signer un texte accusant faussement des tirailleurs sénégalais de crimes. Battu et enfermé, il tente de se trancher la gorge. Il s'appelle Jean Moulin.",
 "Le 17 juin 1940, Jean Moulin, préfet d'Eure-et-Loir à Chartres, refuse de signer une déclaration allemande imputant à des tirailleurs sénégalais le massacre de civils, et tente de se suicider pour ne pas céder.",
 ["Les Allemands entrent dans Chartres le 17 juin. Ils exigent du préfet qu'il signe un document affirmant que des soldats noirs de l'armée française ont tué des femmes et des enfants, alors que les victimes ont péri sous les bombardements. Jean Moulin refuse.",
  "Frappé et enfermé, il craint de céder et se tranche la gorge avec un morceau de verre. Il survit, garde une cicatrice qu'il cache sous une écharpe, et est révoqué par Vichy en novembre 1940. Il rejoint de Gaulle à Londres en 1941 et unifie la Résistance intérieure, avant d'être arrêté à Caluire en 1943 et de mourir sous la torture."],
 "Jean Moulin",
 timeline=T(("1899","Naissance à Béziers."),("1939","Préfet d'Eure-et-Loir."),("1940","Refuse de signer et tente de se donner la mort à Chartres."),("1943","Création du Conseil national de la Résistance ; arrêté à Caluire, il meurt en juillet."))),
A("patrimoine","Le bleu de Chartres et son labyrinthe","XIIIe siècle · Cathédrale Notre-Dame",
 "Reconstruite en vingt-six ans après l'incendie de 1194, la cathédrale de Chartres a conservé l'essentiel de ses vitraux d'origine et, sur son sol, un labyrinthe que les pèlerins parcouraient à genoux.",
 "La cathédrale Notre-Dame de Chartres, rebâtie pour l'essentiel entre 1194 et 1220, est inscrite au patrimoine mondial depuis 1979 pour son architecture gothique et ses vitraux du XIIIe siècle.",
 ["L'incendie de 1194 détruit la cathédrale romane, mais épargne le voile de la Vierge, relique conservée depuis le IXe siècle. Les Chartrains y voient un signe et reconstruisent l'édifice en un temps très court, ce qui lui donne une grande unité de style.",
  "Elle conserve plus de 170 vitraux anciens, célèbres pour leur bleu profond. Dans la nef, un labyrinthe de près de 13 mètres de diamètre est incrusté dans le dallage ; les fidèles le suivaient comme un pèlerinage symbolique. Il est dégagé des chaises certains jours pour être parcouru."],
 "Cathédrale Notre-Dame de Chartres",
 lat=48.4478,lon=1.4878,access="Entrée libre ; labyrinthe dégagé certains jours",protection="Monument historique classé, patrimoine mondial de l'Unesco"),
]

# ---------------------------------------------------------------- BLOIS
blois=[
A("politique","Marc Gricourt, l'héritier de Jack Lang à Blois","1989-2026 · Hôtel de ville",
 "Jack Lang, ministre de la Culture, a été maire de Blois de 1989 à 2000. Marc Gricourt, socialiste, maire depuis 2008, a été réélu en mars 2026 avec 51,74 % des voix.",
 "Marc Gricourt (union de la gauche), maire de Blois depuis 2008, a été réélu au second tour des municipales de mars 2026 avec 51,74 % des voix.",
 ["Jack Lang, ministre de la Culture de François Mitterrand, créateur de la Fête de la musique, est élu maire de Blois en 1989 et le reste jusqu'en 2000. La droite reprend la ville en 2001 avec Nicolas Perruchot, avant le retour de la gauche avec Marc Gricourt en 2008.",
  "En mars 2026, il obtient au second tour 6 942 voix, contre 4 849 à Malik Benakcha, divers droite (36,14 %), et 1 627 au Rassemblement national (12,13 %). Sa liste détient 33 des 43 sièges."],
 "Marc Gricourt"),
A("histoire","L'assassinat du duc de Guise au château de Blois","23 décembre 1588 · Château royal",
 "Le 23 décembre 1588, Henri III fait poignarder au château de Blois le duc de Guise, chef de la Ligue catholique. Le cardinal de Guise est tué le lendemain, et le roi lui-même est assassiné sept mois plus tard.",
 "Le 23 décembre 1588, au château de Blois, les gardes d'Henri III assassinent Henri de Guise, chef de la Ligue catholique, qui menaçait l'autorité du roi.",
 ["En pleines guerres de Religion, le duc de Guise, très populaire à Paris, a chassé le roi de sa capitale lors de la journée des Barricades, en mai 1588. Henri III réunit les états généraux à Blois et décide d'éliminer son rival.",
  "Au petit matin, Guise est convoqué dans le cabinet du roi ; il est frappé par une vingtaine de membres de la garde des Quarante-Cinq. Son frère, le cardinal de Guise, est tué le lendemain. Catherine de Médicis meurt au château deux semaines plus tard. Paris se soulève, et Henri III est assassiné par le moine Jacques Clément le 1er août 1589."],
 "Assassinat du duc de Guise",
 lat=47.5856,lon=1.3311,access="Château royal de Blois, ouvert toute l'année",protection="Monument historique classé"),
A("insolite","Robert-Houdin, père de la magie moderne","1805-1871 · Maison de la magie",
 "Né à Blois en 1805, l'horloger Robert-Houdin est considéré comme le père de la magie moderne. Face au château, sa Maison de la magie fait surgir des dragons de ses fenêtres toutes les demi-heures.",
 "Jean-Eugène Robert-Houdin, né à Blois le 7 décembre 1805, horloger devenu illusionniste, a donné au spectacle de magie sa forme moderne.",
 ["Il ouvre à Paris en 1845 un théâtre où il présente des automates et des illusions fondées sur la mécanique et l'électricité, en habit de soirée plutôt qu'en costume de sorcier. En 1856, le gouvernement l'envoie en Algérie pour impressionner les chefs locaux par ses tours.",
  "Le magicien américain Ehrich Weiss prend en son honneur le nom de Houdini. À Blois, la Maison de la magie, ouverte en 1998 face au château, fait sortir six têtes de dragons de ses fenêtres à intervalles réguliers."],
 "Jean-Eugène Robert-Houdin",
 access="Maison de la magie, place du Château"),
]

# ---------------------------------------------------------------- EVREUX
evreux=[
A("politique","Évreux, de Jean-Louis Debré à Guy Lefrand","2001-2026 · Hôtel de ville",
 "Jean-Louis Debré a été maire d'Évreux de 2001 à 2007, avant de présider le Conseil constitutionnel. Guy Lefrand, maire depuis 2014, a été réélu en mars 2026 dans une quadrangulaire.",
 "Guy Lefrand, divers droite, maire d'Évreux depuis 2014, a été réélu au second tour des municipales de mars 2026 avec 34,58 % des voix.",
 ["Fils de Michel Debré, Jean-Louis Debré est maire d'Évreux de 2001 à 2007, tout en présidant l'Assemblée nationale à partir de 2002 ; il préside ensuite le Conseil constitutionnel de 2007 à 2016. La ville passe à gauche en 2008 avec Michel Champredon, puis revient à droite en 2014 avec Guy Lefrand, ancien député.",
  "En mars 2026, quatre listes se maintiennent au second tour. Guy Lefrand obtient 4 569 voix, devant Samuel Brigantino, divers droite (30,65 %), l'union de la gauche (22,12 %) et le Rassemblement national (12,66 %). Sa liste détient 29 des 43 sièges."],
 "Guy Lefrand"),
A("patrimoine","La cathédrale d'Évreux, incendiée et rebâtie","XIIe-XXe siècles · Centre-ville",
 "Commencée à l'époque romane et achevée à la Renaissance, la cathédrale d'Évreux a été incendiée à plusieurs reprises, dont lors des bombardements de juin 1940 qui ont ravagé le centre de la ville.",
 "La cathédrale Notre-Dame d'Évreux, élevée du XIIe au XVIIe siècle, mêle tous les styles, du roman à la Renaissance, à la suite de destructions et de reconstructions successives.",
 ["Incendiée en 1119 puis en 1194 lors des guerres entre Philippe Auguste et les rois d'Angleterre, elle est reconstruite à partir du XIIIe siècle. Sa façade nord, de style gothique flamboyant, et sa tour-lanterne témoignent des campagnes de travaux suivantes.",
  "En juin 1940, les bombardements allemands provoquent un incendie qui détruit une grande partie du centre-ville et endommage la cathédrale. Ses vitraux, déposés à temps, ont été préservés : l'ensemble des XIVe et XVe siècles compte parmi les plus riches de Normandie."],
 "Cathédrale Notre-Dame d'Évreux",
 lat=49.0234,lon=1.1514,access="Entrée libre en dehors des offices",protection="Monument historique classé"),
]

# ---------------------------------------------------------------- ALENCON
alencon=[
A("politique","Sophie Douvry fait basculer Alençon à droite","2008-2026 · Hôtel de ville",
 "Gouvernée par la gauche depuis 2008, Alençon a élu en mars 2026 Sophie Douvry, divers droite, avec 46,58 % des voix au second tour, face à une gauche divisée.",
 "Sophie Douvry, divers droite, est maire d'Alençon depuis mars 2026, élue au second tour d'une quadrangulaire avec 46,58 % des voix.",
 ["La gauche dirigeait Alençon depuis 2008. En mars 2026, elle se présente divisée, et quatre listes se maintiennent au second tour.",
  "Sophie Douvry obtient 3 436 voix, devant le Rassemblement national d'Oscar Piloquet (20,01 %), la liste divers gauche d'Alain Gallerand (19,86 %) et l'union de la gauche de Johnny Lafresnaye (13,56 %). Sa liste détient 27 des 35 sièges."],
 "Alençon"),
A("personnalites","Thérèse de Lisieux et ses parents, saints d'Alençon","1873 · Maison natale",
 "Sainte Thérèse de Lisieux est née à Alençon en 1873. Ses parents, Louis et Zélie Martin, horloger et dentellière de la ville, sont en 2015 le premier couple canonisé ensemble.",
 "Thérèse Martin, future sainte Thérèse de Lisieux, est née à Alençon le 2 janvier 1873 ; ses parents, Louis et Zélie Martin, ont été canonisés ensemble le 18 octobre 2015.",
 ["Louis Martin est horloger-bijoutier, Zélie dirige une petite entreprise de dentelle au point d'Alençon. Cinq de leurs filles deviennent religieuses. Après la mort de Zélie, en 1877, la famille part pour Lisieux.",
  "Entrée au Carmel à quinze ans, Thérèse y meurt de la tuberculose en 1897, à 24 ans. Son autobiographie, « Histoire d'une âme », connaît un succès mondial ; elle est canonisée en 1925 et proclamée docteur de l'Église en 1997. Sa maison natale, rue Saint-Blaise, est un lieu de pèlerinage."],
 "Thérèse de Lisieux",
 timeline=T(("1873","Naissance à Alençon."),("1888","Entrée au Carmel de Lisieux."),("1897","Mort à Lisieux."),("1925","Canonisation."),("2015","Canonisation de ses parents, Louis et Zélie Martin."))),
A("patrimoine","Le point d'Alençon, dentelle royale","1665 · Musée des Beaux-Arts et de la Dentelle",
 "En 1665, Colbert crée à Alençon une manufacture royale pour concurrencer les dentelles de Venise. Le point d'Alençon, cousu à l'aiguille, est inscrit au patrimoine immatériel de l'Unesco depuis 2010.",
 "Le point d'Alençon, dentelle à l'aiguille née au XVIIe siècle, est inscrit depuis 2010 sur la liste du patrimoine culturel immatériel de l'Unesco.",
 ["Pour limiter les importations coûteuses de dentelle vénitienne, Colbert fonde en 1665 une manufacture royale à Alençon, où des dentellières mettent au point leur propre technique. La « reine des dentelles » orne les tenues de la cour de Louis XIV.",
  "Un centimètre carré peut demander plusieurs heures de travail. L'Atelier national du point d'Alençon, rattaché au Mobilier national, perpétue la technique, transmise oralement, et le musée des Beaux-Arts et de la Dentelle en présente l'histoire."],
 "Point d'Alençon"),
]

# ---------------------------------------------------------------- CHERBOURG
cherbourg=[
A("politique","Camille Margueritte reprend Cherbourg à la gauche","2001-2026 · Hôtel de ville",
 "Ville de Bernard Cazeneuve, Cherbourg est passée à droite en mars 2026 : Camille Margueritte a battu le maire sortant socialiste Benoît Arrivé avec 53,11 % des voix.",
 "Camille Margueritte, divers droite, est maire de Cherbourg-en-Cotentin depuis mars 2026, élue au second tour avec 53,11 % des voix contre le maire sortant Benoît Arrivé.",
 ["Bernard Cazeneuve, maire de Cherbourg-Octeville de 2001 à 2012, devient ministre de l'Intérieur en 2014 puis Premier ministre de décembre 2016 à mai 2017. Benoît Arrivé lui succède et devient en 2016 le premier maire de Cherbourg-en-Cotentin, commune nouvelle née de la fusion de cinq communes.",
  "En mars 2026, Camille Margueritte arrive en tête du premier tour avec 45,23 %, puis l'emporte en duel avec 15 882 voix contre 14 023. Sa liste détient 42 des 55 sièges."],
 "Cherbourg-en-Cotentin"),
A("faits_divers","L'attentat de Karachi et les ouvriers de la DCN","8 mai 2002 · Arsenal de Cherbourg",
 "Le 8 mai 2002, à Karachi, une voiture piégée tue onze salariés de la DCN de Cherbourg venus construire des sous-marins pour le Pakistan. L'enquête dérive vers le financement de la campagne d'Édouard Balladur.",
 "Le 8 mai 2002, un attentat-suicide contre un bus à Karachi, au Pakistan, tue quatorze personnes, dont onze employés français de la Direction des constructions navales, pour la plupart venus de Cherbourg.",
 ["Les ingénieurs et techniciens de l'arsenal de Cherbourg participent à la construction de sous-marins Agosta vendus au Pakistan en 1994. L'attentat est d'abord attribué à Al-Qaïda. À partir de 2008, les familles des victimes poussent les juges à explorer une autre piste : des représailles après l'arrêt du versement de commissions décidé par Jacques Chirac en 1995.",
  "L'enquête met au jour des soupçons de rétrocommissions ayant financé la campagne présidentielle d'Édouard Balladur en 1995, volet distinct de l'attentat lui-même. Le 4 mars 2021, la Cour de justice de la République relaxe Édouard Balladur et condamne son ancien ministre de la Défense, François Léotard, à deux ans de prison avec sursis.",
  "Le mobile de l'attentat n'a jamais été établi par la justice. Un monument rend hommage aux victimes à Cherbourg."],
 "Attentat de Karachi",
 status="Volet financier : Édouard Balladur relaxé et François Léotard condamné par la Cour de justice de la République le 4 mars 2021. Volet terroriste : instruction sans procès à ce jour."),
A("insolite","Le Titanic, escale à Cherbourg et parapluies","1912-1964 · Gare maritime",
 "Le 10 avril 1912, le Titanic fait escale en rade de Cherbourg pour embarquer 274 passagers. Un demi-siècle plus tard, Jacques Demy fait de la ville le décor des « Parapluies de Cherbourg ».",
 "Cherbourg a été la première escale du Titanic, le 10 avril 1912, et a donné son nom au film de Jacques Demy « Les Parapluies de Cherbourg », Palme d'or 1964.",
 ["Faute de quai assez profond, le Titanic mouille en rade le soir du 10 avril 1912 ; des transbordeurs amènent à bord 274 passagers, dont le milliardaire John Jacob Astor et Margaret Brown, future « insubmersible Molly Brown ». La Cité de la Mer, installée dans l'ancienne gare transatlantique, consacre une exposition à cette escale.",
  "En 1963, Jacques Demy tourne dans les rues de Cherbourg « Les Parapluies de Cherbourg », film entièrement chanté sur une musique de Michel Legrand, avec Catherine Deneuve. Il reçoit la Palme d'or à Cannes en 1964."],
 "Les Parapluies de Cherbourg",
 links=[L("film","« Les Parapluies de Cherbourg » (1964), de Jacques Demy","https://fr.wikipedia.org/wiki/Les_Parapluies_de_Cherbourg","Palme d'or, musique de Michel Legrand")]),
]

# ---------------------------------------------------------------- SAINT-BRIEUC
saintbrieuc=[
A("politique","Victor Bonnot bat la gauche à Saint-Brieuc","2020-2026 · Hôtel de ville",
 "Ancrée à gauche, Saint-Brieuc a élu en mars 2026 Victor Bonnot, divers droite, avec 44,56 % des voix au second tour, face au maire sortant Hervé Guihard.",
 "Victor Bonnot, divers droite, est maire de Saint-Brieuc depuis mars 2026, élu au second tour d'une quadrangulaire avec 44,56 % des voix contre le maire sortant Hervé Guihard.",
 ["Hervé Guihard, élu en 2020 à la tête d'une union de la gauche, conduisait la liste « Vivre Saint-Brieuc ». Au second tour, il obtient 6 433 voix, contre 7 115 à Victor Bonnot.",
  "La France insoumise (7,92 %) et une liste classée à l'extrême droite (7,23 %) se sont maintenues. La liste de Victor Bonnot détient 32 des 43 sièges du conseil municipal."],
 "Saint-Brieuc"),
A("nature","Les algues vertes de la baie de Saint-Brieuc","2009-2016 · Baie de Saint-Brieuc",
 "Chaque été, la baie de Saint-Brieuc se couvre d'algues vertes qui dégagent en pourrissant un gaz toxique. Des dizaines de sangliers y meurent en 2011, et deux décès humains sont attribués à ce gaz par les familles.",
 "La baie de Saint-Brieuc est l'un des sites bretons les plus touchés par les marées vertes, des proliférations d'algues favorisées par les nitrates d'origine agricole.",
 ["Les ulves prolifèrent dans les baies peu profondes où les rivières apportent des nitrates issus des engrais et des élevages. En se décomposant sur la plage, elles dégagent de l'hydrogène sulfuré, un gaz mortel à forte concentration.",
  "En 2011, 36 sangliers sont retrouvés morts dans l'estuaire du Gouessant, au fond de la baie ; les analyses mettent en cause l'hydrogène sulfuré. En 2016, la mort d'un joggeur, Jean-René Auffray, dans une vasière de Hillion relance le débat, sans que la justice établisse de lien certain.",
  "La journaliste Inès Léraud a raconté cette histoire dans la bande dessinée « Algues vertes, l'histoire interdite » (2019), adaptée au cinéma par Pierre Jolivet en 2023."],
 "Marée verte",
 links=[L("livre","« Algues vertes, l'histoire interdite » (2019), d'Inès Léraud et Pierre Van Hove","https://fr.wikipedia.org/wiki/Algues_vertes,_l%27histoire_interdite","Enquête en bande dessinée"),
        L("film","« Les Algues vertes » (2023), de Pierre Jolivet","https://fr.wikipedia.org/wiki/Les_Algues_vertes","Avec Céline Sallette dans le rôle d'Inès Léraud")]),
A("personnalites","Louis Guilloux, l'écrivain du Sang noir","1899-1980 · Saint-Brieuc",
 "Fils d'un cordonnier socialiste de Saint-Brieuc, Louis Guilloux décrit sa ville pendant la Grande Guerre dans « Le Sang noir », un des grands romans de l'entre-deux-guerres.",
 "Louis Guilloux, né à Saint-Brieuc le 15 janvier 1899, romancier proche d'André Malraux et d'Albert Camus, a fait de sa ville natale le décor de la plupart de ses livres.",
 ["Il grandit dans un milieu ouvrier et militant. Son roman « Le Sang noir », paru en 1935, raconte une journée de 1917 dans une ville de province qui ressemble à Saint-Brieuc, à travers un professeur de philosophie surnommé Cripure.",
  "Ami de Camus, avec qui il entretient une longue correspondance, il accompagne André Gide en URSS en 1936. Il reçoit le prix Renaudot en 1949 pour « Le Jeu de patience ». Il meurt à Saint-Brieuc en 1980."],
 "Louis Guilloux",
 timeline=T(("1899","Naissance à Saint-Brieuc."),("1935","« Le Sang noir »."),("1949","Prix Renaudot."),("1980","Mort à Saint-Brieuc."))),
]

cities=[("72181","Le Mans","Sarthe",48.0061,0.1996,lemans),
        ("53130","Laval","Mayenne",48.0706,-0.7734,laval),
        ("28085","Chartres","Eure-et-Loir",48.4469,1.4892,chartres),
        ("41018","Blois","Loir-et-Cher",47.5861,1.3359,blois),
        ("27229","Évreux","Eure",49.0241,1.1508,evreux),
        ("61001","Alençon","Orne",48.4329,0.0913,alencon),
        ("50129","Cherbourg-en-Cotentin","Manche",49.6337,-1.6222,cherbourg),
        ("22278","Saint-Brieuc","Côtes-d'Armor",48.5136,-2.7653,saintbrieuc)]
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
