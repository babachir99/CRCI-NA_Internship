#########
# Melissa MENGA
#########
#generation d'un danger

import random
import sys

""" programme permettant de generer un phenomene meterologique dangereux"""

def generate(number=1):

    """
    
    Args:
        number (int) : nombre de mot à générer
    
    """
    
    file=open("generate_danger.txt","w")
    meteo=["tempete", "secheresse","innondation", "pluie", "ouragan", "orage", "insolation"]
    for i in range(number):
        file.write(meteo[random.randint(0,len(meteo)-1)])
        file.write("\n")
    file.close()

if len(sys.argv)>1:
    generate(int(sys.argv[1]))
else:
    generate()