# Making Heatmaps by giving parameters
# source: pythons-graphs-gallery.com adapted by BA_Mohamed
# Libraries
# Adapted by BA_MOhamed 
#This script is not ready yet and will be updated for soon
import seaborn as sns
import sys
import pandas as pd
from matplotlib import pyplot as plt


# Chemin local du fichier Excel et nom de la feuille
chemin = "DifferentialExpression_Fibroblasts.xlsx"
feuille = "MyoPatient.vs.MyoControl"

# Colonnes spécifiques à utiliser
columns_to_use = [
    "GeneName",
    "pvalue",
    "logFC (MyoconvertedPatient / MyoconvertedControl)",
]


# Plus d'options pour le choix des couleurs
def heatmap(col1, col2, col3, file):
    # Data set
    # with open(file, "r") as f:
    df = pd.read_excel(file, sheet_name=feuille, na_values="###", usecols=columns_to_use)
    df.set_index("GeneName")
    # df = df.dropna(how='any',axis=0)
    df = df.sample(40)
    # ma palette pour l'index
    # my_palette = dict(zip(df.GeneName.unique(), col1))
    # row_colors = df.GeneName.map(my_palette)
    # ploting
    sns.clustermap(
        df[["pvalue", "logFC (MyoconvertedPatient / MyoconvertedControl)"]],
        metric="euclidean",
        method="single",
        cmap="Blues",
        standard_scale=1,
        # row_colors=row_colors,
    )


if __name__ == "__main__":
    # if len(sys.argv) != 5:
    #     print("Erreur: Le nombre de paramétre n'est pas respecté")
    #     sys.exit(1)
    # col1 = sys.argv[1]
    # col2 = sys.argv[2]
    # col3 = sys.argv[3]
    # file = sys.argv[4]
    col1 = "S51"
    col2 = "S50"
    col3 = "S49"
    file = chemin
    heatmap(col1, col2, col3, file)
    plt.show()
    plt.savefig("heatmap.png")