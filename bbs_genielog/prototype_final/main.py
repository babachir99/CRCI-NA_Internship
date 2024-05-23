#mCréation du fichier par Melissa menga
#Contribution: Mohammed El Bachir Ba, 
#definition de la fonction principale pour appeler les fonctions precedemment créées et les afficher dans la matrice

import text_defile
from unicorn_hat_sim import unicornhathd
import meteo
import subprocess

def test_fonct():
    subprocess.run(["python", "user.py"])

mode = ""

# Début de boucle pour définir les modes
while mode != "0":
    # choix du mode
    mode = input("Choisissez le mode: éducatif (1), fenêtre (2), alerte (3) (Quitter: 0): ")

    # Mode éducatif
    if mode == "1":
        choix_meteo = input("Veuillez choisir un phénomène météorologique entre: temperature, PA (pression), insolation, vitesse (du vent), humidite (de l'air), precipitations(hauteur des pluies), soleil, pluie, couvert, orage, nuageux, innondation, tornade, ouragan, sécheresse, tempête: ")
        text_defile.texte_afficher('modeeducatif.txt', (255, 0, 0))
        meteo.Affiche_Meteo(choix_meteo)

    # Mode alerte
    elif mode == "3":
        text_defile.texte_afficher('danger.txt', (255, 0, 0))
        file = open('generate_danger.txt', 'r')
        for line in file:
            line = line.rstrip("\n")
            meteo.Affiche_Meteo(line)
        file.close()

    # Mode fenêtre
    elif mode == "2":
        text_defile.texte_afficher('modefenetre.txt', (255, 0, 0))
        print("En métropole, voici la météo: ")
        file = open('data.txt', 'r')
        for line in file:
            line = line.rstrip("\n")
            meteo.Affiche_Meteo(line)
        file.close()

# Exécution test seulement lorsque l'utilisateur choisit de quitter (0)
test_fonct()
