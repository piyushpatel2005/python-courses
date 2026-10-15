---
title: Lock a fixed deposit
slug: fixed-deposit
order: 6
language: python
lesson_type: coding
summary: The third account type holds money without allowing withdrawals. Give it a stricter withdrawal
  policy while reusing savings-account data.
seo_title: Lock a fixed deposit | Object-oriented Python
seo_description: The third account type holds money without allowing withdrawals. Give it a stricter
  withdrawal policy while reusing savings-account data.
seo_keywords:
  - Python
  - Banking project
  - fixed deposit
hints:
  - No amount needs to be subtracted or compared; this policy rejects the operation itself.
---

The third account type holds money without allowing withdrawals. Give it a stricter withdrawal policy while reusing savings-account data.

`FixedDeposit` inherits `SavingsAccount`, so it already accepts `owner`, `balance_cents`, and `rate_bps`. For this small simulation, it stays locked for its entire lifetime: every call to `withdraw`, even a call with zero or an invalid amount, raises `ValueError`. It must never change the balance. Deposits remain allowed through the inherited method. There is no maturity date or unlocking behavior in this project.

This restriction also shows a limit of inheritance: a fixed deposit cannot replace an ordinary account in code that expects a funded withdrawal to succeed. The shared balance and deposit interfaces still work, but callers must allow for the withdrawal policy. In a larger design, you could separate withdrawable accounts from locked holdings instead of giving both the same withdrawal promise.

Use `raise ValueError("message")` to signal that the operation is unavailable. The supplied probe catches that specific exception and prints a label, so pressing Run does not stop with an error.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `FixedDeposit.withdraw(amount_cents)` to reject every call with `ValueError` without changing the balance.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Fixed deposit: locked
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
