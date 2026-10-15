---
title: "Inspect method resolution order"
slug: "inspect-the-mro"
order: 11
language: "python"
lesson_type: "coding"
summary: "Read __mro__ to explain lookup in a diamond-shaped hierarchy."
seo_title: "Inspect method resolution order | Object-oriented Python"
seo_description: "Read __mro__ to explain lookup in a diamond-shaped hierarchy. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "inspect the mro", "object oriented programming"]
hints: ["Read the existing tuple and extract each class object's __name__."]
---

# Inspect method resolution order

Two formatting capabilities share a common ancestor. A report inherits both, creating a diamond-shaped relationship. Before adding cooperative method calls, inspect the order Python actually searches when resolving methods.

The method resolution order, or MRO, is available as `SomeClass.__mro__`. It is a tuple of class objects beginning with the class itself and ending at `object` for ordinary hierarchies. `__bases__` shows only immediate parents; `__mro__` shows the complete lookup order. Use each class's `__name__` when you want readable names rather than the class objects themselves.

Python computes a consistent order using C3 linearization. For a simple diamond with two siblings, the child appears first, then its left base, then its right base, then their shared ancestor. The common ancestor appears once. This preserves the sibling precedence without searching the shared parent before the other sibling has a chance to contribute. Arbitrary multiple-inheritance graphs are not just a depth-first walk; contradictory ordering requirements can make a class definition fail with `TypeError`.

The example inspects a simple chain with different class names. Your function must also handle the supplied diamond and any ordinary class passed into it. Read the class's computed MRO rather than reconstructing it from the immediate bases or hardcoding familiar names.

An MRO is a search order, not a command to execute every method. An ordinary method call stops at the first matching implementation. Other implementations run only when the chosen method calls onward, typically through `super()`. That difference is the reason to inspect lookup before writing the cooperative chain in the next lesson.

The probe prints both the base tuple and your readable order for the report. Compare the two: the full order includes inherited ancestors that the direct-base tuple does not. Submit adds a separate diamond so the helper must genuinely inspect its argument.

## A small example

```python
class Root:
    pass

class Leaf(Root):
    pass

print([cls.__name__ for cls in Leaf.__mro__])
```

## Your Tasks

1. Implement `mro_names(cls)` to return a list of class names from `cls.__mro__` in exactly the computed order, including the class itself and `object`.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
