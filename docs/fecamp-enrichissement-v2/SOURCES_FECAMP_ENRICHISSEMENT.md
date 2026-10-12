# ANECDOTES — Fécamp — Audit des sources et traçabilité V2
Date : 12 octobre 2026. Périmètre : uniquement 76259 Fécamp.

## État de référence et méthode
- Commit main initial : `8e25fcdc69686e512538473c48f40cef57039c99`.
- SHA Git du blob original : `6fc34e6552104018d02d24dcaf5fed56affcfa25`.
- Copie Git : `backup/fecamp-avant-enrichissement-20261012`.
- 16 articles de départ, ordre 0–15 conservé; nouveau contenu ajouté en fin de tableau.
- Les trois catalogues CSV nationaux **ont été lus** : 120 entrées du catalogue, 253 sociétés locales, 108 lignes de couverture territoriale. Méthodologie `sources/README.md` consultée. Le dossier de Seine-Maritime contient 11 sociétés repérées.
- Sources directement pertinentes déjà cataloguées : 0001 Yves Duboys-Fresney, 0005 FSHAN, 0045 Rotomagus, 0046 Nutrisco, 0047 Patrimoine normand, 0070 Inventaire normand, 0075 CTHS, 0077 BnF presse locale, 0078 Gallica, 0079 presse Gallica, 0080 FranceArchives, 0085 RetroNews.
- Sociétés locales sélectionnées : SL0027 Amis du Vieux Fécamp et du pays de Caux, SL0028 Centre havrais de recherche historique, SL0031 Elbeuf, SL0032 Société havraise d’études diverses, SL0033 Société libre d’émulation de Seine-Maritime. Les associations extérieures ont été identifiées dans le catalogue, **pas toutes consultées**. L’annuaire FSHAN constitue une porte d'entrée, pas une validation d'une publication particulière.

## Inventaire des 16 fiches initiales
| Indice stable | Titre | Catégorie | Mots avant (lead et body) | Source principale d’origine | Image originale conservée |
|---:|---|---|---:|---|---|
| 0 | David Roussel, élu maire de Fécamp | politique | 111 | https://fr.wikipedia.org/wiki/F%C3%A9camp | Aucune |
| 1 | Fécamp, capitale des premiers ducs normands | histoire | 95 | https://www.fecamptourisme.com/offres/palais-ducal-fecamp-fr-3758744/ | Fécamp Palais Ducal 1.jpg |
| 2 | L’incendie de 1168 a façonné l’abbatiale | patrimoine | 95 | https://www.fecamptourisme.com/experiences/nos-incontournables/abbatiale-sainte-trinite/ | Intérieur de l'abbatiale de la Trinité à Fécamp (Seine-Maritime) 02.jpg |
| 3 | Le figuier du Précieux-Sang, une légende de pèlerinage | legende | 121 | https://www.fecamptourisme.com/experiences/nos-incontournables/abbatiale-sainte-trinite/ | Precieuxsang.jpg |
| 4 | Un incendie a fait naître le Palais Bénédictine | patrimoine | 105 | https://www.fecamptourisme.com/experiences/portrait/portrait-alexandre-le-grand-createur-de-la-liqueur-benedictine-a-fecamp/ | Fécamp – Palais Bénédictine.jpg |
| 5 | Quand Fécamp devint le premier port morutier français | histoire | 84 | https://www.fecamptourisme.com/experiences/nos-incontournables/les-pecheries/ | FMIB 36602 Premier port d'armement en France pour la peche de la morue Fecamp le bassin Berigny avec ses terre-neuviers pendant l'hiver.jpeg |
| 6 | Léon Dufour et la « Goutte de Lait » | personnalites | 102 | https://www.fecamptourisme.com/experiences/nos-incontournables/les-pecheries/ | Collection de La Goutte de lait - Fécamp - 10.jpg |
| 7 | Le cap Fagnet, poste de guet devenu station radar | histoire | 93 | https://www.fecamptourisme.com/experiences/nos-incontournables/le-cap-fagnet/ | Fécamp - Blockhaus sur la falaise.jpg |
| 8 | En 1986, un musée voulu malgré la peur d’un « tombeau » | politique | 76 | https://www.archives.fecamp-terre-neuve.fr/Musees/MuseeTN.html | MuséeFécamp01b.JPG |
| 9 | Le meurtre présenté comme un suicide : seize mois avant la vérité | faits_divers | 174 | https://www.leprogres.fr/faits-divers/2017/09/20/il-avait-maquille-le-meurtre-de-sa-compagne-en-suicide | Aucune |
| 10 | Le Mordu : deux marins perdus au large de Fécamp | faits_divers | 196 | https://www.premar-manche.gouv.fr/communiques-presse/operation-de-recherche-et-de-secours-au-large-de-fecamp-suite-2 | Aucune |
| 11 | La falaise de Fécamp s’effondre et emporte le calvaire des marins | faits_divers | 169 | https://www.leparisien.fr/seine-maritime-76/emotion-a-fecamp-apres-leffondrement-de-la-falaise-28-02-2023-GKQMS2PI7JH3VFSXNP4HBWCKIY.php | Vue des falaises au nord de Fécamp.jpg |
| 12 | Le Pas de l’Ange : une empreinte tombée du ciel ? | legende | 137 | https://www.fecamptourisme.com/experiences/nos-incontournables/abbatiale-sainte-trinite/ | Abbaye de la Trinité de Fécamp 07 le pas de l'ange.jpg |
| 13 | En 1850, Fécamp expédiait des maisons vers San Francisco | histoire | 152 | https://www.duboysfresney.fr/index.php?page=docu010B | Aucune |
| 14 | Au Nid-de-Verdier, Fécamp élevait 200 000 truites et saumons | histoire | 120 | https://cnum.cnam.fr/pgi/redir.php?ident=12XAE54.10&onglet=c | Aucune |
| 15 | Un canal de l’an Mil coule encore sous Fécamp | patrimoine | 148 | https://data.geopf.fr/annexes/gpu/documents/DU_200069821/eb73bcf6109cb5b19e20e158d1073c49/200069821_liste_sup_20250623.pdf | Aucune |

## Explorations effectivement menées
- **Yves Duboys-Fresney — plan du site** https://www.duboysfresney.fr/index.php?page=docu000 : index et rubriques Fécamp, alentours, mer, littérature, patrimoine, droit, biographies, généalogie, sources anciennes. Plusieurs ressources de quartiers et de localités voisines ont été identifiées sans déplacer leur sujet vers d’autres communes. **Ne pas interpréter ceci comme la lecture intégrale des centaines de pages du site**.
- **Pages spécifiques ouvertes** : https://www.duboysfresney.fr/index.php?page=docu003A (anciennes paroisses) ; https://www.duboysfresney.fr/index.php?page=docu010B (Fréret) ; https://www.duboysfresney.fr/index.php?page=docu001D (Raveret-Wattel) ; https://www.duboysfresney.fr/index.php?page=docu011 (destructions de guerre) ; https://www.duboysfresney.fr/downloaddocu/docu006O.pdf (Prévost et Le Cerf, dix pages) ; https://www.duboysfresney.fr/downloaddocu/docu005B.pdf (commerce en 1763, huit pages).
- **Amis du Vieux Fécamp** : https://www.vieux-fecamp.fr/866-2/ (mémoire de Radio-Normandie) ; https://www.vieux-fecamp.fr/souvenirs-denfance-dannie-ernaux-a-fecamp/ (texte signé Annie Ernaux, 1999) ; https://www.vieux-fecamp.fr/le-coffre-funeraire-du-xiieme-siecle-et-les-differentes-translations/ (mémoire des ducs).
- **Radio-Normandie, collection spécialisée** : https://radio-normandie.pages-perso.free.fr/rn_presse.htm (reprise d’un article local de décembre 1928) ; https://radio-normandie.pages-perso.free.fr/Histoire_de_radio_normandie_frank_tenot.htm (reprise d’un extrait de l’ouvrage Frank Ténot, 1977). Ce corpus a justifié son ajout comme nouvelle entrée 0121 du catalogue national, avec photographie non réutilisée faute de licence.
- **Résultats officiels de 2026** : https://www.resultats-elections.interieur.gouv.fr/municipales2026/ensemble_geographique/28/76/76259/ (élection municipale).
- **Documents municipaux repérés** : https://www.ville-fecamp.fr/app/uploads/2024/04/Parcours-Fecamp.pdf et https://www.ville-fecamp.fr/app/uploads/2024/07/FECAMPMAG-153_VFweb.pdf, pour le patrimoine et la commémoration du 2 septembre.
- **Wikimedia Commons** : cinq fichiers nouveaux sélectionnés après lecture individuelle des pages de description et de licence (auteur, date, crédit, portée du visuel). Références dans `CREDITS_IMAGES_FECAMP.md`.

## Traçabilité des six nouvelles histoires
| Indice | Sujet | Référence principale consultée | Auteur / ouvrage / date | Confiance | Limite et recoupement |
|---:|---|---|---|---|---|
| 16 | Prévost / dom Le Cerf | https://www.duboysfresney.fr/downloaddocu/docu006O.pdf | Yves Duboys-Fresney, étude de 10 pages, « Un complot littéraire à l’abbaye de Fécamp (1723-1726) » ; édition du livre à La Haye en 1726 | Moyen à élevé pour édition 1726, rôle et séjour de Prévost discutés | Publication ancienne mentionnée : Léon Fallue, Histoire de la ville et de l’abbaye de Fécamp (1841), p.430 ; abbé Joseph Daoust, étude 1960, mentionnés par l’auteur. Dates concurrentes conservées. |
| 17 | Arrêt royal et commerce américain | https://www.duboysfresney.fr/downloaddocu/docu005B.pdf | Yves Duboys-Fresney, étude de 8 pages, reproduction de la première page de l’arrêt du Conseil d’État du Roi du 11 avril 1763 ; ouvrages de Jean Tarrade et Jean-François Brière cités | Élevé pour existence, date et objet de l’arrêt; quantité des voyages fécampois inconnue | La reproduction de l’acte est consultée dans le PDF; le dépôt d’archive original n’est pas identifié ici. Ne pas en déduire de voyage esclavagiste fécampois sans pièce dédiée. |
| 18 | Sept paroisses supprimées | https://www.duboysfresney.fr/index.php?page=docu003A | Yves Duboys-Fresney, « Les dix anciennes paroisses de Fécamp »; chronologie 27 mars / 14 juillet / 24–28 août 1791, ventes de 1792 | Moyen à élevé pour chronologie selon auteur; délibérations originales non consultées | Les sept fermetures ne se déroulent pas toutes le même jour. L’église Saint-Benoît cesse le culte dès le 24 août. |
| 19 | Radio-Fécamp puis Radio-Normandie | https://www.vieux-fecamp.fr/866-2/ | Les Amis du Vieux Fécamp, « Radio-Normandie » (témoignage historique); Radio-Normandie archives, reprise du Journal de Fécamp de décembre 1928; extrait Frank Ténot, Radios privées, radios pirates, Denoël 1977 | Élevé pour fondation 1926 et essor 1928–1929; démonstrations télévision 1932 signalées comme témoignage | Corroboration documentaire : https://radio-normandie.pages-perso.free.fr/rn_presse.htm ; https://radio-normandie.pages-perso.free.fr/Histoire_de_radio_normandie_frank_tenot.htm. Images non reprises. |
| 20 | Port saboté en 1944 | https://www.duboysfresney.fr/index.php?page=docu011 | Yves Duboys-Fresney, « Destructions urbaines (1939–1945) »; Ville de Fécamp, parcours patrimonial et bulletin commémoratif 2024 | Élevé pour dates de 1944; certains détails des ouvrages reposent sur l’étude de l’historien | Source municipale pour la Libération : https://www.ville-fecamp.fr/app/uploads/2024/07/FECAMPMAG-153_VFweb.pdf ; contexte du front de mer https://www.ville-fecamp.fr/app/uploads/2024/04/Parcours-Fecamp.pdf. 133 maisons = seul épisode de février 1944. |
| 21 | Annie Ernaux et la mer | https://www.vieux-fecamp.fr/souvenirs-denfance-dannie-ernaux-a-fecamp/ | Annie Ernaux, « Souvenirs d’enfance à Fécamp », Les Amis du Vieux Fécamp, bulletin n°45, 1999, texte signé | Très élevé pour l’existence du souvenir rapporté par l’autrice; année exacte inconnue | Témoignage de première main. Conserver « 1946 ou 1947 », sans confondre perception rétrospective et journal daté. Texte narratif original, pas de reproduction. |

## Enrichissements des histoires existantes
| Indice | Sujet d’origine | Nouveau détail documenté | Preuve |
|---:|---|---|---|
| 0 | Élection David Roussel | 49 voix d’écart entre les listes de tête, source officielle des résultats | https://www.resultats-elections.interieur.gouv.fr/municipales2026/ensemble_geographique/28/76/76259/ |
| 1 | Premiers ducs | Coffre de Richard Ier / II, cérémonie du 22 juin 1947, nuance sur une « translation » | https://www.vieux-fecamp.fr/le-coffre-funeraire-du-xiieme-siecle-et-les-differentes-translations/ |
| 5 | Grande pêche à la morue | 10 navires « banquais » dénombrés pour 1786; ouverture portuaire 1763 distinguée de la pêche | https://www.duboysfresney.fr/downloaddocu/docu005B.pdf |
| 13 | Maisons Fréret pour San Francisco | Débouchés antillais (Gazette de Guadeloupe 5 décembre 1871), Suez, tempête de 1847 et incendie de 1857 | https://www.duboysfresney.fr/index.php?page=docu010B |
| 14 | Nid-de-Verdier | Direction Casimir Raveret-Wattel 1892–1911 et expériences de pisciculture rapportées en 1905 | https://www.duboysfresney.fr/index.php?page=docu001D |

## Pistes non publiées / recherches infructueuses
- Documents corsaires individuels, entreprises de construction métallique et naufrages locaux : index explorés mais pas de pièces suffisantes pour écrire une fiche nouvelle de qualité.
- Les essais de télévision de 1932 sont mentionnés comme **témoignage**, sans vérification d’un programme télévisuel régulier. Aucune image de Radio-Fécamp n'a été reprise des collections privées.
- La vente des églises en 1792 et les épisodes de l’abbé Prévost sont rapportés par des historiens identifiés, mais les minutes de délibération et certains ouvrages anciens cités en seconde main n'ont pas été lus dans leur fonds originel.
- L’arrêt royal de 1763 a été consulté **en reproduction** dans une étude; il n’établit pas à lui seul l’existence de voyages commerciaux ni de traite fécampoise nominative.
- Les annuaires CTHS, FSHAN, Gallica, RetroNews, Persée, POP, les inventaires régionaux, les Archives départementales, la bibliothèque Rotomagus et Nutrisco ne sont pas déclarés **intégralement audités**. Aucun fait inédit ne leur est attribué sans document précis réellement consulté.

## Protection technique
- `index.json` **non modifié** : sa restitution par le connecteur était de longueur nulle alors que son SHA Git n’était pas vide. L’écraser aurait été dangereux; les fiches de Fécamp restent identifiées par le même code.
- Aucun autre `communes/*.json` ni fichier d’application n’a été modifié.
- Aucune coordonnée GPS fine n'a été fabriquée. `lat` et `lon` restent nuls dans les nouveaux articles; les rues, monuments et lieux précis sont décrits dans les textes.
- Les tests applicatifs réels iOS/web nécessitant un environnement de déploiement restent non exécutés et ne sont pas présentés comme réussis.
