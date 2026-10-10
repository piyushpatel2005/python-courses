---
title: "Name the labels"
slug: name-series-labels
order: 6
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Give a Series meaningful labels without changing its values."
seo_title: "Name the labels | Pandas for beginners"
seo_description: "Give a Series meaningful labels without changing its values."
seo_keywords: ["pandas", "Python data analysis", "custom series index labels"]
---

The second stall has a count of `4`, but its name was recorded as `unknown`. Correct the label without changing the count.

In `pd.Series(values, index=labels)`, the first label belongs to the first value, the second label to the second value, and so on. Supply one label per value. Here `fruit` belongs to `12`; the replacement name belongs to `4`.

## Your Task

1. Replace the second index label, `unknown`, with `herbs` in `stalls`, leaving both counts unchanged.

Edit `main.py`, **Run**, and check that the two rows are `fruit: 12` and `herbs: 4`. Then **Submit**. Next you will use supplied names and counts to build a card from scratch.
