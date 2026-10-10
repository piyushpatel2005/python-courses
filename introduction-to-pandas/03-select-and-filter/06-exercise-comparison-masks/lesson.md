---
title: 'Exercise: shortlist ready orders'
slug: exercise-comparison-masks
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Filter orders by a minimum quantity without losing row labels.
seo_title: 'Exercise: shortlist ready orders | Introduction to Pandas'
seo_description: Filter orders by a minimum quantity without losing row labels.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Build the mask from frame["quantity"] and the minimum parameter.
---

The pickup desk needs orders large enough for a shared delivery. This time the cutoff arrives as `minimum`, so a fixed value of 5 would only solve the printed example.

Compare the `quantity` column with that input, then use the resulting mask to select full rows. Keep an order exactly at the minimum. If no order qualifies, return an empty table with the same columns rather than None.

Replace the empty placeholder in `ready_orders`. Run should show B2 and C3, still labeled pickup-b and pickup-c. You can try minimum 8 to see the empty-result case, then restore 5.

## Your Tasks

1. Return every row with `quantity` at least `minimum` from `ready_orders(frame, minimum)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
