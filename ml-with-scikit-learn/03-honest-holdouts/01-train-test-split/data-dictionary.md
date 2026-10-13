# Dataset dictionary

`ids`: unique integer audit IDs, excluded from predictors. `X`: two complete float unitless generated features; `y`: complete float unitless synthetic target. The file preserves `make_regression` output with 80 independent rows, two informative features, noise 3, and seed 17. All inputs belong to an artificial stationary 2025-01-15 snapshot and precede the generated target.

All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.

Files: `observations.csv` (80 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`row_id`: integer audit identifier, excluded from X; `feature_0` onward: float unitless generated predictors in original order; `target`: float unitless generated outcome. All cells are complete.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.
