---
title: "Exercise: set an operational threshold"
slug: "exercise-mixed-project-threshold"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use a reserved validation partition to select a stated recall-constrained threshold after train-only CV."
seo_title: "Exercise: set an operational threshold"
seo_description: "Use a reserved validation partition to select a stated recall-constrained threshold after train-only CV."
seo_keywords:
  - "scikit-learn"
  - "mixed-project-threshold"
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

The fitted search winner now supplies return scores for the separate threshold-validation rows. Find the column for class 1 through `classes_`; do not assume a probability column means positive without checking class order.

Compare thresholds 0.3, 0.5, and 0.7 with `score >= threshold`. Among choices with recall at least 0.75, choose highest precision, then highest threshold. If none qualifies, choose highest recall, then precision, then lowest threshold. This fallback reports the best available candidate rather than pretending the constraint was met.

Keep the fitted model unchanged after selecting the threshold. Refitting on train plus validation would change its scores and break the meaning of the chosen threshold. Final-test rows remain unused.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## Your Tasks

1. Implement `choose_threshold(model, validation)` with the stated three-candidate recall constraint and tie rules, without changing the fitted model.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
