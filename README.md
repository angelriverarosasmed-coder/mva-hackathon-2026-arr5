# ARR5 — MVA Hackathon 2026 Track 1

## Purpose
Reproducible extraction and QC workflow for the Track 1 MVA genomic analysis.

## Primary finding
The submitted prediction is a candidate compound-heterozygous BUB1B pair:
- GRCh38 chr15:40209701 T>G — NM_001211.6:c.2210T>G; p.Leu737Ter
- GRCh38 chr15:40220612 T>G — NM_001211.6:c.3006T>G; p.Asn1002Lys

p.Leu737Ter is treated as the established pathogenic loss-of-function allele.
p.Asn1002Lys remains a missense VUS. Phase was not established from the supplied
VCF, so the report does not claim confirmed biallelic disease-causing variants.

## Reproducibility
The repository contains:
- `config/candidate_loci_grch38.csv` — predefined MVA/mitotic-fidelity loci.
- `track1_variant_analysis/extract_candidate_loci.py` — standard-library Python
  script that scans the challenge VCF and reproduces locus extraction/QC.
- `submission/ARR5_bub1b-genotype-to-mechanism.csv` — final Track 1 prediction.
- `docs/ARR5_track1_report.pdf` — methods/interpretation report.

Example:
```bash
python track1_variant_analysis/extract_candidate_loci.py   --vcf /path/to/WGS_EX2312012_HGWCNDSX7.vcf   --config config/candidate_loci_grch38.csv   --outdir results
```

## Data boundary
No gated VCF/BAM/CRAM, genome-wide genotype table, or other restricted raw
patient genomic data are included. Users must obtain the challenge dataset
through the official gated access process.

## AI assistance
OpenAI ChatGPT (Plus plan) supported literature discovery/synthesis, drafting,
methodology/code planning, and targeted review of reduced/candidate-level
VCF-derived data. Before final submission, the methods report should state the
user's verified relevant ChatGPT data-handling setting/terms; this repository
does not infer or invent that account-specific setting.
