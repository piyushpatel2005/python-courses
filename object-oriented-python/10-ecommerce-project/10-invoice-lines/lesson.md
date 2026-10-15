---
title: Format invoice lines
slug: invoice-lines
order: 10
language: python
lesson_type: coding
summary: Render the immutable purchase rows as readable invoice items.
seo_title: Format invoice lines | Python OOP practice
seo_description: Render the immutable purchase rows as readable invoice items.
seo_keywords:
  - Python
  - invoice lines
  - object oriented programming
hints:
  - Unpack each row and pass its final value to money.
---

# Format invoice lines

Render the immutable purchase rows as readable invoice items.

Formatting belongs outside the cart and order records. The supplied `money` helper uses integer division and a two-digit remainder, so one cent displays as `0.01`. It assumes a nonnegative integer amount, which the product and quantity contracts guarantee. Invoice reads the order snapshot, so a later cart change cannot alter its lines. This invoice has no taxes, discounts, or shipping charges.

Read each stored row as sku, name, quantity, and subtotal. The last number is already the complete line amount. Return a list rather than joining the strings yet: the next lesson will add the heading and total around these individual lines.

## A smaller example

The duration display pads a remainder to two digits, just as cents need two places.

```python
duration = 125
print(f"{duration // 60}:{duration % 60:02d}")
```

## Your Tasks

1. Implement `Invoice.lines()` to return one string per stored order row, preserving row order, in the form `"SKU | Name | Q x | $D.CC"`. Use the row subtotal (not unit price). Return an empty list for no rows.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished line ends with `$25.00`. Press **Submit** to check the behavior with other inputs.
