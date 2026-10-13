# Fixed recommendation data contract

All rows are original synthetic HomeHurray Inc. teaching data. They do not represent customers or commercial results. The exact 18 catalog records, six users, and 30 events live in each exercise's catalog.json, users.csv, and interactions.csv. Main reads these real files. This document is not a runtime dependency.

| Field | Type and domain / unit | Missing policy | Available | Role |
|---|---|---|---|---|
| item_id | string I01–I18, unique, no unit | forbidden | 2025-01-01 | alignment and ascending tie key, never text feature |
| category | string furniture/kitchen/bedding/decor | forbidden | 2025-01-01 | text feature |
| title | original short string | forbidden | 2025-01-01 | text feature |
| description | original attribute string | forbidden | 2025-01-01 | text feature, no user outcomes |
| available_since | ISO date string, 2025-01-01 | forbidden | catalog snapshot | candidate eligibility |
| user_id | synthetic U01–U06 string | forbidden | event timestamp | history grouping, not personal data |
| event_at | ISO date string | forbidden | event timestamp | temporal partition |
| event_type | string view | forbidden | event timestamp | implicit signal, not explicit rating |
| relevant | evaluation-derived set of held-out item IDs | empty set omitted in evaluation | held-out timestamp | proxy outcome, not a stored catalog feature |

Events remain pandas DataFrames with string `user_id`, `item_id`, `event_at`, and `event_type` columns. `pd.read_csv(dtype=str)` and `pd.read_json(orient="records", convert_dates=False)` preserve IDs and ISO dates. Each user has five distinct items at January 5, January 12, January 19, January 26, and February 2, 2025. Three events form training history; one forms validation; one forms final test. The fixture intentionally supplies exactly five events per eligible user. Invalid dates, repeated items, or an unavailable product make that user omitted under the stage-one contract.

TF-IDF fits the entire fixed metadata catalog available by January 19, 2025. Histories and popularity use training events only. All ranking uses k=3, seen filtering, descending scores/counts, then ascending item ID. No validation events are appended for final testing: validation-viewed items remain eligible. The state remains fixed, unlike an online retraining simulator.

The final report compares content and popularity with identical candidate and exclusion rules. Precision uses requested k even for short lists. Recall uses distinct eligible unseen relevance count. Macro metrics average eligible users equally. Hit indicates any hit; with one relevant event per user it equals recall. Binary NDCG rewards earlier first-occurrence hits. Coverage counts distinct recommended products / eligible catalog products. Unobserved products are not proven disliked. The six-user fixture is too small and artificial to establish business quality.

`make_catalog`, `split_interactions`, `build_profiles`, `recommend`, `recommend_with_fallback`, and `evaluate` define the cumulative public API. Later exercise starters preserve completed prior definitions and fixture rows unchanged. Each later exercise and its reference repeat byte-identical dataset files so a fresh lesson can run independently.
