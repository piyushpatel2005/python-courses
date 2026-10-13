---
title: "Exercise: assemble a mixed-feature classifier"
slug: "exercise-mixed-project-build"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Build the preprocessing and LogisticRegression pipeline on a fixed original mixed dataset with supplied sealed split."
seo_title: "Exercise: assemble a mixed-feature classifier"
seo_description: "Build the preprocessing and LogisticRegression pipeline on a fixed original mixed dataset with supplied sealed split."
seo_keywords:
  - "scikit-learn"
  - "mixed-project-build"
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
| `order_id` | Unique string order ID | Checkout; audit only, excluded from X |
| `customer_id` | Unique string customer ID; one customer per order | Checkout; audit only, excluded from X |
| `checkout_date` | ISO date, 2025-01-01 through 2025-02-28 | Provenance, excluded from X |
| `basket_value_usd` | Nonnegative float, USD | Known at checkout; numeric predictor |
| `item_count` | Positive count, stored as float to allow missing cells | Known at checkout; numeric predictor |
| `category` | Nominal furniture / kitchen / bedding | Known at checkout; categorical predictor |
| `returned_30d` | Integer 0/1; 1 means returned within 30 days | Observed after the outcome window; target |
| `actual_delivery_days` | Positive integer days until delivery | Post-checkout; forbidden predictor |

Blank basket values and item counts mean unrecorded inputs; the numeric branch learns replacement medians from training only. Other columns are complete. All 30-day labels have matured by 2025-04-01. An unseen `decor` category appears only in query checks. The fixed partitions remain 108 search-training, 36 threshold-validation, and 36 final-test rows. This stationary same-population fixture is not evidence of future-period accuracy.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

At checkout, HomeHurray Inc. wants an illustrative flag for a return within thirty days. The supplied `orders.csv` contains 180 independent synthetic orders with one customer per order. The split helper reserves 108 search-training rows, 36 threshold-validation rows, and 36 final-test rows before any preprocessing learns statistics.

Build a ColumnTransformer with a median-impute/standard-scale numeric branch and a dense one-hot category branch. `handle_unknown="ignore"` maps an unseen category such as decor to all-zero category indicators. `remainder="drop"` excludes every unspecified column, but still pass the explicit `FEATURES` list to fitting and prediction. Delivery duration is forbidden because it is unavailable at checkout. The returned pipeline is unfitted; the supplied checkpoint fits only search-training rows.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## Your Tasks

1. Return an unfitted mixed preprocessing/LogisticRegression pipeline from `build_model` using the three checkout predictors and the missing/unknown policies described above.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
