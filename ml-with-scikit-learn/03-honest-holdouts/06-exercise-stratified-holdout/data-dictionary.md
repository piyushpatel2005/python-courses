# Dataset dictionary

`ids`: integer row positions, not model features. `labels`: complete integer 0/1 synthetic return labels, with 60 zeros and 40 ones. Independent artificial checkout rows are dated 2025-01-15; all 30-day outcomes are observed by 2025-02-15. There are no missing labels.

All original IDs, label counts, and order are preserved; the file changes storage, not the stratification problem. The reader declares int32 columns and produces native np.intp arrays because the count probe expects native integer input rather than a wider CSV-inferred integer dtype.

Files: `labels.csv` (100 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`row_id`: integer row-position identifier for split audits, not a predictor; `label`: complete integer class code 0 or 1 used for stratification.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. All original IDs, label counts, and order are preserved; the file changes storage, not the stratification problem. The reader declares int32 columns and produces native np.intp arrays because the count probe expects native integer input rather than a wider CSV-inferred integer dtype.
