# NIRMA
# Reproducible Analysis: ARG Detection and Antibiotic Frequency Metrics

This repository contains the supplementary code used to perform antibiotic resistance gene (ARG) detection, phenotype correlation, and comparative benchmarking against NG-STAR for the manuscript [DOI will be inserted post-acceptance]. No genomic data are distributed within this repository.

---

## PURPOSE
To provide the exact computational procedures used to:
* Annotate antibiotic resistance determinants in N. gonorrhoeae genomes.
* Compare the performance of the general-purpose CARD/RGI pipeline against the species-specific NG-STAR scheme.
* Visualize the resistome architecture

---

## MATERIALS
- Python 3.10.14
- RGI (Resistance Gene Identifier) v6.0.3
- CARD Database v3.2.7
- NG-STAR (v2.0.0) / PubMLST
- pandas==2.2.2
- numpy==1.26.4
- seaborn & matplotlib (for visualization)

---
## REPOSITORY CONTENTS
1. `RJBCH_suppl_code.ipynb`
- Processing raw RGI outputs to create the clean dataset (`RGI_tidy_filtered.csv`).
- Aggregating hit-level outputs to strain-level summary metrics
- Linking genotypes to phenotypic data.

2. `compare_card_ngstar.ipynb`
- Harmonizing outputs from CARD/RGI and NG-STAR.
- Performing head-to-head comparison of allele calls across 7 canonical loci.
- Calculating concordance metrics and generating the comparative summary table (`CARD_vs_NGSTAR_FINAL_COMPARISON.csv`).

---
## METHODS (STEPWISE — NON-EXECUTABLE FORM)

1. Perform ARG annotation against CARD 

2. Parse the RGI output tables and extract identifiers, match confidence values, drug‐class associations, and resistance ontology fields.

3. Parse NG-STAR outputs (from PubMLST/CLI) and map CARD predictions to NG-STAR loci to quantify concordance.

4. Aggregate hit-level outputs to sample‐level antibiotic class summary metrics.


---

## OUTPUT ARTIFACTS
Running the above procedure on the original study data yields:
- `RGI_tidy_filtered.csv`: Cleaned matrix of detected resistance genes.
- `CARD_vs_NGSTAR_FINAL_COMPARISON.csv`: Detailed side-by-side comparison of allele calls.
- Per-sample ARG annotation tables
- Aggregated antibiotic class frequency matrices
- Joint taxon–ARG summary tables (if taxonomic integration was executed)

No outputs are distributed in this repository.

---

## MANUSCRIPT REFERENCE
This code accompanies a manuscript under review. The DOI will be inserted in this section after acceptance.

