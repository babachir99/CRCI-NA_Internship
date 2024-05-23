#BA_Mohamed
#generation insolation random text

import random 

file=open("insolation.txt","w")
file.write("Indice UV élevé: ")
file.write(str(random.randint(8,10)))
file.write(", risque d'insolation")
file.close()