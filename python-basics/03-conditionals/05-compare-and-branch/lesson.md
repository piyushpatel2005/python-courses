---
title: "Choose a Stock Message"
slug: compare-and-branch
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Use if, elif, and else to choose a message for remaining bread stock."
seo_title: "Python if, elif, else Branches | Python Basics"
seo_description: "Read an ordered conditional chain for bread-stock levels and change its input."
seo_keywords: [python if else, python elif, stock levels]
---

A bakery checks how many loaves remain before printing a stock message. A comparison produces `True` or `False`; an `if` statement uses that result to choose which assignment runs.

Read the branches in `main.py` from top to bottom:

- `if loaves_left < 8:` asks for more bread when fewer than eight loaves remain.
- `elif loaves_left < 16 and not delivery_today:` checks the next case only if the first was false. Both parts must be true.
- `else:` covers all remaining cases, including a delivery day. It has no condition.

Only the first matching branch runs. Each branch heading ends in a colon, and its assignment is indented four spaces. The unindented `print(stock_message)` runs afterward. With 12 loaves and no delivery today, **Run** prints `Check the bread shelf`.

## Your Tasks

1. Set `loaves_left` to `4` while keeping the branches. **Run** should now print `Bake more bread`.

Edit `main.py`, press **Run**, then **Submit**. Next you'll write the branches yourself.
