#Melissa MENGA

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd 

import time

def execute(meteo,t):
    """
    Fonction qui affiche de manière simulée le rendu d'une matrice et ce pendant un certain temps
    
    Args:
        matrix (np.array) : Matrice de 16x16 cases contenant une image à afficher
        t (int) :  temps d'affichage en secondes
    
    """
 
    for x in range(16):
        for y in range(16):
            if meteo [y][x] == 0:
             r, g, b =(0,0,0)
            elif meteo [y][x] == 1: #jaune
             r,g,b = (255, 255, 0)
            elif meteo [y][x] == 2: #bleu
                r,g,b = (0, 0, 255)
            elif meteo [y][x] == 3: #gris
                r,g,b = (120, 120, 120)
            elif meteo [y][x] == 4: #fauve
                r,g,b = (128, 24, 24)
            elif meteo [y][x] == 5: #tabac
                r,g,b = (159, 85, 30)
            elif meteo [y][x] == 6: #jaune clair
                r,g,b = (255, 255, 153)
            elif meteo [y][x] == 7: #jaune fonce
                r,g,b = (255, 204, 0)
            elif meteo [y][x] == 8:
                r,g,b = (255, 255, 255) #blanc
            elif meteo [y][x] == 9:
                r,g,b = (0, 0, 190) #bleu
            elif meteo [y][x] == 10:
                r,g,b = (121, 121, 248) #Bleu
            elif meteo [y][x] == 11: #gris
                r,g,b = (186, 186, 186)
            elif meteo [y][x] == 12: 
                r,g,b = (118, 111, 100) #bis
            elif meteo [y][x] == 13: 
                r,g,b = (48, 48, 48) #gris anthracite
            elif meteo [y][x] == 14: 
                r,g,b = (239, 239, 239) #argile
            elif meteo [y][x] == 15: 
                r,g,b = (90, 94, 107) #ardoise
            elif meteo [y][x] == 16: 
                r,g,b = (15, 5, 107) #bleu nuit
            
            elif meteo [y][x] == 17: 
                r,g,b = (255, 255, 0) #jaune_vif
            elif meteo [y][x] == 18: 
                r,g,b = (255, 200, 0) #jaune_vit_-
             
            elif meteo [y][x] == 15: 
                r,g,b = (90, 94, 107) #ardoise
            elif meteo [y][x] == 16: 
                r,g,b = (15, 5, 107)
           
            #elif meteo[y][x] == 8:  # Rouge
            #    r, g, b = (255, 0, 0)
            else:  # Par défaut, noir ==1
                 r, g, b = (0, 0, 0)
            

            unicornhathd.set_pixel(x,y,r,g,b)  
    unicornhathd.show()                             
    time.sleep(t) 

