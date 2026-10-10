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
  - "Return totals.to_csv(...) directly, with index=False."
---

# Export a shareable CSV

The coordinator can read the grouped result outside your Python program if you return it as CSV text. The header should be `neighborhood,units,revenue`; analysis row numbers are not part of that report.

The completed pipeline through grouping is already in `main.py`. Write `export_report` using `to_csv(index=False)`. With no destination argument, this returns a string rather than saving a file. If a neighborhood is missing, CSV represents that cell as empty by default; its units and revenue still belong in the report.

Run prints the header and the North and South rows. Submit checks a different report, including an input whose row index is not zero-based. Do not reconstruct the sample values in your function.

## Your Tasks

1. Implement `export_report(totals)` to return CSV text headed `neighborhood,units,revenue`, with every supplied row and no DataFrame index column.
