---
title: "Exercise: measure cluster separation"
slug: "exercise-cluster-validation"
order: 4
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "pandas"
  - "numpy"
  - "scikit-learn"
  - "matplotlib"
language: "python"
summary: "Compute silhouette_score only for valid cluster counts and explain its geometric assumptions."
seo_title: "Exercise: measure cluster separation | Scikit-learn practice"
seo_description: "Compute silhouette_score only for valid cluster counts and explain its geometric assumptions. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "cluster validation"
  - "Python practice"
---

Silhouette compares a row's average distance to its own cluster with its average distance to the closest other cluster. A value near one indicates compact separation; near zero means a boundary, and negative values suggest a row may be closer to another group. It describes the supplied distance geometry, not business usefulness.

`silhouette_score(X, labels)` averages row silhouettes using Euclidean distance by default. It requires at least two labels and fewer labels than rows. Return `None` for invalid counts rather than letting an exploratory run crash. A singleton cluster receives silhouette zero in scikit-learn.

The supplied fixture has two compact groups. The helper should work for any valid labeling, including different numerical label names. Silhouette tends to favor compact separated clusters; it may be misleading for curved density clusters. A noise label such as -1 is treated as a label by the metric, so decide explicitly whether noise belongs in a later density-clustering evaluation.

For a nonsingleton row $i$,

$$
s_i=\frac{b_i-a_i}{\max(a_i,b_i)}.
$$

Here $a_i$ is its mean distance to other rows in its cluster, and $b_i$ the smallest mean distance to any other cluster. $s_i$ is unitless. With $a_i=1$ and $b_i=4$, $s_i=0.75$. The overall score averages $s_i$ over rows; the library handles singleton and zero-distance cases. The illustration explains the formula rather than predicting the fixture's score.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

## Dataset

The supplied `pd.read_csv` setup reads that real file and selects named feature columns; the ID column stays outside the model. The numeric indices are dimensionless synthetic measurements, not currency or measured business outcomes. The snapshot is fixed at 2025-01-15; no field is missing.

`product-measurements.csv` has **36 rows**, each representing one synthetic product measurement.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `product_id` | Synthetic product record ID; excluded from predictors | string; none | ID; excluded from predictors |
| `width_index` | Synthetic normalized width coordinate | float; dimensionless | Supplied predictor input |
| `depth_index` | Synthetic normalized depth coordinate | float; dimensionless | Supplied predictor input |
| `group_label` | Supplied arbitrary cluster name for geometric evaluation | integer; none | Evaluation label; not a predictor |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Implement `safe_silhouette(X, labels)` to return `None` unless the number of unique labels is between 2 and `len(X)-1`; otherwise return `silhouette_score(X, labels)`.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
