# Dataset dictionary

`train`, `query`: float package weight in kg followed by float volume in liters, known before handling. `np.nan` means an unrecorded measurement, not zero. The 32 training packages and two query packages are original synthetic rows at 2025-01-15; no target is used.

The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 32 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.

Files: `training.csv` (32 rows), `queries.csv` (2 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`weight_kg`: float weight in kg; `volume_l`: float packaged volume in liters. These are pre-listing/pre-handling input measurements. Empty CSV cells mean not recorded; query values do not determine training statistics.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 32 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.
