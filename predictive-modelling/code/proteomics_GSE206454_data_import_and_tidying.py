#!/usr/bin/python

# The data obtained from Tarca et al. (2021) study accessible at GEO GSE206454 accession number. 
# Study title: Human Plasma Proteome During Normal Pregnancy
# Number of study participants = 519
# DOI: 10.1021/acs.jproteome.2c00391

import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
import os
#csv.field_size_limit(sys.maxsize)

# Set the working directory
os.chdir('c:/Users/doram/Desktop/Masters/RP-2/code')

# Verify the change
print("Current Working Directory:", os.getcwd())

# Find where the data table begins
print("Looking for the start of the data table in GSE206454_family.soft file...")
with open("../data/tarca-et-al-2021/GSE206454_family.soft", 'r') as f: 
    lines = f.readlines()

# Look for the start of tabular data (usually after "!platform_table_begin")
start_idx = None
for i, line in enumerate(lines):
    if "!platform_table_begin" in line.lower() or line.startswith("ID\t"):
        start_idx = i + 1  # Start after this line
        break

if start_idx:
    data = pd.read_csv("../data/tarca-et-al-2021/GSE206454_family.soft", 
                       sep="\t", 
                       skiprows=start_idx,
                       low_memory=False)
else:
    print("Could not find data table start.")

# Export the entire data + metadata file
data.to_csv("../output/tarca_et_al_2021/GSE206454-term-only/full_data+metadata.csv", index = False)
print("Data file successfully loaded, read, and exported into a full_data+metadata.csv file.")

# 1.0 Restructure the somamer target metadata
print("Restructuring the somamer target matadata file...")
# Create a metadata file
somamer_target_metadata = data[0:7597] 
# Remove the last row
somamer_target_metadata = somamer_target_metadata[:-1]
somamer_target_metadata

# Export metadata to csv file
somamer_target_metadata.to_csv("../output/tarca_et_al_2021/GSE206454-term-only/somamer_target_metadata.csv", index = False)
print("Somamer target metadata file was successfully loaded, read, restructured, and saved to somamer_target_metadata.csv file.")

# 2.0 Build a sample metadata file
print("Building a sample metadata file...")
# Create an empty dictionary
metadata_dict = {
    "Accession": [],
    "Title": [],
    "Sample_type": [],
    "GA": [],
    "Organism": [],
    "Individual": []
}

# Fill in the dictionary with the correct metadata
try:
    with open("../data/tarca-et-al-2021/GSE206454_family.soft", 'r') as f: 
        lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith("^SAMPLE"):
                parts = line.split()
                if len(parts) >= 3:
                    accession = parts[2]
                    metadata_dict["Accession"].append(accession)

            if line.startswith("!Sample_title"):
                parts = line.split()
                if len(parts) >= 3:
                    title = parts[2]
                    metadata_dict["Title"].append(title)

            if line.startswith("!Sample_type"):
                parts = line.split()
                if len(parts) >= 3:
                    sample_type = parts[2]
                    metadata_dict["Sample_type"].append(sample_type)

            if line.startswith("!Sample_characteristics_ch1 = gestational age:"):
                parts = line.split()
                if len(parts) >= 5:
                    ga = parts[4]
                    metadata_dict["GA"].append(ga)

            if line.startswith("!Sample_characteristics_ch1 = individual:"):
                parts = line.split()
                if len(parts) >= 4:
                    individual = parts[3]
                    metadata_dict["Individual"].append(individual)

            if line.startswith("!Sample_organism_ch1"):
                parts = line.split()
                if len(parts) >= 4:
                    organism = " ".join(parts[2:])
                    metadata_dict["Organism"].append(organism)

except Exception as e:
    print(f"An error occurred: {e}")

# QC: Check if the numbers are correct (519 study participants = all values should be 519)
print("The dictionary file successfully built. Checking if the values are correct... Expecting all values to be 519.")
for key, value in metadata_dict.items():
    print(f"{key}: {len(value)}")

# Convert the dictionary to a data frame
sample_metadata = pd.DataFrame(metadata_dict)
sample_metadata

# Export the data frame to a csv file
sample_metadata.to_csv("../output/tarca_et_al_2021/GSE206454-term-only/sample_metadata.csv", index = False)
print("Sample metadata file has been generated and saved into sample_metadata.csv file.")

# 3.0 Build a data file
print("Building a data file...")
# Create an empty dictionary
data_dict = {
    "Accession": [],
    "ID_REF": [],
    "Log2RFU": []
}

# Fill in the dictionary with the correct data
reading_table = False
try:
    with open("../data/tarca-et-al-2021/GSE206454_family.soft", 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith("^SAMPLE"):
                parts = line.split()
                if len(parts) >= 3:
                    accession = parts[2]

            elif line.startswith("ID_REF") and "VALUE" in line:
                reading_table = True  
                continue
    
            elif reading_table:
                if line.startswith("!sample_table_end"):
                    reading_table = False  
                    continue
    
                parts = line.split()
                if len(parts) == 2:
                    id_ref, value = parts
                    data_dict["Accession"].append(accession)
                    data_dict["ID_REF"].append(id_ref)
                    data_dict["Log2RFU"].append(float(value))

except Exception as e:
    print(f"An error occurred: {e}")

# QC: check the structure of the dictionary
data_dict

# QC: check if the numbers are correct (expecting all values to be 3942324)
print("The dictionary file successfully built. Checking if the values are correct... Expecting all values to be 3942324.")
for key, value in data_dict.items():
    print(f"{key}: {len(value)}")

# Convert the dictionary to a data frame
prot_data = pd.DataFrame(data_dict)
prot_data

# Export the data frame to a csv file
prot_data.to_csv("../output/tarca_et_al_2021/GSE206454-term-only/data.csv", index = False)
print("The data file has been successfully generated and saved to data.csv file.")

# 4.0 Merge the data with the metadata
print("Merging the data with the metadata now...")
# Merge the protein data with the somamer target metadata
data_targets_merged = pd.merge(prot_data, somamer_target_metadata, left_on='ID_REF', right_on='ID', how='inner')
data_targets_merged

# Check for the non-human samples
print("Checking for non-human samples...")
#data_targets_merged.value_counts('Organism')

# Remove any non-human samples
print("Removing non-human samples...")
data_targets_merged = data_targets_merged[data_targets_merged['Organism'] == 'Human']

# QC: Confirm only human samples are left
data_targets_merged.value_counts('Organism')

# Merge the above with the sample metadata
merged_controls = pd.merge(data_targets_merged, sample_metadata, on='Accession', how='inner')
merged_controls

# Export the full data into a csv file
merged_controls.to_csv("../output/tarca_et_al_2021/GSE206454-term-only/full_data_merged.csv", index = False)
print("The data has been successfully merged and saved to a full_data_merged.csv file.")