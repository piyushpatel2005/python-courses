---
title: Group neighborhood totals
slug: group-neighborhood-totals
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Aggregate units and revenue by neighborhood in a tidy report.
seo_title: Group neighborhood totals | Introduction to Pandas
seo_description: Aggregate units and revenue by neighborhood in a tidy report.
seo_keywords:
  - pandas
  - community market report
  - groupby
  - aggregate
hints:
  - "Use groupby(\"neighborhood\", as_index=False, dropna=False), select both amount columns, and sum."
---

# Group neighborhood totals

The joined rows can now become a neighborhood report. Group by `neighborhood` and sum `units` and `revenue`. `as_index=False` keeps the neighborhood label as a column, ready for export.

A left join can leave a neighborhood missing. `groupby` drops missing group labels by default, which would hide that sale's contribution. Use `dropna=False` to keep an unknown-neighborhood group. For example, North with 2 units and a missing neighborhood with 3 units must contribute two groups, not just North's 2.

Sort the report by neighborhood, with missing labels last, and reset the row index. This gives readers a predictable order without inventing a name for an unknown stall.

Edit `total_by_neighborhood` in `main.py`. Run should produce North with 3 units and 7.5 revenue, then South with 4 units and 16.0 revenue. Submit also checks repeated neighborhoods and missing labels.

## Your Tasks

1. Implement `total_by_neighborhood(joined)` to return a reset-index DataFrame with `neighborhood`, `units`, and `revenue`, summed by neighborhood and sorted alphabetically with the missing-label group last.
