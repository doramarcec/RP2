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

Citation metadata is also available in [`CITATION.cff`](CITATION.cff) (used by GitHub's "Cite this repository" feature) for BibTeX and other formats.

### License

The code in this repository is licensed under the [MIT License](LICENSE). The dissertation abstract and figures are made available under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
