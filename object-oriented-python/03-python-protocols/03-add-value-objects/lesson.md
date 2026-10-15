---
title: "Add two value objects"
slug: "add-value-objects"
order: 3
language: "python"
lesson_type: "coding"
summary: "Implement nonmutating addition and decline unsupported operands."
seo_title: "Add two value objects | Object-oriented Python"
seo_description: "Implement nonmutating addition and decline unsupported operands. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "add value objects", "object oriented programming"]
hints: ["Check the operand type before reading its measurement."]
---

# Add two value objects

Two lengths of cable can be combined into a new length. The originals still describe the pieces you started with. Your `Cable` objects will support `+` with that value-oriented meaning.

For ordinary same-type operands, `left + right` asks the left operand's class for `__add__(self, other)`. The method receives two objects, not two bare numbers. Read the measurement from each, calculate the combined measurement, and construct a fresh result. Returning a bare number loses the type's meaning; returning and changing `self` unexpectedly changes a value the caller may still need.

An operator also needs a policy for unfamiliar operands. `NotImplemented` is a special return value meaning this method does not support that operand combination. It is not the exception `NotImplementedError`, and you do not raise it. Python may then try the other operand's reflected operation. If neither side supports addition, Python raises `TypeError`, an exception reporting an unsuitable operation or type. The later errors module develops exceptions more fully; here the useful rule is to decline unsupported combinations without pretending they are valid.

Use `isinstance(other, Cable)` to check whether the second object belongs to the supported class before reading `other.metres`. This avoids an accidental attribute error when a number or string reaches the operator. Subclasses will be introduced in the next module; for now this check accepts another cable.

The tiny example combines notebook page counts with an ordinary method. It illustrates returning a new object without changing either input, but leaves the operator protocol for you to implement. The Run probe shows the resulting measurement, while Submit also checks fresh-object behavior and unsupported inputs.

## A small example

```python
class Notebook:
    def __init__(self, pages):
        self.pages = pages

    def joined(self, other):
        return Notebook(self.pages + other.pages)

print(Notebook(12).joined(Notebook(8)).pages)
```

## Your Tasks

1. Implement `Cable.__add__` so two cables produce a new `Cable` whose `metres` is their sum, without changing either input. Return `NotImplemented` for a non-`Cable` operand.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
