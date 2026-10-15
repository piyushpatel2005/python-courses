---
title: Validate a product record
slug: product-record
order: 1
language: python
lesson_type: coding
summary: Start a small shop with an immutable product record priced in integer cents.
seo_title: Validate a product record | Python OOP practice
seo_description: Start a small shop with an immutable product record priced in integer
  cents.
seo_keywords:
  - Python
  - product record
  - object oriented programming
hints:
  - Use .strip() to detect blank text and type(value) is int for prices.
---

# Validate a product record

Start a small shop with an immutable product record priced in integer cents.

This project builds a console shop in one file. It keeps all state in memory; it does not take payments, call a network, or save orders between runs. Each next starter includes the preceding solution. A frozen dataclass supplies initialization and read-only fields. Its `__post_init__` hook runs after initialization, which is a useful place to reject an invalid record. Use exact `int` checks here because Python also treats booleans as instances of `int`.

SKU means stock-keeping unit: it is the identifier used to look up a product later. A blank or whitespace-only identifier cannot do that job. Treat whitespace-only names as empty too, but preserve valid text exactly as supplied rather than stripping it before storing.

## A smaller example

The trail record shows frozen dataclass syntax with unrelated data.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Trail:
    name: str
    distance_m: int

print(Trail("Ridge", 850))
```

## Your Tasks

1. Complete `Product.__post_init__`: require nonblank string `sku` and `name`, and an exact integer `price_cents >= 0`; raise `ValueError` for any violation. Keep the supplied frozen record fields.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The valid Mug record prints first. Once validation works, the second record is rejected and the guarded probe reports `ValueError` instead of displaying a negative price. Press **Submit** to check the behavior with other inputs.
