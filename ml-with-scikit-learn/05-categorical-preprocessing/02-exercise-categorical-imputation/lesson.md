---
title: "Exercise: fill missing categories"
slug: "exercise-categorical-imputation"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use a categorical SimpleImputer with an explicit missing marker and sentinel policy."
seo_title: "Exercise: fill missing categories | Scikit-Learn"
seo_description: "Use a categorical SimpleImputer with an explicit missing marker and sentinel policy in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "categorical imputation"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: fill missing categories

Fill absent kitchenware categories with the reserved sentinel. The category names and missing positions differ from the material demo. The query also includes `"plate"`, which is unfamiliar to training but is not missing.

## Dataset

**Row grain:** one synthetic catalog item. **Files:** `categories.json` (40 rows), `queries.json` (4 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `category` | Product category: pan/bowl/mug | object string; nominal | Input metadata known before listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. JSON null means metadata not recorded; the reader converts it to np.nan, distinct from an observed unfamiliar category. Queries include additional observed strings; unknown values are not missing. The imputation sentinel `missing` is reserved, not a genuine category. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted imputer and the completed query matrix. Keep the object dtype in the supplied fixtures so NaN remains a missing marker rather than a literal string. The helper should replace only those markers, leaving every observed category exactly as provided.

Do not fill absence with the most common category or convert new observed categories to the sentinel. Those policies answer different questions. The output should still have one feature column and the same query row count. The tests include an all-missing training column to verify that your explicit retention policy works.

The supplied setup reads `categories.json` (40 rows), `queries.json` (4 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_json(..., orient="records")` reads the actual array of record objects into a DataFrame. The reader explicitly keeps category values as object data and disables date inference. It maps JSON null to np.nan, then selects the category column before `to_numpy(dtype=object)` at the transformer boundary. Inspect `training.shape`, `training.columns`, and `training.dtypes` if the schema is unclear. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a `SimpleImputer` using `missing_values=np.nan`, `strategy="constant"`, `fill_value="missing"`, and `keep_empty_features=True`; return it and its query transform without changing observed strings.
