---
title: "Recognize the object base"
slug: "the-object-base"
order: 2
language: "python"
lesson_type: "coding"
summary: "Inspect the shared root of ordinary Python class hierarchies."
seo_title: "Recognize the object base | Object-oriented Python"
seo_description: "Inspect the shared root of ordinary Python class hierarchies. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "the object base", "object oriented programming"]
hints: ["Use type(value).__bases__; object itself has no bases."]
---

# Recognize the object base

Even a class written without parentheses participates in inheritance. Python supplies `object` as its base. Explore that common root by writing a small inspection helper rather than adding another specialized subclass.

`object` provides basic behaviors shared by ordinary Python instances, including default representations and identity-oriented equality. That is why a new empty class already works with `repr` and why two fresh instances are normally unequal. You do not need to copy those methods into every class. A plain `class Badge:` has the same immediate base as `class Badge(object):`.

The attribute `SomeClass.__bases__` is a tuple containing that class's direct bases. It is about classes, not instances. For an instance, `type(value)` returns its actual class. Combining these ideas lets you inspect the direct relationship without guessing from a printed class name. A class with one custom parent has that parent in `__bases__`, even though `object` remains farther up the chain.

This distinction matters for the helper you will write. It should report whether the actual class directly lists `object`, not whether the value is an object in the broad sense. `isinstance(value, object)` is true for ordinary values of every class and therefore cannot distinguish a direct base from an ancestor.

The example inspects a class rather than implementing the exercise helper. The trailing comma in `(object,)` means a one-item tuple; parentheses alone would merely group the value. Use class objects themselves in your check, not strings such as `"object"`.

The probe contrasts a plain record with a subclass. Both ultimately inherit from `object`, but only the first has it as its immediate base. Later in this module you will inspect the full method resolution order, which includes the complete chain instead of only direct parents.

## A small example

```python
class Reminder:
    pass

print(Reminder.__bases__ == (object,))
print(isinstance(Reminder(), object))
```

## Your Tasks

1. Implement `direct_object_base(value)` to return whether `object` appears among the direct bases of `type(value)`. It must distinguish a plain class instance from an instance of its subclass.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
