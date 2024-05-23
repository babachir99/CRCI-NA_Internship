Défilement
===========

Cette section vous présente comment faire défiler un texte sur la matrice. C'est une fonctiontrès utilisée, que ce soit pour afficher 
le mode choisit par l'utilisateur, un phénomène métérologique ou bien pour prévenir d'un danger.
Voici les bibliothèques à importer: 

.. code-block:: python

    import time
    from sys import exit
    from unicorn_hat_sim import unicornhathd

Nous définissons ensuite la fonction ainsi que les arguments qu'elle prend: 

.. code-block:: python

    def texte_afficher(fichier,couleur = (255,0,0)):

Ici le premier argument est un fichier, car comme indiqué précedemment, nous voulons que cette fonction puisse servire pour plusieurs documents. 
Le deuxième argument est la couleur. 

Ainsi, voici les lignes qui permettent de choisir le fichier à afficher:

.. code-block:: python

    with open(fichier) as f:
        TEXT = f.read()
    f.close()

Nous avons ensuite paramétré l'affichage: 

.. code-block:: python

    width, height = unicornhathd.get_shape()
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.5)

Voici les valeurs utilisées pour que le texte s'affiche, et se déplace d'une position vers la gauche (1 pixel) et de deux positions vers le bas (2 pixels) par rapport au coin supérieur gauche de la matrice.

.. code-block:: python

    text_x = 1
    text_y = 2

Pour modifier la taille du texte:

.. code-block:: python

    l, t, r, b = font.getbbox(TEXT)

    text_width = int(font.getlength(TEXT))

    text_height = b - t

Nous créons ensuite un "canva" pour pouvoir afficher notre texte. Puis on utilise ImageDraw de PIL.

.. code-block:: python

    image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), TEXT, fill=(255, 0, 0), font=font)


Pour que l'image défile, nous créons une boucle:
Scroll définit la distance vers laquelle on se déplace vers la gauche.
Ensuite, il faut convertir les couleurs en un code r, g, b


.. code-block:: python

    for scroll in range(text_width - width):
        for x in range(width):
            hue = (x + scroll) / float(text_width)
            br, bg, bb = couleur


Pour les couleurs

.. code-block:: python

    for y in range(height):
        pixel = image.getpixel((x + scroll, y))
        r, g, b = [float(n / 255.0) for n in pixel]
        r = int(br * r)
        g = int(bg * g)
        b = int(bb * b)


Pour afficher sur la matrice: 

.. code-block:: python
    
    unicornhathd.set_pixel(width - 1 - x, y, r, g, b)
    unicornhathd.show()


Pour modifier le temps de défilement: 

.. code-block:: python

        time.sleep(0.05)





