---
title: 'Exercise: fit logistic regression'
slug: exercise-logistic-regression
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Fit a scaled LogisticRegression and separate class labels from class probabilities.
seo_title: 'Exercise: fit logistic regression | Scikit-Learn'
seo_description: Fit a scaled LogisticRegression and separate class labels from class
  probabilities with a different practice fixture.
seo_keywords:
  - scikit-learn
  - logistic regression
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

Use the first four measured wine constituents in the bundled wine benchmark to predict its cultivar classes. The source names and measurement definitions are available in `data.feature_names[:4]` and `data.DESCR`; do not label these columns as product measurements. The different units make training-only scaling useful.

For two classes a sigmoid converts a linear score into a probability. Multiclass logistic regression uses a normalized multiclass rule rather than applying one independent binary threshold to every column. The task controls regularization through `C`, the inverse strength: smaller C means stronger regularization. `max_iter=1000` allows this small fit to converge; it is supplied setup.

Dataset provenance: Iris is attributed to R. A. Fisher (UCI DOI 10.24432/C56C76); Wine to Stefan Aeberhard and M. Forina (UCI DOI 10.24432/C5PC7J). Their UCI records specify CC BY 4.0, separately from the scikit-learn software license. Both bundled tables are complete. Iris measurements are in centimeters; Wine constituent scales follow `data.DESCR` rather than invented units. These benchmarks are not company records.

## Your Tasks

1. Implement `fit_classifier(training, labels, C)` as a fitted `scale` → `model` pipeline using `LogisticRegression` with the supplied C, `max_iter=1000` and `n_jobs=1`.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
