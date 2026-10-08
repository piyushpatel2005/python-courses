---
title: 'Exercise: chart item totals'
slug: exercise-item-bars
order: 12
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Group item counts and show sorted totals as readable text bars.
seo_title: 'Exercise: chart item totals | Introduction to Pandas'
seo_description: Group item counts and show sorted totals as readable text bars.
seo_keywords:
- pandas
- text visualization
- groupby item totals
hints:
- Use the example above the task and check the printed result before submitting.
---

# Exercise: chart item totals

The sales desk has rows rather than an already-grouped Series. Sum `units` by `item`, then format the alphabetical totals with one `#` per unit. This produces a tiny visualization that works in plain output.

Edit `main.py`, Run to compare item lengths, then Submit. The tests reorder rows, repeat an item, and add a new item, so compute from the supplied DataFrame.

## Your Tasks

1. Implement `item_bars(frame)` to return alphabetical `item: ###` lines after summing `units` for each item, using one `#` per unit.
