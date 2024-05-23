# bbs_genielog, my meteo report



## Pour commencer

Installation de la documentation: 

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install sphinx
    pip install cloud-sptheme

Consultable sur documentation/docs 

    make html



## Contenu

dossier_administratif:

   - Liste, rôle des porteurs du projet,
   - CV des porteurs du projet,
   - Descriptif de la structure assurant le portage

gestion_projet_scrum

   -  CR SPRINT 1 (SPRINT1.pdf)
   -  CR SPRINT 2 (CR_scrum.pdf)
   -  CR SPRINT 3 (SPRINT3.pdf)

protoype_final

   -  Fichier (.py) des 16 métriques: couvert, innondation, insolation, nuageux, orage, ouraan, pluie, secheresse, soleil, tempete, tornade.
   - fichiers .py générant des .txt: 
        - genDanger (danger.txt): génère un danger parmi une listede phénomènes
        - generate_hauteur_p.py (precipitation.txt): génère une hauteur de pluie, et range dans une catégorie selon la hauteur des précipitation
        - generate insolation.py (insolation.txt); génère un indice UV élevé avec un message de prévention
        - generate_pa (PA.txt): génère une pression atmosphérique
        - generate temperature (temperature.txt): pour générer une température entre -10 et 40°
        - generate_vv (vitesse_vent.txt) génère une vitesse de vent
        - generate.py (data.txt) génère une météo au hasard parmis toute, utile pour le mode fenêtre, sert à afficher la météo en métropole.

   - Autres fichiers .txt:
        - modeeducatif: annonce le mode (1),
        - modefenetre: annonce le mode (2),

   - .gitlab-ci.yml: Pipelien pour la vérification des test unitaires
   





## Integrate with your tools

