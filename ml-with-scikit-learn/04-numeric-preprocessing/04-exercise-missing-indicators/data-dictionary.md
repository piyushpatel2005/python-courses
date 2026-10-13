# Dataset dictionary

Two float columns are product width in cm and volume in liters, known before listing. `np.nan` means unrecorded. Only volume is missing during training, although a query width is missing too. 40 training products and three queries are synthetic at 2025-01-15; no target is supplied.

The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 40 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.

Files: `training.csv` (40 rows), `queries.csv` (3 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`width_cm`: float width in cm; `volume_l`: float packaged volume in liters. These are pre-listing/pre-handling input measurements. Empty CSV cells mean not recorded; query values do not determine training statistics.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The original 8 training rows remain an unchanged prefix; extra deterministic synthetic measurements extend training to 40 rows. Query values and membership are unchanged. The figure and short arithmetic example keep the smaller original values so you can calculate by hand.
