---
title: Add savings account data
slug: savings-account
order: 4
language: python
lesson_type: coding
summary: A savings account follows the ordinary deposit and withdrawal rules, but also records
  an annual interest rate.
seo_title: Add savings account data | Object-oriented Python
seo_description: A savings account follows the ordinary deposit and withdrawal rules, but also
  records an annual interest rate.
seo_keywords:
  - Python
  - Banking project
  - savings account
hints:
  - Let the parent constructor validate opening cents; do not duplicate that logic.
---

A savings account follows the ordinary deposit and withdrawal rules, but also records an annual interest rate.

For this fictional policy, store the rate in integer basis points: 100 basis points means 1 percent per year, so the default 300 means 3 percent. `SavingsAccount(owner, balance_cents=0, rate_bps=300)` inherits Account. Validate that `rate_bps` has exact type `int` and is nonnegative, then reuse the Account constructor for the shared data. Zero is a valid rate. Interest calculation comes later; this stage only records the rate.

Reject an invalid rate by raising `ValueError` with a message of your choice. As before, this built-in error tells the caller that an argument violates the method’s rule.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `SavingsAccount.__init__` to validate and store `rate_bps` and initialize the inherited account through `super().__init__`.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Savings rate: 300
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
