#!/usr/bin/env python3
"""Reconstruct ARR5 Track 2 ranked outputs from the preserved curated screen.

This script reproduces the *reported prioritization*; it does not predict efficacy
and it does not recreate literature curation from raw publications.
"""
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
INPUT = BASE / "data" / "target_space_screen.csv"
OUT = BASE / "results"
OUT.mkdir(exist_ok=True)

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def fnum(x, default=10**9):
    try: return float(x)
    except (TypeError, ValueError): return default

rankable = [r for r in rows if str(r.get("Rankable", "")).strip().lower() == "true"]
ranked = sorted(rankable, key=lambda r: (fnum(r.get("Screen rank")), -fnum(r.get("Priority score"), 0)))

with (OUT / "ranked_candidates.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(ranked)

short = [r for r in ranked if r.get("Screen verdict", "").strip().upper() == "ADVANCE"]
with (OUT / "experimental_shortlist.csv").open("w", newline="", encoding="utf-8") as f:
    fields = ["Screen rank","Candidate","Arm","Mechanism","Priority score","Screen verdict","Interpretation"]
    w=csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(short)

decisions = [
    {"observed_patient_cell_state":"BUB1B-rescuable PP2A/CIN phenotype","path":"WT-BUB1B benchmark -> Arm A fingolimod","advance_requirement":"Target engagement plus reduced missegregation within Rescue Window"},
    {"observed_patient_cell_state":"Proteostasis phenotype","path":"Arm B 4-PBA + arimoclomol mini-screen","advance_requirement":"Correction of measured homeostatic defect with preserved genomic stability"},
    {"observed_patient_cell_state":"Both phenotypes","path":"Validate A and B independently; combine only after single-agent rescue","advance_requirement":"Each arm passes its own functional and safety gates"},
    {"observed_patient_cell_state":"Neither phenotype","path":"Remap mechanism and drug landscape","advance_requirement":"No forced nomination"},
]
with (OUT / "decision_matrix.csv").open("w", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(decisions[0].keys())); w.writeheader(); w.writerows(decisions)

print(f"Loaded {len(rows)} candidates; wrote {len(ranked)} rankable candidates and {len(short)} ADVANCE candidates.")
