---
title: "Exercise: make a vendor contact sheet"
slug: exercise-choose-columns
order: 2
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return a single vendor Series and a two-column contact sheet."
seo_title: "Exercise: make a vendor contact sheet | Introduction to Pandas"
seo_description: "Return a single vendor Series and a two-column contact sheet."
seo_keywords: [pandas, python, data selection]
---

A volunteer needs a quick list of the first few vendors and a compact contact sheet of the latest entries. The preceding card showed why one bracket pair gives a Series and a list inside brackets gives a DataFrame. Combine those selections with the `head` and `tail` previews you used earlier. Keep the original row labels, and handle different roster lengths and requested limits.

## Your Tasks

1. Return the first `limit` values of the `vendor` column as a Series from `vendor_names(frame, limit)`.
2. Return the last `limit` rows with `vendor` then `phone` from `contact_sheet(frame, limit)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
