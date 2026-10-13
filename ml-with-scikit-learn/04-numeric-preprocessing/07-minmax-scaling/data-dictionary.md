# Dataset dictionary

`train`: 80 complete rows of two unitless float generated features; `query`: two rows with the same schema, including extremes. The source generator used seed 17 and two informative features at an artificial stationary 2025-01-15 snapshot; it is not actual product data.

Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.

Files: `training.csv` (80 rows), `queries.csv` (2 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`feature_0` onward: complete float unitless generated inputs in their original column order. No targets or identifiers are included.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.
