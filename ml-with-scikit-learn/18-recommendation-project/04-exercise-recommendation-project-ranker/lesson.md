---
title: "Exercise: build the recommendation function"
slug: "exercise-recommendation-project-ranker"
order: 4
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Add a train-only TF-IDF profile scorer and deterministic filtered top-k function."
seo_title: "Exercise: build the recommendation function | Scikit-learn practice"
seo_description: "Add a train-only TF-IDF profile scorer and deterministic filtered top-k function. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "recommendation project ranker"
  - "Python practice"
---

The completed split now supplies the only interactions the ranker may read. Catalog metadata and interaction histories have different fit rules: all available fixed catalog descriptions may train TF-IDF, but only training views may form a user profile. No labels or future reviews are appended to descriptions.

`build_profiles(catalog)` is supplied setup. It returns sorted IDs, a fitted vectorizer, and a sparse matrix aligned to those IDs. Implement `recommend(ids, matrix, training, user, k=3)` around that alignment. Collect the user's distinct seen IDs, average their eligible item rows, compute cosine scores, exclude seen items, and sort by descending score then ascending item ID. Unknown users and zero profiles return an empty list at this stage; the next stage adds a fallback.

The returned list has at most k IDs, never duplicate items. The previous solution's catalog and split function remain unchanged in the exercise starter. A new catalog order must not silently redirect a user's history to a different matrix row. The probe uses one warm user and one unseen user so both return contracts are visible.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

All completed earlier project helpers and dataset files are supplied unchanged. Only the new helper is unfinished.

## Dataset

The exercise loads its exact 18-product, six-user, 30-view fixture from `catalog.json`, `users.csv`, and `interactions.csv`. The supplied readers use `pd.read_json(..., orient="records", convert_dates=False)` for descriptions and `pd.read_csv(..., dtype=str)` for users/events. IDs and ISO dates remain strings; tables stay DataFrames through filtering and grouping. The reference includes byte-identical data files. These files and all completed helpers carry into later project starters; no data is embedded or fetched remotely.

`catalog.json` has **18 rows**, each representing one catalog product. `users.csv` has **6 rows**, each representing one synthetic user. `interactions.csv` has **30 rows**, each representing one observed synthetic view.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `item_id`, `user_id` | Product alignment / user history grouping | strings; no unit | IDs, not predictors; ascending item-ID ties |
| `category`, `title`, `description` | Original product content | strings; no unit | Text features known on 2025-01-01 |
| `available_since`, `event_at` | Catalog availability / view chronology | ISO date strings | Catalog Jan 1; history Jan 5/12/19; validation Jan 26; test Feb 2, 2025 |
| `event_type` | View, an implicit relevance proxy | string; none | Available only when the event occurs |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete; an empty history means no observed training views, not dislike. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Implement `recommend(ids, matrix, training, user, k=3)` as the training-history mean-profile cosine ranker, filtering seen IDs and resolving ties by ascending ID; return `[]` for absent or zero profiles.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
