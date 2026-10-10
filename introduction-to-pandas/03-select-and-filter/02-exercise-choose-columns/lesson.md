---
title: 'Exercise: make a vendor contact sheet'
slug: exercise-choose-columns
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Return a single vendor Series and a two-column contact sheet.
seo_title: 'Exercise: make a vendor contact sheet | Introduction to Pandas'
seo_description: Return a single vendor Series and a two-column contact sheet.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Select the column or columns first, then call head(limit) or tail(limit).
---

A volunteer needs two views of the vendor roster: names from the beginning and contact details from the end. Combine column selection with the `head` and `tail` methods from the previous module.

A Series is the right shape for names alone. The contact sheet should stay a DataFrame, with `vendor` before `phone`, regardless of the input column order. Keep the original row labels. Here `limit` is a nonnegative count; zero returns no rows and a count larger than the roster returns all available rows.

The supplied empty returns are placeholders, not steps to copy. Replace one function at a time. The two print calls already let you check each result: with limit 1, the names view shows Mina and the contact sheet shows Sol.

## Your Tasks

1. Return the first `limit` values of the `vendor` column as a Series from `vendor_names(frame, limit)`.
2. Return the last `limit` rows with `vendor` then `phone` from `contact_sheet(frame, limit)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
