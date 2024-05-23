Phénomènes illustrés
==========================


Dans cette partie de la documentation, vous retrouverez une illustration des matrices précédemment décrites dans **phénomènes métérologiques**

Tempête
-------


.. code-block:: python

    if (meteo=="tempete"):
            nbMatrice = tempete_gl.nbMatrice()
            for i in range (5): #l'animation va tourner 5 fois
                for j in range (1, nbMatrice+1):
                    test_matrix.execute(tempete_gl.tempete(j),0.5)
                    if (i == 1):
                        if (j==1): #permet d'afficher la meteo
                            print(meteo) 

Ici, c'est la tempête qui s'affiche, avec 2 boucles for: l'une pour définir la durée, l'autre pour alterner et donner l'effet d'animation.
Voici une des images obtenues finalement: 

.. figure:: ./tempete.png
    :alt: sortie si meteo=tempete
    :figclass: Tempete:
    :width: 300px
    :height: 300px
    :align: center

Sécheresse
----------

.. code-block:: python

    elif (meteo=="secheresse"):
        nbMatrice = secheresse_gl.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(secheresse_gl.secheresse(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Ici, c'est la sécheresse qui s'affiche, avec 2 boucles for: l'une pour définir la durée, l'autre pour alterner et donner l'effet d'animation.
Voici une des images en sortie: 

.. figure:: ./secheresse.png
    :alt: sortie si meteo=secheresse
    :figclass: Secheresse:
    :width: 300px
    :height: 300px
    :align: center

Soleil
------

.. code-block:: python

    elif (meteo=="soleil"):
        nbMatrice = soleil.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(soleil.soleil(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Grâce à cette partie de meteo.py, voilà ce que nous avons en sortie: 

.. figure:: ./soleil.png
    :alt: sortie si meteo=soleil
    :figclass: Soleil:
    :width: 300px
    :height: 300px
    :align: center

Inondation
----------

Voici la partie de la boucle qui permet d'afficher le phénomène d'inondation: 

.. code-block:: python

    elif (meteo=="innondation"):
        nbMatrice = Innondation.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Innondation.innondation(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./innondation.png
    :alt: sortie si meteo=innondation
    :figclass: Innondation:
    :width: 300px
    :height: 300px
    :align: center


Pluie
-----
Pour pouvoir afficher la pluie:

.. code-block:: python

    elif (meteo=="pluie"):
        nbMatrice = pluie.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(pluie.pluie(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./pluie.png
    :alt: sortie si meteo=secheresse
    :figclass: Secheresse:
    :width: 300px
    :height: 300px
    :align: center

Nuageux
-------

Pour pouvoir afficher un temps nuageux:

.. code-block:: python

    elif (meteo=="nuageux"):
        nbMatrice = nuageux.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(nuageux.nuageux(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./nuageux.png
    :alt: sortie si meteo=nuageux
    :figclass: Nuageux:
    :width: 300px
    :height: 300px
    :align: center


Couvert
-------

Pour pouvoir afficher un temps couvert:

.. code-block:: python

    elif (meteo=="couvert"):
        nbMatrice = couvert.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(couvert.couvert(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./couvert.png
    :alt: sortie si meteo=Couvert
    :figclass: Couvert:
    :width: 300px
    :height: 300px
    :align: center


Orage
-----

Pour pouvoir afficher un temps Couvert:

.. code-block:: python

    elif (meteo=="orage"):
        nbMatrice = couvert.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(orage.orage(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./orage.png
    :alt: sortie si meteo=Couvert
    :figclass: Couvert:
    :width: 300px
    :height: 300px
    :align: center



Ouragan
-------

Pour pouvoir afficher l'ouragan :

.. code-block:: python

    elif (meteo=="ouragan"):
        nbMatrice = ouragan.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Ouragan.ouragan(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./ouragan.png
    :alt: sortie si meteo=ouragan
    :figclass: ouragan:
    :width: 300px
    :height: 300px
    :align: center
    

Tornade
-------

Pour pouvoir afficher la tornade :

.. code-block:: python

    elif (meteo=="tornade"):
        nbMatrice = tornade.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Tornade.tornade(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

Voici ce que ce programme nous donne en sortie:

.. figure:: ./tornade.png
    :alt: sortie si meteo=tornade
    :figclass: Couvert:
    :width: 300px
    :height: 300px
    :align: center
    


