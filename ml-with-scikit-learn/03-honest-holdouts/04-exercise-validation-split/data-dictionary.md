# Dataset dictionary

`ids`: integer row positions, not predictors. `X`: three complete float unitless generated features; `y`: float unitless target. The 100-row synthetic regression setup uses three informative columns, noise 5, and seed 29 at an artificial stationary 2025-01-15 snapshot. Feature rows precede generated outcomes.

All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.

Files: `observations.csv` (100 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`row_id`: integer audit identifier, excluded from X; `feature_0` onward: float unitless generated predictors in original order; `target`: float unitless generated outcome. All cells are complete.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. All original rows, target values, row IDs, and row order are preserved. The lesson keeps its original split fractions and seeds. Float columns use round-trip CSV parsing.
