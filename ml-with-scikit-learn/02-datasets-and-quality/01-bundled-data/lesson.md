---
title: "Inspect bundled datasets"
slug: "bundled-data"
order: 1
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Read Bunch data target feature_names and target_names and select aligned rows."
seo_title: "Inspect bundled datasets | Scikit-Learn"
seo_description: "Read Bunch data target feature_names and target_names and select aligned rows with a small editable Python example."
seo_keywords:
  - "scikit-learn"
  - "bundled data"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Inspect bundled datasets

You have built `X` and `y` from a small table. A bundled dataset supplies those arrays along with names that explain them. `load_iris()` returns a `Bunch`, a dictionary-like container with dot access: `bundle.data` holds the features and `bundle.target` holds the labels.

`feature_names` names the input columns in order. `target_names` names the classes represented by integer codes in `target`. A target code is a category identifier, not a measured amount: class 2 is not twice class 1. Keep these names as metadata instead of inserting them as extra sample rows or input columns.

The supplied selector picks rows from different parts of Iris. NumPy integer-array indexing preserves the order of the selected positions. Apply that same selector to both `data` and `target`; taking the first few targets merely because their count matches would attach the wrong species to some measurements.

Run the starter and inspect its target codes. Its feature and target shapes already agree, but its selection logic does not. Correct the target indexing, then compare the selected row positions and the returned codes. This example shows why matching lengths alone is not an alignment check.

Iris is a historical educational benchmark, not a HomeHurray table or evidence about retail prediction. The loader's `DESCR` field includes provenance and references. Dataset provenance and terms are separate from the scikit-learn software license; loading a benchmark does not relicense its underlying observations. We use the loader rather than copying its raw table into the course.

The next exercise uses Wine. A helper based on the bundle fields should transfer without hardcoding four columns or three particular flower names.

## Data used here

Iris is an external botanical benchmark, not company data. `data` has four float columns: sepal length, sepal width, petal length, and petal width, all in cm; `target` contains integer class codes 0–2 mapped by `target_names`. Measurements are inputs and species is the target. Row indices are selectors, not predictors. These packaged arrays contain no missing values; they are a static benchmark, not a dated business snapshot.

![Iris Bunch: External Benchmark. Select [0, 50, 100, 149]. Aligned Result](bundled-data-data-flow.svg)

## Small edit

Replace `bundle.target[:len(rows)]` with `bundle.target[rows]`.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return `(X, y, feature_names, target_names)` for `rows` from the supplied dataset bundle, applying the identical row selection to `data` and `target` and retaining both metadata name lists.
