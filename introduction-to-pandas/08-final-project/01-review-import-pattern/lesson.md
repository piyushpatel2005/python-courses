---
title: 'Warm-up: read a ticket sheet'
slug: review-import-pattern
order: 1
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Review in-memory CSV import before building the market report.
seo_title: 'Warm-up: read a ticket sheet | Introduction to Pandas'
seo_description: Review in-memory CSV import before building the market report.
seo_keywords:
- pandas
- community market report
- StringIO
- read_csv
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Warm-up: read a ticket sheet

Before the market report, rehearse the input boundary on a different table: a workshop ticket sheet. `StringIO` turns CSV text into something `pd.read_csv` can read. The header becomes column names, and tickets stay numeric.

The starter uses the wrong separator. In `main.py`, change only `sep=";"` to `sep=","`. Run to see distinct `workshop` and `tickets` columns, then Submit. Next you will use the same pattern with market sales and a stall directory.

## Your Tasks

1. Make `read_tickets(text)` split the two comma-separated columns for any supplied ticket sheet.
