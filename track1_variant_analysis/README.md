# Track 1 reproducibility note

The submitted Track 1 result is preserved at `../submission/ARR5_bub1b-genotype-to-mechanism.csv` and the complete report at `../docs/ARR5_track1_report.pdf`.

The existing project repository previously used:

```text
track1_variant_analysis/extract_candidate_loci.py
config/candidate_loci_grch38.csv
```

for GRCh38 candidate-locus extraction. Those source files should be retained from the existing GitHub repository rather than replaced by reconstructed code. This package intentionally does not fabricate a replacement script when the original source file is not present in the current artifact set.

Raw VCF/BAM/CRAM/FASTQ data are not included and should not be committed to the public repository.
