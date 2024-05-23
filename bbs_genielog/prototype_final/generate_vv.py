#BA_Mohamed
#generation wind speed random text

import random 

file=open("vitesse_vent.txt","w")
file.write("La vitesse du vent est de  ")
file.write(str(random.randint(0,100)))
file.write(" Km/h")
file.close()

