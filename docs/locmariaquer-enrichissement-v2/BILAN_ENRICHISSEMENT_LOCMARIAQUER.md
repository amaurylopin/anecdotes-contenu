# Anecdotes — Locmariaquer — Enrichissement documentaire V2

12 octobre 2026 • Code INSEE 56116

## État initial

Commit initial `ff99e95f8e5c3d3087d677e3fe14e4e81f20ff98` ; blob `94884a4d0c0504b1bd00d6ab9d16c6b2c6a1137c`. Sauvegarde : `backup/locmariaquer-avant-enrichissement-20261012`.

- Avant : 4 anecdotes, 4 illustrations. Catégories : préhistoire 3, histoire 1.
- Après : 12 anecdotes, dont 3 anciennes enrichies, 1 inchangée et 8 inédites ; 4 images ajoutées, aucune remplacée.
- Indices 0 à 3 : même ordre, mêmes titres, mêmes catégories et mêmes images.

## Articles enrichis

| Index | Titre | Intervention |
|---|---|---|
| 0 | Le colosse de pierre qui dépassait vingt mètres | Provenance géologique des blocs d'orthogneiss, source Ministère. |
| 1 | Une dalle gravée démontée puis réemployée | Rappel prudent d'une découverte des fouilles de 1811. |
| 2 | Des objets venus des Alpes et de la péninsule Ibérique | Mention des fouilles 1986–1994. |
| 3 | Le fort de Kerpenhir a disparu, pas sa position stratégique | Préservé sans changement. |

## Nouvelles anecdotes

- **4. Au Mané-Lud, la mystérieuse découverte de crânes de chevaux** — `patrimoine`, 295 mots environ (entrée et corps), illustration avec licence vérifiée.
- **5. Onze haches de jadéite brisées sous une colline de pierres** — `patrimoine`, 296 mots environ (entrée et corps), illustration avec licence vérifiée.
- **6. Le dolmen des Pierres-Plates et son faux menhir indicateur** — `patrimoine`, 285 mots environ (entrée et corps), illustration avec licence vérifiée.
- **7. Le théâtre gallo-romain caché sous le cimetière** — `histoire`, 311 mots environ (entrée et corps), aucune image faute de visuel adéquat juridiquement documenté.
- **8. 1882 : la naissance des parcs à huîtres, puis la catastrophe** — `economie`, 291 mots environ (entrée et corps), aucune image faute de visuel adéquat juridiquement documenté.
- **9. Dans l'église, un vitrail représente des tuiles à huîtres** — `patrimoine`, 295 mots environ (entrée et corps), illustration avec licence vérifiée.
- **10. En 1883, des érudits sauvent la Table des Marchands** — `histoire`, 290 mots environ (entrée et corps), aucune image faute de visuel adéquat juridiquement documenté.
- **11. Quand les tumulus guidaient les marins vers le golfe** — `histoire`, 278 mots environ (entrée et corps), aucune image faute de visuel adéquat juridiquement documenté.

## Contrôles techniques

- JSON valide, commune 56116 inchangée, catégories nouvelles `patrimoine`, `histoire` et `economie` prises en charge par le client web.
- Titres anciens, images et ordre préservés ; aucune autre fiche communale modifiée.
- Liens sources en HTTPS, récits distincts et sans titres identiques.
- Les CSV du catalogue gardent le nombre et l'ordre de leurs colonnes.
- `index.json` n'a pas été modifié : le connecteur ne l'avait pas restitué intégralement, et la tâche automatique d'indexation peut le synchroniser ultérieurement.
- Les contrôles réels de rendu iOS, du cache applicatif et du serveur web ne sont **pas exécutés** depuis cette session ; un test de synchronisation sur appareil est nécessaire.
