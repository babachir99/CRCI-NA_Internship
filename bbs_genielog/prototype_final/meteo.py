#Création: Mélissa MENGA
#Collaboration: Ngone Ba, Ahamed Tchatakoura, Mohammed BA, Awa AMAR
#definition de la fonction principale pour appeler les fonctions precedemment créées et les afficher dans la matrice

#importation des matrices précedemment crées
import soleil
import pluie
import couvert
import orage
import nuageux
import Innondation
import tornade
import ouragan
import secheresse_gl
import tempete_gl


#metriques
import temperature
#import temperature2
import test_matrix
import text_defile
import vitesse
import Insolation

def Affiche_Meteo(meteo):
    """
    >>> Affiche_Meteo("secheresse")
    secheresse
    >>> Affiche_Meteo("tempete")
    tempete
    >>> Affiche_Meteo("soleil")
    soleil
    >>> Affiche_Meteo("innondation")
    innondation
    >>> Affiche_Meteo("pluie")
    pluie
    >>> Affiche_Meteo("nuageux")
    nuageux
    >>> Affiche_Meteo("ouragan")
    ouragan
    >>> Affiche_Meteo("couvert")
    couvert
    >>> Affiche_Meteo("orage")
    orage
    >>> Affiche_Meteo("tornade")
    tornade
    
    >>> Affiche_Meteo("pression_atmospherique")
    pression_atmospherique
    >>> Affiche_Meteo("hauteur_des_pluies")
    hauteur_des_pluies
    >>> Affiche_Meteo("temperature")
    temperature
    """

    if (meteo=="tempete"):
        nbMatrice = tempete_gl.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(tempete_gl.tempete(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
                
    elif (meteo=="secheresse"):
        nbMatrice = secheresse_gl.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(secheresse_gl.secheresse(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
                
    elif (meteo=="soleil"):
        nbMatrice = soleil.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(soleil.soleil(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)

    #ahamed
    elif (meteo=="innondation"):
        nbMatrice = Innondation.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Innondation.innondation(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
    
    elif (meteo=="pluie"):
        nbMatrice = pluie.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(pluie.pluie(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
    #ahamed                   
    elif (meteo=="nuageux"):
        nbMatrice = nuageux.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(nuageux.nuageux(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
    ############
    elif (meteo=="tornade"):
        nbMatrice = tornade.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(tornade.tornade(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
            
    elif (meteo=="ouragan"):
        nbMatrice = ouragan.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(ouragan.ouragan(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
                        
    #ahamed
    
    elif (meteo=="couvert"):
        nbMatrice = couvert.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(couvert.couvert(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
    
    elif (meteo=="orage"):
        nbMatrice = orage.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(orage.orage(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo) 
                        


            """
                Appel des métriques à partir d'ici!
            """
    elif (meteo=="temperature"):
        nbMatrice = temperature.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(temperature.temperature(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
        text_defile.texte_afficher('temperature.txt', (255, 0, 0))
    
    elif (meteo=="vitesse"):
        nbMatrice = vitesse.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(vitesse.vitesse(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
        text_defile.texte_afficher('vitesse_vent.txt', (255, 0, 0))

    elif (meteo=="insolation"):
        nbMatrice = Insolation.nbMatrice()
        for i in range (5): #l'animation va tourner 5 fois
            for j in range (1, nbMatrice+1):
                test_matrix.execute(Insolation.insolation(j),0.5)
                if (i == 1):
                    if (j==1): #permet d'afficher la meteo
                        print(meteo)
        text_defile.texte_afficher('insolation.txt', (255, 0, 0))

    
    elif (meteo=="PA"):
        text_defile.texte_afficher('PA.txt', (255, 0, 0))
        
    elif (meteo=="precipitation"):
        text_defile.texte_afficher('precipitation.txt', (255, 0, 0))
        
    elif (meteo=="humidite"):
        text_defile.texte_afficher('humidite.txt', (255, 0, 0))
    

#file=open('data.txt','r')
#for line in file:
#    line=line.rstrip("\n")
#    Affiche_Meteo(line)
#file.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()