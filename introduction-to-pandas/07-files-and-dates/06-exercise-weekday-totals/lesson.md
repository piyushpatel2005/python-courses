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
  - "Use frame[\"visited_on\"].dt.day_name() as the groupby argument, then sum visits."
---

# Exercise: count visitors by weekday

The visitor counter needs a weekly pattern rather than a day-of-month number. Its `visited_on` column is already datetime. `.dt.day_name()` returns weekday names such as `Monday`; unlike `.dt.day`, this operation is a method and needs parentheses.

You can pass that Series directly to `groupby` as the group labels, then select `visits` and sum. The sample has two Mondays: their counts belong in one total even though the dates are a week apart. A weekday absent from the input should be absent from the result, too.

Pandas normally excludes missing group labels. In this exercise, a row with `NaT` has no known weekday, so leave it out of the weekday totals rather than guessing a day. The final project will show how to retain an unknown-label group when a report needs it.

Edit `visitors_by_weekday` in `main.py`. Run should show Monday 8 and Tuesday 7. Submit checks different dates, repeated weekdays, and a missing date.

## Your Tasks

1. Implement `visitors_by_weekday(frame)` to return summed `visits` indexed by the weekday name of `visited_on`, excluding rows with missing dates.
