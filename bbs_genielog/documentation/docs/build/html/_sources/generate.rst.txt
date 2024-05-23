Programmes Generate
===================

Ces programmes permettent de générer des fichiers txt. Grâce à la fonction affiche_text, décrite dans Défilement, 
on pourra alors faire défiler le texte dans la matrice.

Fichier generate.py
---------------------

Ce programme permet la génération d'une liste de phénomènes métérologiques dans un fichier data.txt.
On choisit le nombre de phénomène à afficher dans les paramètres. Nous avons choisi 1, car ce fichier est 
utilisé pour afficher la météo en métropole dans le mode "fenêtre". Pour préciser
le nombre de phénomènes à générer vous pouvez utiliser un argument (entier) à passer au programme.

Voici comment il fonctionne: 

On va tout d'abord générer le fichier data.txt.
On spécifie que l'on veut 1 phénomène métérologique parmi une liste

.. code-block:: python

    def generate(number=1):

On l'ouvre et on spécifie les arguments:

.. code-block:: python

    file=open("data.txt","w")
    meteo=["tempete", "secheresse", "soleil"] 

On génère ensuite le nombre spécifié de phénomènes (ici, 1). Ils seront alors noté dans le fichier data.txt

.. code-block:: python

    for i in range(number):
        file.write(meteo[random.randint(0, len(meteo) - 1)])
        file.write("\n")

Après avoir fermé le fichier, nous vérifions quand même si la saisie de l'utilisateur est correcte: 

.. code-block:: python

    if len(sys.argv)>1:
    generate(int(sys.argv[1]))
    else:
    generate()

Et voilà ! le fichier data.txt est créé.

Fichier genDanger
------------------------


Ce programme permet la génération d'une liste de phénomènes métérologiques parmi certains phénomènes, 
considérés dangereux dans un fichier generate_danger.txt.
On choisit le nombre de phénomène à afficher dans les paramètres. Nous avons choisi 1, car ce fichier est 
utilisé pour afficher un phénomène dangereux, pour le mode danger. Pour préciser
le nombre de phénomènes à générer vous pouvez utiliser un argument (entier) à passer au programme.


On définit tout d'abord la fonction: 

.. code-block:: python

    def generate(number=1):

On l'ouvre et on spécifie les arguments:

.. code-block:: python

    file=open("generate_danger.txt","w")
        meteo=["tempete", "secheresse", "innondation",]

On génère ensuite le nombre spécifié de phénomènes (ici, 1). Ils seront alors noté dans le fichier *generate_danger.txt*

.. code-block:: python

        for i in range(number):
            file.write(meteo[random.randint(0,len(meteo)-1)])
            file.write("\n")
        file.close()

Après avoir fermé le fichier, nous vérifions si la saisie de l'utilisateur est correcte: 

.. code-block:: python

    if len(sys.argv)>1:
        generate(int(sys.argv[1]))
    else:
        generate()


Fichier generate_insolation
-----------------------------

On créé un fichier 'insolation.txt'

.. code-block:: python

    file=open("insolation.txt","w")


On génère un indice UV considéré comme élevé, entre 8 et 10, après avoir importé random.


.. code-block:: python

    file.write("Indice UV élevé: ")
    file.write(str(random.randint(8,10)))
    file.write(", risque d'insolation")

Puis on ferme le fichier.

.. code-block:: python
    
    file.close()




Fichier generate_pa
------------------------

Ce fichier sert à générer une pression atmosphérique au hasard grâce à la bibliothèque random. 
On créé un fichier 'PA.txt'

.. code-block:: python

    file=open("PA.txt","w")


On génère une pression atmosphérique réaliste.


.. code-block:: python

    file.write("La pression atmospherique est de  ")
    file.write(str(random.randint(1010,1020)))
    file.write("PA")


Puis on ferme le fichier.

.. code-block:: python
    
    file.close()




Fichier generate_temperature
-----------------------------


Ce fichier sert à générer une température au hasard grâce à la bibliothèque random. 
On créé un fichier 'temptxt.txt'


.. code-block:: python

    file=open("temptxt.txt","w")


On génère une température réaliste entre -10 et 40°


.. code-block:: python

    file.write("Il fait ")
    file.write(str(random.randint(-10,40)))
    file.write(" °C")


Puis on ferme le fichier.

.. code-block:: python
    
    file.close()

Fichier generate_vv
------------------------

Ce fichier sert à générer une vitesse de vent au hasard grâce à la bibliothèque random. 
On créé un fichier 'vitesse_ven.txt'

.. code-block:: python

    file=open("vitesse_vent.txt","w")


On génère une vitesse de vent réaliste.


.. code-block:: python

    file.write("La vitesse du vent est de  ")
    file.write(str(random.randint(0,100)))
    file.write(" Km/h")


Puis on ferme le fichier.

.. code-block:: python
    
    file.close()


Fichier generate_hauteur_p
----------------------------

Ce fichier permet de créer une hauteur de pluie, qu'on va ensuite classer dans une catégorie.
Selon la hauteur des pluies générée, on aurant la catégorie: 'très faible', 'faible', 'modéréée',
forte ou très forte, grâce a la fonction categorie_precipitation():

.. code-block:: python

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


On écrit le texte généré dans un nouveau fichier:

.. code-block:: python
    
    with open("precipitation.txt", "w") as file:
    file.write(f"La hauteur des pluies est de {hauteur_precipitation} mm, catégorie: {categorie}")

 