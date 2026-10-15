---
title: Deposit money
slug: deposit-money
order: 2
language: python
lesson_type: coding
summary: An account can store its starting balance. Now let a caller add money through a method
  rather than writing the stored attribute directly.
seo_title: Deposit money | Object-oriented Python
seo_description: An account can store its starting balance. Now let a caller add money through
  a method rather than writing the stored attribute directly.
seo_keywords:
  - Python
  - Banking project
  - deposit money
hints:
  - Validate first, mutate second, return the resulting balance last.
---

An account can store its starting balance. Now let a caller add money through a method rather than writing the stored attribute directly.

`deposit(amount_cents)` accepts a strictly positive integer. Zero, negative values, floats, strings, booleans, and None are invalid. Raise `ValueError` before changing any state when the amount is invalid. For a valid amount, add it once and return the updated integer balance. A deposit changes this account only.

As in the opening-balance check, `raise ValueError("message")` rejects a value and stops the method. A caller may catch it with `except ValueError`; the text of the message is not graded.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `Account.deposit(amount_cents)` with the positive-integer rule, returning the new balance and leaving the balance unchanged on rejection.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
After deposit: 1500
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
