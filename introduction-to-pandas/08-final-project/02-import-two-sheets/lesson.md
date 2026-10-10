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
  - "Assign each pd.read_csv(StringIO(...)) result to its matching variable before the supplied return."
---

# Import the two market sheets

The Community Data Desk receives a sales sheet and a stall directory. Sales use `stall_id`; the directory gives each ID a name and neighborhood. Read them separately so you can inspect both before joining them.

![The sample market data moves from six sales rows to four clean rows and two reported sales](market-report-pipeline.svg)

The example report uses Walk-in sales with revenue of at least 4. North contributes 7.5 and South contributes 16.0. The directory waits for the join; it does not go through sales cleaning.

In `main.py`, `read_tables` already returns a pair. Replace its two empty DataFrames one at a time, using a fresh `StringIO` buffer for each incoming string. Run prints both row counts, even before you finish. Submit after either task to check that table on its own. The completed sample has six sales rows and three directory rows.

From here on, each starter includes the preceding lesson's completed functions and the same sample sheets. You do not need to copy code between lessons; only the new work is graded.

## Your Tasks

1. Make the first value returned by `read_tables(sales_text, stalls_text)` the DataFrame read from `sales_text`.
2. Make its second returned value the DataFrame read from `stalls_text`.
