---
title: Pivot a daily grid
slug: pivot-daily-grid
order: 11
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk needs days as columns and zones as rows.
seo_title: Pivot a daily grid | Introduction to Pandas
seo_description: The desk needs days as columns and zones as rows.
seo_keywords:
- pandas
- pivot daily grid
- community market data
---

# Pivot a daily grid

The desk needs days as columns and zones as rows. `pivot_table` aggregates repeated zone-day entries. An absent combination is missing by default; `fill_value=0` explicitly displays zero without proving an observed zero sale.

![Zone-by-day grid with an absent cell displayed as zero](pivot-grid.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Add `fill_value=0` to `daily_grid`.
