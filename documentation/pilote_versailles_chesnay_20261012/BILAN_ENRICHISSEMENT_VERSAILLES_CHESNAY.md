# ANECDOTES — Bilan éditorial et technique — Versailles et Le Chesnay-Rocquencourt
**Édition :** 12 octobre 2026. **Périmètre :** exactement deux communes du département des Yvelines (78).
**Sauvegarde GitHub avant édition :** `backup/versailles-chesnay-avant-enrichissement-20261012`, pointant sur `8137089a58a73aa38ca09fe7b0f8b4378e45587c`.

## État initial
| Commune INSEE | Anecdotes initiales | Illustrations déjà présentes | Nouvelles anecdotes | Anecdotes finales |
|---|---:|---:|---:|---:|
| 78646 Versailles | 5 | 5 | 3 | 8 |
| 78158 Le Chesnay-Rocquencourt | 5 | 5 | 4 | 9 |
| **Total** | **10** | **10** | **7** | **17** |

### Inventaire des 10 titres originaux, dans l'ordre
**Versailles** : (0) Le roi déguisé en if ; (1) Damiens frappe Louis XV ; (2) Le faux rendez-vous de l'affaire du collier ; (3) Le Jeu de paume ; (4) 1871–1919 dans la galerie des Glaces.

**Le Chesnay-Rocquencourt** : (0) Fusion 2019 ; (1) combat du 1er juillet 1815 ; (2) Parly 2 ; (3) sophora de Chèvreloup ; (4) SHAPE / OTAN.

## Changements aux anecdotes déjà présentes
| Commune et index stable | Décision | Éléments complétés ou corrigés |
|---|---|---|
| 78646 / 0 | Enrichie | Mise en contexte cérémoniel du bal des Ifs ; dossier du château en source |
| 78646 / 1 | Enrichie | Sortie du roi et distinction Versailles / exécution à Paris |
| 78646 / 2 | Enrichie | Mécanique de l'usurpation d'identité dans l'affaire du collier |
| 78646 / 3 | Enrichie | Différence entre salle sportive, serment et Constitution à venir |
| 78646 / 4 | Enrichie | Rôle symbolique d'une galerie conçue pour exalter Louis XIV |
| 78158 / 0 | Enrichie | Fusion administrative et ancrages géographiques conservés |
| 78158 / 1 | Enrichie | Bataille couvrant plusieurs secteurs, prudence géographique |
| 78158 / 2 | Enrichie | Centre commercial replacé dans l'ensemble résidentiel |
| 78158 / 3 | Corrigée et enrichie | Titre et texte ne datent plus définitivement le sophora de 1747 : sources institutionnelles divergentes 1747/1848 |
| 78158 / 4 | Enrichie | Chronologie précise du SHAPE à Rocquencourt et de son transfert |

**Conservation :** mêmes dix sujets, même position de tableau (index 0–4 pour chaque ville) ; aucun article original supprimé ; champs `source`, `image`, `links` et caractéristiques de base gardés, sauf correction factuelle spécifique au sophora. **Les sept nouvelles histoires sont ajoutées en fin de tableau.**

## Nouvelles fiches
| Commune | Index ajouté | Titre | Catégorie | Illustration ajoutée |
|---|---:|---|---|---|
| Versailles | 5 | Le jour où un mouton, un canard et un coq s'envolent devant Louis XVI | histoire | Turgan / domaine public |
| Versailles | 6 | 1686 : l'ambassade du Siam traverse les mers pour rencontrer Louis XIV | histoire | Charles Le Brun / domaine public |
| Versailles | 7 | Le musée né du legs d'une Versaillaise : l'hôtel Lambinet | patrimoine | Henry Salomé / CC BY-SA 4.0 |
| Le Chesnay-Rocquencourt | 5 | La dernière reine du Portugal avait trouvé refuge au Chesnay | personnalites | HistoVERSAILLES / CC BY-SA 4.0 |
| Le Chesnay-Rocquencourt | 6 | 300 000 francs et une dernière volonté : le legs de Juliette Frémillon | personnalites | aucune, droits non identifiés |
| Le Chesnay-Rocquencourt | 7 | Au Chesnay, la République et l'Église s'affrontent jusque dans les écoles | politique | aucune, droits non identifiés |
| Le Chesnay-Rocquencourt | 8 | Le caricaturiste du Chesnay mobilisé pour cacher les canons en 1915 | personnalites | autoportrait / domaine public |

## Catalogue, index, images
- **5 images ajoutées ; 0 image existante supprimée ; 0 remplacée.** Les pages de licence des 5 nouvelles images ont été inspectées.
- **7 nouvelles entrées** `sources/catalogue_national.csv`, **2 sociétés savantes** `sources/societes_locales.csv`, ajustement de la seule ligne de couverture départementale `78` pour passer de 1 à 3 structures. Les ajouts concurrents d'autres lots sont conservés.
- `index.json` : seules les entrées 78646 et 78158 sont modifiées, avec `count`, `written` et `updated`. Les autres ~34 664 communes conservent leurs données originales.
- **Publication directe souhaitée sur `main`**, sans force-push. Le SHA du commit de publication est celui affiché par GitHub après mise à jour effective de la branche ; cette note ne constitue pas à elle seule une preuve de publication.

## Tests réellement réalisés pour les blobs préparés
- Analyse des JSON source des deux communes, contrôle des identifiants et des noms, structures `anecdotes` et champs image/source ; sérialisation et relecture JSON des nouvelles versions.
- Conservation de l'ordre original (index 0–4), absence de doublons de titres, nouvelles fiches append-only.
- Contrôle éditorial : recherches d'institutions identifiées et licences vérifiées de cinq nouveaux médias sur leurs pages Commons.
- Pour `index.json` : lecture intégrale de 3,46 Mo, validation JSON, comparaison des 34 666 entrées, uniquement les deux codes mis à jour.
- Contrôle des identifiants du catalogue depuis la version la plus récente, sans remplacer les ajouts d'autres conversations.

**Tests non exécutés :** lancement réel de l'application iOS ; vérification d'affichage sur appareil ; mesure des caches iOS ; exhaustivité des droits pour les dix illustrations existantes ; dépouillement complet de Gallica ; localisation métrique des 7 nouveautés. Ne jamais annoncer ces contrôles comme passés.

**Attention à la concurrence Git :** depuis le SHA initial, d'autres lots ont actualisé le catalogue. Les nouvelles entrées ont été fusionnées depuis les versions visibles après cette modification. Toute nouvelle évolution avant commit doit provoquer un contrôle du `main` et, si nécessaire, une nouvelle fusion.
