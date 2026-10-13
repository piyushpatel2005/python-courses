# Dataset dictionary

`amount`: float package weight in kg, known before handling; negative values are invalid and `np.nan` means an unrecorded measurement. `label`: complete integer 0/1 later inspection flag, used only to audit target balance. All 32 rows are synthetic; duplicate rows are deliberate defects, not verified duplicate entities.

The first 8 records preserve the original worked fixture; additional authored records extend it to 32 rows. They are synthetic, not collected customer records.

Files: `observations.csv` (32 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

CSV field names and roles are exactly the named DataFrame columns described above. Row order is preserved; no generated index column is stored.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 8 records preserve the original worked fixture; additional authored records extend it to 32 rows. They are synthetic, not collected customer records.
