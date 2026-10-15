---
title: "Multiply a value by a scalar"
slug: "multiply-by-a-scalar"
order: 5
language: "python"
lesson_type: "coding"
summary: "Support integer scaling without mutating the original object."
seo_title: "Multiply a value by a scalar | Object-oriented Python"
seo_description: "Support integer scaling without mutating the original object."
seo_keywords: ["python", "multiply by a scalar", "object oriented programming"]
hints: ["An exact type check distinguishes int from bool for this contract."]
---

# Multiply a value by a scalar

A challenge can repeat the same score adjustment several times. `ScoreDelta` stores a signed number of points; multiplying it by an integer should create a new adjustment. The factor is a plain number, not another score object.

`delta * factor` asks `__mul__(self, factor)` to define this operation. Unlike addition between matching value objects, the two operands have different roles here. Read the count from `self`, use the integer directly, and return a new `ScoreDelta`. The original adjustment remains available for another calculation.

For this exercise the supported scalars are exact integers, including zero and negative integers. That signed model keeps the arithmetic rule visible; a game might impose different score limits. Python's `bool` is a subtype of `int`, so `isinstance(True, int)` is true. We deliberately reject booleans here: `type(factor) is int` expresses the narrower contract. This is a chosen interface, not a universal rule for every numeric class.

Return `NotImplemented` for floats, strings, booleans, and other unsupported inputs. Python can then follow its operator protocol and eventually raise `TypeError` when neither operand handles the pair. A float that happens to hold a whole number is still outside this lesson's exact-integer contract.

The example scales a recipe using a regular function. Its calculation is simple; the exercise adds the object boundary and return-type discipline. Check a factor of zero as well as a positive factor. Zero should create a valid result object, not return `None` or skip the operation.

Only the object-on-the-left spelling is required here. `3 * delta` is a separate dispatch case, which the next lesson adds without changing this method's meaning.

## A small example

```python
def portions(grams_per_serving, people):
    return grams_per_serving * people

print(portions(80, 5))
```

## Your Tasks

1. Implement `ScoreDelta.__mul__` for exact integer factors (not booleans), returning a fresh score adjustment with the multiplied `points`. Do not mutate the original; return `NotImplemented` for unsupported factors.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
