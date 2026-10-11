---
title: 'Exercise: load inventory CSV'
slug: exercise-read-inventory
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Write a reusable function that reads changing inventory CSV text.
seo_title: 'Exercise: load inventory CSV | Introduction to Pandas'
seo_description: Write a reusable function that reads changing inventory CSV text.
seo_keywords:
  - pandas
  - read_csv
  - inventory CSV
hints:
  - "Use the function parameter inside StringIO, not the sample variable below the function."
---

# Exercise: load inventory CSV

The supply desk sends inventory rather than visitor counts. Its header is `item,stock`, so let the CSV reader discover those names rather than building a table of your own.

The imports and a small Run example are already in `main.py`. Replace the empty return value in `load_inventory`. Wrap its `text` parameter in `StringIO`, then give that buffer to `pd.read_csv`. Commas are the default separator. The reader infers numeric stock values from these whole-number cells.

Run should show Paper bags with 20 in stock and Labels with 7. Submit also tries a one-row sheet; the function should work without depending on those sample names.

## Your Tasks

1. Implement `load_inventory(text)` to return a DataFrame with `item` and numeric `stock` columns parsed from the supplied CSV text.
