---
title: Add products to a cart
slug: add-to-cart
order: 4
language: python
lesson_type: coding
summary: Accumulate repeated additions without sharing cart state between shoppers.
seo_title: Add products to a cart | Python OOP practice
seo_description: Accumulate repeated additions without sharing cart state between
  shoppers.
seo_keywords:
  - Python
  - add to cart
  - object oriented programming
hints:
  - Validate first; then update an existing CartLine or create a new one.
---

# Add products to a cart

Accumulate repeated additions without sharing cart state between shoppers.

A cart owns its lines; the catalog owns product lookup. Use the catalog to resolve the SKU before inserting a line. Adding an existing SKU increases its quantity instead of creating a second row. Validate quantity before mutation so a rejected request leaves the cart unchanged. `self.lines` is initialized separately for every cart.

Use the same catalog for two carts and notice that their quantities still stay separate. The catalog can safely share frozen Product objects; the mutable CartLine objects belong to individual carts. Adding a SKU to one cart must not add it to another.

## A smaller example

The color counter demonstrates the existing-key and new-key branches.

```python
counts = {"red": 2}
label = "red"
if label in counts:
    counts[label] += 3
else:
    counts[label] = 3
print(counts)
```

## Your Tasks

1. Implement `Cart.add(sku, quantity)`: require an exact positive integer quantity, resolve the product through the catalog, then insert a CartLine or increase the existing line quantity. Raise `ValueError` for invalid quantities and let unknown SKUs raise `KeyError`, without changing the cart.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Quantity: 2`. Press **Submit** to check the behavior with other inputs.
