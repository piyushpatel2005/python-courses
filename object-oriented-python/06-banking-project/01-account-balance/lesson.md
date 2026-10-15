---
title: Open an account in cents
slug: account-balance
order: 1
language: python
lesson_type: coding
summary: Build a small in-memory banking simulation. Start with an account whose balance is a
  whole number of cents.
seo_title: Open an account in cents | Object-oriented Python
seo_description: Build a small in-memory banking simulation. Start with an account whose balance
  is a whole number of cents.
seo_keywords:
  - Python
  - Banking project
  - account balance
hints:
  - Check the type before comparing with zero; the supplied property reads the stored private-by-convention
    attribute.
---

Build a small in-memory banking simulation. Start with an account whose balance is a whole number of cents.

This is a programming model, not financial advice or a real banking system. `Account(owner, balance_cents=0)` receives an owner string and an opening balance. Store the owner unchanged and store the balance as `_balance_cents`; the supplied read-only property exposes `balance_cents`.

Reject a negative balance or any value whose exact type is not `int`, including booleans. Write `raise ValueError("a useful explanation")` when a value breaks the rule. Raising stops the constructor; `try`/`except ValueError` lets a caller handle that rejection. Error messages are your choice. The dedicated errors module will revisit this in more detail. Use `type(value) is int` for this exercise because `isinstance(True, int)` also accepts a boolean.

## Your Tasks

1. Complete `Account.__init__` to accept nonnegative integer cents, reject invalid opening balances with `ValueError`, and store `owner` and `_balance_cents`.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe should print:

```text
Opening cents: 1250
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
