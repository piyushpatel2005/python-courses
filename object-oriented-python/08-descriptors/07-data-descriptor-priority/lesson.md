---
title: Give a data descriptor priority
slug: data-descriptor-priority
order: 7
language: python
lesson_type: coding
summary: A field that must stay read-only should not be bypassed by an instance attribute with the same public name. Make its descriptor a data descriptor.
seo_title: Give a data descriptor priority | Object-oriented Python
seo_description: A field that must stay read-only should not be bypassed by an instance attribute with the same public name. Make its descriptor a data descriptor.
seo_keywords:
  - Python
  - data descriptor priority
  - object-oriented programming
hints:
  - Define the setter on Serial itself, not on Badge or an individual object.
---

A field that must stay read-only should not be bypassed by an instance attribute with the same public name. Make its descriptor a data descriptor.

A descriptor whose type defines `__set__` or `__delete__` is a data descriptor. For normal instance reads, a data descriptor that defines `__get__` takes priority over a same-named entry in the instance dictionary. A getter-only descriptor has lower priority; the next lesson explores that case.

The setter does not have to accept writes. A read-only descriptor can define `__set__` solely to raise `AttributeError`. It still counts as a data descriptor because classification depends on which methods its type defines, not on whether those methods successfully store anything.

For ordinary attribute lookup using the standard `__getattribute__`, Python first searches the class hierarchy for the attribute. If that yields a data descriptor with a getter, it uses that getter before consulting the instance dictionary. Otherwise an instance entry can win, followed by a non-data descriptor or plain class attribute. A missing lookup may then reach `__getattr__` if the class supplies it.

The example shows the shape of a rejecting setter without reproducing the exercise's getter. Your starter has a getter-only serial field. Add the write hook so a direct public-name dictionary entry can no longer shadow that getter. The checks deliberately inject such an entry to demonstrate lookup priority; ordinary client code should not bypass your object's interface this way.

Return paths are not enough for a rejected assignment. Raising an exception tells the caller the write did not happen and keeps the read-only contract visible.

## A small example

```python
class ReadOnly:
    def __set__(self, instance, value):
        raise AttributeError("This field is read-only")
```

## Your Tasks

1. Add `Serial.__set__` that always raises `AttributeError`, making the supplied getter a read-only data descriptor whose result wins over a same-named instance entry.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
