---
title: Give enum members a method
slug: enum-methods
order: 7
language: python
lesson_type: coding
summary: A shipping tier stores its per-box fee. Put the fee calculation on the member so callers do not maintain a separate table of tier names.
seo_title: Give enum members a method | Object-oriented Python
seo_description: A shipping tier stores its per-box fee. Put the fee calculation on the member so callers do not maintain a separate table of tier names.
seo_keywords:
  - Python
  - enum methods
  - object-oriented programming
hints:
  - Use self.value for the rate and the boxes argument for the quantity.
---

A shipping tier stores its per-box fee. Put the fee calculation on the member so callers do not maintain a separate table of tier names.

Methods in an enum use ordinary method syntax. Define a function in the class body with `self` as its first parameter. Calling `SomeEnum.MEMBER.method(argument)` binds `self` to that member, just as an ordinary instance method binds it to an instance.

The method can read `self.value` to use the value associated with its member. A method definition is behavior, not another enum choice; Python does not add it to the sequence returned by iterating over the enum. Keep the distinction visible by using uppercase names for members and lowercase names for methods.

The example stores a rate in each membership level. Its method calculates with the receiver's own rate, so the same code works for both members. Adding another rate would not require a new branch inside the calculation. This is often simpler than comparing member names repeatedly.

The exercise has the same structural idea but a different calculation: a per-box amount multiplied by a box count. Inputs are non-negative integer counts. You do not need to invent rounding, discounts, or error handling for this task. Returning the amount makes the result usable by other code; the provided probe handles printing it.

Check the zero-count case as you reason through your method. An implementation that returns only a member's stored fee might look right for one box, but it would not use the argument at all.

## A small example

```python
from enum import Enum

class Pass(Enum):
    BASIC = 4
    PREMIUM = 9

    def remaining(self, spent):
        return self.value - spent

print(Pass.PREMIUM.remaining(3))
```

## Your Tasks

1. Implement `Shipping.cost(boxes)` to return that member's per-box value multiplied by `boxes`.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
