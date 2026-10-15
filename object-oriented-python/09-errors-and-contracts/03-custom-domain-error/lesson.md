---
title: Name a domain error
slug: custom-domain-error
order: 3
language: python
lesson_type: coding
summary: Give callers a specific error type for a sold-out workshop.
seo_title: Name a domain error | Python OOP practice
seo_description: Give callers a specific error type for a sold-out workshop.
seo_keywords:
  - Python
  - custom domain error
  - object oriented programming
hints:
  - The base class goes in parentheses after the class name.
---

# Name a domain error

Give callers a specific error type for a sold-out workshop.

A custom exception is an ordinary class that inherits from `Exception` or one of its subclasses. A meaningful name lets callers catch a business condition separately from unrelated invalid values. The supplied `reserve` function already raises `SoldOutError`; your work is to make that name an exception class. It needs no new methods because its base already stores the message.

The starter deliberately defines the right name with the wrong base. Calling it with a message currently fails before it can act as an exception. Change the class declaration, not reserve; callers should then be able to distinguish a full workshop by catching the new type.

## A smaller example

The gate exception inherits message handling without adding an initializer.

```python
class GateClosedError(Exception):
    pass

problem = GateClosedError("west gate")
print(str(problem))
```

## Your Tasks

1. Define `SoldOutError` as a subclass of `Exception` so the supplied `reserve(remaining)` raises a catchable domain error when no places remain.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. After completion the guarded probe reports `SoldOutError`, rather than `TypeError`. Press **Submit** to check the behavior with other inputs.
