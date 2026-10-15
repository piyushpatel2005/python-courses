---
title: Build a searchable catalog
slug: product-catalog
order: 2
language: python
lesson_type: coding
summary: Index products by SKU while keeping catalog display order predictable.
seo_title: Build a searchable catalog | Python OOP practice
seo_description: Index products by SKU while keeping catalog display order predictable.
seo_keywords:
  - Python
  - product catalog
  - object oriented programming
hints:
  - Check whether product.sku is already a key before assigning it.
---

# Build a searchable catalog

Index products by SKU while keeping catalog display order predictable.

The catalog owns a dictionary from SKU to Product. The supplied `get` method uses dictionary lookup, so an unknown SKU raises `KeyError`. Its `all` method returns products sorted by SKU, independent of insertion order. Your constructor builds the index and rejects duplicates rather than silently replacing the first item. Each Catalog needs its own dictionary.

The products parameter is an iterable, so a loop can consume a list, a tuple, or a generator once. Create the dictionary before the loop to handle an empty iterable. Keep the Product objects themselves as values; copying only their names would lose prices needed by the cart.

## A smaller example

The book index separates lookup keys from display titles.

```python
books = {}
for code, title in [("B2", "Maps"), ("A1", "Birds")]:
    books[code] = title
print([books[code] for code in sorted(books)])
```

## Your Tasks

1. Implement `Catalog.__init__(products)` to store each product in `self.products` under its SKU and raise `ValueError("duplicate sku")` if a SKU repeats. An empty iterable must produce an empty catalog.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `['MUG']`. Press **Submit** to check the behavior with other inputs.
