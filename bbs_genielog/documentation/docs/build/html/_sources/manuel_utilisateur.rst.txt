Manuel utilisateur
==================

Cette section permet de mieux comprendre le programme réalisé dans le cadre de My Meteo report.


Configuration
-------------

Pour pouvoir utiliser pleinement My meteo report, assurez vous d'avoir le bon environnement de travail ainsi que les bons modules et 
librairies.

Pour pouvoir visualiser les animations, vous devez installer:  from unicorn_hat_sim import unicornhathd

Pour plus d'information: https://github.com/jayniz/unicorn-hat-sim


Documentation
--------------

Pour avoir accès à cette documentation sous format HTML et non PDF, il faudra tout d'abord installer 
un environnement virtuel de travail: 

.. code-block:: python

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install sphinx

Une fois installé, il vous faudra également installer le thème, pour que cela s'affiche correctement: 

.. code-block:: python

    pip install cloud-sptheme


Fonctionalités
--------------

Pour utiliser notre prototype, l'utilisateur a le choix entre 3 modes: 
-le mode éducatif (1)
-le mode fenêtre (2)
-le mode danger (3)

L'utilisateur, dans un premier temps va choisir le mode souhaité.
Une fois le mode saisi, un premier message s'affiche avec le mode séléctionné.Ensuite, si le mode séléctionné 
est 'éducatif', alors l'utilisateur devra encore une fois entrer une saisie. 
Pour ce mode, il devra entrer une température, et celle ci devra s'afficher sur l'écran.

Le mode fenêtre permet d'afficher la météo en métropole. Si l'utilisateur a choisi ce mode la, 
alors un premier message va défiler, avec le mode choisit. Un phénomène métérologique s'affiche alors, 
avec un message dans le terminal qui indique la météo en métropole.

Le mode danger permet de prévenir d'un danger. Uniquement certaines métriques et phénomènes seront affichés ici.
Si l'utilisateur a choisi ce mode, alors un message d'alerte défile, puis le phénomène dangereux s'affiche alors à l'écran.


