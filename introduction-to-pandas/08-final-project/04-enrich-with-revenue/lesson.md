---
title: Add revenue and sale day
slug: enrich-with-revenue
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Calculate sale revenue and a date label without changing source rows.
seo_title: Add revenue and sale day | Introduction to Pandas
seo_description: Calculate sale revenue and a date label without changing source rows.
seo_keywords:
  - pandas
  - community market report
  - revenue
  - dt strftime
hints:
  - "Use result[\"sold_at\"].dt.strftime(\"%Y-%m-%d\") for the label, not a fixed sample date."
---

# Add revenue and sale day

The cleaned table has usable amounts and datetime values. Add two report columns in `enrich_sales`: the money from each sale and a readable day label. The import and cleaning functions above it are already complete.

Multiplying `units` by `unit_price` works row by row because the two Series have matching row labels. For the label, `.dt.strftime("%Y-%m-%d")` formats each datetime as year-month-day text. Formatting is the reverse direction from parsing: the new `day` column is text, while `sold_at` stays datetime.

Edit the task comments in `main.py`; the copy and return are supplied. Run after either change to see the added column, then Submit. The first sample sale should gain revenue 7.5 and day `2026-09-05`. Each task is checked separately; a missing `day` column will not block credit for revenue.

## Your Tasks

1. Add `revenue` to the returned copy as `units * unit_price`, preserving the source rows and columns.
2. Add `day` to the returned copy as year-month-day text derived from `sold_at`, without changing the input.
