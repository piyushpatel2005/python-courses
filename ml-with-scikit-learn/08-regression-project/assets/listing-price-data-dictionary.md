# Listing-price project data contract

All 120 rows are original synthetic HomeHurray Inc. teaching data, not customer or company observations. Snapshot: **2025-01-15**. Prediction time is before assigning the new listing price. Products are generated independently from one stationary population; random splits do not validate future-period behavior.

| Field | Type and unit/domain | Missing meaning | Available | Role |
|---|---|---|---|---|
| product_id | string HH-001 through HH-120, unique | never missing | before listing | ID/audit only, excluded from X |
| snapshot_date | ISO date string 2025-01-15 | never missing | feature snapshot | provenance only, excluded from X |
| weight_kg | positive float, kilograms; generated [0.3, 8.0) | measurement not recorded | before listing | feature 1 |
| volume_l | positive float, packaged liters; generated [0.5, 35.0) | measurement not recorded | before listing | feature 2 |
| material_cost_usd | positive float, USD procurement estimate; generated [2.0, 40.0) | none injected | before listing | feature 3 |
| listed_price_usd | positive float, USD synthetic list price | none injected | after feature snapshot | regression target; never X |

## Deterministic construction

`make_data()` reads the actual `listing-prices.csv` with pandas and round-trip float parsing. The CSV was created once with a local `np.random.default_rng(41)`: independent weight, volume and material-cost draws in that order, then centered normal noise with standard deviation 2 USD. Its target mechanism combines an intercept, weighted measurements and that noise. The CSV preserves every generated value, missing position and ID; there is no embedded data fallback or regeneration during a lesson. The model must learn only from its permitted training rows.

Missing weight positions are 4, 17, 33, 52, 71, 99; missing volume positions are 8, 22, 46, 63, 86, 112 (zero-based original row positions). They are injected after creating the targets. Learn median fills from training, never the entire table. Row order starts at HH-001 and ends at HH-120.

## Frozen experiment

Two `train_test_split` calls use `random_state=41`. The first seals 20% as test. The second takes 25% of development as validation. The exact ordered memberships are in `listing-price-splits.json`. There are 72 training, 24 validation and 24 test rows. IDs and targets remain aligned with measurements in DataFrames; only `FEATURES` enters the estimator.

The five exercise stages preserve earlier completed source exactly: `make_splits` → `baseline_mae` → `build_model` → `choose_alpha` → `final_report`. `make_data` is supplied from stage one. Choose among alpha 0.1, 1.0 and 10.0 by validation MAE, using the first minimum as tie-break. Refit the frozen alpha on train plus validation only at the final stage. Test targets never select settings or fit preprocessing.

The 20-row demo analogues use seed 19, PARCEL IDs and a different target mechanism. They do not replace or modify project rows between stages.

## Report limits

The output includes the selected alpha, development/test counts, ordered IDs and predictions, MAE, RMSE and R-squared. Dollar errors describe imitation of synthetic listed prices, not an optimal-pricing policy, demand model, causal estimate or actual business gain. Rerunning the deterministic report does not authorize retuning from its test result.
