#Ahamed TCHATAKOURA
#Création d'une matrice 16x16 pour afficher une alerte météo concernant un phénomène de innondation

#definition d'une fonction qui va permettre d'alterner entre les 2 images pour créer un effet d'animation.

def nbMatrice():
    return 2

#definition de la fonction innondation. Les nombres sont associés a une couleur, qui est précisée dans test_matrix
def innondation(matrice):
    
    """
    >>> innondation(1)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0], [0, 0, 8, 9, 9, 0, 8, 8, 0, 0, 8, 0, 9, 9, 8, 0], [0, 8, 9, 9, 9, 9, 9, 9, 8, 8, 9, 9, 9, 9, 9, 8], [8, 9, 9, 9, 0, 0, 9, 9, 0, 9, 9, 0, 0, 0, 9, 9], [9, 9, 0, 0, 8, 8, 0, 9, 9, 9, 0, 8, 8, 8, 8, 0], [9, 0, 0, 8, 9, 9, 8, 8, 0, 0, 8, 0, 9, 9, 9, 8], [0, 0, 8, 9, 9, 9, 9, 9, 8, 8, 9, 9, 9, 0, 9, 9], [8, 8, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0, 9], [9, 9, 0, 8, 8, 8, 0, 0, 9, 0, 0, 8, 8, 8, 0, 0], [9, 0, 8, 9, 9, 9, 8, 0, 0, 0, 8, 9, 9, 9, 8, 0], [0, 8, 9, 9, 0, 9, 9, 8, 8, 8, 9, 9, 9, 9, 9, 8], [8, 9, 9, 8, 8, 8, 9, 9, 9, 9, 9, 8, 8, 9, 9, 0], [9, 9, 8, 0, 0, 0, 8, 9, 9, 8, 8, 0, 0, 8, 9, 9], [8, 8, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 8, 8]]
    """
    #modification des couleurs (detail dans test_matrix.py)
    f = 8
    g = 9 

    # Création d'une matrice qui affiche le pictogramme innondation

    innondation = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
    
    #ajout d'une deuxième matrice pour ajouter du mouvement
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
    
    
    if (matrice == 1):
        return innondation
    elif (matrice == 2):
        return innondation2
    
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()