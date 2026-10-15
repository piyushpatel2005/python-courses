---
title: Allow a current-account overdraft
slug: current-account
order: 5
language: python
lesson_type: coding
summary: A current account uses a different withdrawal boundary. Its balance may go below zero,
  but only as far as its agreed overdraft.
seo_title: Allow a current-account overdraft | Object-oriented Python
seo_description: A current account uses a different withdrawal boundary. Its balance may go below
  zero, but only as far as its agreed overdraft.
seo_keywords:
  - Python
  - Banking project
  - current account
hints:
  - Compare the proposed balance with the negative limit; equality is allowed.
---

A current account uses a different withdrawal boundary. Its balance may go below zero, but only as far as its agreed overdraft.

The supplied `CurrentAccount` constructor already validates a nonnegative integer overdraft and calls the parent constructor. Opening balances still cannot be negative. Only its `withdraw` method is unfinished. A balance of 200 with an overdraft of 500 may reach -500, but not -501. The amount itself must still be a strictly positive integer; reject floats and booleans as before.

Raise `ValueError` before any mutation for an invalid amount or an exceeded limit. This signals rejection to a caller using `except ValueError`. Do not call the parent withdrawal here: that method deliberately disallows negative balances. The inherited deposit can bring an overdrawn balance back toward zero.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `CurrentAccount.withdraw(amount_cents)` to return the new balance when it stays at or above `-self.overdraft_cents`, and otherwise raise `ValueError` without changing state.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Current cents: -500
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
