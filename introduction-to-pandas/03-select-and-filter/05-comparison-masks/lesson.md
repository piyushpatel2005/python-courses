---
title: Filter stalls with a comparison mask
slug: comparison-masks
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Keep rows whose measured stock reaches a supplied cutoff.
seo_title: Filter stalls with a comparison mask | Introduction to Pandas
seo_description: Keep rows whose measured stock reaches a supplied cutoff.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - At least includes equality, so keep the >= comparison.
---

The desk wants stalls with at least eight crates. Comparing a whole column, `frame["crates"] >= 8`, produces a Boolean Series: one True or False decision for each labeled row. This Series is called a mask.

`frame.loc[mask]` keeps the rows whose decision is True. Because this mask comes from the same table, its labels already match. A Boolean Series is aligned by index label, not simply zipped to row positions; keep its labels attached and do not reuse a mask from an unrelated table. Filtering preserves the table's row order and labels.

Change the cutoff in the supplied function from 5 to 8. Run should print Bee and Oak, including Bee exactly on the boundary. The supplied mask print makes the decisions visible before the rows.

![A boolean mask aligns with labeled rows and keeps only matching rows.](filter-mask.svg)

## Your Tasks

1. Set the cutoff in the comparison to 8 crates.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
