#########
# Melissa MENGA
#########

import random
import sys

""" Ce petit programme permet la génération d'une liste de phénomènes meterologiques dans un fichier data.txt

    Une simple execution du programme générera une météo au hasard. Pour préciser
    le nombre d'émotions à générer vous pouvez utiliser un argument (entier) à passer au programme.
"""

def generate(number=1):

    """
    
    Args:
        number (int) : nombre de mot à générer
    
    """
    
    file=open("data.txt","w")
    meteo=["tempete","vitesse" "secheresse", "soleil", "innondation", "pluie","temperature","couvert","orage", "ouragan", "tornade", "humidite", "PA", "precipitation", "vitesse"]
    for i in range(number):
        file.write(meteo[random.randint(0,len(meteo)-1)])
        file.write("\n")
    file.close()

if len(sys.argv)>1:
    generate(int(sys.argv[1]))
else:
    generate()