# Dataset dictionary

`order_id`: string audit identifier, never a predictor. `basket_value_usd`: float USD total and `item_count`: positive integer count, both known at checkout. `actual_delivery_days`: integer days known only after delivery. `returned_30d`: integer 0/1 target known after the 30-day outcome window. These 32 synthetic checkouts are dated 2025-01-15 and their labels are observed by 2025-02-15. No values are missing.

The first 8 records preserve the original worked fixture; additional authored records extend it to 32 rows. They are synthetic, not collected customer records.

Files: `observations.csv` (32 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

CSV field names and roles are exactly the named DataFrame columns described above. Row order is preserved; no generated index column is stored.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 8 records preserve the original worked fixture; additional authored records extend it to 32 rows. They are synthetic, not collected customer records.
