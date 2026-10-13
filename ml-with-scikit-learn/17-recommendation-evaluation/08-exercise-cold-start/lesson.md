---
title: "Exercise: provide a documented fallback"
slug: "exercise-cold-start"
order: 8
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Use training-only item popularity for no-history or zero-vector users and state coverage and bias limits."
seo_title: "Exercise: provide a documented fallback | Scikit-learn practice"
seo_description: "Use training-only item popularity for no-history or zero-vector users and state coverage and bias limits. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "cold start"
  - "Python practice"
---

A user without history has no content profile. A history whose item text becomes a zero vector has the same practical problem. Use a declared fallback rather than pretending that all-zero content scores encode preferences.

The fallback here counts training views per item with `Counter(training_events["item_id"])`. Include eligible catalog items with zero counts, filter seen IDs, then sort by descending count and ascending ID. A count measures exposure in this synthetic history, not intrinsic product quality. Never count validation or test views, even for another user: global popularity can leak future outcomes.

The helper is the popularity branch only; the preceding content ranker remains the warm-user branch. Coverage measures how many different catalog items appear across recommendation lists. High coverage alone does not imply useful recommendations, and a popularity fallback can repeatedly favor already-exposed items. Report this limitation rather than claiming the cold-start problem is solved.

For a nonempty eligible catalog $C$ and union $A$ of recommended IDs,

$$
\mathrm{coverage}=\frac{|A\cap C|}{|C|}.
$$

Vertical bars mean distinct-item counts. Recommending three distinct eligible items from a four-item catalog gives $3/4=0.75$. This is catalog coverage, not the fraction of users served and not recall. Across users, take the union before counting so repeatedly recommending one item does not inflate coverage.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

These are original synthetic fixtures. The fixed training cutoff is 2025-01-19; only declared training partitions may fit state.

## Dataset

`training-views.csv` contains 30 synthetic views from six users, all dated January 5 through January 17, 2025. `catalog.json` declares twelve eligible item IDs available on January 1. The supplied reader uses only user and item IDs for training counts; dates document availability. No validation or test events appear in this file.

`catalog.json` has **12 rows**, each representing one catalog product. `training-views.csv` has **30 rows**, each representing one observed synthetic view.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `user_id` | Synthetic user grouping key; not a personal identifier | string; none | History grouping key |
| `item_id` | Stable product ID; alignment and ascending tie key, not a text feature | string; none | Product identity / deterministic tie key |
| `event_at` | ISO event date for the history/holdout boundary | string; calendar date | Observed view date; history cutoff applies |
| `available_since` | ISO date that determines catalog eligibility | ISO date string; calendar date | Catalog eligibility date |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete; an empty history means no observed training views, not dislike. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Implement `popular_items(ids, training_events, seen, k)` using training-only item counts, seen filtering, and ascending ID ties, including eligible zero-count items.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
