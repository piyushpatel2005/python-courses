---
title: Read a market CSV
slug: read-a-csv
order: 1
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Read a comma-separated table from in-memory text with pandas read_csv.
seo_title: Read a market CSV | Introduction to Pandas
seo_description: Read a comma-separated table from in-memory text with pandas read_csv.
seo_keywords:
- pandas
- read_csv
- StringIO
- CSV columns
hints:
- Use the example above the task and check the printed result before submitting.
---

# Read a market CSV

The market sends a tiny CSV: the first row gives column names and each following row is one sale. `StringIO` wraps a string so `pd.read_csv` can treat it like a file, with no network request or saved file.

![CSV text enters a file-like buffer and becomes a labeled DataFrame](csv-to-table.svg)

The sample uses commas, but `load_visits` currently expects semicolons. Edit **only** its `sep` argument to `","` in `main.py`. Run to see separate `stall` and `visits` columns; Submit to check a second input too.

## Your Tasks

1. Make `load_visits(text)` read the comma-separated text into two correctly named columns.
