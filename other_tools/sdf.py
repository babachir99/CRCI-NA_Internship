#BA_Mohamed
#MAking smiles from sdf files
import sys
from rdkit import Chem

def sdf_to_smiles(sdf_file, output_file):
    # Lire le fichier SDF
    suppl = Chem.SDMolSupplier(sdf_file)
    smiles_list = []

    # Convertir chaque molécule en SMILES et les ajouter à la liste
    for mol in suppl:
        if mol is not None:
            smiles = Chem.MolToSmiles(mol)
            smiles_list.append(smiles)

    # Écrire les SMILES dans un fichier de sortie
    with open(output_file, 'w') as f:
        for smi in smiles_list:
            f.write(smi + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python sdf_to_smiles.py <input.sdf> <output.smi>")
        sys.exit(1)

    sdf_file = sys.argv[1]
    output_file = sys.argv[2]
    sdf_to_smiles(sdf_file, output_file)
    print(f"SMILES file generated: {output_file}")
