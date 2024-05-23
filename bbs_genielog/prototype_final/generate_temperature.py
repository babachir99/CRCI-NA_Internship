#pour généréer une température au hasard
#melissa MENGA
import random 

file=open("temperature.txt","w")
file.write("Il fait ")
file.write(str(random.randint(-10,40)))
file.write(" °C")
file.close()


