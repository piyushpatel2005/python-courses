---
title: "Exercise: Check the new delivery"
slug: exercise-quick-table-check
order: 6
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return delivery previews and a numerical summary for changing inputs."
seo_title: "Exercise: Check the new delivery | Pandas for beginners"
seo_description: "Return delivery previews and a numerical summary for changing inputs."
seo_keywords: ["pandas", "Python data analysis", "table previews and summaries"]
---

The next delivery could contain two rows or two hundred. Write helpers that inspect the table they receive without changing it.

The first helper returns two DataFrames as a tuple: the front preview, then the back preview. Use the supplied non-negative `amount` for each. If the table has fewer rows than requested, return all available rows in both previews.

For the second helper, return the table from `describe()`, rather than the printed information from `info()`. These inputs have at least one numeric column; text columns may appear alongside it.

## Your Tasks

1. Make `ends(table, amount)` return a pair containing the first `amount` rows and the last `amount` rows, using `head` and `tail`.
2. Make `numeric_summary(table)` return the numerical summary DataFrame from `table.describe()`.

Edit `main.py`, **Run**, then **Submit**. In the example with `amount=1`, the previews contain row labels `0` and `2`. The summary's means are `5` for stock and `4` for price.
