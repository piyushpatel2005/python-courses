---
title: Calculate a cart line
slug: cart-line
order: 3
language: python
lesson_type: coding
summary: Combine a product and quantity into a cart line with an exact subtotal.
seo_title: Calculate a cart line | Python OOP practice
seo_description: Combine a product and quantity into a cart line with an exact subtotal.
seo_keywords:
  - Python
  - cart line
  - object oriented programming
hints:
  - The product is available through self.product.
---

# Calculate a cart line

Combine a product and quantity into a cart line with an exact subtotal.

A CartLine holds a Product rather than duplicating its name and price. The constructor already rejects nonpositive or noninteger quantities. The subtotal is a computed property, so it reads the current quantity whenever requested. Do not format money here; other objects still need an integer for arithmetic.

For a product costing 1250 cents, a quantity of two makes a subtotal of 2500 cents. Store the product and quantity, not a cached subtotal: changing quantity should change the next property result. Read the value with line.subtotal_cents, without parentheses.

## A smaller example

The reading property derives seconds whenever it is accessed.

```python
class Reading:
    def __init__(self, minutes):
        self.minutes = minutes

    @property
    def seconds(self):
        return self.minutes * 60
```

## Your Tasks

1. Implement `CartLine.subtotal_cents` as a property returning the product price multiplied by the line quantity.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The completed probe prints `Line cents: 2500`. Press **Submit** to check the behavior with other inputs.
