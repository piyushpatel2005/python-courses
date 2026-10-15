---
title: Recognize property as a descriptor
slug: property-as-descriptor
order: 9
language: python
lesson_type: coding
summary: A rectangle exposes its area as an attribute. Revisit `property` now that you can explain why reading that attribute runs a getter and why an instance entry cannot replace it.
seo_title: Recognize property as a descriptor | Object-oriented Python
seo_description: A rectangle exposes its area as an attribute. Revisit `property` now that you can explain why reading that attribute runs a getter and why an instance entry cannot replace it.
seo_keywords:
  - Python
  - property as descriptor
  - object-oriented programming
hints:
  - Read both dimensions from self inside the property getter.
---

A rectangle exposes its area as an attribute. Revisit `property` now that you can explain why reading that attribute runs a getter and why an instance entry cannot replace it.

The built-in `property` is a descriptor type. `property(getter)` constructs a descriptor from a function, and assigning it in a class gives the public attribute its behavior. The `@property` decorator is a shorter way to perform that arrangement with the same name.

On instance access, the property calls its getter with the instance. On class access, it returns the property object. Even a property with no setter is a data descriptor: attempts to assign through it raise `AttributeError`, and its getter takes priority over a same-named instance dictionary entry.

The example uses the function form to make the connection explicit. `get_double` is an ordinary function in the class body; `double` is the property object created from it. The exercise uses the decorator form, which places the getter function immediately below `@property`. Both forms build a managed attribute rather than storing a one-time calculation.

A computed property should read the current underlying data on each access. If a dimension changes, a later area read should reflect it. Saving one area during initialization would require keeping that saved value synchronized, which is unnecessary for this small calculation.

The starter already contains the decorator and constructor. You only change the getter's return expression. Do not add a setter: the dimensions are writable, but the area is derived from them. The probe changes a dimension between reads so a stale calculation is visible.

## A small example

```python
class Number:
    def __init__(self, value):
        self.value = value

    def get_double(self):
        return self.value * 2

    double = property(get_double)

print(Number(6).double)
```

## Your Tasks

1. Complete `Rectangle.area` so the supplied read-only property returns the current width multiplied by the current height.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
