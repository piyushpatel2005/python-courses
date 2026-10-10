---
title: "Exercise: Make a count card"
slug: exercise-import-pandas
order: 3
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Build a reusable function that turns donation counts into a Series."
seo_title: "Exercise: Make a count card | Pandas for beginners"
seo_description: "Build a reusable function that turns donation counts into a Series."
seo_keywords: ["pandas", "Python data analysis", "create a series from a list"]
---

The donation desk receives a new Python list each day. Write a function that turns the list it receives into a Series, rather than rebuilding one particular day's card.

The import is supplied. Inside `count_card`, replace `return None` with a return statement that uses the `values` parameter. `return` sends the Series back to the caller; the supplied `print(...)` then displays it. You do not need to add another print inside the function.

## Your Task

1. Make `count_card(values)` return a pandas Series containing the supplied values in order, with the default index.

Edit `main.py`, then **Run**. The example should show counts `2`, `9`, and `4` beside labels `0`, `1`, and `2`. **Submit** checks other lists too, including an empty list.
