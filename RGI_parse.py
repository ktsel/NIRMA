import pandas as pd
import glob
import os

# ============================================================================
# RGI (Resistance Gene Identifier) Output Processing Script
# Purpose: Standardization, quality filtering, and mapping to NG-STAR loci
# ============================================================================

# --- 1. Data Loading ---
files = sorted(glob.glob("WHO_*.txt"))
if not files:
    raise FileNotFoundError("No WHO_*.txt files found in working directory")

dfs = []
for f in files:
    strain = os.path.basename(f).replace(".txt", "")
    try:
        df = pd.read_csv(f, sep="\t", low_memory=False)
        df["Source"] = strain
        dfs.append(df)
    except Exception as e:
        print(f"Warning: file {strain} not processed ({e})")

raw = pd.concat(dfs, ignore_index=True)

# --- 2. Column Name Standardization ---
rename_map = {
    "Drug Class": "Drug_Class",
    "Resistance Mechanism": "Resistance_Mechanism",
    "Percentage Length of Reference Sequence": "RefLength_Pct"
}
raw = raw.rename(columns=rename_map)

# --- 3. Quality Filtering ---
# Criteria: Cut_Off = Perfect/Strict, identity ≥ 90%, coverage ≥ 80%
filtered = raw.copy()
filtered = filtered[filtered["Cut_Off"].isin(["Perfect", "Strict"])]

filtered["Best_Identities"] = pd.to_numeric(
    filtered["Best_Identities"], errors="coerce"
)
filtered["RefLength_Pct"] = pd.to_numeric(
    filtered.get("RefLength_Pct", pd.Series(100, index=filtered.index)), 
    errors="coerce"
)

filtered = filtered[
    (filtered["Best_Identities"] >= 90) &
    (filtered["RefLength_Pct"] >= 80)
].copy()

# --- 4. Resistance Gene Mapping to NG-STAR Loci ---
# Correspondence between CARD nomenclature and NG-STAR typing scheme
locus_mapping = {
    # Beta-lactams
    "penA": "penA",
    "ponA": "ponA",
    "TEM": "blaTEM",
    "OXA": "blaOXA",
    "PBP1A": "ponA",
    # Macrolides
    "23S rRNA": "23S_rRNA",
    "erm": "erm",
    "mph": "mph",
    "mef": "mef",
    # Efflux systems
    "mtrR": "mtrR",
    "mtrC": "mtrCDE",
    "mtrD": "mtrCDE",
    "mtrE": "mtrCDE",
    # Porins
    "porB": "porB",
    # Tetracyclines
    "tetM": "tetM",
    # Fluoroquinolones
    "gyrA": "gyrA",
    "parC": "parC",
}

def map_to_ngstar_locus(row):
    """
    Determines corresponding NG-STAR locus based on 
    gene name and family from CARD database
    """
    search_text = (
        f"{row.get('Best_Hit_ARO', '')} "
        f"{row.get('AMR Gene Family', '')}"
    ).lower()
    
    for gene_pattern, ngstar_locus in locus_mapping.items():
        if gene_pattern.lower() in search_text:
            return ngstar_locus
    return None

filtered["NGSTAR_locus"] = filtered.apply(map_to_ngstar_locus, axis=1)

# --- 5. Final Table Construction ---
output_columns = [
    "Source",
    "Best_Hit_ARO",
    "NGSTAR_locus",
    "Drug_Class",
    "Resistance_Mechanism",
    "Best_Identities",
    "RefLength_Pct",
    "Model_type",
    "Cut_Off",
    "SNPs_in_Best_Hit_ARO"
]

# Select only existing columns
output_columns = [col for col in output_columns if col in filtered.columns]

tidy = filtered[output_columns].sort_values(
    ["Source", "NGSTAR_locus", "Best_Hit_ARO"]
)

# --- 6. Results Export ---
tidy.to_csv("RGI_tidy_filtered.csv", index=False)
print(f"Strains processed: {tidy['Source'].nunique()}")
print(f"Total records: {len(tidy)}")
print("Results saved to: RGI_tidy_filtered.csv")
