# Dataset dictionary

One nominal string product-category feature uses pan, bowl, and mug, known before listing. 40 synthetic training items and four queries form a 2025-01-15 snapshot. There are no missing cells or novel query categories. Encoded indicators are unitless numeric features, not ordered category scores.

The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.

Files: `categories.json` (40 rows), `queries.json` (4 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`category`: nominal string metadata with the domain stated above; JSON null means absent metadata, never an unfamiliar observed string. This is an input feature available before listing, not a target.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 40 rows without adding category names. JSON null is converted to np.nan by the supplied reader.
