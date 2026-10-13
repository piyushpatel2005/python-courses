# Dataset dictionary

`amount`: float order value in USD at checkout; negative values are invalid and `np.nan` means not recorded. `label`: complete integer 0/1 later return flag, a target rather than a checkout predictor. 40 synthetic rows include deliberately repeated records. Row position is not a predictor.

The first 10 records preserve the original worked fixture; additional authored records extend it to 40 rows. They are synthetic, not collected customer records.

Files: `orders.csv` (40 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

CSV field names and roles are exactly the named DataFrame columns described above. Row order is preserved; no generated index column is stored.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 10 records preserve the original worked fixture; additional authored records extend it to 40 rows. They are synthetic, not collected customer records.
