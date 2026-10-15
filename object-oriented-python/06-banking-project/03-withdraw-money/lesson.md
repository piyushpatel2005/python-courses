---
title: Withdraw available money
slug: withdraw-money
order: 3
language: python
lesson_type: coding
summary: An ordinary account must not spend more cents than it holds. Add that boundary to withdrawals.
seo_title: Withdraw available money | Object-oriented Python
seo_description: An ordinary account must not spend more cents than it holds. Add that boundary
  to withdrawals.
seo_keywords:
  - Python
  - Banking project
  - withdraw money
hints:
  - Do both checks before subtracting. Equality with the current balance is valid.
---

An ordinary account must not spend more cents than it holds. Add that boundary to withdrawals.

`withdraw(amount_cents)` uses the same strictly positive integer rule as deposit, then checks the available balance. Withdrawing exactly the balance is allowed and leaves zero. More than the balance is rejected. Every rejected call raises `ValueError` before changing the balance; valid calls subtract once and return the new balance.

`ValueError` is the built-in exception used here to signal an unacceptable amount. The caller can catch it with `except ValueError`; you do not need a custom exception class.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `Account.withdraw(amount_cents)` to enforce the amount and available-balance rules, return the remaining cents, and leave rejected withdrawals unchanged.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
After withdrawal: 1100
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
