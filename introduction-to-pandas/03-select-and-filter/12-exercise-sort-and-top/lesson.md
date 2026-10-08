---
title: "Exercise: rank pickup points"
slug: exercise-sort-and-top
order: 12
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Sort a full table and return a requested number of largest values."
seo_title: "Exercise: rank pickup points | Introduction to Pandas"
seo_description: "Sort a full table and return a requested number of largest values."
seo_keywords: [pandas, python, data selection]
---

The pickup team wants an ordered list of all points and a short list for the whiteboard. Use the supplied `visits` column and preserve original row labels. The full ranking includes tied values; the short list returns exactly `count` rows (or all available rows if fewer), so a tie at the cutoff does not add extra rows. Both functions should accept other tables; `top_points` must also accept different values of `count`.

You can now select, filter, and rank the market's records without editing the input table.

## Your Tasks

1. Return all rows in descending `visits` order from `rank_points(frame)`.
2. Return the `count` rows with the largest `visits` from `top_points(frame, count)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
