#generating random atmospheric pressure
#BA Mohamed
import random 

file=open("PA.txt","w")
file.write("La pression atmospherique est de  ")
file.write(str(random.randint(1010,1020)))
file.write("PA")
file.close()


