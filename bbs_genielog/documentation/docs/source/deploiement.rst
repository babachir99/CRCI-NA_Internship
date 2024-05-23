Plan de Déploiement 
====================

Le déploiement de logiciels implique toutes les activités nécessaires pour qu'un système 
ou une application logicielle soit prêt à être utilisé sur un appareil ou un serveur. 

Plan
-----

L'objectif est de déployer notre logiciel sur les serveur de l'université. Pour s'y connecter: 

ip : 172.16.129.2
Adresse : bioinfo.ensinfo.sciences.univ-nantes.prive 
Alias : bioinfo

Notre logiciel entier doit pouvoir être déployé. 
Le problème potentiel pourrait être au niveau de la fonction text_defile, qui ne semble pas fonctionner correctement selon 
l'ordinateur utilisé.

2- Design
----------

Nous avons choisi le déploiement progressif : les applications logicielles seront 
mises à jour lentement et remplaceront l'ancien logiciel. 
L'application originale n'est pas préservée dans le déploiement, mais notre logiciel initial est
facilement retrouvable grâce à l'utilisation de gitlab, et nous pouvons y visualiser toutes les anciennes versions
et le moindre commit est consultable.

3- Test
--------

Les test unitaires, ainsi que les test demandés à l'utilisateur permettent de savoir si notre application est fonctionnelle

Une fois ces étapes réalisés, nous pourrons déployer notre logiciel.
