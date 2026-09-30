# Track 2 Methods and Reproducibility

## Objective
ARR5 uses a mechanism-first **Genotype-to-Rescue** framework to prioritize approved-drug hypotheses for preclinical follow-up in BUB1B-associated Mosaic Variegated Aneuploidy (MVA).

The framework separates:

- **RESTORE** — WT-BUB1B re-expression as a proposed genetic rescue benchmark.
- **REBALANCE (Arm A)** — pharmacologic compensation of ongoing chromosome-segregation error.
- **BUFFER (Arm B)** — controlled buffering of a measured consequence of established aneuploidy.

The Saccharomyces cerevisiae component is a **discovery layer within Arm B**, not a third therapeutic arm.

## Drug prioritization
The curated target-space screen maps candidates to BUBR1 stability, PP2A/kinetochore regulation, proteostasis, redox/ISR biology, mTOR/autophagy, and mitochondrial homeostasis. The supplied reconstruction script deterministically rebuilds the ranking, experimental shortlist, and decision matrix from that curated table.

The score ranks **experiments**, not predicted clinical efficacy.

## Cross-species discovery layer
Large-scale yeast aneuploidy data can nominate conserved buffering processes. The required translation sequence is:

`yeast signal -> conserved human pathway? -> phenotype present in patient cells? -> approved-drug mapping -> human-cell rescue + genomic safety`

Yeast results are hypothesis-generating only. They do not constitute evidence that a candidate will work in BUB1B-MVA.

## Arm A primary endpoint
Chromosome missegregation events per observed mitosis.

Fingolimod advances only if biochemical engagement is accompanied by kinetochore-relevant change and a reproducible reduction in missegregation within the Rescue Window.

## Arm B rule
A candidate advances only if the corresponding patient-cell stress phenotype is demonstrated first. Improved homeostasis is insufficient if chromosome instability worsens.

## Rescue Window
A candidate fails if apparent improvement is explained by major toxicity, extreme proliferation suppression, reduced mitotic entry, artificial mitotic arrest, increased micronuclei, increased chromosome missegregation, increased karyotypic heterogeneity, or expansion of genomically unstable cells.

## What this repository reproduces
- the curated drug landscape;
- the target-space ranking;
- the experimental shortlist/disposition;
- the decision matrix;
- the documented logic connecting the screen to the proposed experimental program;
- the Track 1 candidate-locus extraction workflow, when run by an authorized user against the source genomic data.

## What is proposed, not performed
- patient-derived fibroblast drug exposure;
- WT-BUB1B rescue experiments;
- allele-specific RNA studies;
- BUBR1 turnover/localization studies;
- kinetochore PP2A-B56 imaging;
- chromosome-missegregation and micronucleus assays;
- new yeast perturbation experiments;
- cross-species wet-lab validation;
- combination experiments.

No cellular rescue result or clinical benefit is claimed.

## Clinical boundary
The drug candidates are preclinical hypotheses for further investigation, not treatment recommendations.
