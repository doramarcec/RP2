#!/usr/bin/python

import pandas as pd

# Import the data
preterm_data = pd.read_csv("output/tarca_et_al_2021/GSE150167-term+preterm/full_data_merged.csv")
term_data = pd.read_csv("output/tarca_et_al_2021/GSE206454-term-only/full_data_merged.csv")

# Add GEO accessions
preterm_data['GEO_accession'] = 'GSE150167'
term_data['GEO_accession'] = 'GSE206454'

# Add the Group column to the term data and label as controls
term_data['Group'] = 'Control'

# Are all the Organism values the same and coming from human samples? Yes, they are. 
#term_data.value_counts('Organism_x')
#term_data.value_counts('Organism_y')

# Remove redundant columns 
term_data = term_data.drop(['Organism_x', 'Organism_y', 'ID', 'ID_REF', 'SPOT_ID', 'SeqIdVersion', 'Type', 'Units'], axis = 1)
preterm_data = preterm_data.drop(['ID', 'PT_LIST', 'Sample_channel_count', 'Tissue', 'DiagnosisGA', 'SPOT_ID'], axis = 1)

# Harmonize the column names
preterm_data = preterm_data.rename(columns={'ENTREZ_GENE_ID_LIST': 'EntrezGeneID'})
term_data = term_data.rename(columns={'SomaId': 'ID_REF'})

# Add GA_delivery column and fill with NaNs
term_data['GA_delivery'] = 'NaN'
term_data

# Filter the term dataset to only contain entrez gene symbols present in preterm dataset
filtered_term_data = term_data[term_data['EntrezGeneSymbol'].isin(preterm_data['EntrezGeneSymbol'])]
filtered_term_data

# Concatenate the two datasets
merged_data = pd.concat([preterm_data, filtered_term_data], ignore_index=True)
merged_data

# Export the merged dataset
merged_data.to_csv("output/tarca_et_al_2021/merged_datasets_for_modelling.csv", index=False) # Explore this dataset further in R
