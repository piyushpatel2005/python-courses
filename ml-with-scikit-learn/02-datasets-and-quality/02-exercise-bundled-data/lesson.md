---
title: "Exercise: inspect bundled datasets"
slug: "exercise-bundled-data"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Read Bunch data target feature_names and target_names and select aligned rows."
seo_title: "Exercise: inspect bundled datasets | Scikit-Learn"
seo_description: "Read Bunch data target feature_names and target_names and select aligned rows in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "bundled data"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: inspect bundled datasets

Select an ordered subset of the Wine benchmark while keeping its feature and target metadata. The demo used four Iris inputs; Wine has thirteen chemical-measurement inputs. Your helper must obtain that width and its names from the provided bundle.

The selector is deliberately not sorted. Preserve its order in both outputs, and return ordinary lists for the two name collections. These lists describe columns and classes, not individual samples, so they should not be sliced using the row positions.

The supplied probe prints all feature names and the selected target codes. Use it to confirm that you are working with Wine, not a copied Iris result. You can inspect `bundle.DESCR` separately for the benchmark's origin and measurement descriptions. This exercise only teaches dataset access and alignment; it makes no claim about the quality of a trained classifier.

## Data used here

Wine is an external chemical-analysis benchmark, unrelated to company data. Its 13 float features describe chemical measurements; preserve the exact names in `feature_names` and consult the bundled `DESCR` for their definitions rather than assigning them invented business units. Integer targets 0–2 identify the three class names. Inputs are measurements, targets are wine classes, and row selectors are not features. The packaged table has no missing values and no prediction-time business date.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return `(X, y, feature_names, target_names)` for `rows` from the supplied dataset bundle, applying the identical row selection to `data` and `target` and retaining both metadata name lists.
