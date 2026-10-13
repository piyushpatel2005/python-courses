# Dataset dictionary

One object-dtype nominal product-category feature: pan/bowl/mug during training, with plate as a new observed query value. `np.nan` means unavailable metadata and the string `missing` is a reserved sentinel. 40 synthetic training items and four queries are catalog snapshots available before listing on 2025-01-15; no target is used.

The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.

Files: `categories.json` (40 rows), `queries.json` (4 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`category`: nominal string metadata with the domain stated above; JSON null means absent metadata, never an unfamiliar observed string. This is an input feature available before listing, not a target.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.
