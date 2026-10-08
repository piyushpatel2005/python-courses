---
title: Export CSV without an index
slug: export-without-index
order: 9
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Use to_csv(index=False) to omit the DataFrame row index.
seo_title: Export CSV without an index | Introduction to Pandas
seo_description: Use to_csv(index=False) to omit the DataFrame row index.
seo_keywords:
- pandas
- to_csv
- index False
- CSV export
hints:
- Use the example above the task and check the printed result before submitting.
---

# Export CSV without an index

A shared report should contain the columns readers asked for, not the temporary row numbers used in analysis. `frame.to_csv(index=False)` writes the header and rows as text, leaving out the index. A string return value means there is no file to manage.

Change only `index=True` to `index=False` in `make_guest_csv(frame)`. Run and inspect the first line: it should be `guest,tickets`, not start with an empty index column. Submit to test changed names and counts.

## Your Tasks

1. Make `make_guest_csv(frame)` return CSV text with no index column and with the caller's data intact.
