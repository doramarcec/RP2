# Predictive modelling of prematurity in asymptomatic singleton gestations using maternal plasma proteomics

This repository contains all the code and computational work undertaken as part of my (RP1) dissertation submitted to The University of Manchester for the degree of Master of Science in Bioinformatics and Systems Biology in the Faculty of Biology, Medicine and Health.

---

### Abstract
Premature birth is the leading cause of neonatal mortality and morbidity worldwide. It has 
multiple aetiologies and clinical phenotypes, making it challenging to comprehend the 
underlying drivers of phenotype shift from term to preterm during gestation. This project 
integrated two maternal plasma proteomics datasets to identify differentially expressed 
proteins, visualise the network topology of term and preterm phenotypes in second and third 
trimester via hypergraph analysis, and develop a machine learning classifier to detect term 
versus preterm phenotype based on maternal plasma protein abundance data. The results 
identified 459 and 462 differentially expressed proteins in second and third trimester, 
respectively, and a significant difference in network topology in the second trimester, compared 
to the third trimester. The developed machine learning model achieved AUC of 1.0 (95% CI: 
0.996–0.999), showing great potential in future applications. Future directions for the project 
include development of a hypergraph neural network using the selected features from this 
model for more informed predictions that account for network topology. 

### Repository structure
The project repository is structured in the following manner:

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


