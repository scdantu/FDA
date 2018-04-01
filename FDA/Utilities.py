#!/usr/bin/python
import os, sys

def check_folder(folder_to_create):
    if(os.path.isdir(folder_to_create)==False):
        mkdir="mkdir %s"%(folder_to_create)
        os.system(mkdir)
def write_file(fname,data):
    fwrite=open(fname,"w")
    fwrite.write(data)

def check_file(file_name):
    if(os.path.isfile(file_name)==False):
        print ("%s does not exist. Exiting"%(file_name))
        exit()
def aa_map(residue):
    dict={"ALA":"A",
          "ARG":"R",
          "ASN":"N",
          "ASP":"D",
          "CYS":"C",
          "GLN":"Q",
          "GLU":"E",
          "GLY":"G",
          "HIS":"H",
          "HIP":"H",
          "HIE":"H",
          "ILE":"I",
          "LEU":"L",
          "LYS":"K",
          "MET":"M",
          "PHE":"F",
          "PRO":"P",
          "SER":"S",
          "THR":"T",
          "TYR":"Y",
          "TRP":"W",
          "VAL":"V",
          "DC":"DC",
          
          }
    if(residue in dict):
        return dict[residue]
    else:
        return residue
    


