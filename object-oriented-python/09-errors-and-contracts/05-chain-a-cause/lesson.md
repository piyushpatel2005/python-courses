---
title: Preserve the cause of a failure
slug: chain-a-cause
order: 5
language: python
lesson_type: coding
summary: Translate invalid inventory quantity text into a named error with its cause.
seo_title: Preserve the cause of a failure | Python OOP practice
seo_description: Translate invalid inventory quantity text into a named error with its cause.
seo_keywords:
  - Python
  - chain a cause
  - object oriented programming
hints:
  - Use except ValueError as error, then raise the new error from error.
---

# Preserve the cause of a failure

The inventory screen receives a quantity as text. Convert it to an integer, and give invalid text an `ItemQuantityError` that still points to the original conversion failure.

A public API can use its own exception vocabulary while retaining the original diagnostic information. In `raise NewError(...) from error`, the caught exception becomes the new exception's `__cause__`. Catch only `ValueError` here. A `TypeError`, such as attempting to convert a list, indicates a different problem and must remain visible.

The text "0" and negative integer text are valid conversions here. Parsing and deciding whether a quantity is allowed are different jobs; do not add positivity validation to this helper. The domain error tells a caller the text could not be interpreted as an integer.

## A smaller example

A replay tick parser shows how `except` binds the caught exception to a local name.

```python
try:
    int("paused")
except ValueError as cause:
    # A caller could inspect cause without parsing its text.
    print(type(cause).__name__)
```

## Your Tasks

1. Implement `parse_item_quantity(text)` using `int(text)`. On `ValueError`, raise `ItemQuantityError("item quantity must be an integer") from` the caught exception. Return successful conversions and let other exception types escape.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The completed probe prints `Item quantity: 8`; invalid text is checked on Submit. Press **Submit** to check the behavior with other inputs.
