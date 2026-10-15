---
title: Credit calculated interest
slug: apply-interest
order: 8
language: python
lesson_type: coding
summary: Connect the savings account to the calculator. The account handles its balance; the calculator
  handles the arithmetic.
seo_title: Credit calculated interest | Object-oriented Python
seo_description: Connect the savings account to the calculator. The account handles its balance;
  the calculator handles the arithmetic.
seo_keywords:
  - Python
  - Banking project
  - apply interest
hints:
  - Keep the returned interest in a local variable before deciding whether to deposit it.
---

Connect the savings account to the calculator. The account handles its balance; the calculator handles the arithmetic.

`SavingsAccount.apply_interest(calculator, months)` must call the supplied object’s `calculate` method exactly once with the current balance, stored rate, and requested months. Assume a calculator follows the preceding lesson’s contract and returns nonnegative integer cents. Credit a positive result once through `self.deposit` and return the earned cents, not the new balance. Return zero without calling deposit when nothing was earned, since deposit rejects zero.

Do not copy the interest formula into this method. If the calculator raises `ValueError` for invalid months, let that error reach the caller without changing the account. FixedDeposit inherits this new method and can earn interest while withdrawals stay locked. Each call uses the current balance; repeated calls are separate credits, not an automatic schedule.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `SavingsAccount.apply_interest(calculator, months)` to delegate the calculation and credit only a positive result through `deposit`, returning the earned cents.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Credited: 300 Balance: 10300
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
