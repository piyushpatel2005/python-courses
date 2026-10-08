---
title: 'Exercise: count visitors by weekday'
slug: exercise-weekday-totals
order: 6
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Use the dt accessor and groupby to total visits per weekday.
seo_title: 'Exercise: count visitors by weekday | Introduction to Pandas'
seo_description: Use the dt accessor and groupby to total visits per weekday.
seo_keywords:
- pandas
- dt day_name
- groupby weekdays
hints:
- Use the example above the task and check the printed result before submitting.
---

# Exercise: count visitors by weekday

The visitor counter uses a different date column, `visited_on`. `.dt.day_name()` converts datetimes to weekday names such as `Monday`; group those labels to add up visits across matching days. Return a Series indexed by weekday name, so a day absent from the input is simply absent from the result.

Edit `main.py`, Run to inspect the totals, then Submit. The tests include repeated weekdays and a different week.

## Your Tasks

1. Implement `visitors_by_weekday(frame)` to return a Series of summed `visits` grouped by the weekday name of `visited_on`.
