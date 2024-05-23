##generation de l'humidité de l'air

import random

def categorie_humidite(humidite_relative):
    if humidite_relative < 30:
        return "Très faible"
    elif 30 <= humidite_relative < 50:
        return "Faible"
    elif 50 <= humidite_relative < 70:
        return "Modérée"
    else:
        return "Élevée"


humidite_relative = random.randint(0, 100)
categorie = categorie_humidite(humidite_relative)
with open("humidite.txt", "w") as file:
    file.write(f"L'humidité relative est de {humidite_relative}%, catégorie: {categorie}")
