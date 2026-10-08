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
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Group neighborhood totals

The joined rows are ready for a neighborhood report. `groupby("neighborhood", as_index=False)` keeps the group label as a real column, but **drops missing labels by default**. Add `dropna=False` to keep sales from unknown stalls in their own group. For example, `pd.DataFrame({"neighborhood": ["North", None], "units": [2, 3]}).groupby("neighborhood", dropna=False)["units"].sum()` includes both North's 2 units and the missing-label group's 3 units. Without `dropna=False`, those 3 units disappear from the report. Sum both `units` and `revenue`, order neighborhoods alphabetically, and put missing labels last.

The preceding join is present above the new stub. Edit `total_by_neighborhood`; Run to see a small report, then Submit on changing group sizes.

## Your Tasks

1. Implement `total_by_neighborhood(joined)` to return a reset-index DataFrame with exactly `neighborhood`, `units`, `revenue`, summing values for each neighborhood, including missing labels, sorted by neighborhood with missing labels last.
