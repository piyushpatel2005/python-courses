---
title: Export a shareable CSV
slug: export-neighborhood-report
order: 8
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Export neighborhood totals as CSV without analysis index numbers.
seo_title: Export a shareable CSV | Introduction to Pandas
seo_description: Export neighborhood totals as CSV without analysis index numbers.
seo_keywords:
- pandas
- community market report
- to_csv
- index False
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Export a shareable CSV

The neighborhood totals should be easy to hand to a coordinator. `to_csv(index=False)` returns a plain string with column headers and no row-number column. This text can be sent elsewhere or read back later; this lesson does not write a persistent file.

The imported, cleaned, enriched, filtered, joined, and grouped functions above all carry over. Add `export_report`, Run to inspect its header and rows, then Submit. Tests include a table whose index starts far from zero.

## Your Tasks

1. Implement `export_report(totals)` to return CSV text headed `neighborhood,units,revenue` with all supplied rows and no DataFrame index column.
