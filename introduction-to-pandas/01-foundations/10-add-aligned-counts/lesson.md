---
title: "Add counts by label"
slug: add-aligned-counts
order: 10
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Series arithmetic alignment for a community market data desk."
seo_title: "Add counts by label | Pandas for beginners"
seo_description: "Series arithmetic alignment for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "series arithmetic alignment"]
---
Adding two Series matches **labels**, not positions. The lists below run in opposite orders, yet `north` adds to `north`. Change the second count for `north` and read the updated total. A missing label produces a missing value rather than a positional match.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Change the `north` entry of `afternoon` from 2 to 5 so the combined `north` total is 9.
