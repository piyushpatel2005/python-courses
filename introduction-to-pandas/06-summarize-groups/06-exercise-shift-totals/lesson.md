---
title: 'Exercise: Group shift totals'
slug: exercise-shift-totals
order: 6
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: A fresh receipt file records market and shift separately.
seo_title: 'Exercise: Group shift totals | Introduction to Pandas'
seo_description: A fresh receipt file records market and shift separately.
seo_keywords:
- pandas
- exercise shift totals
- community market data
---

# Exercise: Group shift totals

A fresh receipt file records market and shift separately. Return one total per observed market-and-shift combination.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Complete `shift_totals(a)` by grouping on `market` and `shift` and summing `revenue`.
