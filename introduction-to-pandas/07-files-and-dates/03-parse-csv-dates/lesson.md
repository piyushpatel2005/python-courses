---
title: Parse dates while reading
slug: parse-csv-dates
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Use read_csv parse_dates to turn date text into datetime values.
seo_title: Parse dates while reading | Introduction to Pandas
seo_description: Use read_csv parse_dates to turn date text into datetime values.
seo_keywords:
  - pandas
  - parse_dates
  - CSV dates
hints:
  - "Name arrived_on inside the parse_dates list; leave the crate column alone."
---

# Parse dates while reading

The delivery sheet includes `arrived_on`. A value such as `2026-09-01` looks like a date when printed, but a CSV cell starts as text. A datetime column lets pandas work with calendar parts rather than characters.

For a sheet of valid dates, `parse_dates=["arrived_on"]` tells `pd.read_csv` which column to convert during import. The brackets contain column names, not date values. Here all dates use the unambiguous year-month-day form `YYYY-MM-DD` and have no timezone.

In `main.py`, change only `parse_dates=[]` to `parse_dates=["arrived_on"]`. Run and compare the printed dtypes. The date column should say `datetime64[...]`; the unit inside the brackets can vary between pandas versions. Submit checks fresh dates.

This convenient import option is not a complete data-quality check: an invalid date can leave the column as text. The next lesson shows explicit conversion when you need to decide what happens to bad values.

## Your Tasks

1. Have `read_deliveries(text)` parse `arrived_on` as a datetime column while reading the CSV.
