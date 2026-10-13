# Dataset dictionary

`X_train`, `X_valid`: complete float unitless synthetic measurement column, ignored by this dummy. `y_train`, `y_valid`: float synthetic handling cost in USD observed after measurement. Sixty independent training rows and twenty validation rows form a stationary 2025-01-15 teaching fixture, with deliberately repeated target values and no business-performance claim.

The training and validation files retain the original row counts, repeated target patterns, feature values, and partition membership exactly.

Files: `training.csv` (60 rows), `validation.csv` (20 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`feature_0`: float unitless input ignored by the dummy; `target`: float synthetic handling cost in USD. Both files are complete; their filenames define the fixed training/validation roles.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The training and validation files retain the original row counts, repeated target patterns, feature values, and partition membership exactly.
