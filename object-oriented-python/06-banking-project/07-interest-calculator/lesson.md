---
title: Calculate simple interest separately
slug: interest-calculator
order: 7
language: python
lesson_type: coding
summary: Interest arithmetic does not need to own an account. Put it in an independent calculator
  that receives numbers and returns cents.
seo_title: Calculate simple interest separately | Object-oriented Python
seo_description: Interest arithmetic does not need to own an account. Put it in an independent
  calculator that receives numbers and returns cents.
seo_keywords:
  - Python
  - Banking project
  - interest calculator
hints:
  - Validate each input, then multiply before the single floor division.
---

Interest arithmetic does not need to own an account. Put it in an independent calculator that receives numbers and returns cents.

`InterestCalculator` must remain separate from the Account hierarchy. Its `calculate(principal_cents, rate_bps, months)` method returns simple interest, not principal plus interest. All three arguments must be nonnegative values of exact type `int`; reject other values with `ValueError` before calculating. This built-in error reports invalid inputs, as in the earlier account methods.

The fictional annual policy is `principal_cents * rate_bps * months // 120000`. The denominator combines 10,000 basis points per whole rate and 12 months per year. `//` drops any fraction of a cent once, after multiplying all three values. Do not round each month, use floating-point money, or compound within a call. For example, 20,000 cents at 600 basis points for 3 months earns 300 cents. Any zero input gives zero. This policy is an exercise rule, not advice about real products.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `InterestCalculator.calculate` with the stated integer-input validation and whole-cent simple-interest formula.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Interest cents: 300
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
