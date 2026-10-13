---
title: "Exercise: project standardized features"
slug: "exercise-pca"
order: 10
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "pandas"
  - "numpy"
  - "scikit-learn"
  - "matplotlib"
language: "python"
summary: "Fit PCA on training data and inspect explained_variance_ratio_ without labeling components as selected raw features."
seo_title: "Exercise: project standardized features | Scikit-learn practice"
seo_description: "Fit PCA on training data and inspect explained_variance_ratio_ without labeling components as selected raw features. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "pca"
  - "Python practice"
---

PCA replaces correlated columns with orthogonal linear combinations called components. It centers the training matrix and finds directions of high variance. A component is not a selected input column, and high variance does not guarantee usefulness for a target.

`PCA(n_components=2, svd_solver="full")` learns two directions. `transform` gives two coordinates per new row. `inverse_transform` maps those coordinates back into the original feature space; discarded directions mean the reconstruction is approximate. The preceding demo used the external digits benchmark. Here the supplied matrix instead has three original correlated numeric measurements on a common dimensionless scale.

Fit on training rows before transforming validation. `explained_variance_ratio_` gives one fraction per retained component relative to total training variance. Summing those fractions describes retained variance, not predictive accuracy. Component signs may flip without changing the represented subspace. PCA centers but does not scale columns, so this unscaled example is appropriate only for columns measured on comparable scales.

For $q$ retained components, cumulative explained variance is

$$
R_q=\sum_{j=1}^{q}r_j.
$$

Here $r_j$ is component $j$'s explained-variance fraction and $R_q$ is their total. All are unitless. For illustrative ratios $0.60$ and $0.25$, $R_2=0.85$, or 85% of training variance. The editor computes the corresponding sum for its actual fitted data rather than assuming these illustrative ratios.

This exercise uses 36 original synthetic rows with three dimensionless correlated measurements, not digits. The stored rows were generated from two seeded latent measurements and small independent noise. The goal is a two-coordinate representation; no generator runs in your helper.

## Dataset

The supplied `pd.read_csv` setup reads that real file and selects named feature columns; the ID column stays outside the model. The numeric indices are dimensionless synthetic measurements, not currency or measured business outcomes. The snapshot is fixed at 2025-01-15; no field is missing.

`product-measurements.csv` has **36 rows**, each representing one synthetic product measurement.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `product_id` | Synthetic product record ID; excluded from predictors | string; none | ID; excluded from predictors |
| `width_index` | Synthetic normalized width coordinate | float; dimensionless | Supplied predictor input |
| `depth_index` | Synthetic normalized depth coordinate | float; dimensionless | Supplied predictor input |
| `height_index` | Synthetic correlated height coordinate | float; dimensionless | Supplied predictor input |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Fit and return a two-component `PCA` with `svd_solver="full"` from `fit_projection(X)`; do not fit on the validation array.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
