#Ahamed TCHATAKOURA

#Création d'une matrice 16x16 pour afficher une alerte météo concernant le métrique méteorologique "vitesse du vent"

#definition d'une fonction qui va permettre d'alterner entre les 2 images pour créer un effet d'animation.

def nbMatrice():
    return 2 
  
#definition de la fonction vitesse. Les nombres sont associés a une couleur, qui est précisée dans test_matrix
def vitesse(matrice):
  
  """
    >>> vitesse(1)
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,c,c,c,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,c,0,0], [0,c,c,c,c,c,c,c,c,c,c,c,c,c,0,c], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,c], [0,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,c,0], [0,0,0,0,0,0,0,0,0,0,0,c,0,0,c,0], [0,0,0,0,0,0,0,0,0,0,0,0,c,c,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
  """
  #modification couleur
  c = 8
  
  #matrice vitesse_vent 16x16     
                                     
  vitesse=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,c,c,c,0,0],  
    [0,0,0,0,0,0,0,0,0,0,0,0,0,c,0,0], 
    [0,c,c,c,c,c,c,c,c,c,c,c,c,c,0,c], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,c], 
    [0,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,c,0],
    [0,0,0,0,0,0,0,0,0,0,0,c,0,0,c,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,c,c,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
      
  return (vitesse) 

if __name__ == "__main__":
  import doctest
  doctest.testmod()