Métriques
=========

En plus des phénomènes métérologiques, nous avons fourni des informations primordiales pour
annoncer la météo: la température, la pression atmosphérique, l'insolation, une indication sur
la hauteur des pluies, l'humidité de l'air ainsi que la vitesse du vent. 

Température
-------------

.. code-block:: python

    (meteo=="temperature"):
            nbMatrice = temperature.nbMatrice()
            for i in range (5): #l'animation va tourner 5 fois
                for j in range (1, nbMatrice+1):
                    test_matrix.execute(temperature.temperature(j),0.5)
                    if (i == 1):
                        if (j==1): #permet d'afficher la meteo
                            print(meteo)
            text_defile.texte_afficher('temperature.txt', (255, 0, 0))

Pour afficher la température, tout d'abord, une petite animation apparaît: 
un thermomètre. Ensuite, nous utilisons le fichier *temperature.txt* qui est simplement un texte, généré grâce à
*generate_temperature*. Dans ce texte, l'ordinateur génère aléatoirement une température comprise entre -10 et 40° 
et la fait défiler à l'écran grâce à texte_afficher().

Pression Atmosphérique
-----------------------

.. code-block:: python

    elif (meteo=="PA"):
        text_defile.texte_afficher('PA.txt', (255, 0, 0))

De même pour la pression atmosphérique, nous utilisons un fichier texte généré automatiquement, ou une valeur réaliste de 
pression atmosphérique y est générée aléatoirement. Cette valeur défile alors grâce à la fonction texte_afficher.



Insolation
-------------

.. code-block:: python

    elif (meteo=="insolation"):
        nbMatrice = Insolation.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Insolation.insolation(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
        text_defile.texte_afficher('insolation.txt', (255, 0, 0))

Pour afficher l'insolation, tout d'abord, une petite animation apparaît: 
un soleil. Ensuite, nous utilisons le fichier *insolation.txt* qui est simplement un texte, généré automatiquement grâce à
*generate_insolation*. On le fait défiler à l'écran grâce à la fonction définie dans text_defile.


Précipitation
-------------

.. code-block:: python

    elif (meteo=="precipitation"):
            text_defile.texte_afficher('precipitation.txt', (255, 0, 0))

Pour la hauteur des pluies, nous utilisons un fichier texte généré automatiquement par generate_hauteur, ou une valeur réaliste de 
précipitation en mm est choisi aléatoirement. Cette valeur défile avec une catégorie qui permet de qualifier si les pluies ont été fortes ou non.


Vitesse du Vent
----------------

.. code-block:: python

    elif (meteo=="vitesse"):
        nbMatrice = vitesse.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(vitesse.vitesse(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
        text_defile.texte_afficher('vitesse_vent.txt', (255, 0, 0))

Pour afficher la vitesse du vent, une petite animation apparaît d'abord. Ensuite, 
nous utilisons le fichier *vitesse_vent.txt* qui est simplement un texte, généré automatiquement grâce à
*generate_vv*. Dans ce texte, l'ordinateur génère aléatoirement une vitesse de vent. On la fait alors défiler 
à l'écran grâce à texte_afficher défini dans le fichier text_defile. 

Humidité 
--------

  .. code-block:: python

    elif (meteo=="humidite"):
        text_defile.texte_afficher('humidite.txt', (255, 0, 0))

Pour l'humidité de l'air, nous utilisons un fichier texte généré automatiquement, *humidite.txt*, 
ou un pourcentage d'humidité relative s'affiche,  
avec un commentaire pour savoir si l'air est humide ou non. 
Tout cela défile grâce à la fonction texte_afficher() défini dans text_defile