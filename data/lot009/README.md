# Lot 009 Arras et alentours — images par liens uniquement

50 communes du département 62 identifiées par code INSEE et figées au 10/10/2026.
56 anecdotes existantes conservées sans modification ; 61 propositions nouvelles ; total : 117.
Cinq photographies Wikimedia Commons : **URL directe distante + page + licence + auteur**.
**Aucun téléchargement, aucune photo ou vignette binaire embarquée.**

Par défaut : `bash publier_lot_009_arras.sh` = simulation, aucune écriture dans le dépôt.
`bash publier_lot_009_arras.sh --publier` = fusion vérifiée avec les 50 JSON **déjà présents** dans le clone local de `main`, mise à jour sélective de `index.json`, métadonnées sous `data/lot009/`, commit et push.

Important : le ZIP autonome contient 61 **ajouts**, pas les originaux complets : ils sont vérifiés par SHA Git sur le clone lors de l’exécution. L’environnement de construction ne dispose pas des 50 fichiers complets. Ce compromis assure la conservation exacte des anecdotes anciennes sans les reconstituer ou inventer. En cas de modification externe, le script refuse l’écrasement. La simulation peut fonctionner dans un dépôt Git local ; sans dépôt, les tests d’intégrité internes seuls passent et la publication est impossible.

Les 50 communes ont été sélectionnées depuis les coordonnées arrondies du dépôt ; le contrôle sur contours 2018 diffère légèrement au seuil. L’ordre strict sur les centroïdes officiels 2026 est une **réserve ouverte** et non une conformité certifiée. Sources géographiques : INSEE COG 2026, IGN/INSEE Admin Express 2018, dépôts existants.

**Le JSON app peut ignorer les liens distants** : le placement est fourni sous `data/lot009/placement_images.json`, sans garantir l’affichage par l’iOS actuel. Les licences CC BY-SA imposent la conservation des crédits.
