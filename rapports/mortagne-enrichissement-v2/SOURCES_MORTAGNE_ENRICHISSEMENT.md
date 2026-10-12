# SOURCES — Mortagne-au-Perche — Enrichissement documentaire V2

**Date de la recherche :** 12 octobre 2026. **Code INSEE :** 61293. **Département :** Orne. **Périmètre :** commune de Mortagne-au-Perche uniquement.

## Méthode et état documentaire

Avant rédaction, lecture du JSON courant de `communes/61293.json` (5 articles), de la référence éditoriale `communes/44109.json`, du catalogue national `sources/catalogue_national.csv`, de `sources/societes_locales.csv`, de `sources/couverture_departements.csv` et de `sources/README.md`. L'index initial, très volumineux, a été récupéré intégralement par le blob SHA GitHub et validé comme JSON : 34 666 entrées communales. Consultation de `web/server.mjs`, `web/public/app.js` et `web/README.md` de l'application pour les catégories, les routes, les images, les caches et la lecture de l'index.

Les **catalogues** donnent des portes d'entrée, pas une preuve d'accès à leurs publications. Les cinq nouvelles histoires s'appuient sur des pages précises effectivement ouvertes ; les sommaires de bulletins payants ne sont **pas** présentés comme la lecture intégrale des articles.

### Sources du catalogue déjà présentes et exploitées

- `0003` Les Amis du Perche : [Cahiers percherons n°3 (1957), Philippe Siguret](https://amisduperche.fr/produit/cahiers-percherons-3-1957-3/?v=82a9e4d26595), sommaire consulté ; [n°229 (2022), Marguerite de Lorraine](https://amisduperche.fr/produit/cahiers-percherons-229-2022-1-marguerite-de-lorraine-toucheuses-et-guerisseuses-origny-le-roux-la-gallo-romaine/), sommaire et notices d'auteurs consultés ; [n°171 (2007), réseau Hector à Mortagne](https://amisduperche.fr/produit/cahiers-percherons-171-uniquement-disponible-en-pdf/?v=82a9e4d26595), sommaire consulté ; [n°18 (1963), toiles de Mortagne](https://amisduperche.fr/produit/cahiers-percherons-18-1963-2-lindustrie-dans-le-perche-textile-et-fer/?v=82a9e4d26595), sommaire consulté ; [n°240 (2024), école primaire 1816-1830](https://amisduperche.fr/produit/cahiers-percherons-240-2024-4-le-fief-de-la-boeche-a-yevres-lecole-primaire-a-mortagne-1816-1830-le-peintre-eugene-lavieille/), sommaire consulté. Statut des ouvrages : **repérés/documentés, contenu intégral non lu**.
- `0005` Fédération des sociétés historiques et archéologiques de Normandie : annuaire utilisé via les lignes Orne du catalogue. L'association **Amis du Perche de l'Orne** y est repérée sous `SL0020` ; son statut n'est pas confondu avec un audit de tous ses bulletins.
- `0070` Inventaire de Normandie : [vitrail 1914-1918, IM61004006](https://inventaire-patrimoine.normandie.fr/dossier/IM61004006), notice détaillée effectivement consultée.
- `0081` POP : [porte Saint-Denis PA00110870](https://pop.culture.gouv.fr/notice/merimee/PA00110870), [crypte PA00110858](https://pop.culture.gouv.fr/notice/merimee/PA00110858), [maison Henri IV PA00110869](https://pop.culture.gouv.fr/notice/merimee/PA00110869) préexistants dans le JSON ; nouvelles consultations de [couvent PA00110859](https://pop.culture.gouv.fr/notice/merimee/PA00110859), [maison des comtes PA00110868](https://pop.culture.gouv.fr/notice/merimee/PA00110868), [maison du doyen PA00110866](https://pop.culture.gouv.fr/notice/merimee/PA00110866) (notice visible en recherche, ouverture complète intermittente : 503).
- `0086` Wikimedia Commons : pages descriptives des cinq photographies retenues consultées pour auteur et licence.

### Nouveaux sites effectivement consultés

- [Archives et patrimoine culturel de l'Orne — Inventaires en ligne](https://archives.orne.fr/index.php/inventaires-en-ligne) : inventaires officiels examinés ; contenu intégral des cotes non dépouillé.
- [Association des Amis d'Alain — biographie par Thierry Leterre](https://philosophe-alain.fr/articles_sur_alain/biographie-chronologie-detaillee/) : biographie détaillée consultée et datations examinées ; [association et musée](https://philosophe-alain.fr/qui-sommes-nous/) : conservation et création du musée documentées.
- [BnF, Catalogue collectif de France — fonds Alain](https://ccfr.bnf.fr/portailccfr/ark:/16871/004b79122380) : notice archivistique précise ; les manuscrits ne sont pas réputés lus.
- [Office de tourisme du Pays de Mortagne — boudin noir](https://tourisme-mortagne-au-perche.fr/decouvrir/le-boudin-noir-de-mortagne-au-perche/) et [L'OPT — fiche gastronomique](https://www.lopt.org/carte/perche/produits/boudin-de-mortagne-au-perche) : chronologie et manifestations consultées. Textes possiblement dépendants : ne pas les compter comme corroborations totalement indépendantes.
- [Normandie Tourisme — Mortagne](https://www.normandie-tourisme.fr/sites-lieux-de-visites/mortagne-au-perche-petite-cite-de-caractere/) : topographie de la ville close et quartiers.
- [Larousse — Alain](https://www.larousse.fr/encyclopedie/personnage/%C3%89mile_Chartier_dit_Alain/104506) : contrôle secondaire de l'activité du philosophe.
- [Centre généalogique de l'Orne et du Perche — permanences](https://orne-perche.org/Page/ASS_Permanences.aspx) : collections disponibles signalées, non dépouillées.

## Inventaire initial (avant toute écriture)

| Indice immuable | Sujet préexistant | Catégorie | Récit initial (corps, mots approx.) | Image | Sources déjà présentes | Décision |
|---:|---|---|---:|---|---|---|
| 0 | La porte qui a survécu au fort Toussaint | patrimoine | 144 | Porte saint Denis.jpg | POP PA00110870 | Enrichir, conserver image |
| 1 | Mortagne, un des grands foyers français vers la Nouvelle-France | histoire | 155 | Non | Histoire Canada ; Perche-Québec | Conserver à l'identique |
| 2 | Sous le tribunal, la crypte d’une collégiale disparue | patrimoine | 137 | Crypte collégiale de Toussaint.jpg | POP PA00110858 | Conserver à l'identique |
| 3 | Un vitrail transforme la Grande Guerre en scène de mémoire | histoire | 132 | Non | Inventaire Normandie IM61004006 | Enrichir |
| 4 | La « maison de Henri IV » : un nom célèbre, une visite au conditionnel | insolite | 126 | Maison Henri IV.JPG | POP PA00110869 | Conserver à l'identique |

**État des vérifications initiales :** sources précises identifiées ; autorité des notices de protection confirmée ; les deux pages externes concernant la Nouvelle-France restent des références préexistantes et n'ont pas été individuellement ré-auditées en profondeur. Aucune source valable ni aucune photographie initiale supprimée.

## Nouvelles histoires et traçabilité

| Anecdote | Preuve documentaire réellement consultée | Document secondaire | Confiance / limites |
|---|---|---|---|
| La duchesse qui soignait les malades dans sa maison | POP PA00110859, historique du couvent : pièces de soin, construction 1505, chapelle 1515, transfert mai 1793 | *Cahiers percherons* n°229, 2022 (sommaire seulement) | Haute sur les faits de la notice ; pas de récit individuel de malade |
| Alain : un philosophe né à Mortagne qui écrivait sous un autre nom | Thierry Leterre, biographie Association des Amis d'Alain ; CCFr fonds Alain, cote AL PN 1-260 | Larousse ; association et musée | Haute, dates et inventaire ; pièces du fonds non consultées physiquement |
| La maison des comtes du Perche n'est pas leur maison médiévale | POP PA00110868, Maison des comtes, 8 rue de la Porte-Saint-Denis ; XVIIIe balcon | Association des Amis d'Alain, historique du musée | Haute pour bâti XVIIe et mémoire XIIe **au conditionnel** |
| Le logis du doyen adossé à une tour des remparts | POP PA00110866, notice de protection (résumé public indexé et recherche), 3 rue du Fort | POP PA00110858 ; photo Commons identifiée | Moyenne à haute ; texte de notice retrouvé, ouverture détaillée parfois indisponible |
| Comment un boudin noir est devenu l'emblème de Mortagne | Office de tourisme de Mortagne, chronologie 1931-1963 et foire | L'OPT, fiche boudin noir | Moyenne à haute ; preuves administratives d'époque à rechercher, possible reprise des mêmes informations |

## Décisions éditoriales et exclusions

- **Enrichies** : porte Saint-Denis (contexte de ville close et quartiers), vitrail commémoratif (articulation 1912/1921, commanditaires et sculpture du décor).
- **Conservées sans retouche historique** : départs vers la Nouvelle-France ; crypte de Toussaint ; maison dite de Henri IV.
- **Écartées du JSON à ce stade** : réseau Hector à Mortagne (Yves Duprez et Jacques Henriet, *Cahiers percherons* n°171), butte Saint-Malo (Jean-David Desforges, Fabrice Morand, n°171), toiles de Mortagne et famille Cohin (François Dornic, n°18), difficultés des rues au XVIIIe siècle (Jean-François Suzanne, n°177), école primaire 1816-1830 (Philippe Charpentier de Beauvillé, n°240), libération de Mortagne en 1944 (Michel Ganivet). Ces sujets existent dans des sommaires mais **leurs démonstrations détaillées n'ont pas été lues**. Ne pas construire d'histoires à partir des seuls titres.
- **Politique et actualité électorale** : aucune fiche politique nouvelle faute de contrôle électoral officiel complet adapté à cette rédaction ; ne pas réutiliser des chiffres datés.
- **Marguerite / photographie de chapelle 2026** : écartée malgré une étiquette « domaine public » sur Wikimedia Commons, parce que la photographie contemporaine attribuée à un « auteur inconnu » ne permet pas d'établir correctement les droits photographiques.

## Catalogue national mis à jour

Trois ressources documentaires réellement ouvertes ont été ajoutées à `sources/catalogue_national.csv`, sans modifier les lignes anciennes : Archives de l'Orne (inventaires), Association des Amis d'Alain (biographie et musée), Centre généalogique de l'Orne et du Perche (relevés). Les articles payants simplement listés n'ont pas été copiés et les droits des documents restent à examiner avant toute reproduction.

## Transparence

Recherches web et lecture de notices effectuées. Pas de consultation sur place des archives, pas d'achat des *Cahiers percherons*, pas de lecture de la totalité du fonds Alain, pas de certitude sur les images absentes. Une notice POP a parfois retourné 503 lors de l'ouverture malgré un résumé historique indexé accessible. Les textes produits sont originaux : aucune page web n'a été copiée en bloc.
