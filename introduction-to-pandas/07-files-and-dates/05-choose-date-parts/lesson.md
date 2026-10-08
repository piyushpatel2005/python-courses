---
title: Find the day with dt
slug: choose-date-parts
order: 5
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Access datetime components from a pandas column with dt.
seo_title: Find the day with dt | Introduction to Pandas
seo_description: Access datetime components from a pandas column with dt.
seo_keywords:
- pandas
- dt accessor
- datetime day
hints:
- Use the example above the task and check the printed result before submitting.
---

# Find the day with dt

The market wants to know which calendar day each delivery arrived. A Series of datetime values exposes date parts through `.dt`; `.dt.month` gets month numbers, while `.dt.day` gets day-of-month numbers. The result is a Series aligned with the original rows.

Change only `.dt.month` to `.dt.day` inside `delivery_days(frame)`. Run: the example should print `4, 18` rather than `9, 9`. Submit to try other months and dates.

## Your Tasks

1. Make `delivery_days(frame)` return the day-of-month numbers from its datetime `arrived_on` column.
