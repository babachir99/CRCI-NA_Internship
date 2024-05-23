#BA_Mohamed
#generation wind speed random text

import random

def categorie_precipitation(hauteur):
    if hauteur < 2:
        return "Très faible"
    elif 2 <= hauteur < 10:
        return "Faible"
    elif 10 <= hauteur < 25:
        return "Modérée"
    elif 25 <= hauteur < 50:
        return "Forte"
    else:
        return "Très forte"

hauteur_precipitation = random.randint(0, 50)
categorie = categorie_precipitation(hauteur_precipitation)

# Écriture dans le fichier
with open("precipitation.txt", "w") as file:
    file.write(f"La hauteur des pluies est de {hauteur_precipitation} mm, catégorie: {categorie}")