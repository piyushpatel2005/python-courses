# Dataset dictionary

`ids`: integer row positions used only for partitioning. `labels`: complete integer 0/1 synthetic return labels, with 64 zeros and 16 ones; no predictors are used in this boundary demonstration. Independent artificial checkouts occur on 2025-01-15, with 30-day labels observed by 2025-02-15.

All original IDs, label counts, and order are preserved; the file changes storage, not the stratification problem. The reader declares int32 columns and produces native np.intp arrays because the count probe expects native integer input rather than a wider CSV-inferred integer dtype.

Files: `labels.csv` (80 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`row_id`: integer row-position identifier for split audits, not a predictor; `label`: complete integer class code 0 or 1 used for stratification.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. All original IDs, label counts, and order are preserved; the file changes storage, not the stratification problem. The reader declares int32 columns and produces native np.intp arrays because the count probe expects native integer input rather than a wider CSV-inferred integer dtype.
