---
title: 'Mini project: Publish the market summary'
slug: mini-project-market-summary
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Publish a revenue grid and zone report alongside a missing-amount count."
seo_title: 'Mini project: Publish the market summary | Introduction to Pandas'
seo_description: "Publish a revenue grid and zone report alongside a missing-amount count."
seo_keywords:
  - pandas
  - market report
  - data analysis
hints:
  - 'Use size for entries, and count missing cells from the original amount column rather than from the filled grid.'
---

# Mini project: Publish the market summary

Prepare a weekly summary the Community Data Desk can read without losing sight of incomplete data. Build the zone-by-day revenue grid, a zone report, and a separate missing-amount count. Each function is checked independently.

The sample has two Pier receipts totaling 10 and one Hill row with an unrecorded amount. The default sum of an all-missing group is 0, so Hill can appear as zero revenue even though no amount was recorded. An absent grid cell can also display zero because of `fill_value=0`. Neither zero proves the records are complete.

Keep the missing-amount count next to the report: the completed preview must show 1 unrecorded amount. After this summary, the next module introduces reading and writing small data files.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Write `revenue_grid(a)` as a zero-filled sum pivot with zone rows and day columns.
2. Write `zone_report(a)` with a revenue column containing each zone's amount sum.
3. Add an entries column containing each zone's row count, after revenue.
4. Write `missing_amounts(a)` to count missing values in amount.
