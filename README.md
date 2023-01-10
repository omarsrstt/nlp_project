# nlp_project

### Folder Structure
```
.
S:.
├───data        # Stores datasets
│   ├───iSarcasm
│   ├───iSarcasmEval
│   │   ├───test
│   │   ├───third-party annotations
│   │   └───train
│   └───Reddit
├───models      # Models such as spacy en_core
├───outputs     # Store output files and plots
└───src
    ├───README.md
    ├───config.py
    ├───keyword_classifier.ipynb
    ├───preprocessing.ipynb
    ├───sarcasm_baseline.ipynb 
    └───test.ipynb 
```
---
### Dataset

* The iSarcasm dataset can be downloaded from [iSarcasm Dataset Link](https://aclanthology.org/attachments/2020.acl-main.118.Dataset.zip) and more details related to the dataset can be found on [Dataset ACL Anthology Page](https://aclanthology.org/2020.acl-main.118/)


* The Reddit Dataset is available is posted at the following [link](https://nlp.cs.princeton.edu/SARC/1.0/main/). A cleaned version of the dataset is also available on Kaggle [link](https://www.kaggle.com/datasets/danofer/sarcasm?resource=download&select=train-balanced-sarcasm.csv) but the test file has some problems
