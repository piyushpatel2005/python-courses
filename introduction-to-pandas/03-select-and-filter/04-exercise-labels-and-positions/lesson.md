---
title: 'Exercise: inspect two delivery windows'
slug: exercise-labels-and-positions
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Write label and position selectors that accept changing slice boundaries.
seo_title: 'Exercise: inspect two delivery windows | Introduction to Pandas'
seo_description: Write label and position selectors that accept changing slice boundaries.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Use loc with labels for the first function and iloc with integer slices for the second.
---

Use the ledger selection pattern on a delivery list. The same row can be selected by its label, such as `noon`, or its current position, such as 1. Changing the row labels should not change how a positional slice works.

`label_window` receives existing start and stop labels and must choose the named columns `item` and `count`. `position_window` receives integer positions and must choose the first two columns, whatever their names are. Neither function should reset row labels or edit the input.

The print calls are supplied. After task 1, Run should show Apples and Beans in the first table. After task 2, the second table should show Beans and Bread.

## Your Tasks

1. Use `.loc` to return rows from `start` through `stop`, inclusive, with `item` and `count` in `label_window(frame, start, stop)`.
2. Use `.iloc` to return rows from position `start` up to but not including `stop`, and the first two columns, in `position_window(frame, start, stop)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
