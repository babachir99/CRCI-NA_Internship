# -*- coding: utf-8 -*-
import sys
import os
import time
import pandas as pd
import requests, sys, json
import Bio
from Bio.PDB import PDBList
import pymol
from pymol import cmd, CmdException
import wget
from bioservices.uniprot import UniProt
from goatools import obo_parser
import shutil

u = UniProt(verbose = False)
"""
"""

os.makedirs('./PyMOL_test/', exist_ok=True) # Create the directories for all the files generate by the analysis
os.makedirs('./PyMOL_test/PDB/', exist_ok=True) # Create the directories for all PDB/CIF file

"""#### → Get PDB or AlphaFold files"""




def get_url(url_uniprot) :

    ''' Give the Uniprot URL, and translate it in the json format, for the search of specific data '''

    r = requests.get(url_uniprot, headers={ "Accept" : "application/json"}) #, headers={ "Accept" : "text/x-flatfile"} # Get the Uniprot URL
    #r = requests.get("https://www.uniprot.org/uniprot/?query=protease&sort=score")
    if not r.ok:
        r.raise_for_status()
        sys.exit()

    data = json.loads(r.text) # Load the URL in the JSON format
    return data # Return the result (JSON)




def bootstrapping_alphafold_file_download(proteins) :

    for protein in proteins :
        try :
            url = f'https://alphafold.ebi.ac.uk/files/AF-{protein}-F1-model_v2.pdb'
            wget.download(url, f'./PyMOL_test/PDB/{protein}.pdb')
        except :
            print("Check 2- Il n'y a pas de structure AlphaFold")






def find_pdb_without_duplicates(acc, data):

    ''' Find all the proteins given by the URL (present on the JSON file)
        and put them in a CSV file, no duplicates allowed '''
    try :
        list_convert = u.mapping(fr="UniProtKB_AC-ID", to="PDB", query=acc)
        #print("** Chargement de la structure PDB **")
        for convert in list_convert.values() :
            conv = convert[0]['to']
        get_pdb_file(convert[0]['to'])
        return convert[0]['to']
    except :
        try :
            print('Check 1- Pas de structure PDB')
            bootstrapping_alphafold_file_download([acc])
            #print('** Chargement de la structure AlphaFold **')
        except :
            print("-"*40)
            print("-- Aucune structure 3D trouvée pour ", acc, ' --')
            print("-"*40)




def get_pdb_file(pdb_name) :

    ''' Selecting structures from PDB through the PDB ID '''

    pdbl = PDBList() # Database
    pdbl.retrieve_pdb_file(pdb_name,overwrite = True, pdir='./PyMOL_test/PDB') # Give the file structure in a CIF format for all the PDB ID
    # Set overwrite to "True" allow the overwritting of an existing download PDB file

"""#### → ID conversion"""

# NEW -> Update of Uniprot june/july 2022
POLLING_INTERVAL = 3




def submit_id_mapping(fromDB, toDB, ids):
    r = requests.post(
        "https://rest.uniprot.org/idmapping/run", data={"from": fromDB, "to": toDB, "ids": ids},
    )
    r.raise_for_status()
    return r.json()["jobId"]





def get_id_mapping_results(job_id):
    while True:
        r = requests.get(f"https://rest.uniprot.org/idmapping/status/{job_id}")
        r.raise_for_status()
        job = r.json()
        if "jobStatus" in job:
            if job["jobStatus"] == "RUNNING":
                #print(f"Retrying in {POLLING_INTERVAL}s")
                time.sleep(POLLING_INTERVAL)
            else:
                raise Exception(job["jobStatus"])
        else:
            return job





def convert_ACC_GENENAME(id) : #working
    job_id = submit_id_mapping(
        fromDB="UniProtKB_AC-ID", toDB="Gene_Name", ids=[id] #ChEMBL
    )
    results = get_id_mapping_results(job_id)
    #print(json.dumps(results))
    conversion = json.dumps(results)
    #print(conversion.split(":")[3].split('"')[1])
    return conversion.split(":")[3].split('"')[1]





def convert_GENENAME_ACC(id) : #working
    job_id = submit_id_mapping(
        fromDB="Gene_Name", toDB="UniProtKB", ids=[id] #ChEMBL
    )
    results = get_id_mapping_results(job_id)
    #print(json.dumps(results))
    conversion = json.dumps(results)
    to_acc = json.loads(conversion)
    #if c['results'][value][]
    for value in range(len(to_acc)) :
        if to_acc['results'][value]['to']['organism']['taxonId'] == 9606 :
            #print(to_acc['results'][0]['to']['organism']['taxonId'])
            #print(to_acc['results'][value]['to']['primaryAccession'])
            v = value
    return to_acc['results'][v]['to']['primaryAccession']





def convert_ACC_to_PDB(data_acc) :
    convert = u.mapping(fr="UniProtKB_AC-ID", to="PDB", query=data_acc)
    #print(convert['results'][0]['to'])
    return convert['results'][0]['to']

## NEW --> for sequence and GO term extraction






def convert_PDB_to_ACC(pdb_id) :
    list_convert = u.mapping(fr="PDB", to="UniProtKB", query=pdb_id)
    for value in range(len(list_convert)) :
        if list_convert['results'][value]['to']['organism']['taxonId'] == 9606 :
            conv = list_convert['results'][value]['to']['primaryAccession']
    return list_convert['results'][value]['to']['primaryAccession']

"""#### → Upload the interest protein"""






def find_target(genename, type_of_entry) :
   # Si la protéine entrée est un "Gene Name"
   if type_of_entry == "genename" :
    ## Recherche d'une structure PDB (à partir d'un Nom de gène)
    try :
      id_uniprot = convert_GENENAME_ACC(genename) # convert genename to uniprot ID
      id_pdb = convert_ACC_to_PDB(id_uniprot) # -> if you want to convert uniprot ID to PDB ID
      print('*'*40)
      print("Structure PDB trouvée !")
      print('*'*40)
      try :
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(id_pdb,pdir='./PyMOL_test/') # Only keep the first PDB protein found on Uniprot
        import os
        os.rename(f'./PyMOL_test/{id_pdb.lower()}.cif', f'./PyMOL_test/{genename}.cif')
      except :
        print('-- Impossible de télécharger la structure PDB (protein structure not available ? - check on PDB')
    except :
      print("**",genename, "ne présente pas de structure PDB, recherche d'une structure AlphaFold prédite **")
      try :
        ## Recherche d'une structure AlphaFold (à partir d'un Nom de gène)
        id_uniprot = convert_GENENAME_ACC(genename)
        url = f'https://alphafold.ebi.ac.uk/files/AF-{id_uniprot}-F1-model_v2.pdb'
        wget.download(url, f'./PyMOL_test/{convert_ACC_GENENAME(id_uniprot)}.pdb')
        print('*'*40)
        print("Structure AlphaFold trouvée !")
        print('*'*40)
      except :
        print("La protéine d'intérêt est invalide ou ne présente aucune structure tridimensionnelle définie sur Uniprot !")

   # Si la protéine entrée est un "Identifiant UniProt"
   if type_of_entry == "uniprot" :
    id_uniprot = genename
    print("Identifiant utilisé pour l'analyse : ", id_uniprot)
    ## Recherche d'une structure PDB (à partir d'un Identifiant UniProt)
    try :
      id_pdb = convert_ACC_to_PDB(id_uniprot) # -> if you want to convert uniprot ID to PDB ID
      print('*'*40)
      print("Structure PDB trouvée !")
      print('*'*40)
      try :
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(id_pdb,pdir='./PyMOL_test/') # Only keep the first PDB protein found on Uniprot
        import os
        os.rename(f'./PyMOL_test/{id_pdb.lower()}.cif', f'./PyMOL_test/{genename}.cif')
      except :
        print('-- Impossible de télécharger la structure PDB (protein structure not available ? - check on PDB')
    except :
      print("**",genename, "ne présente pas de structure PDB, recherche d'une structure AlphaFold prédite **")
      try :
        ## Recherche d'une structure AlphaFold (à partir d'un Nom de gène)
        url = f'https://alphafold.ebi.ac.uk/files/AF-{id_uniprot}-F1-model_v2.pdb'
        wget.download(url, f'./PyMOL_test/{convert_ACC_GENENAME(id_uniprot)}.pdb')
        print('*'*40)
        print("Structure AlphaFold trouvée !")
        print('*'*40)
      except :
        print("La protéine d'intérêt est invalide ou ne présente aucune structure tridimensionnelle définie sur Uniprot !")

   # Si la protéine entrée est un "Identifiant PDB"
   if type_of_entry == "PDB" :
     id_pdb = genename
     print("Identifiant utilisé pour l'analyse : ", id_pdb)
     ## Recherche d'une structure PDB (à partir d'un Identifiant PDB)
     try :
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(id_pdb,pdir='./PyMOL_test/') # Only keep the first PDB protein found on Uniprot
        print('*'*40)
        print("Structure PDB trouvée et téléchargée dans le dossier !")
        print('*'*40)
        import os
        os.rename(f'./PyMOL_test/{id_pdb.lower()}.cif', f'./PyMOL_test/{genename}.cif')
     except :
       print('-- Impossible de télécharger la structure PDB (protein structure not available ? - check on PDB')

"""#### → PyMOL visualisation and best RMSD extraction"""






## NEW
def pymol_visualization(protein,data, type_of_entry):

    ''' Open a PyMOL windows and perform a superimposition between
        FAM111B and the other proteases in order to find the lowest RMSDs  '''

    find_target(protein, type_of_entry)

    # Load the interest protein and all the other proteins structures into the PyMOL window
    #from pymol import cmd

    list_RMSD = []
    list_prot = []
    access = []
    list_prot_pdb = []
    print()
    print("-- Recherche des structures tridimensionnelles des protéines issus du mot-clé et calcul du RMSD -- ")
    print()
    for value in range(len(data)):
        access.append(data[value]["accession"])
    for prot in access :
      try :
        mobile = f'./PyMOL_test/{protein}.pdb'
        cmd.load(mobile)
      except :
        try :
          mobile = f'./PyMOL_test/{protein}.cif' # '../Q6SJ93_pdb.pdb'
          cmd.load(mobile)
        except :
          print("Impossible de récupérer la structure 3D de la protéine d'intérêt")
      #print(mobile.split('/')[2].split(".")[0])
      pdb_convert = find_pdb_without_duplicates(prot, data)
      if pdb_convert not in list_prot_pdb or prot not in list_prot_pdb : # To avoid duplicates
        list_prot_pdb.append(pdb_convert)
        list_prot_pdb.append(prot)
        try :
            prot = pdb_convert.split(".")[0]
            #print(prot)
            cmd.load('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
            result = cmd.cealign(mobile.split('/')[2].split(".")[0], prot)
            RMSD = result['RMSD']
        except :
            try :
              prot = prot.split(".")[0]
              #print(prot)
              cmd.load('./PyMOL_test/PDB/'+prot+".pdb")
              result = cmd.cealign(mobile.split('/')[2].split(".")[0], prot)
              RMSD = result['RMSD']
            except :
              print("No 3D structure found for the protein", prot)
        #print(RMSD)
        cmd.delete('all')
        list_prot.append(prot)
        list_RMSD.append(RMSD)
        try :
            os.remove('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
        except :
            try :
              os.remove('./PyMOL_test/PDB/'+prot+".pdb")
            except :
              print('No structure to delete (- cause : no structure charged)')
        #os.remove('./PyMOL_test/PDB/'+prot)
      else : #if pdb_convert in list_prot_pdb : # Suppress the PDB file present in double
        try :
            os.remove('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
        except :
          try :
            os.remove('./PyMOL_test/PDB/'+prot+".pdb")
          except :
            print("Enable to suppress the ", prot, "file")
    list_prot = pd.DataFrame(list_prot)
    list_RMSD = pd.DataFrame(list_RMSD)
    list_data = [list_prot, list_RMSD] # Put all the dataframe into a list
    data_prot = pd.concat(list_data, axis = 1, ignore_index=False, sort=True) # Concatenate on the axis = 1 (columns)  all the dataframe in the list
    data_prot = data_prot.to_csv('./PyMOL_test/rmsd_prot_pymol.csv', sep = ';', index = False, header = False) # Creation of a CSV file of the concatenation --> 'file_domain_begin_end.csv',
    print(data_prot)
    cmd.zoom(selection = 'all')
    cmd.png('./PyMOL_test/image_pymol_superimposition.png') # Capture an image of the current display
    # Move the file to the desired directory
    shutil.move(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
    





def rmsd_min_extraction(number_protein_min_rmsd) :

    ''' Extraction of a list of N proteins with the lowest RMSD  '''

    df = pd.read_csv("./PyMOL_test/rmsd_prot_pymol.csv", delimiter = ';', header = None)
    df_sorted = df.sort_values(1)
    #os.remove("./PyMOL_test/rmsd_prot_pymol.csv")
    #df_sorted = pd.read_csv("./PyMOL_test/rmsd_prot_pymol.csv", delimiter = ';', header = None)
    #print("--SORTED RMSD --\n", df_sorted)
    df_min_t = df_sorted[:number_protein_min_rmsd] #[:10]
    df_min = df_min_t.iloc[:,0]
    print(df_min)
    df_min.to_csv('./PyMOL_test/pdb_rmsd_min.csv', index=False, header = None)

"""#### → Sequences and GO terms extraction"""







def go_term() :
    go_obo_url = 'http://purl.obolibrary.org/obo/go/go-basic.obo'
    data_folder = os.getcwd() + '/data'

    # Check if we have the ./data directory already
    if(not os.path.isfile(data_folder)):
        # Emulate mkdir -p (no error if folder exists)
        try:
            os.mkdir(data_folder)
        except OSError as e:
            if(e.errno != 17):
                raise e
    else:
        raise Exception('Data path (' + data_folder + ') exists as a file. '
                       'Please rename, remove or change the desired location of the data path.')

    # Check if the file exists already
    if(not os.path.isfile(data_folder+'/go-basic.obo')):
        go_obo = wget.download(go_obo_url, data_folder+'/go-basic.obo')
    else:
        go_obo = data_folder+'/go-basic.obo'
    return go_obo






def sequence_extraction(mobile, target) :

    #############################
    #### Sequence extraction ####
    #############################

    _resn_to_aa =  {
            'ALA' : 'A',
            'CYS' : 'C',
            'ASP' : 'D',
            'GLU' : 'E',
            'PHE' : 'F',
            'GLY' : 'G',
            'HIS' : 'H',
            'ILE' : 'I',
            'LYS' : 'K',
            'LEU' : 'L',
            'MET' : 'M',
            'ASN' : 'N',
            'PRO' : 'P',
            'GLN' : 'Q',
            'ARG' : 'R',
            'SER' : 'S',
            'THR' : 'T',
            'VAL' : 'V',
            'TRP' : 'W',
            'TYR' : 'Y',
            # RNA
            'A'   : 'A',
            'U'   : 'U',
            'G'   : 'G',
            'C'   : 'C',
            # DNA
            'DA'  : 'A',
            'DT'  : 'T',
            'DG'  : 'G',
            'DC'  : 'C',
            }

    mobile_seq = {'list_resn_mobile': []}
    cmd.iterate(f'_aln and {mobile}', 'list_resn_mobile.append(resn)', space=mobile_seq)
    valuesList_mobile = list(mobile_seq.values()) # Transform a dict_values into a list
    flat_list_mobile = [item_m for transformed_list_mobile in valuesList_mobile for item_m in transformed_list_mobile] # Transform a list of list into a list
    one_letter_aa_mobile = [_resn_to_aa[x_m] for x_m in flat_list_mobile] # Convert  each 3 letters AA into one letter AA
    #print(one_letter_aa_mobile)
    all_seq_mobile = ''.join(one_letter_aa_mobile)
    print('*'*40)
    mobile_transf = mobile.split('and guide')[0].split("(")[1].split(")")[0]
    print(mobile_transf) # Put convert acc_to_genename function ?
    print('*'*40)
    print("Sequence : ", all_seq_mobile)

    ############################
    #### GO term extraction ####
    ############################

    go_obo = go_term()
    go = obo_parser.GODag(go_obo)

    list_bp = []
    dico_bp = {}
    list_temp=[]
    try :
        #list_bp = []
        #dico_bp = {}
        #list_temp=[]
        r=requests.get(f"http://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId={mobile_transf}")
        data=r.json()
        for j in data["results"]:
            if j["goAspect"]=="biological_process":
                list_temp.append(j["goId"])
                if j["goId"] not in list_bp:
                    list_bp.append(j["goId"])
        dico_bp[mobile_transf]=list_temp
        #print(list_temp)
        for bp in dico_bp[mobile_transf]:
            print("-", bp, "=>", go[bp].name)
        with open("./PyMOL_test/results_seq_go_protein.txt", "a") as f :
            f.write("*"*40)
            f.write('\n')
            mobile_transf = mobile.split('and guide')[0].split("(")[1].split(")")[0]
            f.write(mobile_transf) # Put convert acc_to_genename function ?
            f.write('\n')
            f.write("*"*40)
            f.write('\n')
            f.write("Sequence : "+all_seq_mobile)
            f.write('\n')
            f.write('\n')
            f.write("-"*60)
            f.write('\n')
            for bp in dico_bp[mobile_transf]:
                f.write("- "+bp+" => "+go[bp].name)
                f.write('\n')
            f.write('\n')
            f.write("-"*60)
            f.write('\n')
    except :
        try :
            #list_bp = []
            #dico_bp = {}
            #list_temp=[]
            r=requests.get(f"http://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId={convert_PDB_to_ACC(mobile_transf)}")
            data=r.json()
            for j in data["results"]:
                if j["goAspect"]=="biological_process":
                    list_temp.append(j["goId"])
                    if j["goId"] not in list_bp:
                        list_bp.append(j["goId"])
            dico_bp[convert_PDB_to_ACC(mobile_transf)] = list_temp
            #print(list_temp)
            for bp in dico_bp[convert_PDB_to_ACC(mobile_transf)]:
                print("-", bp, "=>", go[bp].name)
            with open("./PyMOL_test/results_seq_go_protein.txt", "a") as f :
                f.write("*"*40)
                f.write('\n')
                mobile_transf = mobile.split('and guide')[0].split("(")[1].split(")")[0]
                f.write(mobile_transf) # Put convert acc_to_genename function ?
                f.write('\n')
                f.write("*"*40)
                f.write('\n')
                f.write("Sequence : "+all_seq_mobile)
                f.write('\n')
                f.write('\n')
                f.write("-"*60)
                f.write('\n')
                for bp in dico_bp[convert_PDB_to_ACC(mobile_transf)]:
                    f.write("- "+bp+" => "+go[bp].name)
                    f.write('\n')
                f.write('\n')
                f.write("-"*60)
                f.write('\n')
        except :
            print("-"*40)
            print('Aucun GO term associé')
            print("-"*40)

    #!cp "./PyMOL_test/results_seq_go_protein.txt" "/content/drive/My Drive/3D_Protein_Comparison_and_Visualization/"
    #files.download("./PyMOL_test/results_seq_go_protein.txt")
    shutil.move("./PyMOL_test/results_seq_go_protein.txt")
    """
    target_seq = {'list_resn_target': []}
    cmd.iterate(f'_aln and {target}', 'list_resn_target.append(resn)', space=target_seq)
    valuesList_target = list(target_seq.values()) # Transform a dict_values into a list
    flat_list_target = [item_t for transformed_list_target in valuesList_target for item_t in transformed_list_target] # Transform a list of list into a list
    one_letter_aa_target = [_resn_to_aa[x_t] for x_t in flat_list_target] # Convert  each 3 letters AA into one letter AA
    #print(one_letter_aa_target)
    all_seq_target = ''.join(one_letter_aa_target)
    print('*'*40)
    target_transf = target.split('and guide')[0].split("(")[1].split(")")[0]
    print(target_transf) # Put convert acc_to_genename function ?
    print('*'*40)
    print(all_seq_target)
    """
    return all_seq_mobile # Return one sequence but should return a list of all the sequences (from the proteins with best RMSD)

"""#### → Coloration RMSD"""








def colorbyrmsd(mobile, target, method='cealign', doAlign=1, doPretty=1, guide=1, quiet=1): #method='cealign',

    '''
    http://pymolwiki.org/index.php/ColorByRMSD

    Original Authors: Shivender Shandilya; Jason Vertrees
    Complete rewrite by Thomas Holder

    License: BSD-2-Clause
    '''

    from chempy import cpv

    doAlign, doPretty = int(doAlign), int(doPretty)
    guide, quiet = int(guide), int(quiet)
    aln, seleboth = '_aln', '_objSelBoth'


    try:
        align = cmd.keyword[method][0]
    except:
        print(' Error: no such method: ' + str(method))
        raise CmdException

    if guide:
        mobile = '(%s) and guide' % mobile
        target = '(%s) and guide' % target

    try:
        if doAlign:
            # superpose
            align(mobile, target) #align #cmd.super

        # get alignment without superposing
        align(mobile, target, transform=0, object=aln) # align #cmd.align #, cycles=0
    except:
        print(' Error: Alignment with method %s failed CEALIGN' ) #% (method)
        raise CmdException

    cmd.select(seleboth, '(%s) or (%s)' % (mobile, target))

    idx2coords = dict()
    cmd.iterate_state(-1, seleboth, 'idx2coords[model,index] = (x,y,z)', space=locals())

    if cmd.count_atoms('?' + aln, 1, 1) == 0:
        # this should ensure that "aln" will be available as selectable object
        cmd.refresh()

    b_dict = dict()
    for col in cmd.get_raw_alignment(aln):
        assert len(col) == 2
        b = cpv.distance(idx2coords[col[0]], idx2coords[col[1]])
        for idx in col:
            b_dict[idx] = b

    cmd.alter(seleboth, 'b = b_dict.get((model, index), -1)', space=locals())

    if doPretty:
        cmd.orient(seleboth)
        cmd.show_as('cartoon', 'byobj ' + seleboth)
        cmd.color('gray', seleboth)
        cmd.spectrum('b', 'blue_red', seleboth + ' and b > -0.5')

    if not quiet:
        print(" ColorByRMSD: Minimum Distance: %.2f" % (min(b_dict.values())))
        print(" ColorByRMSD: Maximum Distance: %.2f" % (max(b_dict.values())))
        print(" ColorByRMSD: Average Distance: %.2f" % (sum(b_dict.values()) / len(b_dict)))

    seq_mobile = sequence_extraction(mobile, target)
    cmd.delete(aln)
    cmd.delete(seleboth)

"""#### → Visualisation best colored RMSD"""

## NEW





def pymol_visualization_best_rmsd(protein, data):

    ''' Open a PyMOL windows and perform a superimposition between
        FAM111B and the other proteases in order to find the lowest RMSDs  '''
    #print(protein)
    print('-- Analyse des meilleures protéines --')
    # Load the interest protein and all the other proteins structures into the PyMOL window
    #from pymol import cmd

    RMSD_min_protein = pd.read_csv("./PyMOL_test/pdb_rmsd_min.csv", delimiter = ';', header = None)
    for file_protein_pdb in RMSD_min_protein.iloc[:,0] : # os.listdir('./PDB/') ==> look at every files (anonym patients) in the associated directory
        #pdb_convert = find_pdb_without_duplicates(file_protein_pdb, data)
        try :
          target = f'./PyMOL_test/{protein}.pdb' #'../Q6SJ93_pdb.pdb'
          cmd.load(target)
        except :
          try :
            target = f'./PyMOL_test/{protein}.cif'
            cmd.load(target)
            #print(target)
          except :
            print("Impossible de récupérer la structure 3D de la protéine d'intérêt (-- retrouver le meilleure RMSD --)")
        #print(target.split('/')[2].split(".")[0])
        prot = file_protein_pdb.split(".")[0]
        #print('Protéine', prot)
        print('\n')
        print("**", target.split('/')[2].split(".")[0], "->", prot, '**')
        try :
            if file_protein_pdb != target.split(".")[0] :
                get_pdb_file(file_protein_pdb)
                cmd.load('./PyMOL_test/PDB/'+file_protein_pdb.lower()+".cif")
        except :
            try :
              if file_protein_pdb != target.split(".")[0] :
                  bootstrapping_alphafold_file_download([file_protein_pdb])
                  cmd.load('./PyMOL_test/PDB/'+file_protein_pdb+".pdb")
            except :
              print("Enable to charged the structure of the protein", file_protein_pdb)
        colorbyrmsd(prot, target.split('/')[2].split(".")[0]) #file_protein_pdb[0:4]
        cmd.zoom(target.split('/')[2].split(".")[0]) #selection = 'all'
        auto_zoom = cmd.get("auto_zoom")
        cmd.set("auto_zoom", 0)
        cmd.png(f'./PyMOL_test/image_pymol_superimposition_{prot}.png') # Capture an image of the current

        cmd.hide(representation='everything', selection="prot")
        #!cp f'./PyMOL_test/image_pymol_superimposition_{prot}.png' "/content/drive/My Drive/3D_Protein_Comparison_and_Visualization/"
       # files.download(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
        cmd.delete('all')
        #Move the file to the desired directory
        shutil.move(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')








    cmd.zoom(target.split('/')[2].split(".")[0]) #selection = 'all'
    #auto_zoom = cmd.get("auto_zoom")
    #cmd.set("auto_zoom", 0)
    cmd.png(f'./PyMOL_test/image_pymol_superimposition_{prot}.png') # Capture an image of the current display
    cmd.hide(representation='everything', selection="prot")
    #!cp f'./PyMOL_test/image_pymol_superimposition_{prot}.png' "/content/drive/My Drive/3D_Protein_Comparison_and_Visualization/"
    #files.download(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
    cmd.delete('all')
    shutil.move(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')



"""#### → Choosing specific domain to analyze for the interest protein"""










def pymol_visualization_domain(protein,data,part_target_begin,par_target_end, type_of_entry):

    ''' Open a PyMOL windows and perform a superimposition between
        FAM111B and the other proteases in order to find the lowest RMSDs  '''

    find_target(protein, type_of_entry)

    # Load the interest protein and all the other proteins structures into the PyMOL window
    from pymol import cmd
    """
    mobile = f'./PyMOL_test/{protein}.pdb' #'../Q6SJ93_pdb.pdb'
    print(mobile.split('/')[2].split(".")[0])
    cmd.load(mobile)
    """
    list_RMSD = []
    list_prot = []
    access = []
    list_prot_pdb = []
    for value in range(len(data)):
        access.append(data[value]["accession"])
    for prot in access :
      try :
        mobile = f'./PyMOL_test/{protein}.pdb' #'../Q6SJ93_pdb.pdb'
        cmd.load(mobile)
      except :
        try :
          mobile = f'./PyMOL_test/{protein}.cif'
          cmd.load(mobile)
        except :
          print("Impossible de récupérer la structure 3D de la protéine d'intérêt (-- Comparaison de structures à partir d'un domaine définit au préalable --)")
      #print(mobile.split('/')[2].split(".")[0])
      ## NEW domain
      s = cmd.select(f"resid {part_target_begin}:{part_target_begin}") # Selection les aa pour ne recuperer que le domaine à aligner
      cmd.extract("domain", "s") # enleve les aa (TEST -> color les aa)
      cmd.delete(mobile.split('/')[2].split(".")[0])
      ##
      pdb_convert = find_pdb_without_duplicates(prot, data)
      if pdb_convert not in list_prot_pdb or prot not in list_prot_pdb : # To avoid duplicates
        list_prot_pdb.append(pdb_convert)
        list_prot_pdb.append(prot)
        try :
            prot = pdb_convert.split(".")[0]
            print(prot)
            cmd.load('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
            result = cmd.cealign("domain", prot)
            RMSD = result['RMSD']
        except :
            try :
              prot = prot.split(".")[0]
              print(prot)
              cmd.load('./PyMOL_test/PDB/'+prot+".pdb")
              result = cmd.cealign("domain", prot)
              RMSD = result['RMSD']
            except :
              print("No 3D structure found for the protein", prot)
        print(RMSD)
        cmd.delete('all')
        list_prot.append(prot)
        list_RMSD.append(RMSD)
        try :
            os.remove('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
        except :
            try :
              os.remove('./PyMOL_test/PDB/'+prot+".pdb")
            except :
              print('No structure to delete (- cause : no structure charged)')
        #os.remove('./PyMOL_test/PDB/'+prot)
      else : #if pdb_convert in list_prot_pdb : # Suppress the PDB file present in double
        try :
            os.remove('./PyMOL_test/PDB/'+prot.lower()+".cif") #file_domain_cif
        except :
          try :
            os.remove('./PyMOL_test/PDB/'+prot+".pdb")
          except :
            print("Enable to suppress the ", prot, "file")
    list_prot = pd.DataFrame(list_prot)
    list_RMSD = pd.DataFrame(list_RMSD)
    list_data = [list_prot, list_RMSD] # Put all the dataframe into a list
    data_prot = pd.concat(list_data, axis = 1, ignore_index=False, sort=False) # Concatenate on the axis = 1 (columns)  all the dataframe in the list
    data_prot = data_prot.to_csv('./PyMOL_test/rmsd_prot_pymol.csv', sep = ';', index = False, header = False) # Creation of a CSV file of the concatenation --> 'file_domain_begin_end.csv',
    print(data_prot)
    cmd.zoom(selection = 'all')
    cmd.png('./PyMOL_test/image_pymol_superimposition.png') # Capture an image of the current display







def pymol_visualization_best_rmsd_domain(protein, data):

    ''' Open a PyMOL windows and perform a superimposition between
        FAM111B and the other proteases in order to find the lowest RMSDs  '''


    # Load the interest protein and all the other proteins structures into the PyMOL window
    from pymol import cmd

    RMSD_min_protein = pd.read_csv("./PyMOL_test/pdb_rmsd_min.csv", delimiter = ';', header = None)
    for file_protein_pdb in RMSD_min_protein.iloc[:,0] : # os.listdir('./PDB/') ==> look at every files (anonym patients) in the associated directory
        #pdb_convert = find_pdb_without_duplicates(file_protein_pdb, data)
        try :
          target = f'./PyMOL_test/{protein}.pdb' #'../Q6SJ93_pdb.pdb'
          cmd.load(target)
        except :
          try :
            target = f'./PyMOL_test/{protein}.cif'
            cmd.load(target)
          except :
            print("Impossible de récupérer la structure 3D de la protéine d'intérêt (-- retrouver le meilleure RMSD --)")
        prot = file_protein_pdb.split(".")[0]
        #print('Protéine', prot)
        print('\n')
        print("**", target.split('/')[2].split(".")[0], "->", prot, '**')
        try :
            if file_protein_pdb != target.split(".")[0] :
                get_pdb_file(file_protein_pdb)
                cmd.load('./PyMOL_test/PDB/'+file_protein_pdb.lower()+".cif")
        except :
            try :
              if file_protein_pdb != target.split(".")[0] :
                  bootstrapping_alphafold_file_download([file_protein_pdb])
                  cmd.load('./PyMOL_test/PDB/'+file_protein_pdb+".pdb")
            except :
              print("Enable to charged the structure of the protein", file_protein_pdb)
        colorbyrmsd(prot, target.split('/')[2].split(".")[0]) #file_protein_pdb[0:4]
        cmd.zoom(target.split('/')[2].split(".")[0]) #selection = 'all'
        auto_zoom = cmd.get("auto_zoom")
        cmd.set("auto_zoom", 0)
        cmd.png(f'./PyMOL_test/image_pymol_superimposition_{prot}.png') # Capture an image of the current display
        cmd.hide(representation='everything', selection="prot")
        #!cp f'./PyMOL_test/image_pymol_superimposition_{prot}.png' "/content/drive/My Drive/"
        #files.download(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
        # Move the file to the desired directory
        shutil.move(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
        cmd.delete('all')

    cmd.zoom(target.split('/')[2].split(".")[0]) #selection = 'all'
    #auto_zoom = cmd.get("auto_zoom")
    #cmd.set("auto_zoom", 0)
    cmd.png(f'./PyMOL_test/image_pymol_superimposition_{prot}.png') # Capture an image of the current display
    cmd.hide(representation='everything', selection="prot")
    #!cp f'./PyMOL_test/image_pymol_superimposition_{prot}.png' "/content/drive/My Drive/"
    #files.download(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')
    # Move the file to the desired directory
    shutil.move(f'./PyMOL_test/image_pymol_superimposition_{prot}.png')

    cmd.delete('all')



"""
---

## MAIN PROGRAM

---

##### PARAMETRES   

- **Target** = 'FAM111B' *(valeur par défault)* ==> nom du gène (ou ID) de la protéine d'intêret
- **Keywords** = 'protein' *(valeur par défault)*.
- **type_of_entry** = 'genename' *(valeur par défault)* ==> type de nom de protéine mis en dans le paramètre "Target". Choisir parmi les OPTIONS suivantes : "genename" (nom de gène), "PDB" (Identifiant PDB) et "uniprot" (Identifiant UniProt). Il est conseillé de favoriser les identifiants plutôt que les noms de gène.                                   
- **method_superimposition** = 'cealign' *(valeur par défault)*. Possibilité de mettre "super" (déconseillé).                                 
- **number_protein_min_rmsd** = 10 *(valeur par défault)*.
- **choose_domain** = False *(valeur par défault)*. Si ce paramètre = 'True', alors vous pourrez définir les positions du domaine de votre protéine qui vous intéresse (exemple : domaine entre les positions 444 et 690"""







def _main_3D_search_tool(target = 'FAM111B', Keywords='protein', type_of_entry = "genename", method_superimposition = 'cealign', number_protein_min_rmsd = 10, choose_domain = False):
    #target = 'FAM111B',
    requested_url = f"https://www.ebi.ac.uk/proteins/api/proteins?keywords={Keywords}&organism=Homo%20sapiens&reviewed=true&size=2000"
    data = get_url(requested_url)
    if choose_domain :
        part_target_begin = print(input('What is the begin position of your protein you want to analyze ?' ))
        part_target_end = print(input('What is the end position of your protein you want to analyze ?' ))
        pymol_visualization_domain(target,data,part_target_begin,part_target_end,type_of_entry)
        rmsd_min_extraction(number_protein_min_rmsd)
        pymol_visualization_best_rmsd_domain(target, data, part_target_begin, part_target_end)
    pymol_visualization(target,data, type_of_entry) #target
    rmsd_min_extraction(number_protein_min_rmsd) # Reading the function "lowest RMSD extraction"
    pymol_visualization_best_rmsd(target, data)

"""
---
## ▬ **RESULTS** ▬
---"""

_main_3D_search_tool(target = 'FAM111B', Keywords='ubl', type_of_entry = 'genename', number_protein_min_rmsd = 10)

# to delete the directory
#import shutil
#shutil.rmtree('./PyMOL_test/')