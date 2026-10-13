# Dataset dictionary

`order_id`: string audit ID. `basket_value_usd`: float USD and `item_count`: positive integer, both available at checkout. `actual_delivery_days`: integer days, available later. `returned_30d`: 0/1 target after 30 days. `return_reason`: later string none/size/damage, a target proxy unavailable at checkout. 40 synthetic checkouts are dated 2025-01-15; labels are observed by 2025-02-15. Values are complete.

The first 10 records preserve the original worked fixture; additional authored records extend it to 40 rows. They are synthetic, not collected customer records.

Files: `orders.csv` (40 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

CSV field names and roles are exactly the named DataFrame columns described above. Row order is preserved; no generated index column is stored.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 10 records preserve the original worked fixture; additional authored records extend it to 40 rows. They are synthetic, not collected customer records.
