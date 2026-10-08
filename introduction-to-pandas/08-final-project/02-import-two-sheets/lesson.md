---
title: Import the two market sheets
slug: import-two-sheets
order: 2
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Read sales and stall directory CSV text as two DataFrames.
seo_title: Import the two market sheets | Introduction to Pandas
seo_description: Read sales and stall directory CSV text as two DataFrames.
seo_keywords:
- pandas
- community market report
- import CSV
- two tables
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Import the two market sheets

The market desk receives two small sheets. Sales identify stalls by `stall_id`; a separate directory names each stall and neighborhood. Keep the two inputs separate for now so each can be checked before a join. Both CSV strings are in memory; nothing needs downloading or saving.

![Market report stages from input sheets through cleanup and enrichment to a joined export](market-report-pipeline.svg)

Edit only `read_tables` at the bottom of `main.py`. Run to inspect the two table shapes, then Submit. This first milestone supplies the data that every later starter carries forward.

## Your Tasks

1. Implement `read_tables(sales_text, stalls_text)` to return `(sales_frame, stalls_frame)` by reading **each supplied string** with `StringIO` and `pd.read_csv`.
