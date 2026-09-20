#!/usr/bin/env python3
"""Extract predefined MVA/mitotic-fidelity loci from a GRCh38 single-sample VCF.

No gated genomic data are included in this repository.
Usage:
  python track1_variant_analysis/extract_candidate_loci.py \
      --vcf /path/to/WGS_EX2312012_HGWCNDSX7.vcf \
      --config config/candidate_loci_grch38.csv \
      --outdir results
"""
import argparse, csv
from pathlib import Path

def norm_chrom(c):
    c=c.strip()
    return c if c.startswith("chr") else "chr"+c

def parse_gt(fmt, sample):
    keys=fmt.split(":"); vals=sample.split(":")
    d=dict(zip(keys, vals))
    return d.get("GT",""), d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--vcf",required=True)
    ap.add_argument("--config",required=True)
    ap.add_argument("--outdir",required=True)
    a=ap.parse_args()
    out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)

    loci=[]
    with open(a.config,newline="") as f:
        for r in csv.DictReader(f):
            loci.append((r["gene"],norm_chrom(r["chrom"]),int(r["start"]),int(r["end"])))

    headers=["GENE","CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO","FORMAT","SAMPLE"]
    all_rows=[]; total=0
    with open(a.vcf,encoding="utf-8",errors="replace") as f:
        for line in f:
            if line.startswith("#"): continue
            total += 1
            p=line.rstrip("\n").split("\t")
            if len(p)<10: continue
            chrom=norm_chrom(p[0]); pos=int(p[1])
            for gene,c,s,e in loci:
                if chrom==c and s<=pos<=e:
                    all_rows.append([gene,chrom,pos,p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]])
                    break

    def write(name, rows):
        with open(out/name,"w",newline="",encoding="utf-8") as f:
            w=csv.writer(f,delimiter="\t"); w.writerow(headers); w.writerows(rows)

    write("01_ALL_CANDIDATE_LOCI.tsv",all_rows)
    passed=[r for r in all_rows if r[7]=="PASS"]
    write("02_PASS_VARIANTS.tsv",passed)

    het=[]; homalt=[]
    for r in passed:
        gt,_=parse_gt(r[9],r[10])
        alleles=gt.replace("|","/").split("/")
        if len(alleles)==2 and "." not in alleles:
            if alleles[0]!=alleles[1]: het.append(r)
            elif alleles[0]!="0": homalt.append(r)
    write("03_HETEROZYGOUS_PASS.tsv",het)
    write("04_HOMOZYGOUS_ALT_PASS.tsv",homalt)
    write("05_BUB1B_COMPLETE.tsv",[r for r in all_rows if r[0]=="BUB1B"])

    counts={g:0 for g,_,_,_ in loci}
    for r in passed: counts[r[0]]+=1
    with open(out/"07_GENE_COUNTS.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["GENE","PASS_COUNT"])
        for g in counts: w.writerow([g,counts[g]])

    targets={40209701:("T","G","p.Leu737Ter"),40220612:("T","G","p.Asn1002Lys")}
    found=[]
    for r in passed:
        if r[0]=="BUB1B" and r[2] in targets and r[4]==targets[r[2]][0] and targets[r[2]][1] in r[5].split(","):
            found.append((r[1],r[2],r[4],r[5],targets[r[2]][2],r[10]))

    with open(out/"06_QC_SUMMARY.txt","w") as f:
        f.write("Reference build: GRCh38\n")
        f.write(f"Total VCF records scanned: {total}\n")
        f.write(f"Candidate-locus variants: {len(all_rows)}\n")
        f.write(f"PASS: {len(passed)}\n")
        f.write(f"Heterozygous PASS: {len(het)}\n")
        f.write(f"Homozygous-alt PASS: {len(homalt)}\n")
        for x in found: f.write("BUB1B target FOUND: %s:%s %s>%s %s SAMPLE=%s\n"%x)
        f.write("\nImportant: locus extraction is not full functional annotation.\n")
        f.write("Phase cannot be established from two unphased 0/1 VCF calls alone.\n")
    print("Done:",out)

if __name__=="__main__":
    main()
