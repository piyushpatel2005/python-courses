# Dataset dictionary

`train`, `validation`: complete float package weights in kg measured before handling. 32 independent synthetic training rows and two distinct validation rows belong to a stationary 2025-01-15 snapshot. No target is needed to demonstrate preprocessing leakage; partition membership is supplied.

The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 32 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.

Files: `training.csv` (32 rows), `queries.csv` (2 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`weight_kg`: float weight in kg. These are pre-listing/pre-handling input measurements. Empty CSV cells mean not recorded; query values do not determine training statistics.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 32 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.
