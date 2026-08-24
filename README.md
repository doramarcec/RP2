# Predictive modelling of prematurity in asymptomatic singleton gestations using maternal plasma proteomics

This repository contains all the code and computational work undertaken as part of my (RP1) dissertation submitted to The University of Manchester for the degree of Master of Science in Bioinformatics and Systems Biology in the Faculty of Biology, Medicine and Health.

---

### Abstract
Premature birth is the leading cause of neonatal mortality and morbidity worldwide. It has 
multiple aetiologies and clinical phenotypes, making it challenging to comprehend the 
underlying drivers of phenotype shift from term to preterm during gestation. This project 
integrated two maternal plasma proteomics datasets to identify differentially expressed 
proteins, visualise the network topology of term and preterm phenotypes in the second and third 
trimester via hypergraph analysis, and develop a machine learning classifier to detect term 
versus preterm phenotype based on maternal plasma protein abundance data. The results 
identified 459 and 462 differentially expressed proteins in the second and third trimester, 
respectively, and a significant difference in network topology in the second trimester, compared 
to the third trimester. The developed machine learning model achieved an AUC of 1.0 (95% CI: 
0.996–0.999), showing great potential in future applications. Future directions for the project 
include development of a hypergraph neural network using the selected features from this 
model for more informed predictions that account for network topology. 

### Main results 

PCA of sample signals demonstrates efficient batch correction across second (left) and third (right) trimesters, with clear 
clustering based on the underlying biology. In second and third trimester data, the first principal 
component (PC1) explains 17.26% and 27.68% of variance, respectively, whereas the second 
principal component (PC2) explains 12.07% and 7.46% of variance. Total 
cumulative variance explained by 20 PCs is 61.76%. The PC1 scores were found to differ 
significantly across control, pPROM and sPTD groups, meaning that the three 
pregnancy outcomes differ across the primary, and strongest, axis of variance in the data – 
ultimately depicting that the features (i.e. plasma proteins) that load onto and strongly 
contribute to PC1, also known as the first latent variable (LV1), are differentially expressed 
across pregnancy outcomes, with the strongest difference occurring between control and sPTD 
samples.
<img width="5591" height="2091" alt="RP2-batch-correction-PCA" src="https://github.com/user-attachments/assets/68c2eb6b-2ee6-4653-b788-283db41a1560" />

A binary classification model has been developed, using a random forest classifier, to assess 
the predictive power of plasma protein abundance data in predicting sPTD. Five sets of 50 
selected features were used to train separate models for comparison, including i) PC1 loadings, 
ii) differentially expressed proteins, iii-iv) proteins with normalised ranks in the 90th and 10th 
percentile of the hypergraph, and v) proteins whose normalised ranks are in the 90th percentile 
in controls and 10th percentile in sPTD group. In evaluation, this project focused on specificity, 
sensitivity and AUC as evaluation metrics due to their high adoption and prevalence in 
biomedical and clinical studies, accompanied by MCC for validation. 
<img width="1500" height="1000" alt="ai-ml-models" src="https://github.com/user-attachments/assets/76f6b4f5-7b03-47b7-84f4-56d5e90091b7" />

The cross-validation scores [...] follow a consistent 
increase until 500 data samples, where they decrease together with the training scores. Despite 
the different patterns, ROC analysis yielded an AUC of 1.0 (95% CI: 0.996–0.999) and 0.99 
(95% CI: 0.989–0.998) for models trained on the PC1 loadings and DE proteins as features, 
respectively, suggesting excellent discriminative ability against the control and sPTD classes. Both models achieved specificity of 1.0 and sensitivity of 0.99, suggesting a strong 
capability of accurately identifying positive classes while minimising false positives. The 
model scoring third by predictive power was trained on the top 50 proteins with the lowest 
normalised ranks in the 10th percentile of central clusters from the hypergraph analysis. That 
model achieved an AUC of 0.90 (95% CI: 0.875–0.934), specificity of 0.87 and sensitivity of 
0.85, suggesting strong predictive potential among central cluster proteins within the 10th 
percentile of hypergraph normalised ranks, compared to highly functional proteins in the 90th 
percentile, which achieved an AUC of 0.5 (95% CI: 0.447–0.557), equivalent to random 
guessing, demonstrating no evidence of discriminatory ability between sPTD and control 
groups.  

The PC1 and DE-feature models reached an MCC of 0.96, reaching a strong positive 
correlation between predicted and true group classifications, and reinforcing the previous 
model evaluation, demonstrating robust and strong predictive abilities of these features. The 
model trained on the 10th percentile proteins reached an MCC of 0.56, a moderate positive 
correlation, whereas models trained on the 90th percentile proteins, and proteins that were 
within the 90th percentile in controls but in 10th percentile in the sPTD group had MCC values 
of 0, indicating no correlation between predicted and true group classifications.  

From the selected protein features from PC1 loadings, DE and 10th percentile proteins used to 
train the model, 40%, 26%, and 18% were found evolutionarily constrained (LOEUF < 0.6), 
respectively, whereas no overlap with human accelerated regions was found by genomic ranges 
encoding the plasma proteins used.  

### Repository structure
The project repository is structured in the following manner:

```
002_RP2/
├── hypergraph/
│   ├── hypergraph.Rproj
│   ├── code/
│   ├── data/
│   │   ├── HARs/science.abm1696_table_s1.xlsx
│   │   ├── loeuf/gnomad.v4.1.constraint_metrics.tsv
│   │   ├── hu_et_al_2025/
│   │   │   ├── hu_amnion_obs.csv / _var.csv / _X.csv
│   │   │   └── data_conversion/ (Rmd + amnion.h5ad/.h5Seurat + GSE260715_amnion.RData(.gz))
│   │   └── tarca_et_al_2021/
│   └── output/
│       └── tarca/ 
├── predictive-modelling/
│   ├── code/ 
│   ├── data/
│   │   ├── clinical-means-of-preterm-birth-prediction.xlsx
│   │   └── tarca-et-al-2021/ 
│   └── output/
│       └── tarca_et_al_2021/
└── single-cell-exploration/
    ├── notebooks/
    ├── data/
    │   ├── arutyunyan-et-al-2023/
    │   ├── barrozo-et-al-2023/ 
    │   ├── suryawanshi-et-al-2018/ 
    │   ├── sc-prematurity/ 
    │   ├── vento-tormo-et-al-2018/ 
    │   ├── wang-et-al-2024/ 
    │   └── uhm-et-al-2025/ 
    └── output/
        ├── ivans/
        └── wang/
```

### Requirements

This project combines a Python workflow (`predictive-modelling/`) and an R workflow (`hypergraph/`). The `single-cell-exploration/` was an exploratory part conducted at early stages of the project, that did not make it into the results. Package requirements and versions are listed below. 

#### Python (`predictive-modelling/`)

| Package         | Version |
|-----------------|---------|
| Python          | 3.12.1  |
| Jupyter Lab     | 4.4.5   |
| pandas          | 2.2.3   |
| matplotlib      | 3.9.2   |
| numpy           | 2.0.0   |
| sklearn         | 1.6.1   |
| seaborn         | 0.13.2  |
| plotly          | 5.24.1  |
| pycombat        | 0.3.3   |
| neuroCombat     | 0.2.12  |
| harmonypy       | 0.0.10  |
| fancyimpute     | 0.7.0   |
| scipy           | 1.16.0  |
| torch           | 2.7.1   |
| torch_geometric | 2.6.1   |

#### R (`hypergraph/`)

| Package                           | Version       | 
|-----------------------------------|---------------|
| R                                 | 4.4.1         |
| RStudio                           | 2024.12.1+563 |
| tidyverse                         | 2.0.0         |
| rstatix                           | 0.7.2         |
| dendextend                        | 1.19.1        |
| gplots                            | 3.2.0         |
| plyr                              | 1.8.9         |
| ggpubr                            | 0.6.1         |
| ggsci                             | 3.2.0         |
| BioQC                             | 1.34.0        |
| readxl                            | 1.4.5         |
| GenomicRanges                     | 1.58.0        |
| GenomicFeatures                   | 1.58.0        |
| AnnotationDbi                     | 1.68.0        |
| TxDb.Hsapiens.UCSC.hg38.knownGene | 3.20.0        |
| org.Hs.eg.db                      | 3.20.0        |
| annotables                        | 0.2.0         |
| clusterProfiler                   | 4.14.6        |
| enrichplot                        | 1.26.6        |
| pathview                          | 1.46.0        |
| janitor                           | 2.2.1         |

### Citation

If you use or refer to this work, please cite it as:

Marčec, D. (2026). *Predictive modelling of prematurity in asymptomatic singleton gestations using maternal plasma proteomics* [Master's thesis, University of Manchester]. GitHub. https://github.com/doramarcec/RP2

### License

The code in this repository is licensed under the [MIT License](LICENSE). The dissertation abstract, text (`Main results`) and figures are made available under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
