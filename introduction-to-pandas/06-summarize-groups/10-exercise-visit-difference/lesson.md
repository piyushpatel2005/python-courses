---
title: 'Exercise: Compare visits to a group'
slug: exercise-visit-difference
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Subtract each category mean without losing original row labels."
seo_title: 'Exercise: Compare visits to a group | Introduction to Pandas'
seo_description: "Subtract each category mean without losing original row labels."
seo_keywords:
  - pandas
  - exercise visit difference
  - community market data
hints:
  - 'Subtract the transformed category mean from the visitor Series, not the other way round.'
---

# Exercise: Compare visits to a group

Compare each stall with other stalls in its category. First use `groupby(...).transform("mean")` to calculate a category baseline with the same index as the original visitor counts. Then subtract that baseline from `a["visitors"]`.

Food visits are 10 and 14, so the baseline is 12 for both rows. Their differences are -2 and 2; Art has only one row, so its difference is 0. Negative means below the category mean, not an invalid visit count. Preserve the input index and order so each difference stays attached to the right stall.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `visit_difference(a)` using `groupby(...).transform("mean")` to subtract each category baseline.
