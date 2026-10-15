---
title: Remove a cart line
slug: remove-from-cart
order: 5
language: python
lesson_type: coding
summary: Let a shopper remove one entire product line from the cart.
seo_title: Remove a cart line | Python OOP practice
seo_description: Let a shopper remove one entire product line from the cart.
seo_keywords:
  - Python
  - remove from cart
  - object oriented programming
hints:
  - Check membership before using del.
---

# Remove a cart line

Let a shopper remove one entire product line from the cart.

Removal works at the line level in this shop: it removes every unit of the chosen SKU. A boolean result tells the command layer whether anything changed. Treat a missing SKU as a normal no-op, not an exception. This makes a repeated remove command safe and keeps the command response simple.

Return True only when a deletion happened. Returning the removed CartLine would be truthy, but it is not the boolean interface requested here. The later router uses the boolean to choose between "Removed" and "Not in cart" responses.

## A smaller example

Deleting the blue key removes that entry while leaving gold untouched.

```python
colors = {"blue": 4, "gold": 2}
if "blue" in colors:
    del colors["blue"]
print(colors)
```

## Your Tasks

1. Implement `Cart.remove(sku)` to delete the entire matching line and return `True`; if the SKU is absent, return `False` without changing other lines.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Removed: False`. Press **Submit** to check the behavior with other inputs.
