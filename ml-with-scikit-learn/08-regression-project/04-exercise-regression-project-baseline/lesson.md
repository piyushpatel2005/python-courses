---
title: 'Exercise: record a regression baseline'
slug: exercise-regression-project-baseline
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Add a train-only DummyRegressor validation MAE to the saved project state.
seo_title: 'Exercise: record a regression baseline | Scikit-Learn'
seo_description: Add a train-only DummyRegressor validation MAE to the saved project
  state with a different practice fixture.
seo_keywords:
  - scikit-learn
  - regression project baseline
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

Add a reference error that a feature-based model must be compared with fairly.

The mean baseline predicts one number for every validation row: the training target mean. `DummyRegressor(strategy="mean")` still expects X during fit and prediction, but it ignores feature values. Supplied zero arrays have the required row counts and avoid involving missing measurements before imputation is introduced.

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

Validation targets are used only to calculate the error after prediction. If you compute the constant from validation prices, the supposedly held-out reference has already learned from its answers. The next model must be evaluated on these same validation rows; changing the split would confound the comparison.

Keep the prior stage unchanged. Its saved membership contract is part of the experiment. This stage returns one MAE scalar and does not claim an improvement. A later model may or may not beat the baseline on these synthetic rows.

The starter preserves the completed earlier project stages byte for byte and adds only this stage's unfinished helper. The fixture and column contract appear in the Dataset section above; the delivered project assets also preserve the complete split membership audit.

## Your Tasks

1. Implement `baseline_mae(train, validation)` to fit `DummyRegressor(strategy="mean")` on training prices only and return validation MAE. Use constant placeholder X arrays because this baseline ignores measurements.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
