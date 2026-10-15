---
title: "Support reflected multiplication"
slug: "reflected-multiplication"
order: 6
language: "python"
lesson_type: "coding"
summary: "Delegate __rmul__ to an existing multiplication policy."
seo_title: "Support reflected multiplication | Object-oriented Python"
seo_description: "Delegate __rmul__ to an existing multiplication policy."
seo_keywords: ["python", "reflected multiplication", "object oriented programming"]
hints: ["Call the existing multiplication method on self and return what it returns."]
---

# Support reflected multiplication

The score code should accept both `delta * 3` and `3 * delta`. The previous lesson added the first form. This starter supplies that multiplication policy; make the reversed spelling reuse it.

When an integer cannot multiply a custom object, Python can ask the custom object's `__rmul__` method to handle the operation. The letter r means reflected. The object is still `self`; the other operand arrives as the method's argument. Reflected dispatch is how a class cooperates with types it does not control. You do not need to edit Python's integer class.

Our `ScoreDelta.__mul__` already creates a new delta and accepts exact integers only. Reusing that method from `__rmul__` avoids maintaining a second copy of the type check and calculation. Delegation means asking an existing operation to do the work, then returning its result. It also carries the existing `NotImplemented` behavior into the reflected path.

Do not implement the reflected method by writing the same reversed expression again. An expression such as `factor * self` inside `__rmul__` requests the operation that led into the method and can recurse repeatedly. Call the existing method directly instead. Recursion means a function calls itself, directly or indirectly; an endless chain eventually raises an error rather than producing a delta.

The example uses a named convenience method to delegate a measurement calculation. Its second method does not duplicate the arithmetic. Apply that relationship to the two multiplication hooks in the starter.

After editing, compare the point totals from both operand orders and check that the source points stay unchanged. The tests also use zero and a negative factor, because delegating correctly should preserve the whole contract rather than only the visible sample.

## A small example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

    def square_units(self):
        return self.area()

print(Rectangle(3, 8).square_units())
```

## Picture the behavior

This diagram traces the same dispatch rule with a vector. `NotImplemented` lets Python try another supported route; it is different from raising `NotImplementedError`.

![Integer multiplication declines an unrelated Vector, then Python tries Vector.__rmul__; both declining causes TypeError.](reflected-operator-dispatch.svg)

## Your Tasks

1. Implement `ScoreDelta.__rmul__` by delegating to the supplied `__mul__`, so exact integer factors work on either side and unsupported factors return `NotImplemented`.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
