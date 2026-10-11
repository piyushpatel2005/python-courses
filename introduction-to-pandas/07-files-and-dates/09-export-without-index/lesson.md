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
  - "The index option controls row labels; it does not remove the guest column."
---

# Export CSV without an index

The guest list is ready to share. Its row index helped you select records, but it is not one of the columns the coordinator requested.

`frame.to_csv()` returns CSV text when you do not supply a destination. It includes the index by default; `index=False` leaves it out while keeping the column headers. Nothing is written to a saved file in this lesson.

Change only `index=True` to `index=False` in `make_guest_csv` in `main.py`. Run and inspect the first line: it should be `guest,tickets`, with no leading comma or extra row numbers. Submit also tries an index that starts at 40.

## Your Tasks

1. Make `make_guest_csv(frame)` return CSV text containing the caller's columns and values but no index column.
