---
title: Implement a credit fee policy
slug: implement-a-contract
order: 8
language: python
lesson_type: coding
summary: Implement a purchase fee that is waived at a credit threshold.
seo_title: Implement a credit fee policy | Python OOP practice
seo_description: Implement a purchase fee that is waived at a credit threshold.
seo_keywords:
  - Python
  - implement a contract
  - object oriented programming
hints:
  - Use >= so the exact threshold receives a waived fee.
---

# Implement a credit fee policy

The game shop waives its purchase fee when a player spends enough credits. Implement that rule as a concrete `CreditFeePolicy`, so the caller can ask for a fee without knowing which rule produced it.

A subclass satisfies an abstract method by providing a regular method with the same name. Keep the public signature compatible so callers can use any policy through the same interface. The supplied base and constructor are complete. Subtotals, thresholds, and fees use whole fictional credits, not cents. The threshold is inclusive: a purchase exactly at the threshold has a zero-credit fee. Callers supply nonnegative integer subtotals and valid policy settings; validation is outside this exercise.

Read the comparison carefully at the threshold. With a threshold of 500 credits, subtotals of 499 and 500 credits belong to different branches. The constructor is supplied because this exercise is about fulfilling the policy method, not about validating its configuration.

## A smaller example

A formatter supplies a concrete method that callers can invoke normally.

```python
class PrefixFormatter:
    def format(self, text):
        return "Quest: " + text

print(PrefixFormatter().format("light the beacon"))
```

## Your Tasks

1. Implement `ThresholdFee.fee_credits(subtotal_credits)` to return zero when the subtotal is at least `self.threshold_credits`, otherwise return `self.flat_credits`. Keep it a concrete subclass of the supplied contract.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Fee (credits): 0`. Press **Submit** to check the behavior with other inputs.

## Next: a separate console shop project

The next module leaves Lantern Vale for an unrelated e-commerce application. You will apply the same exception and contract ideas to products, carts, and orders. That project is self-contained and uses integer cents, not game credits; its delivery policy and other classes are supplied within its own lessons.
