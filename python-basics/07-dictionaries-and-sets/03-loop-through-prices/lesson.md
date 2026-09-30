---
title: Loop Through Dictionary Entries
slug: loop-through-prices
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Unpack key-value pairs with dictionary items().
seo_title: Loop Through Dictionary Entries | Python Basics
seo_description: Unpack key-value pairs with dictionary items() with an editable Python
  example and checked task.
seo_keywords:
- python dictionary-loop
- beginner dictionary-loop exercise
---

To visit both keys and values, `prices.items()` yields pairs. `for item, price in prices.items():` unpacks each pair, preserving insertion order in modern Python. `prices.keys()` visits just keys; `prices.values()` visits just values. A dictionary has no numbered key positions.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change the loop to append the item name rather than its price. Run should print the two item names; then Submit.

## Your Task

1. Loop through `prices.items()` and append each key to `items`.
