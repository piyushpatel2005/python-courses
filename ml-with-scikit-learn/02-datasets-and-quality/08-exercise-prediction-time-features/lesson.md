---
title: "Exercise: exclude unavailable features"
slug: "exercise-prediction-time-features"
order: 8
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Select a feature schema available at prediction time and exclude IDs target proxies and post-outcome columns."
seo_title: "Exercise: exclude unavailable features | Scikit-Learn"
seo_description: "Select a feature schema available at prediction time and exclude IDs target proxies and post-outcome columns in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "prediction time features"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: exclude unavailable features

Select the checkout feature schema from a different synthetic order table. It contains an extra `return_reason` field that was not in the demo. That field may be highly related to returns precisely because it is recorded after a return, so it cannot be an input for a checkout-time prediction.

## Dataset

**Row grain:** one independent synthetic checkout. **Files:** `orders.csv` (40 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `order_id` | Checkout identifier | string | Audit only; never a predictor |
| `basket_value_usd` | Basket total | float; USD | Input available at checkout |
| `item_count` | Items in the basket | integer; count | Input available at checkout |
| `actual_delivery_days` | Observed delivery duration | integer; days | Later information; excluded at checkout |
| `returned_30d` | Returned within 30 days | integer; 0/1 | Target; available after outcome window |
| `return_reason` | Observed return reason | string; none/size/damage | Later target proxy; excluded at checkout |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. Checkouts are dated 2025-01-15; 30-day outcomes are observed by 2025-02-15. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the two allowed columns in the declared order and preserve the original row index. Use the helper's DataFrame argument; do not rebuild a table from the visible values. A fixed allowlist automatically excludes both the known forbidden fields and any additional columns a caller supplies.

Run should show basket value followed by item count. Changing delivery duration or return reason should not change this selected feature matrix. Changing basket value should change it. Those two observations distinguish correct availability-based selection from a helper that merely returns an unrelated constant table.

The supplied setup reads `orders.csv` (40 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return a DataFrame containing only `basket_value_usd` and `item_count`, in that order and with the original row index; exclude identifiers, later outcomes, and any extra columns.
