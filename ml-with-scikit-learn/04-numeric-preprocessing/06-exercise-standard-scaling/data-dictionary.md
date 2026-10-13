# Dataset dictionary

`train`: 100 rows of three complete float unitless generated features; `query`: three rows in that feature order. The source generator used three informative features and seed 29 at an artificial stationary 2025-01-15 snapshot; there are no missing values or IDs.

Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.

Files: `training.csv` (100 rows), `queries.csv` (3 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`feature_0` onward: complete float unitless generated inputs in their original column order. No targets or identifiers are included.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.
