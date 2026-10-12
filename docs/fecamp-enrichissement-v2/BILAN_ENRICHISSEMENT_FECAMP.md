# Bilan éditorial et technique — Fécamp 76259, enrichissement V2
Date : 12 octobre 2026.

## Références et sauvegarde
- Commit main avant mission : `8e25fcdc69686e512538473c48f40cef57039c99`.
- Blob original Fécamp : `6fc34e6552104018d02d24dcaf5fed56affcfa25`.
- Branche de sauvegarde créée : `backup/fecamp-avant-enrichissement-20261012`.

## Résultat avant / après
| Indicateur | Avant | Après |
|---|---:|---:|
| Anecdotes | 16 | 22 |
| Fiches originales conservées dans le même ordre | 16 | 16 |
| Fiches initiales enrichies | 0 | 5 |
| Fiches inédites | 0 | 6 |
| Fiches illustrées | 10 | 15 |
| Images initiales remplacées / supprimées | 0 | 0 |
| Sources nationales cataloguées | 120 | 121 |
| URLs documentaires ou iconographiques distinctes supplémentaires dans les fiches | — | 16 |

Catégories de départ : politique 2; histoire 5; patrimoine 3; legende 2; personnalites 1; faits_divers 3.

## Historique de chaque anecdote initiale
| Indice stable | Titre | Décision | Détail |
|---:|---|---|---|
| 0 | David Roussel, élu maire de Fécamp | Enrichie | Résultats du ministère de l’Intérieur : 49 voix d’écart et 24 sièges |
| 1 | Fécamp, capitale des premiers ducs normands | Enrichie | Coffre funéraire des ducs et cérémonie de 1947 |
| 2 | L’incendie de 1168 a façonné l’abbatiale | Conservée | Intégralement inchangée |
| 3 | Le figuier du Précieux-Sang, une légende de pèlerinage | Conservée | Intégralement inchangée |
| 4 | Un incendie a fait naître le Palais Bénédictine | Conservée | Intégralement inchangée |
| 5 | Quand Fécamp devint le premier port morutier français | Enrichie | Banquais de 1786, arrêté du 11 avril 1763 |
| 6 | Léon Dufour et la « Goutte de Lait » | Conservée | Intégralement inchangée |
| 7 | Le cap Fagnet, poste de guet devenu station radar | Conservée | Intégralement inchangée |
| 8 | En 1986, un musée voulu malgré la peur d’un « tombeau » | Conservée | Intégralement inchangée |
| 9 | Le meurtre présenté comme un suicide : seize mois avant la vérité | Conservée | Intégralement inchangée |
| 10 | Le Mordu : deux marins perdus au large de Fécamp | Conservée | Intégralement inchangée |
| 11 | La falaise de Fécamp s’effondre et emporte le calvaire des marins | Conservée | Intégralement inchangée |
| 12 | Le Pas de l’Ange : une empreinte tombée du ciel ? | Conservée | Intégralement inchangée |
| 13 | En 1850, Fécamp expédiait des maisons vers San Francisco | Enrichie | Industrie Fréret : Guadeloupe, Suez, intempéries et incendie |
| 14 | Au Nid-de-Verdier, Fécamp élevait 200 000 truites et saumons | Enrichie | Raveret-Wattel, expérience piscicole et direction du Nid-de-Verdier |
| 15 | Un canal de l’an Mil coule encore sous Fécamp | Conservée | Intégralement inchangée |

## Anecdotes inédites
| Indice | Titre | Catégorie | Mots narratifs | Photo |
|---:|---|---|---:|---|
| 16 | L’abbé Prévost et le livre que l’abbaye ne voulait pas publier | personnalites | 331 | Abbé Prévost.jpg |
| 17 | 1763 : le roi autorise Fécamp à commercer avec l’Amérique | economie | 310 | Vue port Fécamp.JPG |
| 18 | 1791 : sept églises disparaissent de la carte de Fécamp | politique | 318 | A Fécamp - Église Saint-Etienne.jpg |
| 19 | Radio-Fécamp : d’un salon privé à la voix de « Tante Francine » | culture | 342 | Aucune (droits non vérifiés) |
| 20 | 1944 : le port de Fécamp saboté avant l’arrivée des Alliés | histoire | 313 | Fécamp Phare.jpg |
| 21 | Annie Ernaux : sa première rencontre avec la mer fut à Fécamp | personnalites | 345 | Annie Ernaux.jpg |

## Sources et décisions
Les sources vérifiées sont détaillées dans `SOURCES_FECAMP_ENRICHISSEMENT.md`, et les illustrations dans `CREDITS_IMAGES_FECAMP.md`. Les recherches d’Yves Duboys-Fresney, les publications des Amis du Vieux Fécamp et les documents radio ont permis de sélectionner six sujets distincts. Une source déjà exploitée sur l’entreprise Fréret a été utilisée pour **enrichir** la fiche préexistante et éviter un doublon. Les pistes dont l’attribution ou la preuve restait trop faible ont été écartées.

## Tests sur les données réellement exécutés
- PASSÉ — Commune 76259 Fécamp et structure générale inchangées
- PASSÉ — 16 anecdotes avant, 22 après
- PASSÉ — Les 16 titres et indices sont conservés
- PASSÉ — Tous les champs existants sont toujours présents
- PASSÉ — Aucun paragraphe historique initial supprimé
- PASSÉ — Toutes les sources initiales conservées
- PASSÉ — Toutes les images anciennes conservées
- PASSÉ — Onze articles initiaux non enrichis identiques
- PASSÉ — Aucun doublon de titre
- PASSÉ — Six nouvelles fiches de 300 à 450 mots
- PASSÉ — Six nouvelles fiches, schéma complet
- PASSÉ — Toutes les catégories prises en charge par la webapp
- PASSÉ — Five new licensed images
- PASSÉ — 121 lignes de ressources, entrée 0121 ajoutée
- PASSÉ — JSON GitHub relu et parsé

## Limites des tests
- Le code `web/public/app.js` et `web/server.mjs` a été consulté afin de vérifier les catégories, le chargement des fiches et la navigation par index; les nouveaux objets réutilisent les champs compatibles.
- **Non exécuté** : compilation Xcode, tests sur iPhone, campagne Node `npm test` en environnement web, rechargement cache de production VPS, test d'affichage de chaque photographie dans les clients.
- **Non exécuté** : vérification GPS précise des anciens bâtiments et lieux; aucune coordonnée d'article n'a été inventée (`lat:null`, `lon:null`).
- `index.json` **non modifié** : sa lecture par le connecteur renvoyait un corps vide malgré la présence d'un blob distant identifié; cela ne permettait aucune réécriture sûre. Aucun impact sur les autres communes ni changement global d’index.
- L’exhaustivité de l'exploration des centaines de pages du site Duboys-Fresney ou de tous les documents de Gallica, CTHS et sociétés savantes n’est pas revendiquée.
- La branche `main` sera mise à jour seulement par fast-forward après confirmation qu'elle a toujours son SHA de départ; la publication doit être vérifiée séparément après cette opération.
