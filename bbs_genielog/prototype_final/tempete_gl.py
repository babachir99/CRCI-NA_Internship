#coding utf8
#Mélissa MENGA
#Création d'une matrice 16x16 pour afficher une alerte météo concernant une temmpete

# definition de la fonction nbMatrice pour ajouter du mouvement (amelioration à venir)
def nbMatrice():
    return 2

def tempete(matrice):

    """
    >>> tempete(1)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 0, 0], [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0], [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0], [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """

    #modification des couleurs (detail dans test_matrix.py)
    j = 1
    b = 2
    g = 3
    
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
    
    tempete2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #ligne 1
            [0,0,0,0,0,0,0,0,0,g,g,g,0,0,0,0], #ligne 2
            [0,0,0,g,g,g,g,0,g,g,g,g,g,0,0,0], #ligne 3
            [0,0,g,g,g,g,g,g,g,g,g,g,g,g,0,0], #ligne 4
            [0,g,g,g,g,g,g,g,g,g,g,g,g,g,g,0], #ligne 5
            [0,g,g,g,g,g,g,g,g,g,g,g,g,g,g,0], #ligne 6
            [0,0,g,g,g,g,g,g,g,g,g,g,g,g,0,0], #ligne 7
            [0,0,0,g,g,g,g,g,g,g,g,g,g,0,0,0], #ligne 8
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #ligne 9
            [0,b,0,b,0,0,b,0,b,0,b,0,b,0,b,0], #ligne 10
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #ligne 11
            [0,0,0,0,0,b,0,0,b,0,b,0,0,b,0,0], #ligne 12
            [0,0,0,b,0,0,0,b,0,0,0,0,b,0,0,0], #ligne 13
            [0,0,0,0,0,b,0,0,0,b,0,0,0,0,b,0], #ligne 14
            [0,b,0,0,0,0,0,b,0,0,0,b,0,0,0,0], #ligne 15
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] #ligne 16
    
    if (matrice == 1):
        return tempete
    elif (matrice == 2):
        return tempete2

if __name__ == "__main__":
    import doctest
    doctest.testmod()