---
title: "Compare objects by value"
slug: "value-equality"
order: 7
language: "python"
lesson_type: "coding"
summary: "Define equality from fields while cooperating with unfamiliar types."
seo_title: "Compare objects by value | Object-oriented Python"
seo_description: "Define equality from fields while cooperating with unfamiliar types."
seo_keywords: ["python", "value equality", "object oriented programming"]
hints: ["A tuple comparison can express equality of both fields together."]
---

# Compare objects by value

Two independently created save-slot descriptions can refer to the same place in Lantern Vale. Compare `SaveSlot` objects by their profile and slot number, even when they are different instances. This is metadata in memory, not a file-writing exercise.

Identity, tested with `is`, asks whether two references point to the very same object. Equality, tested with `==`, asks the objects' comparison protocol. A class can define `__eq__(self, other)` to choose what equal means. For a save slot, both fields matter: profile A slot 4 and profile B slot 4 are not interchangeable.

First decide whether the operand is supported. This lesson compares `SaveSlot` instances, so use an instance check before reading the other's fields. Return `NotImplemented` for an unrelated object. Returning `False` immediately would claim to know that the pair is unequal and can prevent the other object's comparison from participating. `NotImplemented` is a dispatch signal, not an exception and not a truth value to test.

When neither side supports equality, Python falls back to identity. Therefore comparing a save slot with an unrelated string normally gives `False` rather than raising `TypeError`. That differs from unsupported ordering, which the next lesson explores. You can call `__eq__` directly in a diagnostic to inspect the dispatch signal, but application code should normally use `==`.

The example shows value and identity on built-in lists. Their equality already compares contents; your class needs its own rule. Return the result of comparing relevant data rather than comparing string representations, which are designed for display and may change.

Defining value equality also affects hashing. Python normally makes a class with a new `__eq__` unhashable unless hashing is deliberately provided. That is a useful safety default for mutable objects. Keep this save slot mutable and unhashable; a later lesson uses a separate immutable key.

## A small example

```python
left = ["north", 2]
right = ["north", 2]
print(left == right)
print(left is right)
```

## Your Tasks

1. Implement `SaveSlot.__eq__` so save slots compare equal exactly when both `profile` and `number` match. Return `NotImplemented` for unrelated objects; do not add hashing to this mutable class.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
