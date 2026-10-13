---
title: 'Exercise: fit Gaussian naive Bayes'
slug: exercise-naive-bayes
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Use GaussianNB and explain its conditional-independence assumption.
seo_title: 'Exercise: fit Gaussian naive Bayes | Scikit-Learn'
seo_description: Use GaussianNB and explain its conditional-independence assumption
  with a different practice fixture.
seo_keywords:
  - scikit-learn
  - naive bayes
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

Predict wine cultivar classes from the first three measured constituents. The supplied prior values are a teaching assumption, not a claim about a real wine population. Preserve their correspondence with sorted class labels and return a fitted estimator.

The iris demo uses observed class frequencies by default in its unfinished version. The task changes it to the supplied explicit priors. That isolates how prior knowledge enters the classifier without changing its class-specific feature estimates. GaussianNB does not need an `n_jobs` argument and does not expose one. The transfer uses a different educational benchmark.

Dataset provenance: Iris is attributed to R. A. Fisher (UCI DOI 10.24432/C56C76); Wine to Stefan Aeberhard and M. Forina (UCI DOI 10.24432/C5PC7J). Their UCI records specify CC BY 4.0, separately from the scikit-learn software license. Both bundled tables are complete. Iris measurements are in centimeters; Wine constituent scales follow `data.DESCR` rather than invented units. These benchmarks are not company records.

## Your Tasks

1. Implement `fit_bayes(training, labels, priors)` to fit and return `GaussianNB` with the supplied prior array in sorted class order.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
