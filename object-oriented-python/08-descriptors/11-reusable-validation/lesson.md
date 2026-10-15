---
title: Reuse one validation rule across fields
slug: reusable-validation
order: 11
language: python
lesson_type: coding
summary: A hitbox has a width and a height, and both must stay positive. Reuse a descriptor class while giving each field its own descriptor object and storage key.
seo_title: Reuse one validation rule across fields | Object-oriented Python
seo_description: A hitbox has a width and a height, and both must stay positive. Reuse a descriptor class while giving each field its own descriptor object and storage key.
seo_keywords:
  - Python
  - reusable validation
  - object-oriented programming
hints:
  - Perform the type check, then the range check, then the write.
---

A hitbox has a width and a height, and both must stay positive. Reuse a descriptor class while giving each field its own descriptor object and storage key.

A descriptor can hold field configuration while each owner instance holds its own values. `__set_name__` supplies a distinct backing key for each descriptor object. `__set__` applies the common validation rule and saves accepted data in the selected owner's dictionary.

The example's two descriptor instances show the reuse pattern. They come from the same class, but they are not the same object. This matters because each object remembers one attribute name. Assigning one shared descriptor object under both names would overwrite that single-name configuration during class creation.

Validation should happen before storage so a rejected update leaves the old value intact. This exercise has an explicit type policy: accept built-in `int` and `float`, reject booleans and all other types with `TypeError`, then reject numeric values less than or equal to zero with `ValueError`. A Boolean is a subclass of `int`, so a broad `isinstance(value, int)` check alone would accidentally accept `True`.

Using `type(value) in (int, float)` expresses this particular built-in-only policy. Other applications may reasonably accept numeric subclasses; the point is to state the contract rather than let it happen by accident. Inputs here are finite numbers, so you do not need an additional infinity or NaN policy.

The starter provides naming and reads. Complete only the setter, then observe the two fields and two records independently. The check includes valid updates after a rejected attempt so the descriptor remains usable.

## A small example

```python
class NamedStorage:
    def __set_name__(self, owner, name):
        self.key = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

class SpriteMetrics:
    scale = NamedStorage()
    width = NamedStorage()

print(SpriteMetrics.scale is SpriteMetrics.width)
```

## Your Tasks

1. Implement `Positive.__set__`: accept only built-in integers/floats greater than zero, raise `TypeError` for other types (including bool), raise `ValueError` for nonpositive numbers, and store accepted values at `instance.__dict__[self.key]` without changing old data on rejection.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
