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
  - "Match the separator to the comma in workshop,tickets."
---

# Warm-up: read a ticket sheet

Before starting the market report, check the import pattern on a workshop ticket sheet. `StringIO` gives `pd.read_csv` a file-like view of the supplied text; the header names the columns, and the ticket counts become numbers.

In `main.py`, change only `sep=";"` to `sep=","` inside `read_tickets`. Run should show Pottery with 7 tickets and Printing with 4, rather than one combined column. Submit checks another sheet.

This warm-up stands alone. The next lesson starts a continuing project with sales and a stall directory.

## Your Tasks

1. Make `read_tickets(text)` return the two-column DataFrame from any supplied comma-separated ticket sheet.
