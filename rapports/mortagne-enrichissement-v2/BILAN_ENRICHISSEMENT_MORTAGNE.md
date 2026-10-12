# Anecdotes — Bilan avant / après — Mortagne-au-Perche V2

**Date :** 12 octobre 2026. **INSEE :** 61293. **Périmètre :** commune de Mortagne-au-Perche, département de l'Orne, exclusivement.

## Référence initiale

- Départ de la branche `main` : `8137089a58a73aa38ca09fe7b0f8b4378e45587c`.
- SHA blob initial de `communes/61293.json` : `0a78012de894a6c4953fb2157fc0ac60ec588a8a`.
- Sauvegarde Git créée **avant modification** : `backup/mortagne-avant-enrichissement-20261012`.
- **5 anecdotes**, dans l'ordre : porte Saint-Denis ; départs vers la Nouvelle-France ; crypte de Toussaint ; vitrail mémorial de la Grande Guerre ; maison dite de Henri IV.
- Catégories initiales : patrimoine 2, histoire 2, insolite 1. **3 images** initiales. Tous les articles avaient déjà une source citée.
- Index national initial : 34 666 entrées ; Mortagne `count=5`, `written=5`, `updated=2026-10-10`.

## Conservation des articles existants

| Indice stable | Article | Intervention |
|---:|---|---|
| 0 | La porte qui a survécu au fort Toussaint | Ajout de contexte sur la ville close et ses quartiers ; source Normandie Tourisme ajoutée |
| 1 | Mortagne, un des grands foyers français vers la Nouvelle-France | Conservé sans modification |
| 2 | Sous le tribunal, la crypte d’une collégiale disparue | Conservé sans modification |
| 3 | Un vitrail transforme la Grande Guerre en scène de mémoire | Ajout d'un paragraphe sur les commandes de 1912 et 1921 à partir du dossier Inventaire général IM61004006 |
| 4 | La « maison de Henri IV » : un nom célèbre, une visite au conditionnel | Conservé sans modification |

Les cinq titres, les catégories, les textes initiaux dans leur ordre, les sources précédemment enregistrées, les images présentes et les identifiants de route ont été conservés. **Aucun article n'a été supprimé ou déplacé.**

## Nouvelles anecdotes (ajoutées après les cinq existantes)

| Indice | Anecdote | Catégorie | Longueur du récit | Illustration | Source documentaire |
|---:|---|---|---:|---|---|
| 5 | La duchesse qui soignait les malades dans sa maison | histoire | 354 mots | Aucune, droits non suffisamment documentés | POP PA00110859 ; *Cahiers percherons* 229 : sommaire seulement |
| 6 | Alain : un philosophe né à Mortagne qui écrivait sous un autre nom | personnalites | 368 mots | Aucune, licence sûre non identifiée | Biographie Thierry Leterre, Association des Amis d'Alain ; CCFr BnF |
| 7 | La maison des comtes du Perche n'est pas leur maison médiévale | patrimoine | 367 mots | Brunodumaine, CC BY-SA 4.0 | POP PA00110868 |
| 8 | Le logis du doyen adossé à une tour des remparts | patrimoine | 356 mots | Benjism89, CC BY-SA 2.5 | POP PA00110866 ; PA00110858 |
| 9 | Comment un boudin noir est devenu l'emblème de Mortagne | gastronomie | 347 mots | Aucune image contextuelle trompeuse | Office de tourisme de Mortagne ; L'OPT |

La chronologie n'est pas inventée à partir de traditions locales. Pour la maison des comtes, l'habitation médiévale à l'emplacement actuel reste hypothétique ; pour la maison Henri IV, la visite du roi demeure au conditionnel. Le statut **simplement bibliographique** des anciens *Cahiers percherons* non dépouillés est explicité dans l'audit documentaire.

## Résultats chiffrés

| Indicateur | Avant | Après |
|---|---:|---:|
| Anecdotes | 5 | 10 |
| Articles initiaux conservés | 5 | 5 |
| Articles existants enrichis | 0 | 2 |
| Nouvelles anecdotes | 0 | 5 |
| Images référencées | 3 | 5 |
| Images remplacées | 0 | 0 |
| Entrées documentaires supplémentaires au catalogue | 0 | 3 |

Catégories finales : patrimoine 4, histoire 3, insolite 1, personnalites 1, gastronomie 1.

## Contrôles et limites

- JSON de Mortagne produit et réanalysé en JavaScript ; champs `id`, `insee`, `name`, `anecdotes`, catégories et liens source contrôlés.
- Vérification mécanique : les cinq anciens titres et catégories sont immuables, les paragraphes des récits d'origine conservés à leur place, les illustrations initiales intactes. Unicité des titres.
- `index.json` téléchargé **intégralement** depuis son SHA de blob GitHub, analysé et re-sérialisé ; seule l'entrée `61293` doit changer, avec `count=10`, `written=10`, `updated=2026-10-12`. Les 34 666 codes INSEE restent présents.
- Sources du dépôt `sources/catalogue_national.csv`, `sources/societes_locales.csv`, `sources/couverture_departements.csv`, `sources/README.md` examinées ; 3 ressources documentaires additionnelles enregistrées dans le catalogue national, sans modification des entrées existantes.
- `web/server.mjs`, `web/public/app.js` et documentation applicative consultés pour contrôler **statiquement** le format et la stabilité des URLs de type `/commune/61293/article/<index>`.
- Les photographies identifiées sont associées à des pages Commons avec attribution et licences ; 3 images initiales gardées et 2 ajoutées, aucune image de licence incertaine intégrée.
- **Tests non exécutés** : exécution sur iPhone/Xcode, navigateur avec le serveur de production, rafraîchissement sur l'appareil, vérification du chargement des images au travers des API en production, dépouillement complet de revues savantes, visite des édifices et des fonds d'archives physiques.
- Risques documentaires résiduels et pistes de recherche écartées : voir `SOURCES_MORTAGNE_ENRICHISSEMENT.md`.

## Publication

Toutes les modifications ont d'abord été préparées sur `enrichissement-mortagne-v2-20261012` après création de la sauvegarde `backup/mortagne-avant-enrichissement-20261012`. L'état de publication sur `main` et son SHA final doivent être confirmés par la branche GitHub distante et ne se déduisent pas de l'existence de ce rapport. Aucun force-push autorisé. Aucun fichier d'une autre commune modifié.
