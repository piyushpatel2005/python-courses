# Dataset dictionary

One nominal material feature has wood/metal/fabric in training and glass as an observed novel query category. 32 synthetic training rows and three query products have complete metadata available before listing on 2025-01-15. Novel does not mean missing; there are no NaN markers. Output indicators are unitless.

The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 32 rows without adding category names. JSON null is converted to np.nan by the supplied reader.

Files: `categories.json` (32 rows), `queries.json` (3 rows). The column names in those files map directly to the roles and units above. Training/query filenames encode supplied membership; they are not model features.

`category`: nominal string metadata with the domain stated above; JSON null means absent metadata, never an unfamiliar observed string. This is an input feature available before listing, not a target.

## Provenance

Original synthetic HomeHurray Inc. teaching fixtures. No real customer records or business-performance claims. The first 12 training categories and every query value are unchanged. Additional synthetic products extend training to 32 rows without adding category names. JSON null is converted to np.nan by the supplied reader.
