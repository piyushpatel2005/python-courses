---
title: "Exercise: tune with stratified folds"
slug: "exercise-mixed-project-tune"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Tune C on search-training rows only, reserving separate threshold-validation and final-test rows."
seo_title: "Exercise: tune with stratified folds"
seo_description: "Tune C on search-training rows only, reserving separate threshold-validation and final-test rows."
seo_keywords:
  - "scikit-learn"
  - "mixed-project-tune"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

This cumulative exercise uses the fixed checkout-order fixture, distinct from the preceding furniture-handling analogue.

## Dataset

`orders.csv` contains 180 original synthetic HomeHurray Inc. observations. One independent synthetic checkout order per row, with a distinct customer for each order. These are teaching data, not actual company performance.

| Column | Meaning and type / unit | Availability / role |
|---|---|---|
| `basket_value_usd` | Nonnegative float, USD | Known at checkout; numeric predictor |
| `item_count` | Positive count, stored as float to allow missing cells | Known at checkout; numeric predictor |
| `category` | Nominal furniture / kitchen / bedding | Known at checkout; categorical predictor |

This stage keeps the same fields and partitions. Keep the unique string `order_id` and `customer_id` fields and the ISO `checkout_date` (2025-01-01 through 2025-02-28) for audits, never as predictors. `returned_30d` is the observed integer 0/1 target; positive means returned within 30 days. `actual_delivery_days` is a post-delivery integer day count and stays outside X.

Blank basket values and item counts mean unrecorded inputs; the numeric branch learns replacement medians from training only. Other columns are complete. All 30-day labels have matured by 2025-04-01. An unseen `decor` category appears only in query checks. The fixed partitions remain 108 search-training, 36 threshold-validation, and 36 final-test rows. This stationary same-population fixture is not evidence of future-period accuracy.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

The previous stage's CSV bytes, splits, and mixed pipeline are preserved. This stage selects the logistic regularization parameter C without looking at threshold-validation labels or final-test outcomes. `logistic__C` reaches into the named pipeline step.

Pass only the search-training table to `tune_model`. Compare C values 0.1, 1, and 10 with three shuffled stratified folds and macro F1. Every fold refits the entire preprocessing pipeline. `refit=True` fits the selected pipeline on the same search-training partition after comparison; it does not authorize fitting on validation. The reserved validation rows have a different job in the next stage.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## Your Tasks

1. Return `tune_model(train)` as the specified three-C, three-fold macro-F1 search fitted only on the supplied search-training rows.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
