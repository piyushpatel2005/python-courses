---
title: "Choose a Stock Message"
slug: compare-and-branch
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Use if, elif, and else to choose a message for remaining bread stock."
seo_title: "Python if, elif, else Branches | Python Basics"
seo_description: "Read an ordered conditional chain for bread-stock levels and change its input."
seo_keywords: [python if else, python elif, stock levels]
---

A bakery checks how many loaves remain before printing a stock message. A comparison produces `True` or `False`; an `if` statement uses that result to choose which assignment runs.

The basic structure of `if..elif..else` looks like this.

```python
if condition1:
    ... ...
elif condition2:
    ... ...
else:
    ... ...
```

In this case, Python interpreter checks one condition at a time and flows from top to bottom. If one of the condition is met, that code blocks is executed. If none of the conditions met, finally, it will execute the `else` block. Again, remember the code block is the code indented after the colon (`:`) symbol in Python.

Read the branches in `main.py` from top to bottom:

- `if loaves_left < 8:` asks to bake more breads
- `elif loaves_left < 16 and not delivery_today:` asks to check the bread shelf
- `else:` asks to count inventory

## Your Tasks

1. Set `loaves_left` to `4` while keeping the branches. **Run** should now print `Bake more bread`.

Edit `main.py`, press **Run**, then **Submit**. Next you'll write the branches yourself.
