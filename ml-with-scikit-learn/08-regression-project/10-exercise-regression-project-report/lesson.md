---
title: 'Exercise: evaluate the frozen regression model'
slug: exercise-regression-project-report
order: 10
language: python
lesson_type: coding
runtime: pyodide
summary: Refit frozen settings on development data and add one final test report with
  limitations.
seo_title: 'Exercise: evaluate the frozen regression model | Scikit-Learn'
seo_description: Refit frozen settings on development data and add one final test
  report with limitations with a different practice fixture.
seo_keywords:
  - scikit-learn
  - regression project report
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

Use the frozen setting for one final evaluation and state exactly what the result measures.

Concatenate training then validation to form development. Refit a fresh pipeline with the selected alpha on those rows; this legitimately updates imputation and scaling because validation is no longer being used to select settings. The sealed test remains outside every fitted statistic.

## Dataset

The read-only `listing-prices.csv` tab contains the real input file. `make_data()` reads that file with `pd.read_csv`; it does not generate replacement rows. Each Run starts from the authored snapshot. Empty numeric cells mean unrecorded measurements, not zero.

| Column | Type / unit | Available | Role |
|---|---|---|---|
| product_id | unique string | before listing | audit only |
| snapshot_date | ISO date, 2025-01-15 | before listing | provenance only |
| weight_kg | positive float, kg; missing allowed | before listing | predictor |
| volume_l | positive float, liters; missing allowed | before listing | predictor |
| material_cost_usd | positive float, USD; complete | before listing | predictor |
| listed_price_usd | positive float, USD; complete | after feature snapshot | target, never X |

The project uses 120 fixed product rows; demos use a separate 20-row parcel analogue. Both are synthetic. File loading is supplied setup rather than a second assessed task. `float_precision="round_trip"` preserves the saved numeric precision.

## Worked explanation

Return a dictionary with `model`, `alpha`, `development_ids`, `test_ids`, `n_development`, `n_test`, `predicted`, `mae`, `rmse`, and `r2`. Preserve test row order in both IDs and predictions. MAE and RMSE are in dollars; R-squared is unitless and may be negative. The supplied print loop excludes the model object and reports these fields without inventing a gain.

This is one deterministic teaching report, even if you rerun the code. Do not adjust alpha after reading it. The 96 development and 24 test products come from a stationary synthetic population with independent rows, known pre-listing inputs and a simple target mechanism. The result does not establish optimal pricing, demand response, fairness, real commercial improvement or performance on future inventory.

The starter preserves the completed earlier project stages byte for byte and adds only this stage's unfinished helper. The fixture and column contract appear in the Dataset section above; the delivered project assets also preserve the complete split membership audit.

The supplied output is the completion report for this project. Save the selected setting and counts alongside its errors; do not infer a real-world gain from synthetic data.

## Your Tasks

1. Implement `final_report(train, validation, test, alpha)` to refit the frozen alpha on concatenated development rows and return the specified model, IDs, counts, predictions and final test metrics. Use test rows only for prediction and metric calculation.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
