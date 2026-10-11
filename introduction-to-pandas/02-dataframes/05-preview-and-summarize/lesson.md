---
title: "Preview and summarize rows"
slug: preview-and-summarize
order: 5
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Preview table rows and read a first numerical summary."
seo_title: "Preview and summarize rows | Pandas for beginners"
seo_description: "Preview table rows and read a first numerical summary."
seo_keywords: ["pandas", "Python data analysis", "head tail info describe"]
---

A long table is easier to inspect a few rows at a time. `sales.head(n)` returns the first `n` rows; `sales.tail(n)` returns the last `n`. Both keep the original row labels and leave `sales` unchanged.

The starter also shows two different kinds of summary. `sales.info()` prints column names, non-missing counts, and dtypes directly, so it does not need `print(...)` around it. `sales.describe()` returns a summary table, which we print ourselves.

For the numeric `sold` column, `count` is the number of non-missing values and `mean` is their average. `min` and `max` are the smallest and largest counts. The percentage rows describe positions in the sorted values, and `std` describes their spread; you do not need those statistics for this task.

## Your Task

1. Set `preview` to the first three rows of `sales` using `head(3)`.

Edit `main.py` and **Run**. The first printed table should include tea, bread, and jam. The later summaries still describe all four rows. **Submit** checks the preview.
