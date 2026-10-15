---
title: Give enum members a method
slug: enum-methods
order: 7
language: python
lesson_type: coding
summary: Each Lantern Vale ability stores its mana cost per cast. Put the total-cost calculation on the member so callers do not maintain a separate table of ability names.
seo_title: Give enum members a method | Object-oriented Python
seo_description: Each Lantern Vale ability stores its mana cost per cast. Put the total-cost calculation on the member so callers do not maintain a separate table of ability names.
seo_keywords:
  - Python
  - enum methods
  - object-oriented programming
hints:
  - Use self.value for the rate and the casts argument for the quantity.
---

Each Lantern Vale ability stores its mana cost per cast. Put the total-cost calculation on the member so callers do not maintain a separate table of ability names.

Methods in an enum use ordinary method syntax. Define a function in the class body with `self` as its first parameter. Calling `SomeEnum.MEMBER.method(argument)` binds `self` to that member, just as an ordinary instance method binds it to an instance.

The method can read `self.value` to use the value associated with its member. A method definition is behavior, not another enum choice; Python does not add it to the sequence returned by iterating over the enum. Keep the distinction visible by using uppercase names for members and lowercase names for methods.

The example stores an energy allowance in each stance. Its method calculates with the receiver's own allowance, so the same code works for both members. Adding another stance would not require a new branch inside the calculation. This is often simpler than comparing member names repeatedly.

The exercise has the same structural idea but a different calculation: a per-cast amount multiplied by a cast count. Inputs are non-negative integer counts. You do not need to invent cooldowns, damage bonuses, or error handling for this task. Returning the amount makes the result usable by other code; the provided probe handles printing it.

Check the zero-count case as you reason through your method. An implementation that returns only a member's stored mana cost might look right for one cast, but it would not use the argument at all.

## A small example

```python
from enum import Enum

class Stance(Enum):
    SCOUT = 4
    GUARD = 9

    def remaining(self, spent):
        return self.value - spent

print(Stance.GUARD.remaining(3))
```

## Your Tasks

1. Implement `Ability.cost(casts)` to return that member's per-cast value multiplied by `casts`.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
