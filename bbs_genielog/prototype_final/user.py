import sys

def calculer_score_mot(mot):
    scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}
    return sum(scores.get(lettre, 0) for lettre in mot)

def trouver_mot_plus_long(dictionary_path, lettres):
    if len(lettres) != 7:
        print("Erreur: Le deuxième paramètre doit contenir 7 lettres.")
        return 2

    meilleur_score = 0
    meilleur_mot = ""

    with open(dictionary_path, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mot = ligne.strip()
            if all(lettre in mot for lettre in lettres):
                score = calculer_score_mot(mot)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_mot = mot

    if meilleur_mot:
        print(meilleur_mot)
        return 0
    else:
        print("Aucun mot trouvé avec les lettres fournies.")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Erreur: Nombre de paramètres incorrect.")
        sys.exit(1)

    chemin_dictionnaire = sys.argv[1]
    lettres = sys.argv[2]

    code_erreur = trouver_mot_plus_long(chemin_dictionnaire, lettres)
    sys.exit(code_erreur)
