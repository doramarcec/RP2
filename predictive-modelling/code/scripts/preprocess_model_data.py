#!/usr/bin/python

import pandas as pd

def process_model_data(second_trimester_data, third_trimester_data, model):
    """
    Process data for either a outcome classification model or GA regression model. 

    Parameters
    ----------
    second_trimester_data : pd.DataFrame
        Long-format data for second trimester
    third_trimester_data : pd.DataFrame
        Long-format data for third trimester
    model : str
        Either 'outcome' (binary classification using Group) 
        or 'ga' (regression using GA_delivery)
    
    Returns
    -------
    full_data_model : pd.DataFrame
        Combined dataset from second and third trimester
    """
    
    # Remove PPROM samples
    second_trimester_data = second_trimester_data[second_trimester_data['Group'] != "PPROM"].copy()
    third_trimester_data = third_trimester_data[third_trimester_data['Group'] != "PPROM"].copy()

    # Change group labels to numbers
    mapping = {'Control': 0, 'sPTD': 1}
    second_trimester_data.loc[:, 'Group'] = second_trimester_data['Group'].replace(mapping)
    third_trimester_data.loc[:, 'Group'] = third_trimester_data['Group'].replace(mapping)
        
    # Pivot the data into a wide format
    second_trimester_wide = second_trimester_data.pivot(index = 'Accession', columns = 'Target', values = 'Log2RFU')
    third_trimester_wide = third_trimester_data.pivot(index = 'Accession', columns = 'Target', values = 'Log2RFU')
    
    # Merge with the original data to include relevant columns
    second_trimester_model2 = pd.merge(second_trimester_wide, second_trimester_data, on='Accession', how='inner')
    third_trimester_model2 = pd.merge(third_trimester_wide, third_trimester_data, on='Accession', how='inner')

    if model == 'outcome':
        target = 'Group'
        drop_cols = ['GA_delivery', 'GEO_accession', 'Target', 'Log2RFU'] if 'GA_delivery' in second_trimester_model2.columns else []
    elif model == 'ga':
        target = 'GA_delivery'
        drop_cols = ['Group', 'GEO_accession', 'Target', 'Log2RFU'] if 'Group' in second_trimester_model2.columns else []
    else:
        raise ValueError(f"Invalid model: {model}. Must be 'outcome' or 'ga'.")

    # def finalize(df, trimester):
    #     # Add trimester column
    #     df['Trimester'] = trimester
    #     # Move trimester column to the front
    #     cols = ['Trimester'] + [c for c in df.columns if c != 'Trimester']
    #     return df[cols]
    # second_trimester_model2 = finalize(second_trimester_model, 2)
    # third_trimester_model2 = finalize(third_trimester_model, 3)

    # Reorder: target column first, followed by all other predictors
    def prepare(df):
        reordered = df[[target] + [c for c in df.columns if c != target]]
        return reordered.drop(columns=drop_cols, errors='ignore')
    second_trimester_model3 = prepare(second_trimester_model2)
    third_trimester_model3 = prepare(third_trimester_model2)

    # Merge the datasets
    full_data_model = pd.concat([second_trimester_model3, third_trimester_model3], ignore_index = True, join = 'outer')
    full_data_model = full_data_model.drop_duplicates()

    # Expect 690 rows 
    return full_data_model