# NIRMA
# Reproducible Analysis: ARG Detection and Antibiotic Frequency Metrics

This repository contains the supplementary code used to perform antibiotic resistance gene (ARG) detection and related downstream metric extraction for the manuscript [DOI will be inserted post-acceptance]. No data are distributed within this repository.

---

## PURPOSE
To provide the exact computational procedures used to annotate antibiotic resistance determinants and quantify antibiotic class–specific frequency metrics from metagenomic assemblies and/or read-level data, in a form suitable for independent reproducibility.

---

## MATERIALS
- Python 3.10.14
- RGI (Resistance Gene Identifier) v6.0.3
- CARD Database v3.2.7
- MetaPhlAn v4.1.0 (for taxonomic steps where applicable)
- pandas==2.2.2
- numpy==1.26.4

---

## METHODS (STEPWISE — NON-EXECUTABLE FORM)

1. Perform ARG annotation against CARD 

2. Parse the RGI output tables and extract identifiers, match confidence values, drug‐class associations, and resistance ontology fields.

3. Aggregate hit-level outputs to sample‐level antibiotic class summary metrics (e.g., class presence, normalized counts, frequency ratios).

4. For analyses requiring taxonomic anchoring, derive taxonomic profiles from shotgun reads using MetaPhlAn and merge summary tables with ARG metrics at the sample level.

5. Produce final aggregated tables of antibiotic class frequencies and (where applicable) joint taxon–ARG structures for statistical consumption.

---

## OUTPUT ARTIFACTS
Running the above procedure on the original study data yields:
- Per-sample ARG annotation tables
- Aggregated antibiotic class frequency matrices
- Joint taxon–ARG summary tables (if taxonomic integration was executed)

No outputs are distributed in this repository.

---

## MANUSCRIPT REFERENCE
This code accompanies a manuscript under review. The DOI will be inserted in this section after acceptance.

