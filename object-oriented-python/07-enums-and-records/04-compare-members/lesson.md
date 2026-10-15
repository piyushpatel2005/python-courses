---
title: Compare members, not raw codes
slug: compare-members
order: 4
language: python
lesson_type: coding
summary: A task can be archived only when its state is the supplied enum's completed member. A matching string from elsewhere should not count as that member.
seo_title: Compare members, not raw codes | Object-oriented Python
seo_description: A task can be archived only when its state is the supplied enum's completed member. A matching string from elsewhere should not count as that member.
seo_keywords:
  - Python
  - compare members
  - object-oriented programming
hints:
  - Compare the input with the specific member object rather than its value.
---

A task can be archived only when its state is the supplied enum's completed member. A matching string from elsewhere should not count as that member.

Enum members support equality comparisons. Repeated access to the same member returns the same object, so an identity comparison with `is` is also appropriate when checking one specific member. Plain `Enum` members are not equal to their raw values. Members of unrelated plain enums are distinct even when their values match.

The example distinguishes a `Traffic` member from the string it contains. This protects the boundary between an internal choice and unvalidated external text. If you deliberately want to convert a raw value, call the enum first, as in the preceding lesson. Do not make every comparison silently perform that conversion.

Plain enum members do not gain numeric ordering merely because their values are numbers. Expressions such as `first < second` raise `TypeError` unless you define suitable behavior. If an application really needs order, decide what ordering means instead of assuming that the declaration provides it.

Membership has another meaning: asking whether an object belongs to an enum. A known member can be checked with `member in State`. Raw-value containment changed in Python 3.12, so this course does not use `raw_value in State` as a portable validation rule. A later lesson uses `isinstance` when a function needs any member of one enum.

Here you only need to recognize one member. The supplied enum is complete; change the helper's return expression and leave the definition alone.

## A small example

```python
from enum import Enum

class Traffic(Enum):
    STOP = "stop"
    GO = "go"

print(Traffic.GO == Traffic.GO)
print(Traffic.GO == "go")
```

## Your Tasks

1. Implement `can_archive(state)` to return `True` only for `WorkState.COMPLETE`, and `False` for every other input.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
