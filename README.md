# Anecdotes par commune

Contenu historique et anecdotique pour les communes de France, destiné à une application qui, à l'arrivée
dans une ville ou un village, montre des faits historiques rattachés à des lieux précis.

## Contenu
- `contenu/<département>/<code INSEE>-<nom>.json` : fiches V1, extraites automatiquement de Wikipédia
  (présentation, histoire, frise datée, lieux géolocalisés avec faits datés et traces actuelles).
- `contenu_ia/<département>/<code INSEE>-<nom>.json` : fiches réécrites par IA à partir des seules sources de la V1
  (accroche, récit, lieux avec coordonnées, sources numérotées et contrôles qualité). Couverture partielle :
  les communes les plus peuplées d'abord.

## Scripts
- `anecdotes_commune.py` : génération des fiches V1 (mode `--lot` pour toute la France, reprise automatique).
- `pilote_openai.py`, `reecriture_openai.py` : réécriture par IA avec budget plafonné, contrôles et reprise.

## Licences et sources
Voir `DONNEES.md`.
