---
title: Profile values and labels
slug: profile-values
order: 3
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk checks distributions before publishing a report.
seo_title: Profile values and labels | Introduction to Pandas
seo_description: The desk checks distributions before publishing a report.
seo_keywords:
- pandas
- profile values
- community market data
---

# Profile values and labels

The desk checks distributions before publishing a report. `describe()` summarizes numeric spread and known count; `value_counts()` tallies labels. `dropna=False` includes missing labels, which otherwise disappear.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `dropna=True` to `dropna=False` in `profile_sales`.
