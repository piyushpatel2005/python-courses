# Dataset dictionary

`ids`: integer row positions for selecting aligned arrays, never predictors. `X`: two complete float unitless synthetic features; `y`: float unitless target. The exported 80-row regression fixture uses seed 17, two informative columns, and noise 3 at an artificial stationary 2025-01-15 snapshot.

All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.

Files: `observations.csv` (80 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`row_id`: integer audit identifier, excluded from X; `feature_0` onward: float unitless generated predictors in original order; `target`: float unitless generated outcome. All cells are complete.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.
