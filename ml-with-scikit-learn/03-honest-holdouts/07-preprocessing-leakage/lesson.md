---
title: "Keep learned statistics inside training"
slug: "preprocessing-leakage"
order: 7
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit a supplied scaler on training rows only and transform validation rows."
seo_title: "Keep learned statistics inside training | Scikit-Learn"
seo_description: "Fit a supplied scaler on training rows only and transform validation rows with a small editable Python example."
seo_keywords:
  - "scikit-learn"
  - "preprocessing leakage"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Keep learned statistics inside training

Preprocessing can leak held-out information even when it never reads a target. A scaler fitted on validation inputs learns something about their distribution. If that fitted state is then used while training or comparing models, the validation partition is no longer wholly outside the learning process.

## Dataset

**Row grain:** one synthetic package measurement. **Files:** `training.csv` (32 rows), `queries.csv` (2 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `weight_kg` | Package weight | float; kg | Input recorded before handling |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. The figure uses the explicitly labeled eight-row illustration; the files contain the larger runnable dataset. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

The helper receives two already separated matrices. Fit `StandardScaler` on `train` and use its `transform` method on `validation`. This is the same state-reuse contract introduced earlier, now attached to a held-out boundary. The function returns both the fitted scaler and the transformed values so you can inspect how the state was learned.

The starter combines the matrices with `np.vstack` before fitting. Stacking here puts validation rows underneath training rows; it does not create new features. The combined matrix is valid input to `fit`, which is why the program runs. The defect is methodological rather than a Python exception.

Compare the learned mean with the training values. The validation weights are deliberately much larger, so including them shifts the mean visibly. Remove them from the fit call and Run again. The transformed validation numbers can now be large because they are measured relative to training statistics. A large standardized value is not a reason to refit on the held-out batch.

A useful check holds training fixed while changing validation values to extreme alternatives. The saved mean and scale should remain unchanged, while the transformed validation output should change. This distinguishes an honest training-only fit from a helper that learns from all rows or returns a hardcoded transformed array.

The demonstration does not yet compare prediction quality. It establishes the boundary that later imputation, scaling, and model-selection workflows must retain.

The supplied setup reads `training.csv` (32 rows), `queries.csv` (2 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

## Worked calculation

A separate tiny illustration uses training values 2, 4, and 6 kg and a validation value 100 kg. With $\mu$ denoting a fitted mean,

$$
\mu_{train}=\frac{2+4+6}{3}=4\text{ kg},
$$

$$
\mu_{leaked}=\frac{2+4+6+100}{4}=28\text{ kg}.
$$

The held-out value must not contribute to the learned mean.

![Small Worked Example (8 Rows). Learned Training State. Validation: [100, 120] kg](preprocessing-leakage-data-flow.svg)

## Small edit

Replace `np.vstack([train, validation])` in the fit call with `train`.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a `StandardScaler` only on `train`, then return `(scaler, transformed_validation)` using that same fitted scaler to transform `validation`.
