---
title: Register and track an order
slug: order-registry
order: 9
language: python
lesson_type: coding
summary: Store completed orders separately from their delivery status.
seo_title: Register and track an order | Python OOP practice
seo_description: Store completed orders separately from their delivery status.
seo_keywords:
  - Python
  - order registry
  - object oriented programming
hints:
  - Reject duplicates before updating either orders or statuses.
---

# Register and track an order

Store completed orders separately from their delivery status.

The registry supplies lookup and status tracking. Purchase records stay frozen, while a separate status dictionary can move from `placed` to `shipped` to `delivered`. That transition method is provided and rejects skipped or backward steps. Your task is the registration boundary: duplicate IDs must not overwrite an existing purchase or reset its status. Different registry instances must not share dictionaries.

Use the order ID consistently in both dictionaries. A duplicate must be rejected before either assignment, particularly after an order has shipped; resetting its status to placed would erase real progress. Tracking changes only statuses, so the price and quantities remain the original purchase values.

## A smaller example

The record dictionary refuses an ID that is already present.

```python
records = {}
code = "R4"
if code in records:
    raise ValueError("duplicate record")
records[code] = ("registered", 12)
```

## Your Tasks

1. Implement `OrderRegistry.add(order)` to reject duplicate IDs with `ValueError("duplicate order")`, otherwise store the exact order in `self.orders` and initialize its status to `"placed"` in `self.statuses`. Do not change either dictionary on rejection.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Status: placed`. Press **Submit** to check the behavior with other inputs.
