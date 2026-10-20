---
title: "Index a grocery list"
slug: index-a-supply-list
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: "Read the final item in an ordered grocery list."
seo_title: "Index a grocery list | Python Basics"
seo_description: "Read the final item in an ordered grocery list."
seo_keywords: [python basics, python collections, beginner python]
---

A grocery list has an order: the first item is the one you plan to pick up first. In Python, a list puts values between square brackets. Each value has an index, starting at `0`. A negative index counts back from the end, so `groceries[-1]` reads the last item. This works like indexing a string, but returns a whole list item rather than one character.

`len(groceries)` gives the number of items. Reading an index outside the list raises `IndexError`. For an empty list, there is no last item.

![Three grocery items with indexes 0, 1, 2 and -3, -2, -1; apples are at -1](list-indexing.svg "List indexes from either end")

The starter reads the first item. In `main.py`, change the index to read the last one. Press **Run** to see `apples`, then **Submit** to check your change.

## Your Task

1. Set `last_item` to the last item in `groceries`.
