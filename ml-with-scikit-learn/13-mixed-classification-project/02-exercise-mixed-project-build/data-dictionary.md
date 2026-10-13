# Return-risk project data contract

| Field | Type / units / domain | Missing meaning | Availability | Role |
|---|---|---|---|---|
| `order_id` | unique string O000 onward | none | checkout | audit ID, never X |
| `customer_id` | unique string C000 onward | none; one per order | checkout | audit ID, never X |
| `checkout_date` | ISO date, 2025-01-01 through 2025-02-28 | none | checkout | provenance, never X |
| `basket_value_usd` | nonnegative float USD | unavailable measurement, NaN | checkout | predictor |
| `item_count` | positive whole-number count stored as float | unavailable count, NaN | checkout | predictor |
| `category` | furniture/kitchen/bedding; query may contain decor | none | checkout | nominal predictor |
| `returned_30d` | integer 0/1; 1 means returned | none; mature observed labels | after 30-day window | target, never X |
| `actual_delivery_days` | positive integer days | none | after delivery | forbidden post-checkout field |

All 180 labels are observed by the fixed 2025-04-01 snapshot. Each order has a distinct customer; these artificial rows are stationary and independent. Stratified random partitions estimate same-population behavior, not future forecasting. Missing inputs are injected after labels are generated. The sampled labels are not actual customer outcomes.

Search uses only training rows; threshold validation is separate. Freeze the fit after threshold choice. Open test only in final_report. IDs remain outside predictors.
