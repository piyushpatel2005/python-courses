---
title: "Exercise: audit a feature table"
slug: "exercise-data-quality"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Return a compact audit of missing cells duplicates invalid ranges and target imbalance without automatic deletion."
seo_title: "Exercise: audit a feature table | Scikit-Learn"
seo_description: "Return a compact audit of missing cells duplicates invalid ranges and target imbalance without automatic deletion in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "data quality"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: audit a feature table

Audit a synthetic order-value table whose defects differ from the package example. Implement the same four-entry report using the helper argument. There are 40 rows, two missing cells, and invalid values at different positions, so copying the visible demo's counts will not work.

## Dataset

**Row grain:** one synthetic order record. **Files:** `orders.csv` (40 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `amount` | Order value | float; USD | Known at checkout |
| `label` | Return flag | integer; 0/1 | Later outcome; audit/stratification only |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. An empty numeric CSV cell means not recorded, not zero; pandas reads it as NaN. Deliberate repeated rows and negative amounts are audit defects; do not delete them automatically. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Use exactly these keys: `missing_fraction`, `duplicate_rows`, `invalid_amounts`, and `positive_fraction`. The label column is complete and binary. Missing fractions use all table cells as their denominator, whereas positive fractions use the number of rows. The duplicate count includes only later occurrences of identical complete rows.

Do not fill, drop, sort, or deduplicate the table in this function. Those would be data changes rather than an audit. The supplied row-count probe helps you notice accidental deletion, and the tests also compare the table before and after the helper call.

The supplied setup reads `orders.csv` (40 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. Inspect `table.shape` for row/column counts, `table.columns` for names, and `table.dtypes` for parsed types. A DataFrame keeps that schema visible while the audit works on cells. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return the four-entry audit dictionary described above without modifying the table: missing-cell fraction, repeated full-row count after the first copy, negative amount count, and label-1 fraction.
