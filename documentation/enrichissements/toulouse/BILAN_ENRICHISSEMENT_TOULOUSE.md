# ANECDOTES — TOULOUSE — BILAN ENRICHISSEMENT V2

**Commune :** 31555 Toulouse · **Date :** 12 octobre 2026.

## Avant
- 5 anecdotes aux indices 0–4 : Moudenc, la droite qui tient le Capitole ; AZF : 31 morts et une ville soufflée ; Le pastel, l'or bleu qui a bâti les hôtels roses ; Airbus, l'A380 et les convois de nuit ; Saint-Sernin, la plus grande église romane d'Europe.
- Aucun objet image déclaré ; sources principales à dominante Wikipédia.
- Copie initiale sécurisée par une branche `backup/toulouse-avant-enrichissement-20261012-3aaa138c` ; une sauvegarde supplémentaire est établie sur le dernier commit initial lors de la publication.

## Après
- **12 anecdotes**, dont **5 anciennes conservées**, **5 enrichies** et **7 nouvelles**.
- Les cinq titres, les catégories et les positions des articles d'origine ont été conservés.
- **4 illustrations** sous licences Creative Commons identifiées et créditées.
- Nouveaux récits : Calas : une maison, un procès, puis Voltaire ; 1218 : le projectile qui tue Simon de Montfort ; 1814 : une bataille après l'abdication de Napoléon ; Ponts-Jumeaux : quand les canaux deviennent une sculpture ; 1793 : les portraits des capitouls brûlés devant la mairie ; La Halle aux Grains, du marché à l'orchestre ; 1680 : la ville entière dessinée parcelle par parcelle.

## Principales améliorations
- Politique : élections de mars 2026 sur source officielle.
- AZF : masse stockée ≠ masse qui a détoné.
- Pastel : retrait d'une assertion non démontrée sur Jean de Bernuy.
- Aéronautique : distinction géographique Toulouse / Blagnac.
- Saint-Sernin : restauration de 1993 et formulation plus prudente de la tradition des reliques.
- Nouvelles histoires : justice, Moyen Âge, bataille de 1814, patrimoine fluvial, Révolution, reconversion urbaine et archives cadastrales.

## Impact technique
- `communes/31555.json` modifié sans renumérotation des anciens articles.
- `index.json` : seule entrée Toulouse modifiée (5 → 12 ; 2026-10-08 → 2026-10-12). Les **34 665 autres communes** restent inchangées.
- `sources/` : référence municipale et société savante ajoutées, compteur départemental Haute-Garonne adapté.
- Aucun autre JSON communal ni aucun fichier de l'application modifié.

## Tests réellement effectués
Vérification du JSON (commune + index), maintien des indices 0–4, récits non vides, catégories et schéma, cohérence des couples lat/lon, source principale HTTPS, crédits et licences des quatre photographies, non-modification des autres entrées de l'index, construction d'un commit Git descendant du commit de base, sans force-push. Vérification distante prévue à l'étape de publication.

## Tests non effectués
Test physique de l'application iOS, rechargement de la webapp et contrôle du cache en production, affichage effectif des images sur les appareils, contrôle HTTP automatique de tous les liens, dépouillement exhaustif des collections historiques. Ces tests ne sont pas présentés comme réussis.
