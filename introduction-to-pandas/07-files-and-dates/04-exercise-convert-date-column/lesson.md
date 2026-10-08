---
title: 'Exercise: convert sign-up dates'
slug: exercise-convert-date-column
order: 4
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Convert a DataFrame string column to datetimes with to_datetime.
seo_title: 'Exercise: convert sign-up dates | Introduction to Pandas'
seo_description: Convert a DataFrame string column to datetimes with to_datetime.
seo_keywords:
- pandas
- to_datetime
- DataFrame dates
hints:
- Use the example above the task and check the printed result before submitting.
---

# Exercise: convert sign-up dates

Sometimes a DataFrame already exists when you notice that its `signed_on` column is still text. `pd.to_datetime(frame["signed_on"])` converts that column without reading the source again. Work on a copy so a caller can keep its original table.

Edit `main.py`, Run to compare the original and converted dtypes, then Submit. This time the input is a **DataFrame**, not CSV text.

## Your Tasks

1. Implement `convert_signups(frame)` to return a copy whose `signed_on` column contains datetime values, without changing the incoming frame.
