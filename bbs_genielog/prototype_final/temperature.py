# AWA AMAR
# Création de la matrice de taille 16x16 pixels pour la temperature

# Définition fonction qui pour avoir de l'animation, du mouvement 
def nbMatrice():
    return 2

# Définition de la fonction temperature
def temperature(matrice):
    """
    >>> temperature(1)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 8, 2, 2, 2, 2, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 8, 2, 2, 2, 2, 2, 2, 8, 0, 0, 0, 0, 0], [0, 0, 0, 8, 2, 2, 2, 2, 2, 2, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    
    # modification des couleurs (détails dans test-matrix)
    b = 8
    l = 2
    r = 4

    # matrice pluie
    temperature = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,b,b,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,0,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,0,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,b,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,0,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,b,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,0,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,b,l,l,l,l,b,0,0,0,0,0,0],
        [0,0,0,b,l,l,l,l,l,l,b,0,0,0,0,0],
        [0,0,0,b,l,l,l,l,l,l,b,0,0,0,0,0],
        [0,0,0,0,b,b,b,b,b,b,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

    # ajout d'une deuxième matrice pour ajouter de l'animation en déplaçant les symboles "t" et "f".
    temperature2 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,b,b,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,0,0,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,r,r,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,b,r,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,r,r,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,b,r,b,0,0,0,0,0,0,0],
        [0,0,0,0,0,b,r,r,b,0,0,0,0,0,0,0],
        [0,0,0,0,b,r,r,r,r,b,0,0,0,0,0,0],
        [0,0,0,b,r,r,r,r,r,r,b,0,0,0,0,0],
        [0,0,0,b,r,r,r,r,r,r,b,0,0,0,0,0],
        [0,0,0,0,b,b,b,b,b,b,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

    if matrice == 1:
        return temperature
    elif matrice == 2:
        return temperature2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
