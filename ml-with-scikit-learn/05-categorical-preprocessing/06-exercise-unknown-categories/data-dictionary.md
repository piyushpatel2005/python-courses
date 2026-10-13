# Dataset dictionary

One nominal product-category feature has pan/bowl/mug in training and plate/tray as observed novel categories. 40 synthetic training items and four queries are dated 2025-01-15 with metadata known before listing. All cells are observed, and there is no target or ID predictor.

The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.

Files: `categories.json` (40 rows), `queries.json` (4 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`category`: nominal string metadata with the domain stated above; JSON null means absent metadata, never an unfamiliar observed string. This is an input feature available before listing, not a target.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.
