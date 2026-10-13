---
title: 'Exercise: combine column-specific transforms'
slug: exercise-column-transformer
order: 10
language: python
lesson_type: coding
runtime: pyodide
summary: Route named numeric and categorical columns through ColumnTransformer and
  inspect output order.
seo_title: 'Exercise: combine column-specific transforms | Scikit-Learn'
seo_description: Route named numeric and categorical columns through ColumnTransformer
  and inspect output order with a different practice fixture.
seo_keywords:
  - scikit-learn
  - column transformer
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

Kitchenware volume and finish replace weight and material. Pass the supplied column names into your helper instead of hardcoding the demo names. The product IDs must not appear in the output.

`remainder="drop"` excludes everything not explicitly selected. In particular, a product ID is an audit key, not a measurement. `get_feature_names_out()` exposes the branch and original feature in each output name. Fit once on training rows, then call `transform` on queries. These tables are clean so routing is the only new problem; missing values return in the next lesson.

## Your Tasks

1. Implement `route_columns(training, numeric, category)` to fit and return a `ColumnTransformer` that scales the named numeric column, densely one-hot encodes the named category with unknowns ignored, and drops unselected columns.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
