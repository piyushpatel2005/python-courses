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
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Add revenue and sale day

A clean row still lacks the two values the report needs: revenue and a readable day. `units * unit_price` multiplies aligned columns row by row. Since `sold_at` is now datetime, `.dt.strftime("%Y-%m-%d")` can make a day label without changing its timestamp.

The previous import and cleaning functions are complete above your new `enrich_sales` stub. Edit that function, Run to inspect its columns, then Submit.

## Your Tasks

1. Implement `enrich_sales(cleaned)` to return a copy with numeric `revenue = units * unit_price` and a string `day` in `YYYY-MM-DD` format derived from `sold_at`, preserving all source rows and columns.
