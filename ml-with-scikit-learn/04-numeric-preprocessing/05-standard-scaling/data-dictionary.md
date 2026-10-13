# Dataset dictionary

`train`: 80 rows of two float unitless generated features; `query`: two complete rows with the same schema. The source generator had two informative features and seed 17. This is an artificial stationary 2025-01-15 feature snapshot, not measured product data.

Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.

Files: `training.csv` (80 rows), `queries.csv` (2 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`feature_0` onward: complete float unitless generated inputs in their original column order. No targets or identifiers are included.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. Training and query numeric values are unchanged from the original pinned-generator fixture. The unused synthetic target is intentionally not included because scaling has no target input.
