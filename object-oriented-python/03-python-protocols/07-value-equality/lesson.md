---
title: "Compare objects by value"
slug: "value-equality"
order: 7
language: "python"
lesson_type: "coding"
summary: "Define equality from fields while cooperating with unfamiliar types."
seo_title: "Compare objects by value | Object-oriented Python"
seo_description: "Define equality from fields while cooperating with unfamiliar types. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "value equality", "object oriented programming"]
hints: ["A tuple comparison can express equality of both fields together."]
---

# Compare objects by value

Two independently created seat labels can name the same place. They are different objects, but your application should consider them equal when their row and number match. Implement that distinction for `Seat`.

Identity, tested with `is`, asks whether two references point to the very same object. Equality, tested with `==`, asks the objects' comparison protocol. A class can define `__eq__(self, other)` to choose what equal means. For a seat, both fields matter: row A seat 4 and row B seat 4 are not interchangeable.

First decide whether the operand is supported. This lesson compares `Seat` instances, so use an instance check before reading the other's fields. Return `NotImplemented` for an unrelated object. Returning `False` immediately would claim to know that the pair is unequal and can prevent the other object's comparison from participating. `NotImplemented` is a dispatch signal, not an exception and not a truth value to test.

When neither side supports equality, Python falls back to identity. Therefore comparing a seat with an unrelated string normally gives `False` rather than raising `TypeError`. That differs from unsupported ordering, which the next lesson explores. You can call `__eq__` directly in a diagnostic to inspect the dispatch signal, but application code should normally use `==`.

The example shows value and identity on built-in lists. Their equality already compares contents; your class needs its own rule. Return the result of comparing relevant data rather than comparing string representations, which are designed for display and may change.

Defining value equality also affects hashing. Python normally makes a class with a new `__eq__` unhashable unless hashing is deliberately provided. That is a useful safety default for mutable objects. Keep this seat mutable and unhashable; a later lesson uses a separate immutable key.

## A small example

```python
left = ["north", 2]
right = ["north", 2]
print(left == right)
print(left is right)
```

## Your Tasks

1. Implement `Seat.__eq__` so seats compare equal exactly when both `row` and `number` match. Return `NotImplemented` for unrelated objects; do not add hashing to this mutable class.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
