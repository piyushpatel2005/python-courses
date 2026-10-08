---
title: "Exercise: Assemble two tables"
slug: exercise-two-table-shapes
order: 2
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Columns and row records for a community market data desk."
seo_title: "Exercise: Assemble two tables | Pandas for beginners"
seo_description: "Columns and row records for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "columns and row records"]
---
The supply desk receives one batch as a column dictionary and another as a list of records. Build a table from each without fixing the number of rows. Both functions should preserve incoming column names and values.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `from_columns(columns)` return a DataFrame built from the supplied dictionary of column lists.
2. Make `from_records(records)` return a DataFrame built from the supplied list of row dictionaries.
