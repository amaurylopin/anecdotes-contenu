# Catalogue national de sources — Projet Anecdotes

**Version :** 2026-10-12 (premier inventaire structuré ; enrichissement progressif)

Ce dossier réunit des sources de recherche historique et patrimoniale utilisables pour sélectionner des anecdotes originales sur les communes françaises et les territoires ultramarins. Il est **indépendant des JSON éditoriaux** dans `contenu/` et `contenu_ia/`. Ce n'est pas un import automatique d'histoires ni une autorisation de réutiliser les textes et photographies.

## Fichiers et effectifs initiaux

| Fichier | Enregistrements | Utilisation |
| --- | ---: | --- |
| [catalogue_national.csv](catalogue_national.csv) | 120 | Portails, fonds de presse, historiens locaux, revues, fédérations et bases d'archives |
| [societes_locales.csv](societes_locales.csv) | 253 | Associations et publications historiques **repérées**, avec département et localité/zone lorsqu'identifiable |
| [couverture_departements.csv](couverture_departements.csv) | 108 | 96 départements métropolitains (Corse en 2A/2B) et 12 territoires/collectivités ultramarins, ainsi que les portes d'entrée de recherche |

Lors de cette version, **59 des 108 zones administratives** possèdent au moins une association ou publication locale repérée dans `societes_locales.csv` ; 49 ont seulement un annuaire et/ou une base régionale en point de départ. Les collectivités ultramarines ne sont pas toutes des « départements » : le fichier distingue le code et le libellé de chaque territoire.

Ce chiffre ne mesure **ni le nombre d'associations existantes, ni le nombre de communes documentées**. Les annuaires référencent souvent seulement le siège d'une association ; son périmètre de recherche peut inclure des dizaines de communes. Certaines associations sont historiques ou dissoutes. Plusieurs liens directs restent à identifier.

## Le parcours de recherche par commune

1. À partir d'un **code INSEE**, retrouver le département (les exceptions 2A/2B, l'outre-mer et les changements de communes nécessitent la correspondance officielle, plutôt qu'un simple `INSEE[:2]`).
2. Filtrer `couverture_departements.csv` sur le code de département/collectivité pour obtenir l'inventaire régional et un annuaire de sociétés savantes.
3. Filtrer `societes_locales.csv` sur `departement`, puis comparer la commune recherchée et les communes voisines aux champs `commune_ou_zone`. Une différence de nom n'implique **pas** l'absence d'intérêt.
4. Consulter le site de l'association, ses bulletins ou ouvrages; élargir à la presse ancienne (BnF/Gallica/RetroNews), aux inventaires et aux archives.
5. Exiger une preuve pour chaque fait significatif : date, protagoniste, localisation, traces actuelles et source consultable (ouvrage, page, année, cote).
6. Rédiger une **fiche originale**, ne pas copier-coller les articles, et vérifier séparément les droits des images.

## Colonnes et statuts

### catalogue_national.csv

- `nom, type, region, departements, communes_ou_territoires, url, richesse_documentaire` : repérage des sources.
- `priorite_1_5` : priorité **potentielle** d'exploration pour Anecdotes, pas une note de fiabilité ou de qualité des textes.
- `origine` : source de découverte du site.
- `statut_editorial` : **A AUDITER** tant que ses contenus et conditions juridiques n'ont pas été évalués.

### societes_locales.csv

- `departement, commune_ou_zone, societe_ou_association` : ancrage géographique indicatif.
- `site_direct_si_identifie` : adresse directe lorsqu'elle a été repérée ; une case vide ne signifie pas que le site n'existe pas.
- `url_annuaire_preuve` : page de fédération, annuaire ou document dans lequel cette société ou publication a été repérée.
- `statut_decouverte, audit_contenu` : **le repérage ne vaut pas validation de l'activité actuelle ni des publications**.

### couverture_departements.csv

- `societes_locales_reperes` : comptage brut de lignes correspondantes, pas total réel des sociétés du département.
- `annuaire_principal_url, inventaire_regional_url, cths_annuaire_url` : portes d'entrée pour tous les territoires.
- `etat_de_prospection` : distingue les unités avec premiers organismes indexés des territoires encore à explorer.

## Sources d'annuaires structurantes

- [Comité des travaux historiques et scientifiques (CTHS)](https://cths.fr/an/annuaire.php) : formulaire par **ville et département**, sociétés actuelles et anciennes (base de plus de 4 000 notices, inégalement renseignées).
- [Normandie — FSHAN](https://fshan.fr/index.php/associations-adherentes) : associations adhérentes par département.
- [Bourgogne savante](https://www.bourgogne-savante.fr/index.php/societes-membres/) : listes de sociétés membres par département et localité.
- [Alsace — Bas-Rhin](https://www.alsace-histoire.org/societes_affiliees/?zone=bas-rhin) et [Haut-Rhin](https://www.alsace-histoire.org/societes_affiliees/?zone=haut-rhin) : fiches d'associations locales.
- [Île-de-France — fédération](https://www.federation-histoire-idf.fr/listing-des-societes/) : sociétés par département / arrondissement de Paris.
- [Bretagne — sociétés](https://www.bretagne-histoire.org/societes-historiques/) : sites de sociétés locales.
- [Provence — associations](https://www.lafhp.fr/liste-des-associations/) : fédération par département.
- [Savoie](https://www.societes-savantes-savoie.org/les-societes-savantes-de-savoie/) : sociétés de Savoie et Haute-Savoie.
- [Aisne](https://histoireaisne.fr/) : fédération historique départementale.
- [Loire-Atlantique](https://archives.loire-atlantique.fr/44/les-societes-savantes/c_40307) : annuaire départemental.

## Qualification éditoriale pour les futurs lots

Pour chaque candidate :

- **À PROSPECTER** : société ou site trouvé dans un annuaire, sans consultation critique de son contenu.
- **SOURCE AUDITÉE** : pages et publications réelles vérifiées, auteurs et datations identifiés.
- **ANECDOTE POTENTIELLE** : événement singulier avec un lien précis à une commune ou un lieu.
- **VÉRIFIÉE** : faits triangulés, sources datées, localisation cohérente et droits documentés.
- **PUBLIABLE** : récit original prêt à être intégré au JSON du lot, avec ses références et visuels utilisables.

Pour les photographies et documents numérisés, vérifier **par fichier** auteur, date, licence, restrictions et crédits requis. Les monographies anciennes peuvent être dans le domaine public, mais les scans, bases documentaires, commentaires récents et photographies peuvent imposer des conditions distinctes. N'aspirer aucun site en masse sans vérifier robots.txt et conditions d'utilisation.

## Limites et prochaines étapes

Cet inventaire est un **premier maillage national, non exhaustif**. Il ne prétend ni avoir exploré individuellement plus de 4 000 notices du CTHS ni identifier une association active pour chacune des 35 000 communes. La prochaine vague doit cibler les 49 zones administratives sans organisme local indexé, puis compléter les milliers de communes encore dépourvues de correspondance, en priorité en reliant les lieux du catalogue à leur **code INSEE** après vérification.

Les erreurs ou liens devenus inaccessibles doivent être corrigés après une vérification dédiée : l'existence d'une URL dans le catalogue ne démontre pas qu'elle répond aujourd'hui ni que chaque notice est pertinente pour Anecdotes.
