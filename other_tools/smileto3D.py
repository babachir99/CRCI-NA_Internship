#coding 'UTF-8'
#BA_Mohamed
#I'm trying to have a view for every smile made by the autoencoder
#Improvement in progress
from rdkit import Chem
from rdkit.Chem import AllChem
from pymol import cmd, stored
import os

def smiles_to_3d_mol(smiles, filename):
    # Convertir SMILES en molécule RDKit
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        # Générer des coordonnées 3D
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())
        AllChem.UFFOptimizeMolecule(mol)
        # Sauvegarder la molécule en format .mol
        Chem.MolToMolFile(mol, filename)
        return mol
    return None

def visualize_with_pymol(mol, output_image):
    # Convertir la molécule RDKit en structure PyMOL
    block = Chem.MolToMolBlock(mol)
    cmd.read_molstr(block, 'molecule')
    # Visualiser et sauvegarder l'image
    cmd.hide('everything', 'all')
    cmd.show('sticks', 'molecule')
    cmd.zoom()
    cmd.png(output_image, ray=True)  # Ray tracing pour une meilleure qualité

def process_smiles_file(input_file, output_dir='output_molecules'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(input_file, 'r') as file:
        for line in file:
            smiles = line.strip()
            output_file = os.path.join(output_dir, f'{smiles}.mol')
            output_image = os.path.join(output_dir, f'{smiles}.png')
            mol = smiles_to_3d_mol(smiles, output_file)
            if mol:
                visualize_with_pymol(mol, output_image)
                print(f'Successfully created: {output_image}')
            else:
                print(f'Failed to create molecule for: {smiles}')

# Exemple d'utilisation
input_smiles_file = 'smiles.txt'
process_smiles_file(input_smiles_file)
