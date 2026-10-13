---
title: "Exercise: average a user's observed item vectors"
slug: "exercise-user-profiles"
order: 10
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Build a mean profile from training interactions only and rank unseen items."
seo_title: "Exercise: average a user's observed item vectors | Scikit-learn practice"
seo_description: "Build a mean profile from training interactions only and rank unseen items. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "user profiles"
  - "Python practice"
---

An item profile describes a product. A user profile can be the mean of product vectors from that user's training history. This simple model gives each distinct viewed product equal weight. It cannot tell a deliberate purchase from an accidental view.

`item_matrix` has one row per entry in `ids`. Build an ID-to-row lookup, select the history rows, and average them along axis zero. Return a two-dimensional array with shape `(1, n_features)` so it can go directly into `cosine_similarity`. Sparse `.mean(axis=0)` returns a matrix-like object; `np.asarray` makes the result an ordinary dense array for this one small profile.

The helper receives training IDs only. Validation and test events are deliberately absent from its arguments. Empty histories return a zero row; a later fallback handles that no-information case. The supplied ranking probe excludes the training history and orders ties by item ID. Do not append held-out interactions merely because they are available in the evaluation file.

For nonempty distinct history $H$,

$$
p=\frac{1}{|H|}\sum_{i\in H}x_i.
$$

Here $x_i$ is the item vector for item $i$, $|H|$ is the number of eligible distinct history items, and $p$ is the mean profile. Two vectors $[1,0]$ and $[0,1]$ produce $[0.5,0.5]$. These are feature weights, not probabilities. An empty $H$ uses an explicit zero-vector policy instead of dividing by zero.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

These are original synthetic fixtures. The fixed teaching snapshot is 2025-01-15; only declared training partitions may fit state.

### Fixture fields

| Field | Type and units | Role |
|---|---|---|
| `ids` | unique string list | item row map |
| `item_matrix` | sparse float matrix | nonnegative item feature weights |
| `history` | list of string item IDs | training views only; repeated IDs count once |

## Your Tasks

1. Implement `mean_profile(ids, item_matrix, history)` as the mean of distinct history-item rows, with a `(1, n_features)` zero array for empty history. Ignore history IDs absent from the catalog.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
