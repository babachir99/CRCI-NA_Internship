#NGONE BA 
# Création de la matrice de taille 16x16 pixels pour la tornade 

# définition fonction qui pour avoir de l'animation, du mouvement 
def nbMatrice():
    return 2

def tornade(matrice):
    """
    >>> tornade(1)
    [[0, 0, 0, 13, 12, 12, 13, 13, 13, 13, 13, 12, 12, 13, 0, 0], [0, 0, 13, 12, 12, 13, 12, 12, 12, 12, 12, 13, 12, 12, 13, 0], [0, 0, 13, 12, 12, 13, 13, 13, 13, 13, 13, 13, 12, 12, 13, 0], [0, 0, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 0, 0], [0, 0, 13, 12, 13, 13, 13, 13, 13, 13, 13, 13, 12, 13, 0, 0], [0, 0, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 0, 0], [0, 0, 0, 13, 12, 13, 13, 13, 12, 12, 12, 12, 12, 13, 0, 0], [0, 0, 0, 13, 12, 12, 12, 12, 12, 12, 12, 12, 13, 0, 0, 0], [0, 0, 0, 0, 13, 12, 12, 12, 13, 13, 13, 12, 13, 0, 0, 0], [0, 0, 0, 0, 0, 13, 12, 12, 12, 12, 12, 13, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 13, 12, 12, 12, 13, 13, 13, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 13, 12, 12, 12, 12, 13, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 13, 12, 12, 13, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 13, 13, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """

    # Modification des couleurs, les couleurs associées sont précisées dans test-matrix
    b = 12
    g = 13

    # Matrice tornade
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

    # Ajout d'une deuxième matrice pour ajouter de l'animation en déplaçant les symboles "b" et "g" vers le bas.
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

    if matrice == 1:
        return tornade
    elif matrice == 2:
        return tornade2


if __name__ == "__main__":
    import doctest
    doctest.testmod()