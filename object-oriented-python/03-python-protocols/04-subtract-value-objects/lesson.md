---
title: "Subtract value objects"
slug: "subtract-value-objects"
order: 4
language: "python"
lesson_type: "coding"
summary: "Return a new signed displacement from __sub__."
seo_title: "Subtract value objects | Object-oriented Python"
seo_description: "Return a new signed displacement from __sub__."
seo_keywords: ["python", "subtract value objects", "object oriented programming"]
hints: ["The result can be negative; do not use abs or clamp it."]
---

# Subtract value objects

Lantern Vale also needs the difference between two movement offsets. Moving backward must remain negative rather than being clamped to zero. Add subtraction to `MovementOffset` while keeping both inputs intact.

The operator `left - right` uses `__sub__(self, other)` for supported same-type values. The order matters. Addition sometimes hides a swapped operand because the result happens to match, but subtraction does not. Treat `self` as the left-hand offset and `other` as the right-hand offset throughout the calculation.

This lesson continues the value-object convention from addition. Return a new `MovementOffset`, even if its displacement is zero, rather than a number or a modified operand. A caller can then use the result wherever another offset is expected. You are defining the meaning of an operation for your class; Python does not infer that meaning from an attribute named `steps`.

The example uses temperature readings and an ordinary helper. Its output is signed because argument order is part of the contract. Your class method will apply that idea to objects and make it available through the subtraction symbol.

Keep the unsupported-operand path explicit. Returning `NotImplemented` tells Python to continue its operator dispatch instead of making up a result. If no implementation supports the pair, the expression raises `TypeError`. That exception is an ordinary report of an invalid operation; the guarded Run probe catches it so unfinished code remains runnable. Submit calls your method with both valid and invalid inputs.

Try two unequal offsets in both orders after your first successful Run. Then subtract an offset from itself. Those cases expose sign mistakes and unwanted reuse of the original object more clearly than one positive example.

## A small example

```python
def temperature_change(current, previous):
    return current - previous

print(temperature_change(8, 11))
```

## Your Tasks

1. Implement `MovementOffset.__sub__` to return a fresh `MovementOffset` with `steps` equal to the left value minus the right value. Leave the inputs unchanged and return `NotImplemented` for other operand types.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
