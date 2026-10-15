---
title: Preserve the cause of a failure
slug: chain-a-cause
order: 5
language: python
lesson_type: coding
summary: Translate an integer conversion failure into a named quantity error.
seo_title: Preserve the cause of a failure | Python OOP practice
seo_description: Translate an integer conversion failure into a named quantity error.
seo_keywords:
  - Python
  - chain a cause
  - object oriented programming
hints:
  - Use except ValueError as error, then raise the new error from error.
---

# Preserve the cause of a failure

Translate an integer conversion failure into a named quantity error.

A public API can use its own exception vocabulary while retaining the original diagnostic information. In `raise NewError(...) from error`, the caught exception becomes the new exception's `__cause__`. Catch only `ValueError` here. A `TypeError`, such as attempting to convert a list, indicates a different problem and must remain visible.

The text "0" and negative integer text are valid conversions here. Parsing and deciding whether a quantity is allowed are different jobs; do not add positivity validation to this helper. The domain error tells a caller the text could not be interpreted as an integer.

## A smaller example

The age example shows how except binds the caught exception to a local name.

```python
class InvalidAge(Exception):
    pass

try:
    int("old")
except ValueError as cause:
    # A caller could inspect cause without parsing its text.
    print(type(cause).__name__)
```

## Your Tasks

1. Implement `parse_quantity(text)` using `int(text)`. On `ValueError`, raise `QuantityError("quantity must be an integer") from` the caught exception. Return successful conversions and let other exception types escape.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The completed probe prints `Quantity: 8`; invalid text is checked on Submit. Press **Submit** to check the behavior with other inputs.
