---
title: Implement a delivery policy
slug: implement-a-contract
order: 8
language: python
lesson_type: coding
summary: Provide a concrete delivery fee policy with a free-delivery threshold.
seo_title: Implement a delivery policy | Python OOP practice
seo_description: Provide a concrete delivery fee policy with a free-delivery threshold.
seo_keywords:
  - Python
  - implement a contract
  - object oriented programming
hints:
  - Use >= so the exact threshold receives free delivery.
---

# Implement a delivery policy

Provide a concrete delivery fee policy with a free-delivery threshold.

A subclass satisfies an abstract method by providing a regular method with the same name. Keep the public signature compatible so callers can use any policy through the same interface. The supplied base and constructor are complete. Prices and fees use integer cents: the threshold is inclusive, so an order exactly at the threshold receives free delivery.

Read the comparison carefully at the threshold. With a threshold of 5000, subtotals of 4999 and 5000 belong to different branches. The constructor is supplied because this exercise is about fulfilling the policy method, not about validating its configuration.

## A smaller example

A formatter supplies a concrete method that callers can invoke normally.

```python
class PrefixFormatter:
    def format(self, text):
        return "Note: " + text

print(PrefixFormatter().format("bring water"))
```

## Your Tasks

1. Implement `ThresholdDelivery.fee_cents(subtotal_cents)` to return zero when the subtotal is at least `self.threshold_cents`, otherwise return `self.flat_cents`. Keep it a concrete subclass of the supplied contract.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Delivery: 0`. Press **Submit** to check the behavior with other inputs.
