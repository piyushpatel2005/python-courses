---
title: Property setters
slug: property-setters
order: 10
language: python
lesson_type: coding
summary: 'Add the `Tool.loan_days` setter: accept and store positive integer inputs in `_loan_days`, but raise `ValueError`
  for zero or negative inputs before changing stored state. The supplied initializer must use the same rule.'
seo_title: Property setters | Python OOP practice
seo_description: 'Add the `Tool.loan_days` setter: accept and store positive integer inputs in `_loan_days`, but raise `ValueError`
  for zero or negative inputs before changing stored state. The supplied initializer must use the same rule.'
seo_keywords:
- Python OOP
- property setters
- coding practice
---

# Property setters

A tool's loan period may change, but it must stay positive. Keep attribute-style assignment while putting the rule in one place. A property setter receives attempted assignments and decides whether to store them.

## Pair a setter with its getter

```python
class Volume:
    def __init__(self, level):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            raise ValueError("level must be nonnegative")
        self._level = value
```

First define the getter with `@property`. Then `@level.setter` creates a version of that property with a setter attached. Reuse the same method name, `level`, so the class name refers to the combined property. The setter takes `self` and the attempted value; `volume.level = 4` supplies that value automatically.

Store accepted values under a different name such as `_level`. Assigning to `self.level` inside its own setter would call the setter again, repeatedly, rather than saving the data.

`raise ValueError(...)` stops the operation and signals that the supplied value violates the rule. Check before changing storage so a rejected assignment preserves the previous valid value. The message explains the problem, although this exercise does not require an exact message.

The initializer's `self.level = level` also goes through the setter. This lets construction and later updates share the same rule. The getter reads backing storage, while the setter validates and writes it.

The workshop starter supplies the initializer and getter for `loan_days`. Add the matching setter below them. Inputs will be integers; accept values greater than zero and reject zero or negative values. You do not need separate type checking. The supplied probe catches the expected error, then reads the period again so you can confirm an invalid assignment did not overwrite the last accepted value.

## Your Tasks

1. Add the `Tool.loan_days` setter: accept and store positive integer inputs in `_loan_days`, but raise `ValueError` for zero or negative inputs before changing stored state. The supplied initializer must use the same rule.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe keeps `14` after rejecting zero.
