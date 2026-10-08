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
- Use the example above the task and check the printed result before submitting.
---

# Parse dates while reading

A delivery CSV stores dates as strings. Parsing on import gives a datetime column you can filter and calculate with, rather than comparing date-shaped text. In `pd.read_csv(..., parse_dates=["arrived_on"])`, the list names the column to convert.

Change only `parse_dates=[]` to `parse_dates=["arrived_on"]` in `main.py`. Run: the printed values look similar, but the displayed `dtype` changes to `datetime64[...]`. Submit to check both a single-day and a multi-day sheet.

## Your Tasks

1. Have `read_deliveries(text)` parse `arrived_on` as a datetime column while reading the CSV.
