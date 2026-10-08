---
title: Clean the sale rows
slug: clean-sale-rows
order: 3
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Convert types, remove repeated IDs and discard unusable sales.
seo_title: Clean the sale rows | Introduction to Pandas
seo_description: Convert types, remove repeated IDs and discard unusable sales.
seo_keywords:
- pandas
- community market report
- drop_duplicates
- to_numeric
- to_datetime
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Clean the sale rows

The sales sheet repeats ID 2 and leaves one unit count blank. Before computing totals, discard duplicate sale IDs, convert date and numeric columns, and remove rows lacking a usable date or amount. Only positive unit counts and nonnegative prices can be counted as sales. Work on a copy: callers may still need the raw records for an audit.

`read_tables` above is **your completed import from the previous milestone**. Edit only `clean_sales`; Run to compare raw and cleaned rows, then Submit. In the next starter, this completed cleaning function remains in place.

## Your Tasks

1. Implement `clean_sales(sales)` to keep the first row for each `sale_id`, parse `sold_at` with `pd.to_datetime(..., errors="coerce")`, convert `units` and `unit_price` with `pd.to_numeric(..., errors="coerce")`, drop missing or invalid dates/amounts, retain `units > 0` and `unit_price >= 0`, and return a reset-index copy without mutating `sales`.
