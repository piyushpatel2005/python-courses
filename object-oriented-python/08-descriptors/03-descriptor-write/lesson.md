---
title: Intercept an attribute assignment
slug: descriptor-write
order: 3
language: python
lesson_type: coding
summary: A mana pool must reject negative amounts. A descriptor setter can enforce that rule whenever code assigns to the public field.
seo_title: Intercept an attribute assignment | Object-oriented Python
seo_description: A mana pool must reject negative amounts. A descriptor setter can enforce that rule whenever code assigns to the public field.
seo_keywords:
  - Python
  - descriptor write
  - object-oriented programming
hints:
  - Check value before assigning the backing attribute used by the getter.
---

A mana pool must reject negative amounts. A descriptor setter can enforce that rule whenever code assigns to the public field.

Define `__set__(self, instance, value)` on the descriptor type to intercept `instance.field = value`. Here `self` is still the shared helper, `instance` is the record being changed, and `value` is the proposed new value. The setter normally stores data and returns nothing useful to the assignment statement.

Validate before writing. `raise ValueError("message")` stops the assignment and tells the caller that the proposed value is unacceptable. If the old value must survive a rejected update, perform the check before changing storage. The later errors module studies exception design in more detail; this task needs only that simple rejection rule.

The example strips surrounding spaces from a text label and stores it under a different attribute name. The `strip()` string method returns a cleaned string without changing the original. Writing `instance.label = value` from the setter for `label` would call the same setter again. A separate backing attribute avoids that recursion. The exercise supplies a getter that reads its backing attribute, so the read/write pair must agree about storage.

This class uses ordinary instance dictionaries, not `__slots__`. The backing attribute belongs to each record. The descriptor itself should hold the rule, not a single mana amount shared by all records. The next lesson examines that distinction more closely.

You only need to handle numeric mana amounts in this exercise; fractional amounts are allowed. Do not add unrelated string conversion or type policies. The visible probe tries a successful update and then a negative one, making the preservation of the last accepted value observable.

## A small example

```python
class TrimmedPlayerName:
    def __set__(self, instance, value):
        instance._saved = value.strip()

class PlayerProfile:
    label = TrimmedPlayerName()

profile = PlayerProfile()
profile.label = "  Mira  "
print(profile._saved)
```

## Your Tasks

1. Implement `ManaAmount.__set__` to reject negative numbers with `ValueError` and otherwise store the value in `instance._mana`, leaving the previous value unchanged after rejection.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
