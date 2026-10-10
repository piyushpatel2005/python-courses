---
title: 'Exercise: Group shift totals'
slug: exercise-shift-totals
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Produce a revenue total for each market and shift combination."
seo_title: 'Exercise: Group shift totals | Introduction to Pandas'
seo_description: "Produce a revenue total for each market and shift combination."
seo_keywords:
  - pandas
  - exercise shift totals
  - community market data
hints:
  - 'Group by ["market", "shift"], select revenue, then sum each group.'
---

# Exercise: Group shift totals

The receipt file records market and shift in separate columns. Keep both labels so Harbor morning revenue is not blended with Harbor afternoon revenue.

Return a Series with a two-level index ordered as market, then shift. The supplied data should give Harbor/AM 12, Harbor/PM 8, and Park/AM 4. If several rows share a pair, add their revenue rather than keeping just the first row.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `shift_totals(a)` by grouping on `market` and `shift` and summing `revenue`.
