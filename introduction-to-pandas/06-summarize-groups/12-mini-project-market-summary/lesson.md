---
title: 'Mini project: Publish the market summary'
slug: mini-project-market-summary
order: 12
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk needs a compact weekly report from sales.
seo_title: 'Mini project: Publish the market summary | Introduction to Pandas'
seo_description: The desk needs a compact weekly report from sales.
seo_keywords:
- pandas
- market report
- data analysis
---

# Mini project: Publish the market summary

The desk needs a compact weekly report from sales. Build a grid, grouped totals, and a separate count of missing amounts so zero-filled cells are not mistaken for complete records.

Edit `main.py`, press **Run** to inspect the current report, then **Submit** after each checkpoint.

## Your Tasks

1. Write `revenue_grid(a)` as a zero-filled sum pivot with zone rows and day columns.
2. Write `zone_report(a)` with named `revenue` (sum) and `entries` (size) grouped by zone.
3. Write `missing_amounts(a)` to count missing values in `amount`.
