# ARR5 — Rare Disease, Real Kid: MVA Hackathon 2026

## Genotype-to-Rescue
A mechanism-first analysis of a **BUB1B-associated Mosaic Variegated Aneuploidy (MVA)** case, followed by systematic approved-drug hypothesis prioritization and a cross-species aneuploidy discovery layer for preclinical follow-up.

## Results at a glance
Track 1 recovered the hackathon-confirmed BUB1B variant pair at rank 1 (rank points 100/100; F-max 1.000): **NM_001211.6:c.2210T>G (p.Leu737Ter)** and **c.3006T>G (p.Asn1002Lys)**. p.Leu737Ter is treated as an established pathogenic loss-of-function allele; p.Asn1002Lys remains a VUS and phase remains unresolved.

Track 2 separates three concepts:

**RESTORE** — WT-BUB1B re-expression is the proposed genetic rescue benchmark.

**REBALANCE** — fingolimod (FTY720) is the lead Arm A approved-drug hypothesis, testing whether SET/PP2A modulation can produce kinetochore-relevant rescue and reduce chromosome missegregation.

**BUFFER** — 4-PBA is the lead Arm B proteostasis hypothesis, with arimoclomol as a mechanistically distinct comparator. Arm B advances only if the corresponding patient-cell phenotype is demonstrated and genomic stability is preserved.

### Cross-species discovery layer
Large-scale **Saccharomyces cerevisiae aneuploidy** data are used only as a hypothesis-generation engine inside Arm B:

`yeast signal -> conserved human pathway? -> patient-cell phenotype? -> approved-drug mapping -> human-cell rescue + genomic safety`

Yeast tells us what *might* matter; patient-derived human cells determine whether it actually does. Yeast evidence is never treated as direct evidence of therapeutic efficacy in MVA.

## Repository map
- `docs/ARR5_track1_report.pdf` — Track 1 report.
- `docs/ARR5_track2_report.pdf` — final Track 2 report with the yeast discovery layer.
- `submission/ARR5_bub1b-genotype-to-mechanism.csv` — Track 1 submission output.
- `track1_variant_analysis/extract_candidate_loci.py` — original candidate-locus extraction script.
- `config/candidate_loci_grch38.csv` — original candidate-locus configuration.
- `track2_drug_repurposing/data/drug_landscape.csv` — first-pass drug landscape.
- `track2_drug_repurposing/data/target_space_screen.csv` — scored target-space screen.
- `track2_drug_repurposing/data/*.xlsx` — broader audit workbooks.
- `track2_drug_repurposing/scripts/reproduce_track2.py` — deterministic reconstruction of ranking, shortlist, and decision matrix.
- `track2_drug_repurposing/METHODS.md` — methods, gates, and experimental boundaries.
- `track2_drug_repurposing/yeast_discovery/README.md` — cross-species discovery logic and translation gates.
- `track2_drug_repurposing/yeast_discovery/evidence_anchors.csv` — selected evidence anchors and boundaries.

## Quick start — Track 2
Python 3.10+ is sufficient; the reconstruction script uses only the standard library.

```bash
python track2_drug_repurposing/scripts/reproduce_track2.py
```

Expected outputs:

```text
track2_drug_repurposing/results/ranked_candidates.csv
track2_drug_repurposing/results/experimental_shortlist.csv
track2_drug_repurposing/results/decision_matrix.csv
```

The script reconstructs the prioritization already encoded in the curated target-space screen. It is **not** an efficacy-prediction model.

## Track 1
Raw genomic data are not included. Authorized users can run the included candidate-locus extraction workflow against their own local copy of the hackathon source VCF.

## Reproduced vs proposed
**Reproduced/documented here:** candidate-level Track 1 output, candidate-locus extraction workflow, curated drug landscape, target-space ranking, shortlist/disposition, decision matrix, and the cross-species translation logic.

**Proposed but not performed:** patient-derived cell experiments, WT-BUB1B rescue, allele-specific RNA/protein studies, kinetochore PP2A-B56 imaging, chromosome-missegregation assays, micronucleus assays, new yeast perturbation experiments, and drug-combination experiments.

No cellular rescue result or clinical benefit is claimed.

## Rescue Window
A pharmacologic candidate advances only if its pre-specified phenotype improves without major toxicity, extreme proliferation suppression, reduced mitotic entry, artificial mitotic arrest, increased micronuclei, increased chromosome missegregation, or greater karyotypic heterogeneity.

## Data handling
Raw hackathon genomic data are **not redistributed**. Derived candidate-level output needed to document the submitted result is included.

## Clinical boundary
This repository contains **preclinical drug-repurposing hypotheses**, not treatment recommendations. None of the proposed drugs should be administered to the child on the basis of this analysis. Cellular rescue would not establish neurological, developmental, oncologic, or systemic clinical benefit.

## AI disclosure
OpenAI ChatGPT Plus was used collaboratively for literature synthesis, code development, methodological review, adversarial hypothesis testing, scientific writing, and report development; the account-level “Improve the model for everyone” setting was subsequently disabled.
