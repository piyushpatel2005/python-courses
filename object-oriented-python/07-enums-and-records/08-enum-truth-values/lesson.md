---
title: Choose an enum truth rule
slug: enum-truth-values
order: 8
language: python
lesson_type: coding
summary: A signal enum includes a zero-valued inactive state. Decide explicitly whether that state should behave as false in a condition.
seo_title: Choose an enum truth rule | Object-oriented Python
seo_description: A signal enum includes a zero-valued inactive state. Decide explicitly whether that state should behave as false in a condition.
seo_keywords:
  - Python
  - enum truth values
  - object-oriented programming
hints:
  - Call bool on self.value so the method returns a real Boolean.
---

A signal enum includes a zero-valued inactive state. Decide explicitly whether that state should behave as false in a condition.

A plain `Enum` member is truthy by default, even if its `.value` is zero, an empty string, or another false value. The member is a distinct object; Python does not automatically delegate its truth test to the stored value. Do not assume that numeric-looking member values behave like integers.

You can define `__bool__(self)` in the enum when the domain has a useful truth rule. As with other classes, this special method must return an actual `bool`. Returning zero or one directly is not enough: Python requires `False` or `True`, rather than an integer that merely behaves similarly in many comparisons.

The example makes one specific state false. It does not change equality or turn the member into its raw string. A truth rule is a separate decision about how an object behaves in `if`, `while`, and `bool(...)`.

In the exercise the values intentionally encode inactivity as zero and activity as a nonzero number. Delegating to `bool` of the stored value expresses that policy without naming a particular active member. The enum and the probe are supplied, so your only edit is the special method's body.

This lesson uses plain `Enum`, not `IntEnum` or flags, whose numeric behavior introduces additional rules. Be clear about which base class you are reading before predicting a member's truth value.

## A small example

```python
from enum import Enum

class Access(Enum):
    BLOCKED = "blocked"
    OPEN = "open"

    def __bool__(self):
        return self is not Access.BLOCKED

print(bool(Access.BLOCKED), bool(Access.OPEN))
```

## Your Tasks

1. Implement `Signal.__bool__` so each member has the truth value of its stored numeric value: zero is false and nonzero is true.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
