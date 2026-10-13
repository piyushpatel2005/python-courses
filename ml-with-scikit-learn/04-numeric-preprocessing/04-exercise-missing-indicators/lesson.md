---
title: "Exercise: keep missingness information"
slug: "exercise-missing-indicators"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use add_indicator=True and identify columns appended from training missingness."
seo_title: "Exercise: keep missingness information | Scikit-Learn"
seo_description: "Use add_indicator=True and identify columns appended from training missingness in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "missing indicators"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: keep missingness information

Append missingness flags for a different training pattern. This time only the second original feature, volume, has missing training values. The first query lacks volume, while another query lacks width, so the flags must follow the fitted feature positions rather than the demo's weight column.

## Dataset

**Row grain:** one synthetic product measurement. **Files:** `training.csv` (40 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `width_cm` | Product width | float; cm | Input recorded before listing |
| `volume_l` | Packaged volume | float; liters | Input recorded before handling/listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. An empty numeric CSV cell means not recorded, not zero; pandas reads it as NaN. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted imputer and its transformed query. Use the same median strategy and retain empty features as in the preceding lesson. The new behavior is enabling indicators; the initial original-feature columns should still contain their usual imputed values.

Inspect the output width and `indicator_.features_`. With two original columns and one flagged training column, the visible query should have three output columns. A query-only missing width must not grow another indicator column. The tests also change which training column has missingness to check that your helper respects the fitted schema.

The supplied setup reads `training.csv` (40 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return a training-fitted median `SimpleImputer` and its query transform with `add_indicator=True` and `keep_empty_features=True`, appending missingness flags after the imputed feature columns.
