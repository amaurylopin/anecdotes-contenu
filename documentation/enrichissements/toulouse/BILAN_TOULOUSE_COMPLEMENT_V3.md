# ANECDOTES — TOULOUSE — BILAN AVANT/APRÈS — V3

**Territoire :** Toulouse (31555) uniquement. **Date :** 12 octobre 2026.

## Avant le correctif

12 anecdotes publiées en V2, dont 5 originelles conservées, avec 4 images vérifiées. Le lot V2 omettait notamment les attentats de Mohammed Merah en mars 2012 et plusieurs événements historiques majeurs.

## Après complément V3

- **28 anecdotes** : les **12 antérieures strictement conservées aux indices 0–11**, et **16 nouvelles ajoutées aux indices 12–27**, sans réordonnancement.
- **7 illustrations** au total : 4 antérieures préservées + 3 nouvelles, avec auteur et licence contrôlés.
- Principales nouvelles fiches : Mars 2012 : les attentats de Mohammed Merah ; 1463 : le grand incendie parti d'une boulangerie ; Mai 1562 : une guerre de Religion dans les rues ; 1875 : la crue de la Garonne fait 209 morts ; 1942 : la lettre de l'archevêque Saliège contre les persécutions ; Le 11 novembre 1942, Toulouse voit entrer la Wehrmacht ; 1944 : les bombes alliées sur les usines de Toulouse ; Août 1944 : Toulouse libérée, une nouvelle mairie au Capitole ; Alfred Nakache : champion, déporté, puis olympien ; 1229 : l'université naît d'un traité de paix ; Pont-Neuf : 88 ans pour construire un pont qui n'est plus neuf ; Riquet meurt avant de voir le canal du Midi inauguré ; 1907 : le Stade Toulousain naît d'une fusion ; Toulouse, capitale de l'exil républicain espagnol ; 1936 : la CGT se réunifie à Toulouse ; Les Jacobins : un palmier de pierre et les reliques de Thomas d'Aquin.
- **Mémoire de mars 2012 :** une histoire indépendante, précise sur Toulouse et Montauban et centrée sur les victimes.
- Catalogue national : entrée Université Toulouse Capitole ajoutée pour la documentation du traité de 1229.

## Vérifications techniques

Le document `communes/31555.json` est une fusion conservatrice de la version V2 et des nouvelles anecdotes. Contrôles réalisés : syntaxe JSON ; 12 entrées initiales identiques objet par objet ; catégories connues ; récits développés et non vides ; liens externes HTTPS ; auteurs et licences des 3 illustrations ; ajout exclusivement à la fin du tableau. `index.json` conserve ses **34 666 entrées**, à l'exception du compteur Toulouse passant de 12 à 28 ; date de mise à jour conservée au 12 octobre 2026 puisque le travail se poursuit le même jour.

Publication prévue par commit unique créé sur l'arbre Git distant, avec branche de sauvegarde, vérification fast-forward et relecture après publication. Aucun autre JSON communal, aucune source antérieure ni aucun fichier du dépôt applicatif modifiés.

## Contrôles non réalisés

Aucun lancement réel de l'application iOS, aucun test sur appareil du rafraîchissement, du cache ou de l'affichage de toutes les images, aucun dépouillement exhaustif des journaux et annuaires historiques. Ne pas les annoncer comme réussis. Le correctif de contenu ne constitue pas une garantie que le client iOS actualise automatiquement ses données.
