import sys
import random

with open('app/data/astral-scopdom-seqres-gd-sel-gs-bib-40-1.75.fa') as f:
    lines = f.readlines() # read all clustered lines
    lines = [l[1:].split(' ')[:2] for l in lines if l.startswith(">")] # extract all superfamily and PDB id
    pairs=[]
    for (value,key) in lines:
        substr=key.split('.')
        newkey=substr[0]+'.'+substr[1]+'.'+substr[2]
        pairs.append((newkey,value))

with open(sys.argv[1], 'r') as f:
    for line in f:
        cat=random.choice(pairs)[0]
        print(cat)
# key2paths = [(key, f"pdbstyle-2.08/{value[2:4]}/{value}.ent") for (key, value) in pairs] # parse the pdb file paths



