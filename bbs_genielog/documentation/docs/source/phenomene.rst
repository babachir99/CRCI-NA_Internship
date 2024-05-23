Phénomènes métérologiques
===========================

Cette page retrace 10 phénomènes métérologiques. Les fonctions présentées dans la section ci-dessous premettent 
d'afficher un phénomène sur une matrice 16x16.

Soleil
-------
Le soleil a pointé le bout de son nez ? Grâce à la fonction soleil(), il est possible d'afficher dans la matrice 
un soleil, bien jaune et brillant. 

Voilà comment il se présente 

.. code-block:: python

            soleil = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,f,0,0,0,0,0,0,0,0],
            [0,0,f,0,0,0,0,f,0,0,0,0,f,0,0,0],
            [0,0,0,f,0,0,0,0,0,0,0,f,0,0,0,0],
            [0,0,0,0,0,0,t,t,t,0,0,0,0,0,0,0],
            [0,0,0,0,0,t,t,t,t,t,0,0,0,0,0,0],
            [0,0,0,0,t,t,t,t,t,t,t,0,0,0,0,0],
            [0,f,f,0,t,t,t,t,t,t,t,0,f,f,0,0],
            [0,0,0,0,0,t,t,t,t,t,0,0,0,0,0,0],
            [0,0,0,0,0,0,t,t,t,0,0,0,0,0,0,0],
            [0,0,0,0,f,0,0,0,0,0,f,0,0,0,0,0],
            [0,0,0,f,0,0,0,f,0,0,0,f,0,0,0,0],
            [0,0,0,0,0,0,0,f,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

            soleil2 =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,f,0,0,0,0,0,0,0,0],
            [0,f,0,0,0,0,0,f,0,0,0,0,0,f,0,0],
            [0,0,f,0,0,0,0,0,0,0,0,0,f,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,t,t,t,0,0,0,0,0,0,0],
            [0,0,0,0,0,t,t,t,t,t,0,0,0,0,0,0],
            [0,0,0,0,t,t,t,t,t,t,t,0,0,0,0,0],
            [f,f,0,0,t,t,t,t,t,t,t,0,f,f,0,0],
            [0,0,0,0,0,t,t,t,t,t,0,0,0,0,0,0],
            [0,0,0,0,0,0,t,t,t,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,f,0,0,0,0,0,0,0,f,0,0,0,0],
            [0,0,f,0,0,0,0,f,0,0,0,0,f,0,0,0],
            [0,0,0,0,0,0,0,f,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


Les lettres T et F sont définies dans un autre fichier, test_matrix. Elles permettent d'afficher le soleil aussi lumineux que nous le 
voyons!

Pour alterner entre ces deux matrices, nous avons créé une autre fonction, nbMatrice(), qui va permettre d'associer 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py

.. code-block:: python

    def nbMatrice()
    return 2

Ainsi que la boucle pour qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return soleil
    elif (matrice == 2)
        return soleil2

**Test Unitaire**

Pour assurer le fonctionnement de cette fonction, nous y avons ajouté des test unitaires grâce à doctest:

.. code-block:: python

        #"""
        #>>> soleil()
        #ici on copie la matrice soleil
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
    #if __name__ == "__main__":
    #import doctest
    #doctest.testmod()


Sécheresse
-----------

Cette fonction permet d'afficher à l'écran une alerte sécheresse. On y voit un sol craquelé ainsi que des vagues de chaleur pour l'illustrer.
La particularité de la fonction sécheresse est qu'elle est animée. Cela a été décidé car le pictogramme était difficilement lisible 
sur une matrice 16x16. Pour créer cette effet d'animation, nous avons codé pas une, mais 2 matrices qu'il est possible d'alterner rapidement 
pour donner un effet de mouvement. 

.. code-block:: python

    secheresse = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,f,0,0,0,0,f,0,0,0,f,0,0,0,0],
    [0,0,0,f,0,0,0,0,f,0,0,0,f,0,0,0],
    [0,0,0,0,f,0,0,0,0,f,0,0,0,f,0,0],
    [0,0,0,f,0,0,0,0,f,0,0,0,f,0,0,0],
    [0,0,f,0,0,0,0,f,0,0,0,f,0,0,0,0],
    [0,0,0,f,0,0,0,0,f,0,0,0,f,0,0,0],
    [0,0,0,0,f,0,0,0,0,f,0,0,0,f,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [t,t,t,t,t,t,t,t,0,t,0,t,t,t,t,t],
    [t,0,0,0,0,t,0,0,t,0,0,t,0,0,t,0],
    [0,t,0,0,t,0,0,0,0,t,t,0,0,t,0,0],
    [t,0,0,t,0,0,0,0,0,t,0,0,0,0,t,0],
    [0,0,0,t,0,0,0,0,t,0,0,0,0,0,0,t]]

    secheresse2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,f,0,0,0,f,0,0,0,0,f,0,0],
    [0,0,0,f,0,0,0,f,0,0,0,0,f,0,0,0],
    [0,0,0,0,f,0,0,0,f,0,0,0,0,f,0,0],
    [0,0,0,f,0,0,0,f,0,0,0,0,f,0,0,0],
    [0,0,0,0,f,0,0,0,f,0,0,0,0,f,0,0],
    [0,0,0,f,0,0,0,f,0,0,0,0,f,0,0,0],
    [0,0,0,0,f,0,0,0,f,0,0,0,0,f,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [t,t,t,t,t,t,t,t,0,t,0,t,t,t,t,t],
    [t,0,0,0,0,t,0,0,t,0,0,t,0,0,t,0],
    [0,t,0,0,t,0,0,0,0,t,t,0,0,t,0,0],
    [t,0,0,t,0,0,0,0,0,t,0,0,0,0,t,0],
    [0,0,0,t,0,0,0,0,t,0,0,0,0,0,0,t]]


Pour alterner entre ces deux matrices, nous avons créé une autre fonction, nbMatrice, qui va permettre d'associer 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py

.. code-block:: python

    def nbMatrice()
    return 2

Ainsi que la boucle pour qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return secheresse
    elif (matrice == 2)
        return secheresse2


**Test unitaire**

Pour assurer le fonctionnement de cette fonction, nous y avons ajouté des test unitaires grâce à doctest:

.. code-block:: python

    #"""
    #>>> secheresse(1)
    #on copie la matrice secheresse(1) ici
    #"""

Puis on importe doctest() et on teste.

.. code-block:: python

    #if __name__ == "__main__":
    #import doctest
    #doctest.testmod()

Tempête
--------

Pour la fonction tempête, c'est un nuage foncé qui s'affiche, ainsi que des éclairs et de la pluie. Pour ce faire, voici la matrice correspondante:

.. code-block:: python

    tempete = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #ligne 1
    [0,0,0,0,0,0,0,0,0,g,g,g,0,0,0,0], #ligne 2
    [0,0,0,g,g,g,g,0,g,g,g,g,g,0,0,0], #ligne 3
    [0,0,g,g,g,g,g,g,g,g,g,g,g,g,0,0], #ligne 4
    [0,g,g,g,g,g,g,g,g,g,g,g,g,g,g,0], #ligne 5
    [0,g,g,g,g,g,g,g,g,g,g,g,g,g,g,0], #ligne 6
    [0,0,g,g,g,g,g,g,g,g,g,g,g,g,0,0], #ligne 7
    [0,0,0,g,g,g,g,g,g,g,g,g,g,0,0,0], #ligne 8
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #ligne 9
    [0,b,0,b,0,0,j,0,b,0,j,0,b,0,b,0], #ligne 10
    [0,0,0,0,0,j,0,0,0,j,0,0,0,0,0,0], #ligne 11
    [0,b,0,0,j,j,j,0,j,j,j,0,0,0,0,0], #ligne 12
    [0,0,0,b,0,j,0,b,0,j,0,0,b,0,0,0], #ligne 13
    [0,0,0,0,j,0,0,0,j,0,0,0,0,0,b,0], #ligne 14
    [0,b,0,0,0,0,0,0,0,0,0,b,0,0,0,0], #ligne 15
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] #ligne 16

**Tets Unitaires**

Voici le test réalisé pour vérifier le bon fonctionnement: 

.. code-block:: python

    #"""
    #>>> tempete()
    #on copie la matrice tempête
    #"""

Puis on importe doctest et on vérifie: 

.. code-block:: python
    
    #if __name__ == "__main__":
    #import doctest
    #doctest.testmod()


Pluie
-------

Voici comment nous avons décidé de représenter la pluie:

.. code-block:: python

    pluie =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,f,f,f,f,f,0,0,0,0],
    [0,0,0,0,0,f,f,f,0,0,0,0,f,0,0,0],
    [0,0,0,0,0,f,0,0,0,0,0,0,0,f,0,0],
    [0,0,0,f,f,0,0,0,0,0,0,0,f,f,0,0],
    [0,0,0,f,0,0,0,0,0,0,0,0,0,0,f,0],
    [0,0,0,f,f,f,f,f,0,0,f,f,f,f,f,0],
    [0,0,0,0,0,0,0,f,f,f,f,0,0,0,0,0],
    [0,0,0,0,0,t,0,t,0,t,0,t,t,0,0,0],
    [0,0,0,0,t,0,t,0,t,0,t,0,t,0,t,0],
    [0,0,0,0,0,t,0,t,0,t,0,t,0,t,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    pluie2 =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,f,f,f,f,f,0,0,0,0],
    [0,0,0,0,0,f,f,f,0,0,0,0,f,0,0,0],
    [0,0,0,0,0,f,0,0,0,0,0,0,0,f,0,0],
    [0,0,0,f,f,0,0,0,0,0,0,0,f,f,0,0],
    [0,0,0,f,0,0,0,0,0,0,0,0,0,0,f,0],
    [0,0,0,f,f,f,f,f,0,0,f,f,f,f,f,0],
    [0,0,0,0,0,0,0,f,f,f,f,0,0,0,0,0],
    [0,t,0,t,0,t,0,t,0,t,0,t,t,0,t,0],
    [t,0,t,0,t,0,t,0,t,0,t,0,t,0,t,0],
    [0,t,0,t,0,t,0,t,0,t,0,t,0,t,0,t],
    [t,0,t,0,0,t,0,0,t,0,0,t,0,0,t,0],
    [ 0,t,0,t,0,t,0,t,0,t,0,t,0,t,0,0]]


Les lettres t (bleu) et f(gris) sont définies dans un autre fichier, test_matrix. Elles permettent de colorer l'image et d'avoir une jolie pluie.
La pluie est également animée grâce à la fonction nbMatrice(). Pour alterner entre ces deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle  qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return pluie
    elif (matrice == 2)
        return pluie2
 
**Test Unitaire**

Pour assurer le fonctionnement de la fonction pluie, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> pluie()
        #ici on copie la matrice pluie
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
    #if __name__ == "__main__":
    #import doctest
    #doctest.testmod()


Innondation
--------------

Voici comment nous avons décidé de représenter le phénomène d'innondation sur la matrice:

.. code-block:: python

    innondation =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,f,f,f,0,0,0,0,0,f,f,f,0,0],
    [0,0,f,g,g,0,f,f,0,0,f,0,g,g,f,0],
    [0,f,g,g,g,g,g,g,f,f,g,g,g,g,g,f],
    [f,g,g,g,0,0,g,g,0,g,g,0,0,0,g,g],
    [g,g,0,0,f,f,0,g,g,g,0,f,f,f,f,0],
    [g,0,0,f,g,g,f,f,0,0,f,0,g,g,g,f],
    [0,0,f,g,g,g,g,g,f,f,g,g,g,0,g,g],
    [f,f,g,g,0,0,0,g,g,g,g,0,0,0,0,g],
    [g,g,0,f,f,f,0,0,g,0,0,f,f,f,0,0],
    [g,0,f,g,g,g,f,0,0,0,f,g,g,g,f,0],
    [0,f,g,g,0,g,g,f,f,f,g,g,g,g,g,f],
    [f,g,g,f,f,f,g,g,g,g,g,f,f,g,g,0],
    [g,g,f,0,0,0,f,g,g,f,f,0,0,f,g,g],
    [f,f,0,0,0,0,0,f,f,0,0,0,0,0,f,f]]

.. code-block:: python

    innondation2 =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,g,g,0,0,0,0,0,0,0,g,g,g,0],
    [0,0,g,g,g,g,g,g,0,0,g,g,g,g,g,g],
    [g,g,g,g,0,0,g,g,0,g,g,0,0,0,g,g],
    [0,0,f,f,f,f,0,g,g,g,0,f,f,f,f,0],
    [f,f,0,g,g,g,f,f,0,0,f,0,g,g,g,f],
    [g,g,g,g,g,g,g,g,f,f,g,g,g,0,g,g],
    [g,g,g,g,0,0,0,g,g,g,g,0,0,0,0,g],
    [f,f,f,f,f,f,0,0,g,0,0,f,f,f,0,0],
    [g,g,g,g,g,g,f,0,0,0,f,g,g,g,f,0],
    [g,g,g,g,0,g,g,f,f,f,g,g,g,g,g,f],
    [f,f,f,f,f,f,g,g,g,g,g,f,f,g,g,0],
    [0,0,0,0,0,0,f,g,g,f,f,0,0,f,g,g],
    [0,0,0,0,0,0,0,f,f,0,0,0,0,0,f,f]]


Les lettres f (blanc) et g(bleu) sont définies dans un autre fichier, test_matrix. Elles permettent d'avoir une image colorée.
Le phénomène d'innondation est également animée grâce à la fonction nbMatrice(). Pour alterner entre ces deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return innondation
    elif (matrice == 2)
        return innondation2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> innondation()
        #ici on copie la matrice innondation
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
    #if __name__ == "__main__":
    #import doctest
    #doctest.testmod()


Nuageux 
---------

Voici comment nous avons représenté le phénomène "nuageux" sur la matrice:

.. code-block:: python

    nageux =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,t,t,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,t,t,t,t,0], 
    [0,0,0,0,g,g,0,0,0,0,0,t,t,t,t,0], 
    [0,0,0,g,g,g,g,0,0,0,0,0,t,t,0,0],  
    [0,0,g,g,g,g,g,g,0,g,g,g,0,0,0,0], 
    [0,g,g,g,g,g,g,g,g,g,g,g,g,0,0,0], 
    [0,g,g,g,g,g,g,g,g,g,g,g,g,0,0,0], 
    [0,0,g,g,g,g,g,g,g,g,g,g,0,0,0,0], 
    [0,0,0,g,g,g,g,g,g,g,g,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    nuageux2 = [[0,t,t,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [t,t,t,t,0,0,0,0,0,0,0,0,0,0,0,0], 
    [t,t,t,t,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,t,t,0,g,g,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,g,g,g,g,0,0,0,0,0,0,0,0,0],  
    [0,0,g,g,g,g,g,g,0,g,g,g,0,0,0,0], 
    [0,g,g,g,g,g,g,g,g,g,g,g,g,0,0,0], 
    [0,g,g,g,g,g,g,g,g,g,g,g,g,0,0,0], 
    [0,0,g,g,g,g,g,g,g,g,g,g,0,0,0,0], 
    [0,0,0,g,g,g,g,g,g,g,g,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



Les lettres g (gris) et t(jaune) sont définies dans un autre fichier, test_matrix. Elles permettent de projetter une image colorée sur la matrice.
Le phénomène "nuageux" est également animée grâce à la fonction nbMatrice(). Pour alterner entre  deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return nuageux
    elif (matrice == 2)
        return nuageux2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> nuageux()
        #ici on copie la matrice nuageux
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
        #if __name__ == "__main__":
        #import doctest
        #doctest.testmod()


Couvert 
---------

Voici comment nous avons représenté le phénomène "couvert" *(le soleil n'est pas visible)* sur la matrice:

.. code-block:: python

    couvert =    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, 0, 0, 0, 0],
                [0, 0, 0, 0, a, a, a, 0, a, a, a, a, a, 0, 0, 0],
                [0, a, a, a, a, a, a, a, a, a, a, a, a, 0, 0, 0],
                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0],
                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0],
                [0, a, a, a, a, a, a, a, a, a, a, a, a, a, 0, 0],
                [0, 0, 0, a, a, a, a, a, a, a, a, a, a, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    
    couvert_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, 0, 0, 0],
                [0, 0, 0, 0, 0, a, a, a, 0, a, a, a, a, a, 0, 0],
                [0, 0, 0, a, a, a, a, a, a, a, a, a, a, a, 0, 0],
                [0, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
                [0, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
                [0, 0, 0, a, a, a, a, a, a, a, a, a, a, a, a, 0],
                [0, 0, 0, 0, a, a, a, a, a, a, a, a, a, a, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]



La lettre a (gris) est définie dans un autre fichier, test_matrix. Elle permet de projetter une image colorée sur la matrice.
Le phénomène "couvert" est également animée grâce à la fonction nbMatrice(). Pour alterner entre  deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return couvert
    elif (matrice == 2)
        return couvert2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> couvert()
        #ici on copie la matrice couvert
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
        #if __name__ == "__main__":
        #import doctest
        #doctest.testmod()




Orage 
---------

Voici comment nous avons représenté l'orage sur la matrice:

.. code-block:: python

    orage = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, 0, 0, 0, 0],
        [0, 0, 0, 0, a, a, a, 0, a, a, a, a, a, 0, 0, 0],
        [0, 0, a, a, a, a, a, a, a, a, a, a, a, 0, 0, 0],
        [0, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0],
        [0, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0],
        [0, 0, a, a, a, a, a, a, a, a, a, a, a, a, 0, 0],
        [0, 0, 0, a, a, a, a, a, a, a, a, a, a, 0, 0, 0],
        [0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0, 0],
        [0, 0, 0, b, 0, 0, b, 0, 0, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0, 0],
        [0, 0, 0, b, 0, 0, b, 0, 0, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, b, 0, 0, 0, 0, b, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, b, 0, 0, 0, 0, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    orage2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, 0, 0, 0],
        [0, 0, 0, 0, 0, a, a, a, 0, a, a, a, a, a, 0, 0],
        [0, 0, 0, a, a, a, a, a, a, a, a, a, a, a, 0, 0],
        [0, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
        [0, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
        [0, 0, 0, a, a, a, a, a, a, a, a, a, a, a, a, 0],
        [0, 0, 0, 0, a, a, a, a, a, a, a, a, a, a, 0, 0],
        [0, 0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0],
        [0, 0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, b, 0, 0, b, 0, 0, b, 0, 0, 0, 0],
        [0, 0, 0, 0, b, 0, 0, b, 0, 0, 0, 0, b, 0, 0, 0],
        [0, 0, 0, b, 0, 0, b, 0, 0, 0, 0, 0, 0, b, 0, 0]]



Les lettres a (gris) et b (jaune) sont définies dans un autre fichier, test_matrix. Elles permettent de projetter une image colorée sur la matrice.
Le phénomène "orage" est également animé grâce à la fonction nbMatrice(). Pour alterner entre  deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return orage
    elif (matrice == 2)
        return orage2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> orage()
        #ici on copie la matrice orage
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
        #if __name__ == "__main__":
        #import doctest
        #doctest.testmod()


Tornade 
---------

Voici comment nous avons représenté le phénomène "nuageux" sur la matrice:

.. code-block:: python

    tornade = [[0, 0, 0, g, b, b, g, g, g, g, g, b, b, g, 0, 0],
            [0, 0, g, b, b, g, b, b, b, b, b, g, b, b, g, 0],
            [0, 0, g, b, b, g, g, g, g, g, g, g, b, b, g, 0],
            [0, 0, g, g, b, b, b, b, b, b, b, b, g, g, 0, 0],
            [0, 0, g, b, g, g, g, g, g, g, g, g, b, g, 0, 0],
            [0, 0, g, b, b, b, b, b, b, b, b, b, b, g, 0, 0],
            [0, 0, 0, g, b, g, g, g, b, b, b, b, b, g, 0, 0],
            [0, 0, 0, g, b, b, b, b, b, b, b, b, g, 0, 0, 0],
            [0, 0, 0, 0, g, b, b, b, g, g, g, b, g, 0, 0, 0],
            [0, 0, 0, 0, 0, g, b, b, b, b, b, g, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, g, b, b, b, g, g, g, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, g, b, b, b, b, g, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, g, g, g, b, b, g, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, g, g, g, g, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

   tornade2 = [
        [0, 0, 0, g, b, b, g, g, g, g, g, b, b, g, g, 0],
        [0, 0, g, b, b, g, b, b, b, b, b, g, b, b, g, 0],
        [0, 0, g, b, b, g, g, g, g, g, g, g, b, b, g, 0],
        [0, 0, g, g, b, b, b, b, b, b, b, b, g, g, 0, 0],
        [0, 0, g, b, g, g, g, g, g, g, g, g, b, g, 0, 0],
        [0, 0, 0, b, b, b, b, b, b, b, b, b, b, g, 0, 0],
        [0, 0, 0, g, b, g, g, g, b, b, b, b, b, g, 0, 0],
        [0, 0, 0, 0, b, b, b, b, b, b, b, b, g, 0, 0, 0],
        [0, 0, 0, 0, b, b, b, g, g, g, b, g, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, b, b, b, b, g, g, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, b, b, g, g, g, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, b, b, b, b, g, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, g, g, b, b, g, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, g, g, g, g, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, g, g, g, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, g, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


Les lettres g (gris fonce) et b(gris clair) sont définies dans un autre fichier, test_matrix. Elles permettent de projetter une image colorée sur la matrice.
La tornade est également animée grâce à la fonction nbMatrice(). Pour alterner entre  deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return tornade
    elif (matrice == 2)
        return tornade 2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> tornade()
        #ici on copie la matrice tornade
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
        #if __name__ == "__main__":
        #import doctest
        #doctest.testmod()



Ouragan 
---------

Voici comment nous avons représenté un ouragan sur la matrice:

.. code-block:: python

    ouragan = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, b, b, b, 0, 0, 0, 0],
        [0, 0, 0, 0, b, b, b, 0, b, b, b, b, b, 0, 0, 0],
        [0, 0, b, b, b, b, b, b, b, b, b, b, b, b, 0, 0],
        [0, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 0],
        [0, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 0],
        [0, 0, b, b, b, n, n, n, b, b, b, b, b, b, 0, 0],
        [0, 0, 0, 0, n, 0, 0, n, n, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, n, n, 0, n, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, n, n, 0, 0, n, n, 0, 0, 0],
        [0, 0, n, n, n, n, n, 0, 0, n, n, 0, n, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    ouragan2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, b, b, b, 0, 0, 0, 0],
        [0, 0, 0, 0, b, b, b, 0, b, b, b, b, b, 0, 0, 0],
        [0, 0, b, b, b, b, b, b, b, b, b, b, b, b, 0, 0],
        [0, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 0],
        [0, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 0],
        [0, 0, b, b, b, b, n, n, n, b, b, b, b, b, 0, 0],
        [0, 0, 0, 0, 0, n, 0, n, n, n, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, n, n, 0, 0, n, n, 0, 0],
        [0, 0, 0, n, n, n, n, n, 0, 0, n, n, 0, n, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


Les lettres  sont définies dans un autre fichier, test_matrix. Elles permettent de projetter une image colorée sur la matrice.
L'ouragan est également animée grâce à la fonction nbMatrice(). Pour alterner entre  deux matrices, nbMatrice()  associe 
à une matrice un nombre, facilitant l'alternance entre les 2 dans la fonction main.py:

.. code-block:: python

    def nbMatrice()
    return 2

On crée ensuite une boucle qui attribue à chaque matrice un nombre permettant l'alternance dans la fonction principale: 

.. code-block:: python

    if (matrice == 1)
        return ouragan
    elif (matrice == 2)
        return ouragan2
 
**Test Unitaire**

Pour assurer le fonctionnement de notre fonction, nous y avons ajouté un test unitaire grâce à doctest:

.. code-block:: python

        #"""
        #>>> ouragan()
        #ici on copie la matrice ouragan
        #"""

A la fin de la fonction, il est nécéssaire d'importer doctest() pour pouvoir tester la fonction:

.. code-block:: python
    
        #if __name__ == "__main__":
        #import doctest
        #doctest.testmod()