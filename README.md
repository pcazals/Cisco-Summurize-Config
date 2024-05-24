
# README

## Description

Ce script Python permet de lire un fichier de configuration réseau, d'extraire les interfaces et leurs configurations, de regrouper les interfaces ayant des configurations identiques, et d'afficher ces groupes sous forme de tableau.

## Prérequis

- Python 3.x
- Bibliothèques Python : `pandas`, `tabulate`

## Installation

Pour installer les bibliothèques nécessaires, exécutez :

```sh
pip install pandas tabulate
```

## Utilisation

1. Placez le fichier de configuration réseau dans le même répertoire que le script ou adaptez le chemin du fichier dans la fonction `main`.

2. Modifiez la variable `chemin_fichier` dans la fonction `main` pour pointer vers votre fichier de configuration. Par défaut, il est défini sur `'TDL.txt'`.

3. Exécutez le script :

```sh
python script.py
```

## Fonctionnalités

- **Lire Configuration** : La fonction `lire_configuration(fichier)` lit le contenu d'un fichier de configuration réseau.
  
- **Extraire Interfaces** : La fonction `extraire_interfaces(contenu)` analyse le contenu du fichier et extrait les interfaces et leurs configurations.

- **Regrouper Interfaces** : La fonction `regrouper_interfaces(interfaces)` regroupe les interfaces ayant des configurations identiques.

- **Afficher Groupes** : La fonction `afficher_groupes(config_group)` affiche les groupes d'interfaces et leurs configurations sous forme de tableau en utilisant la bibliothèque `tabulate`.

## Exemple de sortie

Le script affiche un tableau dans la console similaire à celui-ci :

```
+--------------------+------------------------+
| Interfaces         | Configuration          |
+====================+========================+
| interface1         | configuration_line1    |
| interface2         | configuration_line2    |
| interface3         | configuration_line3    |
+--------------------+------------------------+
| interface4         | configuration_line1    |
| interface5         | configuration_line2    |
+--------------------+------------------------+
```

## Auteurs

Votre Nom

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
