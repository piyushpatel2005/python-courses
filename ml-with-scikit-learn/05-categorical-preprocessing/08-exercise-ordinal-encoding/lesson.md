---
title: 'Exercise: encode ordered categories'
slug: exercise-ordinal-encoding
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Use OrdinalEncoder with explicit category order and unknown_value=-1 without
  inventing order for nominal values.
seo_title: 'Exercise: encode ordered categories | Scikit-Learn'
seo_description: Use OrdinalEncoder with explicit category order and unknown_value=-1
  without inventing order for nominal values with a different practice fixture.
seo_keywords:
  - scikit-learn
  - ordinal encoding
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The storage-tray fixture uses depth labels rather than garment-style sizes. Its intended order is shallow, standard, deep. An extra-deep query is deliberately outside the declared vocabulary; do not add it to the fitted categories just to avoid the sentinel.

Set `handle_unknown="use_encoded_value"` with `unknown_value=-1` to reserve a separate code for a label absent from the declared vocabulary. The sentinel does not mean that an unknown size is physically smaller than small. It is a policy the downstream model must handle deliberately. Missing values are a separate issue and should follow the imputation policy taught earlier.

## Your Tasks

1. Implement `encode_sizes(training, incoming, levels)` with an explicit ordered category list and an unknown code of -1. Return a two-dimensional numeric array in incoming-row order.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
