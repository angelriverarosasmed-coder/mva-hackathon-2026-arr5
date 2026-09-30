# Cross-species aneuploidy discovery layer

This directory documents the **proposed** Saccharomyces cerevisiae discovery layer used in the final ARR5 Track 2 framework.

## Purpose
Yeast aneuploidy data are used only to nominate conserved cellular processes that may buffer chromosome-dosage imbalance, including proteostasis, protein turnover, translation control, chaperone capacity, mitochondrial homeostasis, and stress-response state.

## Translation rule
`yeast signal -> conserved human pathway? -> phenotype present in patient-derived BUB1B-MVA cells? -> approved-drug mapping -> human-cell rescue + genomic-safety confirmation`

A yeast phenotype is **not** treated as evidence of therapeutic efficacy in MVA. Patient-derived human cells remain the decisive validation model.

## Framework
The conceptual workflow is:

**PREDICT -> PERTURB -> VALIDATE -> TRANSLATE**

1. **PREDICT:** use large-scale aneuploidy biology to nominate buffering pathways.
2. **PERTURB:** identify an experimentally testable pathway/drug relationship.
3. **VALIDATE:** require human conservation and the corresponding phenotype in patient-derived cells.
4. **TRANSLATE:** advance an approved-drug hypothesis only after target engagement, functional rescue, and genomic safety agree.

## Status
No new yeast wet-lab experiment or patient-cell experiment is claimed as completed in this hackathon submission. This layer is a hypothesis-generation strategy integrated into Arm B.
