# Project 1

This group project focused on building a file converter for text datasets from the UC Irvine Machine Learning Repository so they could be used with WEKA, the open-source machine learning software.

WEKA:
https://ml.cms.waikato.ac.nz/weka/

The current layout separates source code from archived data artifacts:

- `src/` contains the Python converter script.
- `data/raw/` contains the original text datasets used as converter inputs.
- `data/converted/` contains generated `.arff` files produced by the converter.
- `data/results/` contains archived result outputs from the group project, organized by dataset.

Within `data/results/`, dataset directories use readable snake_case names that match the underlying datasets, such as `abalone`, `cmc`, `letter_rec`, `tic_tac_toe`, and `wine`.

Result filenames also use readable snake_case so the dataset, model, and validation setup are easy to scan at a glance. For example: `wine_-_logistic_regression_w_10_fold_cross_validation_-_17sep17.txt`.

The converter script in `src/arff_converter.py` reads `.txt` datasets from `data/raw/` and writes generated `.arff` files into `data/converted/` for later use in WEKA.
