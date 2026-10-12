# Anecdotes — Nantes (44109) — Bilan de l'enrichissement V2
**Préparé le 12 octobre 2026.**

## État initial contrôlé
- **Commit de référence :** `8137089a58a73aa38ca09fe7b0f8b4378e45587c`.
- **Fichier initial :** `communes/44109.json`, blob `471c62e8e13ff3f4595ec4299fc76033235c2296`.
- **73 anecdotes**, dont **4 illustrations**, réparties : histoire 13, faits_divers 14, personnalites 11, patrimoine 11, insolite 8, gastronomie 5, sport 2, legende 3, nature 3, politique 3.
- La plupart des fiches initiales disposent d'une URL principale, souvent Wikipédia. Le recensement de toutes les références a été réalisé par programme mais la validité documentaire de chacun des 73 récits n'a **pas** été revue intégralement.
- **Index avant :** entrée Nantes à 69 anecdotes, alors que le fichier courant en possède 73 : métadonnées déjà désynchronisées.
- **Sauvegarde Git :** `backup/nantes-avant-enrichissement-20261012-8137089a`, sur le commit initial.

## Enrichissements des sept récits conservés à leur index
| Index | Sujet initial | Modification motivée |
|---:|---|---|
| 0 | Cours des 50-Otages | Dénomination décidée en 1944 et non 1945 ; histoire de l'Erdre et 48 otages. |
| 1 | Édit de Nantes | Précision sur la portée limitée de la coexistence confessionnelle, ajout d'un lieu de mémoire. Date exacte d'avril discutée. |
| 2 | Traite atlantique | Correction de 450 000 à environ 553 000 victimes déportées ; 1 754 voyages selon Olivier Grenouilleau. |
| 6 | Incendies de la cathédrale | Histoire et perte du grand orgue. |
| 13 | Passage Pommeraye | Associé Charles Guilloux, montage de 1841, crise et galerie de 1852. |
| 32 | Bombardements de septembre 1943 | Bilan documenté à 1 463 morts ; chronologie des raids ; sources municipales. |
| 41 | Pont transbordeur | Titre corrigé de 70 à 50 m (hauteur du tablier), tests de la nacelle et anecdotes d'époque. |

Tous les autres récits, y compris les quatre fiches Belem/Dubigeon publiées précédemment, conservent leur contenu et leur ordre.

## Cinq nouvelles anecdotes, appendues aux indices 73–77
| Index | Titre | Catégorie | Illustration | Lieu |
|---:|---|---|---|---|
| 73 | Elsa, la lionne qui vivait en HLM à Chantenay | insolite | Aucune, faute de droits | Secteur Chantenay, sans domicile privé |
| 74 | Le zoo oublié de la Jonelière et son dernier drame | patrimoine | Quartier Jonelière, CC BY 2.0 | Domaine disparu, pas de coordonnées inventées |
| 75 | Annie Nouaille, celle qui a fait renaître le Katorza | personnalites | Façade Katorza, CC BY-SA 4.0 | Cinéma rue Corneille |
| 76 | La baleine arrivée au port sur le nez d'un méthanier | insolite | Véritable rorqual, CC BY-SA 4.0 | Muséum fermé au public |
| 77 | Un jouet neuf pour entrer au concert : les Rockeurs ont du cœur | insolite | Aucune, faute de droits | Concerts itinérants |

## Publication et sécurité
- **Résultat éditorial visé :** 73 conservées, 7 enrichies, 5 nouvelles, **78 au total**, 4 anciennes images conservées et 3 images Commons ajoutées (7 images au total).
- L'identité de chaque article existant est déterminée par son index, conservé **strictement**. Seul le titre historiquement imprécis de l'article 41 est corrigé, au même index.
- Correction ciblée de `index.json` : seule l'entrée 44109 doit passer de 69 à 78, avec la date de mise à jour du 12 octobre 2026. Les 34 665 autres entrées restent inchangées.
- Le catalogue national a reçu trois ressources distinctes dans `sources/catalogue_national.csv`; pas de remplacement des sociétés savantes, pas de réindexation nationale.
- **Branches :** sauvegarde du commit initial et branche de travail `travail/enrichissement-nantes-v2-20261012-8137089a`.
- **Statut avant la bascule sur main :** projet préparé sur branche séparée, non publié tant qu'un fast-forward explicite et une relecture distante de `main` ne sont pas confirmés.
- **Compatibilité :** lecture du code `web/public/app.js` (articles accessibles par index, champ `image.commons`) et `web/server.mjs` (chargement des `communes/<INSEE>.json`, synchronisation `index.json`). Aucun changement applicatif.
- **Tests disponibles :** validation des objets JSON en mémoire, catégories compatibles, préservation des 73 positions, conservation des sources/images précédentes, absence de doublon parmi les nouveaux titres, JSON d'index complet et modification unique de l'entrée Nantes.
- **Tests non exécutés :** exécution réelle de l'application iOS, tests end-to-end de la webapp déployée, contrôle visuel de toutes les images par l'appareil et accès aux caches clients réels. Une compilation iOS ne peut être déduite de la seule conformité du JSON.

Voir [SOURCES_NANTES_ENRICHISSEMENT.md](SOURCES_NANTES_ENRICHISSEMENT.md) et [CREDITS_IMAGES_NANTES.md](CREDITS_IMAGES_NANTES.md) pour références et licences.
