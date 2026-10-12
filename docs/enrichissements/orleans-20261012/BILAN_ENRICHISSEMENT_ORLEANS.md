# ANECDOTES — Enrichissement documentaire : Orléans (45234)

**Date de l'audit :** 12 octobre 2026. **Périmètre :** commune d'Orléans exclusivement. **État Git initial :** `4154d5666099537702ecd67de34f0bac5c960a3b` ; **blob initial :** `374b7776478f74cf4b91f29cb0135b3fca08f0fd`. **Sauvegarde créée :** [backup/orleans-avant-enrichissement-20261012](https://github.com/amaurylopin/anecdotes-contenu/tree/backup/orleans-avant-enrichissement-20261012).

## État avant/après
| Indicateur | Avant | Après |
|---|---:|---:|
| Anecdotes | 4 | 12 |
| Anecdotes antérieures conservées à l'identique quant au titre/position | 4 | 4 |
| Anecdotes antérieures enrichies ou corrigées | 0 | 4 |
| Anecdotes nouvelles | 0 | 8 |
| Images `image.commons` | 0 | 6 |
| Anecdotes avec `links` documentaires | 0 | 12 |

## Inventaire initial et interventions
| Index stable | Titre conservé | Mots (corps) avant → après | Intervention |
|---:|---|---:|---|
| 0 | Serge Grouard triomphe à Orléans en 2026 | 126 → 254 | Correction de 2015 (santé), date tramway, officialisation du scrutin 2026, chronologie |
| 1 | Le siège levé par Jeanne d'Arc en neuf jours | 131 → 270 | Récit du siège, pluralité des acteurs, lieux et commémorations |
| 2 | La maison de Jeanne d'Arc à Orléans | 93 → 244 | Adresse corrigée : place du Général-de-Gaulle ; reconstruction après 1940 ; image légendée |
| 3 | Charles Péguy, l'écrivain d'Orléans | 109 → 248 | Parcours biographique et traces visibles, sources muséales |

## Histoires ajoutées à la fin du tableau
| Index | Titre | Catégorie | Mots du récit | Image |
|---:|---|---|---:|---|
| 4 | Le roi de dix-sept ans qui mourut à l'Hôtel Groslot | histoire | 255 | Commons vérifié |
| 5 | Une cathédrale gothique rebâtie à l'âge classique | patrimoine | 251 | Commons vérifié |
| 6 | 1022 : le bûcher des clercs accusés d'hérésie | histoire | 251 | Aucune image pertinente réutilisable retenue |
| 7 | L'université fondée en 1306 dont subsiste la salle des Thèses | histoire | 244 | Commons vérifié |
| 8 | La rue Royale : derrière les arcades, une ville reconstruite | patrimoine | 253 | Commons vérifié |
| 9 | La rumeur d'Orléans : en 1969, un mensonge fait le tour de la ville | faits_divers | 255 | Aucune image pertinente réutilisable retenue |
| 10 | 1870 : Orléans prise, reprise, puis de nouveau occupée | histoire | 263 | Aucune image pertinente réutilisable retenue |
| 11 | Deux Jeanne d'Arc pour raconter une même délivrance | patrimoine | 251 | Commons vérifié |

## Contrôles et non-régression
- `id`, `insee`, `name`, `dept`, `kind` et racine JSON conservés.
- Quatre articles préexistants conservés aux indices 0, 1, 2, 3 ; aucun changement de titre ni réordonnancement.
- Toutes les nouvelles fiches ajoutées exclusivement en fin de tableau, sans doublon de titre.
- Clés et types éditoriaux compatibles avec les objets du dépôt ; sources et URL documentaires de chaque nouvel article ; licences déclarées et crédits de six photographies.
- Contrôle documentaire : les URL et les statuts sont détaillés dans le dossier SOURCES ; les cas sensibles comportent les réserves nécessaires.
- `index.json` volontairement inchangé : sa restitution par l'interface GitHub était vide malgré un SHA existant, insuffisante pour une mise à jour fiable. L'indexation automatique, si activée par GitHub Actions, est indépendante du présent commit.
- Aucune fiche d'une autre commune et aucun fichier du dépôt de l'application n'ont été modifiés.
- La vérification de l'affichage réel sur iOS, du cache distant et de la navigation après rafraîchissement n'est **pas exécutée** dans cette session. Pas de garantie de mise à jour iOS sans contrôle côté client.

## Modification du catalogue
Quatre organismes/portails ajoutés au catalogue national, deux sociétés locales identifiées à Orléans ; la couverture du Loiret passe de 0 à 2 associations repérées. Le chiffre ne signifie pas que le département a été prospecté exhaustivement.

## Référence Git
Sauvegarde initiale : `backup/orleans-avant-enrichissement-20261012`. Un commit unique est créé à partir de l'état `main` constaté au moment de la publication, sans force-push. Le SHA final et la vérification distante sont fournis dans le compte rendu de publication associé.
