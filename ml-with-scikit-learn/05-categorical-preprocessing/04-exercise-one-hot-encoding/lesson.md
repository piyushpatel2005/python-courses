---
title: "Exercise: encode nominal categories"
slug: "exercise-one-hot-encoding"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit OneHotEncoder(sparse_output=False) and read get_feature_names_out."
seo_title: "Exercise: encode nominal categories | Scikit-Learn"
seo_description: "Fit OneHotEncoder(sparse_output=False) and read get_feature_names_out in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "one hot encoding"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: encode nominal categories

Encode a different vocabulary of kitchenware categories. The returned indicator order must come from the fitted encoder, not from the material example's names. The query repeats one category so you can verify that equal categories produce equal numeric rows.

## Dataset

**Row grain:** one synthetic catalog item. **Files:** `categories.json` (40 rows), `queries.json` (4 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `category` | Product category: pan/bowl/mug | object string; nominal | Input metadata known before listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. JSON null means metadata not recorded; the reader converts it to np.nan, distinct from an observed unfamiliar category. All supplied queries use known categories; this lesson keeps the unknown-category policy as error. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the encoder, its dense query transform, and the names produced for input column `category`. Preserve every learned category with `drop=None`. The printed names are part of interpreting the result, not decorative labels you can invent independently of the numeric columns.

Keep the unknown-category policy as `"error"` here. All supplied queries are known, and the next lesson handles novel values. The hidden checks change the number and order of training categories, so a fixed three-column matrix will not satisfy the general encoding contract.

The supplied setup reads `categories.json` (40 rows), `queries.json` (4 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_json(..., orient="records")` reads the actual array of record objects into a DataFrame. The reader explicitly keeps category values as object data and disables date inference. It maps JSON null to np.nan, then selects the category column before `to_numpy(dtype=object)` at the transformer boundary. Inspect `training.shape`, `training.columns`, and `training.dtypes` if the schema is unclear. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a dense `OneHotEncoder` on training categories with `handle_unknown="error"` and `drop=None`; return `(encoder, encoded_query, names)` using `get_feature_names_out(["category"])`.
