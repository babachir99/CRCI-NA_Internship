#Ahamed TCHATAKOURA
#Création d'une matrice 16x16 pour afficher une alerte météo concernant la métrique méteorologique "vitesse du vent"

#definition d'une fonction qui va permettre d'alterner entre les 2 images pour créer un effet d'animation.

def nbMatrice():
    return 2 

#definition de la fonction insolation. Les nombres sont associés a une couleur, qui est précisée dans test_matrix
def insolation(matrice):
  
    """
    >>> insolation(1)
    [[0, 17, 17, 17, 17, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [17, 17, 17, 17, 17, 17, 17, 0, 18, 0, 0, 0, 0, 0, 0, 0], [17, 17, 17, 17, 17, 17, 17, 0, 0, 18, 0, 0, 0, 0, 0, 0], [17, 17, 17, 17, 17, 17, 17, 0, 0, 0, 18, 0, 18, 0, 0, 0], [17, 17, 17, 17, 17, 17, 0, 18, 0, 0, 0, 18, 18, 0, 0, 0], [0, 17, 17, 17, 17, 0, 0, 0, 18, 0, 18, 18, 18, 0, 0, 0], [0, 0, 18, 0, 0, 18, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0], [0, 0, 0, 18, 0, 0, 18, 0, 0, 0, 18, 0, 18, 0, 0, 0], [0, 0, 0, 0, 18, 0, 0, 18, 0, 0, 0, 18, 18, 0, 0, 0], [0, 0, 0, 0, 0, 18, 0, 18, 18, 0, 18, 18, 18, 0, 0, 0], [0, 0, 0, 0, 0, 0, 18, 18, 0, 18, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 18, 18, 18, 0, 0, 18, 18, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 18, 18, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    #modification des couleurs
    g = 17
    I = 17
    J = 18
  
    #matrice insolation 16x16
    insolation = [[0,I,I,I,I,I,0,0,0,0,0,0,0,0,0,0],
                  [I,I,g,g,g,g,I,0,J,0,0,0,0,0,0,0],
                  [I,g,g,g,g,g,g,0,0,J,0,0,0,0,0,0],
                  [I,g,g,g,g,g,g,0,0,0,J,0,J,0,0,0],
                  [I,I,g,g,g,g,0,J,0,0,0,J,J,0,0,0],
                  [0,I,I,I,I,0,0,0,J,0,J,J,J,0,0,0],
                  [0,0,J,0,0,J,0,0,0,J,0,0,0,0,0,0],
                  [0,0,0,J,0,0,J,0,0,0,J,0,J,0,0,0],
                  [0,0,0,0,J,0,0,J,0,0,0,J,J,0,0,0],
                  [0,0,0,0,0,J,0,J,J,0,J,J,J,0,0,0],
                  [0,0,0,0,0,0,J,J,0,J,0,0,0,0,0,0],
                  [0,0,0,0,0,J,J,J,0,0,J,J,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,J,J,J,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
  
    #ajout d'une deuxième matrice pour ajouter du mouvement
    insolation2 = [[0,I,I,I,I,I,0,0,0,0,0,0,0,0,0,0],
                  [I,I,g,g,g,g,I,0,0,0,0,0,0,0,0,0],
                  [I,g,g,g,g,g,g,0,0,J,0,0,0,0,0,0],
                  [I,g,g,g,g,g,g,0,0,0,J,0,0,0,0,0],
                  [I,I,g,g,g,g,0,0,0,0,0,J,0,J,0,0],
                  [0,I,I,I,I,0,0,0,J,0,0,0,J,J,0,0],
                  [0,0,0,0,0,0,0,0,0,J,0,J,J,J,0,0],
                  [0,0,0,J,0,0,J,0,0,0,J,0,0,0,0,0],
                  [0,0,0,0,J,0,0,J,0,0,0,J,0,J,0,0],
                  [0,0,0,0,0,J,0,0,J,0,0,0,J,J,0,0],
                  [0,0,0,0,0,0,J,0,0,J,0,J,J,J,0,0],
                  [0,0,0,0,0,0,0,J,J,0,J,0,0,0,0,0],
                  [0,0,0,0,0,0,J,J,J,0,0,J,J,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,J,J,J,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    if (matrice == 1):
            return insolation
    elif (matrice == 2):
            return insolation2
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()  