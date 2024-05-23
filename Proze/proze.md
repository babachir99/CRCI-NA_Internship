
  

# The ProZE tool

  

## Overview

ProZE can therefore visualize and compare the three-dimensional structures
structures of multiple proteins to a single target protein. This tool enables
structure superposition between a protein of interest and a selection of human
protein of interest and a selection of human proteins. These are pre-selected
selected by a keyword. As an output, the tool extracts (i) the characteristics
of the best proteins, defined by a low RMSD (ontological terms, superimposed sequences
sequences, RMSD); (ii) an overlay image for each of these proteins by
by coloring the overlay area (the RMSD coloring script was extracted from the open source
open source function written by Shivender Shandilya, Jason Vertrees and Thomas Holder).
It is also possible to superimpose only on a part of the protein of interest, or a domain of the protein.
protein of interest, or a specific domain, instead of using the complete structure of the
protein.
The advantage of our tool is its keyword-based operation, which facilitates
access and automatic downloading of a set of proteins (possibility of extracting up to
2000 proteins). But also, access to structures derived from the PDB and those
predicted by AlphaFold. 


## Installation

  

### Prerequisites

- Anaconda or Miniconda (Recommended for managing dependencies)
- You can use also mamba (a faster and lighter version of anaconda)

### Downloading the miniforge
```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
```
### Installing it 
```bash
sh Miniforge3-Linux-x86_64.sh
# Accept the licence
# Define the pathway
# Initialise the shell by the way of installation
```

### Environment Setup

To set up the Python environment with all the necessary dependencies, follow these steps:

  

1. Clone the repository:

```bash

git clone https://gitlab.univ-nantes.fr/E235985F/internship.git

cd autoencoder

```

  

2. Create the environment from the `all.yml` file:

```bash

conda env create -f proze.yml

```

  

3. Activate the environment:

```bash

conda activate proze

```
4. You have to download PyMOL with conda. Then after activating the environment use this command:

```bash

conda install -c conda-forge -c schrodinger pymol-bundle=2.6

```

## Usage

To run The ProZE, follow these steps after activating the environment:

  

```bash

python3  proze.py

```

  


## Recommendations
This tool does not requires a fairly large RAM, so it takes a lot of time to finish execution, so we advise you to run it on a cluster!

