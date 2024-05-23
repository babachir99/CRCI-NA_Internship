"""
BA Mohamed
fonction matricielle orage

Ce script définit une fonction qui affiche un motif représentant un orage sur un Unicorn HAT HD 
en utilisant la bibliothèque unicorn_hat_sim.

"""

def nbMatrice():
    return 2

def orage(matrice):
    
    """
    >>> orage(1)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 0, 0, 0, 0], [0, 0, 0, 0, 11, 11, 11, 0, 11, 11, 11, 11, 11, 0, 0, 0], [0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0, 0], [0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0], [0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0], [0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0], [0, 0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0, 0], [0, 0, 0, 0, 17, 0, 0, 17, 0, 0, 17, 0, 0, 0, 0, 0], [0, 0, 0, 17, 0, 0, 17, 0, 0, 0, 0, 17, 0, 0, 0, 0], [0, 0, 0, 0, 17, 0, 0, 17, 0, 0, 17, 0, 0, 0, 0, 0], [0, 0, 0, 17, 0, 0, 17, 0, 0, 0, 0, 17, 0, 0, 0, 0], [0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0], [0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """

    # Définir les couleurs par défaut (a et b)
    a = 11
    b = 17

    # Définir le motif 'orage' comme un tableau 2D de 16x16
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
        [0, 0, 0, b, 0, 0, b, 0, 0, 0, 0, 0, 0, b, 0, 0]
    ]

    if (matrice == 1):
        return orage
    elif (matrice == 2):
        return orage2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

