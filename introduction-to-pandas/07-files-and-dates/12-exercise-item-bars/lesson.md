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
  - "Create a grouped totals Series first, then iterate over totals.items() to format the bars."
---

# Exercise: chart item totals

The sales desk now sends individual rows, so repeated items need to be combined before you draw their bars. The sample contains Jam twice; its two counts should become a single bar.

Group by `item`, sum `units`, and use `sort_index()` on the resulting Series to put item labels in alphabetical order. Then use the formatting pattern from the previous lesson. Inputs contain nonnegative whole-number counts without missing values; each mark still means one unit.

Edit `item_bars` in `main.py`. Run should show `Jam: #####` followed by `Tea: #`. Submit changes the row order and repeats a different item. This is the last small report before you combine reading, cleaning, and reporting in the market project.

## Your Tasks

1. Implement `item_bars(frame)` to return alphabetical `item: ###` lines from summed `units` per item, with one `#` per unit.
