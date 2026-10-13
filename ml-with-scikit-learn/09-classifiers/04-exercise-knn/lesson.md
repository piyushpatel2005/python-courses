---
title: 'Exercise: classify by nearest neighbors'
slug: exercise-knn
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Use KNeighborsClassifier after scaling and relate k to voting.
seo_title: 'Exercise: classify by nearest neighbors | Scikit-Learn'
seo_description: Use KNeighborsClassifier after scaling and relate k to voting with
  a different practice fixture.
seo_keywords:
  - scikit-learn
  - knn
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

The wine fixture uses alcohol and flavanoids measurements to predict cultivar classes. Their ranges differ. Build the pipeline from the given arrays without fitting on the query partition or hardcoding the first five outputs.

The iris demo and wine transfer use bundled educational benchmarks, not company data. Increasing k makes the vote include a larger neighborhood; it does not guarantee better held-out accuracy. The task uses k=3 so a designed binary neighborhood can have a clear majority. For multiclass ties, label ordering can affect the result, which is one reason not to assign meaning to incidental tie outcomes.

Dataset provenance: Iris is attributed to R. A. Fisher (UCI DOI 10.24432/C56C76); Wine to Stefan Aeberhard and M. Forina (UCI DOI 10.24432/C5PC7J). Their UCI records specify CC BY 4.0, separately from the scikit-learn software license. Both bundled tables are complete. Iris measurements are in centimeters; Wine constituent scales follow `data.DESCR` rather than invented units. These benchmarks are not company records.

## Your Tasks

1. Implement `fit_neighbors(training, labels, k)` to return a fitted `scale` → `model` pipeline with `KNeighborsClassifier(n_neighbors=k, n_jobs=1)`.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
