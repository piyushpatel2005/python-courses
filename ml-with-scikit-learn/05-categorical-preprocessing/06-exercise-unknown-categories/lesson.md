---
title: "Exercise: handle unseen categories"
slug: "exercise-unknown-categories"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Transform novel categories with handle_unknown='ignore' and explain the all-zero row."
seo_title: "Exercise: handle unseen categories | Scikit-Learn"
seo_description: "Transform novel categories with handle_unknown='ignore' and explain the all-zero row in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "unknown categories"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: handle unseen categories

Transform kitchenware queries containing two new categories while retaining a training-only vocabulary. The demo had one unfamiliar material; this fixture has both plate and tray, neither of which should add an output column.

## Dataset

**Row grain:** one synthetic catalog item. **Files:** `categories.json` (40 rows), `queries.json` (4 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `category` | Product category: pan/bowl/mug | object string; nominal | Input metadata known before listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. JSON null means metadata not recorded; the reader converts it to np.nan, distinct from an observed unfamiliar category. Queries include additional observed strings; unknown values are not missing. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted encoder and its dense query matrix. The two novel rows should both be all zeros across the known category columns, while mug and bowl should activate their own existing columns. Preserve the full query row count and order.

Do not fit on a combined table, refit on the query, or silently replace unfamiliar text with a familiar category. Those operations either change the vocabulary or invent information. Keeping `drop=None` makes the distinction between known and unknown rows visible in this small example, though different unknown values still share the same zero representation.

The supplied setup reads `categories.json` (40 rows), `queries.json` (4 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_json(..., orient="records")` reads the actual array of record objects into a DataFrame. The reader explicitly keeps category values as object data and disables date inference. It maps JSON null to np.nan, then selects the category column before `to_numpy(dtype=object)` at the transformer boundary. Inspect `training.shape`, `training.columns`, and `training.dtypes` if the schema is unclear. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a dense `OneHotEncoder(handle_unknown="ignore", drop=None)` on `train` only and return the encoder with its query transform, giving novel categories all-zero rows without extending the vocabulary.
