# ANECDOTES — BILAN — SCEAUX (92071)

Date de préparation : 12 octobre 2026. **Publication GitHub non effectuée au moment de la génération de ce livrable de secours** : le contrôle de sécurité du connecteur a refusé les écritures. Ce document décrit le **contenu préparé**, non un état de production confirmé.

## Audit de l'état GitHub avant préparation

- `main` observée au commit `8137089a58a73aa38ca09fe7b0f8b4378e45587c` ; arbre `450d1cfd86424a6d6cb8f2e104f1ea5a55dff525`.
- Blob original `communes/92071.json` : `878614667a299bf46b79ee2267bc1386c0088f1a`.
- 4 anecdotes initiales ; 2 illustrations liées à deux articles ; catégories : 1 politique, 1 histoire, 2 patrimoine.
- Sauvegarde Git **créée et confirmée** : `backup/sceaux-avant-enrichissement-20261012` (commit `8137089a58a73aa38ca09fe7b0f8b4378e45587c`).
- `index.json` **non modifié**, sa lecture via le connecteur n'étant pas fiable pour un fichier très volumineux.

## Articles initiaux conservés à leurs indices

| Indice | Titre initial | Action préparée |
|---:|---|---|
| 0 | Philippe Laurent, maire après les municipales de 2026 | Enrichissement (+2 paragraphe(s), nouvelles sources, aucune suppression) |
| 1 | Le château de Colbert a disparu : celui d’aujourd’hui date du Second Empire | Enrichissement (+1 paragraphe(s), nouvelles sources, aucune suppression) |
| 2 | Le Nôtre a dessiné des perspectives qui débordent la commune | Enrichissement (+2 paragraphe(s), nouvelles sources, aucune suppression) |
| 3 | Une faïencerie “japonnée” a fait de Sceaux un centre de céramique | Enrichissement (+2 paragraphe(s), nouvelles sources, aucune suppression) |

## Nouvelles histoires (ajoutées en fin de tableau)

| Nouvel indice (si aucun contenu concurrent) | Catégorie | Titre | Mots (lead + corps) | Illustration |
|---:|---|---|---:|---|
| 4 | patrimoine | Le pavillon de l'Aurore : la coupole qui a survécu au château | 300 | Oui |
| 5 | histoire | Les Grandes Nuits : quand Sceaux faisait concurrence à Versailles | 296 | Non |
| 6 | economie | Le marché aux bestiaux de Colbert qui nourrissait Paris | 300 | Oui |
| 7 | culture | Le Bal de Sceaux, du jardin populaire au roman de Balzac | 296 | Non |
| 8 | patrimoine | Lakanal : le lycée imaginé comme une école à la campagne | 298 | Oui |
| 9 | culture | Un jardin de Sceaux consacré aux poètes de la langue d’oc | 273 | Oui |
| 10 | histoire | 1923 : le domaine de Sceaux sauvé des lotissements | 302 | Non |
| 11 | patrimoine | L'Orangerie conçue pour des arbres et devenue galerie de tableaux | 279 | Oui |
| 12 | patrimoine | Le Petit Château : le rescapé discret du Grand Siècle | 290 | Oui |

## Bilan prévu après publication réussie

- **4** articles d'origine maintenus et enrichis ; **9** nouveaux, soit **13** au total sur la base observée.
- **8** illustrations conservées ou ajoutées : 2 anciennes + 6 nouvelles.
- **3** nouvelles sources au catalogue national si elles n'y sont pas déjà ; 1 entrée de société locale renseignée.
- Les liens d'article `/commune/92071/article/<index>` restent stables par préservation de l'ordre d'origine.

## Contrôles et limites

- Construction des 9 JSON d'article, contrôle de présence des champs, corps en liste, titres uniques et catégories connues.
- Préservation des 4 entrées initiales : le script de secours vérifie les titres et compare les entrées avant/après, conservant leur contenu original, leurs sources et leurs images ; les nouvelles fiches sont ajoutées à la suite.
- Exécution de l'application iOS et tests de la webapp déployée : **non réalisés**.
- Lecture intégrale des bulletins et publications anciennes des Amis de Sceaux : **non réalisée**.
- Mise à jour de `index.json` : **non réalisée**, pour éviter un écrasement accidentel. Le workflow habituel de synchronisation de l'index doit être contrôlé après la publication.
- Aucune modification du dépôt applicatif ni d'autres communes.

## Pour publier

Exécuter `publier_enrichissement_sceaux.sh` depuis un environnement autorisé avec `git` et `python3` et un dépôt local `amaurylopin/anecdotes-contenu` accessible en écriture. **Simulation par défaut** ; ajout du seul argument `--publier` pour sauvegarder, commiter puis pousser sans forcer. Voir README du lot et sortie du script.
