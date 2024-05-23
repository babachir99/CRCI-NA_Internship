Affichage
=============

Pour pouvoir afficher nos matrices, il a fallu créer la fonction execute().
Cette fonction a pour argument : "meteo", ainsi que t.
meteo va permettre le choix des couleurs dans les matrices car chaque phénomène a ses propres couleurs (un soleil bleu aurait pu être très beau, mais 
peu réaliste).

**Couleur**

Les premières boucles permettent d'attribuer à chaque couleur un numéro pour que ces couleurs puissent être correctement prises en compte lors de l'affichage de la matrice.

Par exemple pour une des nuances de jaune choisie, on aura: 

.. code-block:: python

    for x in range(16):
        for y in range(16):
            if meteo [y][x] == 0:
                r,g,b = (255, 255, 0)

                
Ensuite, grâce à l'argument t, nous pourrons afficher le phénomène t secondes:

.. code-block:: python 

    unicornhathd.set_pixel(x,y,r,g,b)  
    unicornhathd.show()                             
    time.sleep(t)

 
