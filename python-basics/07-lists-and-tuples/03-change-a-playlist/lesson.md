---
title: "Change an order list"
slug: change-a-playlist
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: "Replace an item at a known list index."
seo_title: "Change an order list | Python Basics"
seo_description: "Replace an item at a known list index."
seo_keywords: [python basics, python collections, beginner python]
---

A customer changed the first item in an order. Lists are mutable: you can assign a new value to one position without building a new list. For example, `order[1] = "Tea"` replaces the second item. Strings themselves do not support assignment to a character position.

You can also grow and shrink a list. Run this separate grocery example:

```python run
basket = ["rice", "tea"]
basket.append("milk")
print(basket)
basket.remove("tea")
print(basket)
```

`append()` puts one item at the end. `remove()` removes the first matching value; if it is absent, Python raises `ValueError`. `pop()` removes and returns the last item when no index is given.

In `main.py`, the starter changes the wrong position in the order. Change its index so the first item becomes `Pasta`. Press **Run** to inspect the order, then **Submit**.

## Your Task

1. Replace the first item of `order` with `Pasta` using an index assignment.
