---
title: 'Exercise: Compare visits to a group'
slug: exercise-visit-difference
order: 10
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: A new log records visits per stall category.
seo_title: 'Exercise: Compare visits to a group | Introduction to Pandas'
seo_description: A new log records visits per stall category.
seo_keywords:
- pandas
- exercise visit difference
- community market data
---

# Exercise: Compare visits to a group

A new log records visits per stall category. Subtract each category mean from each row’s visits while preserving its original index and order.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Complete `visit_difference(a)` using `groupby(...).transform("mean")` to subtract each category baseline.
