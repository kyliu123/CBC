import os
import random
import sys

os.system('conda install -c conda-forge -c bioconda foldseek')

with open('app/data/astral-scopdom-seqres-gd-sel-gs-bib-40-1.75.fa') as f:
    lines = f.readlines() # read all clustered lines
lines = [l[1:].split(' ')[:2] for l in lines if l.startswith(">")] # extract all superfamily and PDB id
file2scope={}
pairs=[]
for (value,key) in lines:
    substr=key.split('.')
    newkey = substr[0] + '.' + substr[1] + '.' + substr[2]
    file2scope[value]=newkey
    pairs.append((newkey,value))
result=[]
ans=0
with open (sys.argv[1],'r') as f :
    for line in f:
        line= line.strip()
        os.system('foldseek easy-search '+line+' targetDB ./result/out tmpFolder >not')
        if os.path.getsize('./result/out')==0:
            cat=random.choice(pairs)[0]
            print(cat)
        else:
            with open('./result/out') as f:
                line=f.readline()
                file=(line.split('\t')[1]).split('.')[0]
            if file in file2scope:
                print(file2scope[file])
            else:
                print(random.choice(pairs)[0])

            

