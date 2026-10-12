# Bilan — Enrichissement de La Gâtine

**Date :** 12 octobre 2026  
**Commune :** Villiers-sous-Mortagne, Orne, INSEE 61507  
**Commit de base :** cf96a0a36d615718048b9fb90653d957e58cdd6d  
**Blob initial :** d27fb4e244cc33d4bfe99938f0fffeb7b5b49c50  
**Sauvegarde :** [backup/gatine-avant-enrichissement-20261012](https://github.com/amaurylopin/anecdotes-contenu/tree/backup/gatine-avant-enrichissement-20261012)

## Comptage
| Indicateur | Avant | Après |
|---|---:|---:|
| Anecdotes totales de la commune | 3 | 5 |
| Anecdotes initiales conservées | 3 | 3 |
| Anecdotes enrichies | 0 | 1 |
| Anecdotes créées | 0 | 2 |
| Illustrations intégrées | 0 | 0 |
| Liens iconographiques exacts de la Gâtine | 4 | 5 |
| Nouvelle ressource du catalogue | 0 | 1 |

## Conservation et décisions
| Index | Sujet d’origine | Décision |
|---|---|---|
| 0 | La Gâtine : le « château » est en réalité une demeure profondément remaniée | Conservée et enrichie : organisation du domaine, matériaux, distinction entre fief et logis |
| 1 | Nonantel conserve un vrai manoir du XVIe siècle | Conservée à l’identique |
| 2 | Avant la Révolution, le lin faisait travailler les hameaux | Conservée à l’identique |

**Nouvel index 3 :** « En 1923, trois noms et un même château dans l’annuaire des historiens ». Publication de la Société historique et archéologique de l’Orne de 1923. Prudence sur les dates d’adhésion, la possession et la résidence.

**Nouvel index 4 :** « La mystérieuse construction octogonale du parc de la Gâtine ». Description de l’Inventaire IA61001428 et photographie officielle IVR25_20156100162NUCA, hypothèses présentées au conditionnel.

## Tests et limites
- Test de parse JSON ; identité INSEE conservée ; 3 anciens titres à leur index ; anciens paragraphes et liens maintenus ; articles 1 et 2 strictement identiques.
- Ajout minimal à `index.json` limité à l’entrée 61507 (compteur 5, articles rédigés 5, date 2026-10-12). Toutes les autres entrées préservées.
- `sources/catalogue_national.csv` : ajout uniquement de la ligne 0127. Aucune modification des sociétés historiques existantes.
- Photographies non libres non incorporées ; documents consultables en liens.
- Aucune modification du dépôt applicatif, d’aucune autre commune, ni force-push.
- Tests iOS et web en production, rafraîchissement des caches : non réalisés dans l’environnement de cette mission ; ces résultats ne sont pas déclarés comme validés.

Consulter `SOURCES_GATINE_ENRICHISSEMENT.md` et `CREDITS_IMAGES_GATINE.md`. État du commit publié à établir sur GitHub après l’opération de référence distante.
