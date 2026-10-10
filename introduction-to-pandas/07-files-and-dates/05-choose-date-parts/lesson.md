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
  - "Select arrived_on first, then use its dt.day property without parentheses."
---

# Find the day with dt

The delivery dates are now genuine datetime values. `.dt` is an **accessor**: it gives a Series a set of date operations that act on every row. It is not a function, so there are no parentheses after `dt`.

`.dt.month` returns month numbers; `.dt.day` returns day-of-month numbers. Neither changes the source column. The result keeps its row labels, which matters when you assign it to another column. A missing datetime produces a missing date part, not zero.

In `main.py`, change only `.dt.month` to `.dt.day` inside `delivery_days`. Run should show `[4, 18]` instead of `[9, 9]`. Submit checks another month and a missing date. These are calendar days, not weekday numbers.

## Your Tasks

1. Make `delivery_days(frame)` return the day-of-month Series from its datetime `arrived_on` column, preserving row labels and missing values.
