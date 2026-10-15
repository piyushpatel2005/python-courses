---
title: Summarize the cart
slug: cart-summary
order: 6
language: python
lesson_type: coding
summary: Return stable cart rows and an integer total for display.
seo_title: Summarize the cart | Python OOP practice
seo_description: Return stable cart rows and an integer total for display.
seo_keywords:
  - Python
  - cart summary
  - object oriented programming
hints:
  - Each CartLine already exposes its subtotal_cents property.
---

# Summarize the cart

Return stable cart rows and an integer total for display.

The cart summary is structured data, not printed text. Return a pair: a list of `(sku, name, quantity, subtotal_cents)` tuples and the total cents. Sort by SKU so a shopper sees the same order regardless of the order of additions. Building fresh tuples also prevents a consumer from accidentally changing cart quantities through the summary.

The subtotal in each row already accounts for quantity. Summing unit prices would undercount repeated items, and multiplying the subtotal by quantity again would overcount them. Build the rows without removing anything from self.lines, since callers may request the same summary repeatedly.

## A smaller example

The visit rows pair each label with its count before summing.

```python
visits = {"Tue": 3, "Mon": 5}
rows = [(day, visits[day]) for day in sorted(visits)]
print(rows, sum(count for day, count in rows))
```

## Your Tasks

1. Implement `Cart.summary()` to return `(rows, total_cents)` with rows shaped `(sku, name, quantity, subtotal_cents)` in SKU order. An empty cart returns `([], 0)`; do not mutate the cart.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished summary includes one row and a total of `2500` cents. Press **Submit** to check the behavior with other inputs.
