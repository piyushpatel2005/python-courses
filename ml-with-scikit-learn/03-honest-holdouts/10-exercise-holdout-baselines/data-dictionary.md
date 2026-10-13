# Dataset dictionary

`X_train`, `X_valid`: complete float unitless synthetic feature, ignored by the dummy. `y_train`, `y_valid`: complete integer 0/1 synthetic 30-day return targets. Seventy-five training and twenty-five validation checkouts are independent artificial rows dated 2025-01-15, observed through 2025-02-15.

The training and validation files retain the original row counts, repeated target patterns, feature values, and partition membership exactly.

Files: `training.csv` (75 rows), `validation.csv` (25 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`feature_0`: float unitless input ignored by the dummy; `target`: integer 0/1 outcome label. Both files are complete; their filenames define the fixed training/validation roles.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The training and validation files retain the original row counts, repeated target patterns, feature values, and partition membership exactly.
