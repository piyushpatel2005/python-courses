---
title: "Exercise: separate precision and recall"
slug: "exercise-precision-recall"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Calculate precision and recall for a specified positive class including zero denominators."
seo_title: "Exercise: separate precision and recall"
seo_description: "Calculate precision and recall for a specified positive class including zero denominators."
seo_keywords:
  - "scikit-learn"
  - "precision-recall"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

The demo uses synthetic furniture-return decisions; this exercise uses a different kitchenware flag table.

## Dataset

`observations.csv` contains 96 original synthetic HomeHurray Inc. observations. One independent synthetic measurement observation per row. These are teaching data, not actual company performance.

| Column | Meaning and type / unit | Availability / role |
|---|---|---|
| `observation_id` | Unique string observation ID | Audit metadata, excluded from X |
| `measurement_a` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `measurement_b` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `measurement_c` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `truth` | Integer 0/1 synthetic outcome; 1 is positive | Observed label used for metric arithmetic |
| `predicted` | Fabricated integer 0/1 decision | Supplied prediction, not an input feature |
| `score` | Fabricated float in [0, 1], larger favors class 1 | Supplied score, not an input feature |

All stored values are complete. The fixed observation snapshot is 2025-01-15. The values retain their original seeded-fixture order and precision. Decisions and scores were deliberately fabricated from labels to practice metrics; they are not independent fitted-model evaluation. Figures use separate tiny illustrative counts.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

Precision asks how many flagged orders actually returned. Recall asks how many observed returns were flagged. These denominators answer different questions: adding false alarms changes precision; missing returns changes recall. `pos_label` selects the outcome of interest even when labels are strings.

If there are no positive predictions, precision has a zero denominator. Use `zero_division=0` as an explicit reporting policy rather than claiming perfect precision. The same policy applies to recall when there are no actual positives. Always keep the relevant counts when interpreting this edge case.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## A small calculation

$$
P=\frac{TP}{TP+FP},\qquad R=\frac{TP}{TP+FN}
$$

$TP$ counts true positives, $FP$ false positives, and $FN$ false negatives.

$P$ is precision and $R$ is recall. For $TP=2$, $FP=1$, $FN=2$, $P=0.6667$ and $R=0.5$.

## Your Tasks

1. Implement `measure` to return `(precision, recall)` for `positive`, reporting zero when a denominator is zero.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
