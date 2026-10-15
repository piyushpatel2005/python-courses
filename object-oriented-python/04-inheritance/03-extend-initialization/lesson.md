---
title: "Extend initialization with super"
slug: "extend-initialization"
order: 3
language: "python"
lesson_type: "coding"
summary: "Initialize base state before storing a subclass-specific field."
seo_title: "Extend initialization with super | Object-oriented Python"
seo_description: "Initialize base state before storing a subclass-specific field."
seo_keywords: ["python", "extend initialization", "object oriented programming"]
hints: ["The base receives only its own argument; the subclass stores its extra field afterward."]
---

# Extend initialization with super

An ability with a cooldown needs its usual title plus a delay before reuse. The starter supplies `Ability` and `CooldownAbility`; finish only the subclass initializer so each class stores the data it owns.

Defining `__init__` in a subclass replaces the inherited initializer for construction. Python does not automatically run both bodies. If the base initializer establishes fields that its methods need, the subclass must arrange that work. Otherwise a seemingly successful construction can fail later when an inherited method reads missing state.

Inside an instance method, `super()` provides access to the next implementation in the instance's method resolution order. With this simple single-inheritance chain, that next initializer is the base class's initializer. Calling `super().__init__(argument)` passes the instance automatically; do not supply `self` again. After the base setup, assign the subclass's additional field.

The example adds a color to a geometric point. Its base owns a coordinate, so the specialized initializer forwards that argument rather than reimplementing the coordinate assignment. Your ability classes have different fields, but the ownership boundary is the same. If the base later validates or normalizes its input, a delegating subclass will still use that behavior.

Keep method signatures in view. A signature is the list of parameters a callable accepts. The ability base accepts one title argument; the cooldown ability accepts a title and cooldown. Only the title belongs in the call to the base initializer. Forwarding both would raise `TypeError` because that initializer has no cooldown parameter.

The tests temporarily observe the base initializer to verify delegation, not just the final attributes. That protects the learning goal: copying the base assignment may produce the same sample label but bypass the shared initialization policy.

## A small example

```python
class Point:
    def __init__(self, x):
        self.x = x

class ColoredPoint(Point):
    def __init__(self, x, color):
        super().__init__(x)
        self.color = color

print(ColoredPoint(5, "blue").x)
```

## Your Tasks

1. Complete `CooldownAbility.__init__(title, cooldown)` by calling the base initializer through `super()` with `title`, then storing `cooldown` on this instance.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
