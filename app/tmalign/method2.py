import subprocess
import sys

def TMalign(path1, path2):
    try:
        result = subprocess.run(["./TMalign", path1, path2], capture_output=True, text=True)
        ret = result.stdout.split('\n')
        ret = [r for r in ret if r.startswith('TM-score')]
        return float(ret[1].split()[1])
    except:
        return 0

def main():
    with open('astral-scopdom-seqres-gd-sel-gs-bib-40-1.75.fa') as f:
        lines = f.readlines() # read all clustered lines
    lines = [l[1:].split(' ')[:2] for l in lines if l.startswith(">")] # extract all superfamily and PDB id
    pairs=[]
    for (value,key) in lines:
        substr=key.split('.')
        newkey=substr[0]+'.'+substr[1]+'.'+substr[2]
        pairs.append((newkey,value)) #key是scope类别 value是文件名

    # pairs = [(key[:-2], value) for (value, key) in lines] # rearrange to (key, value) pairs
    key2paths = [(key, f"pdbstyle-2.08/{value[2:4]}/{value}.ent") for (key, value) in pairs] # parse the pdb file paths
    # 一个类别里的所有文件
    grouped_spf = {} # grouped superfamilies
    for k,p in key2paths:
        if k not in grouped_spf:
            grouped_spf[k] = []
        grouped_spf[k].append(p)
    ori= sys.argv[1]
    spfscore = {k: 0 for k in grouped_spf}
    result=[]
    with open(ori) as ori_file:
        ori_paths = ori_file.readlines()
        for o in ori_paths:
            for key in grouped_spf:
                score=0
                for p in grouped_spf[key]:
                    o, p= o.strip(), p.strip()
                    score =max(score,TMalign(o,p))
                spfscore[key]=score
            result.append(max(spfscore,key=spfscore.get))
    with open('datas/out3.lst','w') as f:
        for i in result:
            f.write("%s\n" %i)
if __name__ == "__main__":
    main()
