---
title: Reject duplicate enum values
slug: unique-values
order: 5
language: python
lesson_type: coding
summary: A menu must not accidentally give two choices the same code. Apply a check while building its enum so a duplicate becomes an error rather than a hidden alias.
seo_title: Reject duplicate enum values | Object-oriented Python
seo_description: A menu must not accidentally give two choices the same code. Apply a check while building its enum so a duplicate becomes an error rather than a hidden alias.
seo_keywords:
  - Python
  - unique values
  - object-oriented programming
hints:
  - The decorator belongs immediately above the indented class definition.
---

A menu must not accidentally give two choices the same code. Apply a check while building its enum so a duplicate becomes an error rather than a hidden alias.

A plain enum normally permits two names with equal values. The later name becomes an alias of the first member. Both names work for lookup, but they refer to the same object. This can be intentional for an old spelling; it can also conceal an accidental copy-and-paste error.

Import `unique` from `enum` and write `@unique` immediately above an enum class. A decorator receives the newly created class. This one checks for aliases and raises `ValueError` if it finds them. It does not pick a different number or delete a duplicate for you.

In the example the two values differ, so construction succeeds. If the second value were changed to `"am"`, the decorator would reject the definition. This lesson places the enum inside a factory function so you can try different values without making the entire starter fail when it is imported.

A function can define a local class and return that class. Each call creates a fresh enum from the supplied pair of values. The tests call your factory more than once: a valid pair should return an enum, while an equal pair should raise an error. Do not catch that error inside the factory; callers need to know that their configuration is invalid.

The starter already declares and returns the local class. Your change adds the uniqueness policy at the point where that class is created.

## A small example

```python
from enum import Enum, unique

@unique
class Session(Enum):
    MORNING = "am"
    EVENING = "pm"

print(Session.EVENING.value)
```

## Your Tasks

1. Apply `@unique` to the local `Choice` enum in `make_choices(first, second)` so equal values raise `ValueError` and distinct values remain unchanged.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
