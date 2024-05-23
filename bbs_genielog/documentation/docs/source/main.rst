Fichier Main
=============

Le fichier main est LE fichier qui nous intéresse. Il permet d'afficher toutes les fonctions précédemment créées, tout en y important une fonctionnalité importante: un **mode**.
En effet,  3 modes sont disponibles.

Nous avons ainsi fait un menu interactif grâce à une boucle *while*.

.. code-block:: python
    
    while mode!="0":
    mode = input("Choisissez le mode: éducatif (1), fenêtre (2), alerte (3) (Quitter: 0): ") 

On demande alors à l'utilisateur de sélectionner un mode. Pour faciliter la saisie et éviter toute erreur, nous avons faiclité l'entrée utilisateur avec des chiffres plutôt que des chaînes de caractères.


Mode éducatif
--------------

Dans le mode éducatif, l'utilisateur peut saisir la météo qu'il veux afficher, parmis un choix de 10 phénomènes métérologiques et 6 métriques

.. code-block:: python

    if mode == "1":
        choix_meteo = input("Veuillez choisir un phénomène météorologique entre: temperature, PA (pression), insolation, vitesse (du vent), humidite (de l'air), precipitations(hauteur des pluies), soleil, pluie, couvert, orage, nuageux, innondation, tornade, ouragan, sécheresse, tempête: ")
        text_defile.texte_afficher('modeeducatif.txt', (255, 0, 0))
        meteo.Affiche_Meteo(choix_meteo)

Si l'utilisateur tape '1', le mode éducatif s'affiche. Pour prévenir l'utiliateur, un message défile d'abord: "*Mode: éducatif*". L'utilisateur peut ensuite choisir le phénomène qu'il souhaite voir s'afficher.

Mode alerte
------------

Lorsque le mode alerte est choisi, un message d'alerte défile alors sur la matrice. Puis un phénomène est ensuite affiché sur l'écran.
Ce phénomène est généré par hasard grâce à genDanger.py, qui génère un ficher generete_danger.txt. Dans ce fichier un phénomène métérologique choisi au hasard par l'ordinateur y est inscrit.

.. code-block:: python
    
    elif mode.lower() == "alerte":
        text_defile.texte_afficher('danger.txt', (255, 0, 0))
        file = open('generate_danger.txt', 'r')
        for line in file:
            line = line.rstrip("\n")
            meteo.Affiche_Meteo(line)
            file.close()



Mode fenêtre
------------
Si l'utilisateur entre '2', le mode fenêtre s'affiche alors. Ce mode permet à l'utilisateur de consulter la météo en métropole.
Lors du choix de ce mode, un message s'affiche pour notifier l'utilisateur du mode choisi: "*Mode: Fenêtre*". Le texte à afficher provient du document *modefenetre.txt*
Le phénomène affiché pour indiquer la météo en métropole est définit de manière aléatoire grâce à generate.py, qui 
crée un fichier data.txt avec un phénomène inscrit.

.. code-block:: python

     elif mode == "2":
        text_defile.texte_afficher('modefenetre.txt', (255, 0, 0))
        print("En métropole, voici la météo: ")
        file = open('data.txt', 'r')
        for line in file:
            line = line.rstrip("\n")
            meteo.Affiche_Meteo(line)

Quitter
---------
Pour quitter le menu, il suffit simplement à l'utilisateur de rentrer "0", ce qui met fin à la boucle.








