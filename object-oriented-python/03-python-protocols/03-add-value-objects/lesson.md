---
title: "Add two value objects"
slug: "add-value-objects"
order: 3
language: "python"
lesson_type: "coding"
summary: "Implement nonmutating addition and decline unsupported operands."
seo_title: "Add two value objects | Object-oriented Python"
seo_description: "Implement nonmutating addition and decline unsupported operands."
seo_keywords: ["python", "add value objects", "object oriented programming"]
hints: ["Check the operand type before reading its offset."]
---

# Add two value objects

Two movement offsets along one axis can combine into a new offset. Keep the originals unchanged so the game can reuse them when planning another move. Your `MovementOffset` will support `+` with that meaning.

For ordinary same-type operands, `left + right` asks the left operand's class for `__add__(self, other)`. The method receives two objects, not two bare numbers. Read the offset from each, calculate the combined offset, and construct a fresh result. Returning a bare number loses the type's meaning; returning and changing `self` unexpectedly changes a value the caller may still need.

An operator also needs a policy for unfamiliar operands. `NotImplemented` is a special return value meaning this method does not support that operand combination. It is not the exception `NotImplementedError`, and you do not raise it. Python may then try the other operand's reflected operation. If neither side supports addition, Python raises `TypeError`, an exception reporting an unsuitable operation or type. The later errors module develops exceptions more fully; here the useful rule is to decline unsupported combinations without pretending they are valid.

Use `isinstance(other, MovementOffset)` to check whether the second object belongs to the supported class before reading `other.steps`. This avoids an accidental attribute error when a number or string reaches the operator. Subclasses will be introduced in the next module; for now this check accepts another movement offset.

The tiny example combines experience rewards with an ordinary method. It illustrates returning a new object without changing either input, but leaves the operator protocol for you to implement. The Run probe shows the resulting offset, while Submit also checks fresh-object behavior and unsupported inputs.

## A small example

```python
from __future__ import annotations

class ExperienceReward:
    def __init__(self, points: int) -> None:
        self.points: int = points

    def combined_with(self, other: ExperienceReward) -> ExperienceReward:
        return ExperienceReward(self.points + other.points)

print(ExperienceReward(12).combined_with(ExperienceReward(8)).points)
```

## Your Tasks

1. Implement `MovementOffset.__add__` so two movement offsets produce a new `MovementOffset` whose `steps` is their sum, without changing either input. Return `NotImplemented` for a non-`MovementOffset` operand.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
