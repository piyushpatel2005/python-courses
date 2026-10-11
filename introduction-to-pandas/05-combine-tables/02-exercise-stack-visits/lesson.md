---
title: 'Exercise: Stack visit logs'
slug: exercise-stack-visits
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Combine two visit logs in order with a fresh consecutive index."
seo_title: 'Exercise: Stack visit logs | Introduction to Pandas'
seo_description: "Combine two visit logs in order with a fresh consecutive index."
seo_keywords:
  - pandas
  - exercise stack visits
  - community market data
hints:
  - 'Use the same row-stacking operation as the delivery example, with a fresh index.'
---

# Exercise: Stack visit logs

The next market sends separate visit logs. The first has Fern with 3 visits; the second has Ash with 8. Combine both rows without treating their old labels, 9 and 2, as meaningful data.

The supplied return currently copies only the first log. Replace it with a call to `pd.concat`, keeping `a` before `b`. Your result should show both stalls with labels 0 and 1.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `stack_visits(a, b)` with row concatenation and a fresh index.
