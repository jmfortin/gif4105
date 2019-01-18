# Démonstrations pour le cours GIF-4105/7105

Dans ce repo, vous trouverez toutes les démonstrations du cours [GIF-4105/7105 Photographie Algorithmique](http://vision.gel.ulaval.ca/~jflalonde/cours/4105/h19/). Celles-ci sont implémentées en python. 

# Procédure d'installation

Pour exécuter les démonstrations sur votre ordinateur, voici une procédure facile d'installation. 

## Utilisation d'un "virtual environment" 

1. Installer `virtualenv` à partir d'une installation python3 de base: 

`pip install virtualenv`
  
2. Se créer un environment virtuel pour le cours

`virtualenv gif4105-env`

3. Démarrer l'environnement virtuel du cours

`source gif4105-env/bin/activate`

## Installation des "packages" de base nécessaires

Les "packages" suivants seront nécessaires pour l'exécution de toutes les démonstrations. Pour les installer, il suffit habituellement d'utiliser la commande suivante, _après avoir démarré le "virtualenv"_:

`pip install <packagename>`

1. [Jupyter](https://jupyter.org/install) 
2. [imageio](https://pypi.org/project/imageio/) 
3. [numpy](https://pypi.org/project/numpy/)
4. [scikit-image](http://scikit-image.org/docs/dev/install.html)
5. [matplotlib](https://matplotlib.org/users/installing.html)
6. [Pillow](https://pypi.org/project/Pillow/2.2.1/)

## Cloner les démonstration de github

1. Installez [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) sur votre ordinateur, si vous ne l'avez pas déjà. 

2. Clonez le "repo" du cours: 

`git clone https://github.com/lvsn/gif4105.git gif4105-demos`

# Démarrage des démonstrations

Pour démarrer les démonstrations lorsque tout est installé, il suffit donc de: 

1. Activer le "virtualenv"

`source gif4105-env/bin/activate`

2. Démarrer le "jupyter notebook"

`cd gif4105-demos; jupyter notebook`

Ceci démarre votre navigateur web, et vous devriez voir les différentes démonstrations disponibles. 

## Remerciements

Merci à Jinsong Zhang pour son aide!
