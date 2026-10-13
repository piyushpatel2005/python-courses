---
title: "Exercise: select features inside validation"
slug: "exercise-feature-selection"
order: 6
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "pandas"
  - "numpy"
  - "scikit-learn"
language: "python"
summary: "Put SelectKBest in Pipeline so selection learns only inside each fold."
seo_title: "Exercise: select features inside validation | Scikit-learn practice"
seo_description: "Put SelectKBest in Pipeline so selection learns only inside each fold. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "feature selection"
  - "Python practice"
---

A feature selector is fitted preprocessing: it uses training labels to decide which columns to keep. Selecting columns before cross-validation exposes every fold to information from its held-out labels. Put the selector inside a `Pipeline` so each fit learns its own selection.

`SelectKBest(f_classif, k=2)` computes a univariate class-separation score for each column and retains two. `f_classif` compares between-class variation with within-class variation; it does not detect every useful interaction. `get_support()` returns a Boolean mask in original column order. This keeps original columns. The later PCA lesson instead builds new columns by combining the originals.

The classifier follows the selector in the pipeline. The supplied three-fold `cross_val_score` clones and fits the whole pipeline on each training fold. The final fit shown in the editor still uses only the training partition. Validation labels are used to inspect predictions, never to choose the mask.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

## Dataset

The supplied `pd.read_csv` setup reads that real file and selects named feature columns; the ID column stays outside the model. The numeric indices are dimensionless synthetic measurements, not currency or measured business outcomes. `returned` is a synthetic binary teaching label; only the training partition may fit model state.

`checkout-measurements.csv` has **36 rows**, each representing one synthetic checkout.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `order_id` | Synthetic checkout record ID; excluded from predictors | string; none | ID; excluded from predictors |
| `basket_index` | Synthetic basket measurement on a dimensionless scale | float; dimensionless | Supplied predictor input |
| `item_count_index` | Synthetic checkout size index; not a literal item count | float; dimensionless | Supplied predictor input |
| `category_index` | Synthetic numeric product-mix index; not an encoded category ID | float; dimensionless | Supplied predictor input |
| `season_index` | Synthetic numeric context index; not a future timestamp | float; dimensionless | Supplied predictor input |
| `returned` | Artificial binary outcome, 0 or 1; not a feature | integer; none | Outcome label; not a predictor |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Implement `fit_selected(X, y)` as a fitted pipeline named `select` then `model`, with `SelectKBest(f_classif, k=2)` and `LogisticRegression(max_iter=300, n_jobs=1)`.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
