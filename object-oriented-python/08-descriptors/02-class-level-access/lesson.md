---
title: Handle class-level descriptor access
slug: class-level-access
order: 2
language: python
lesson_type: coding
summary: Tools often inspect a field through its class rather than through a record. Give your descriptor a useful response when there is no individual record to read.
seo_title: Handle class-level descriptor access | Object-oriented Python
seo_description: Tools often inspect a field through its class rather than through a record. Give your descriptor a useful response when there is no individual record to read.
seo_keywords:
  - Python
  - class level access
  - object-oriented programming
hints:
  - Return self from the class-access branch.
---

Tools often inspect a field through its class rather than through a record. Give your descriptor a useful response when there is no individual record to read.

Reading `record.field` normally calls the descriptor with the record as `instance`. Reading `Record.field` calls it with `instance=None`. The `owner` argument still identifies the owner class. A getter that blindly reads `instance.some_attribute` will therefore fail on class access.

A common convention is to return `self` when `instance is None`. That exposes the descriptor object so callers can inspect its configuration, such as a label or a default. This is a convention you choose in `__get__`, not a result automatically guaranteed for every descriptor.

In the example, the class-level read returns the `Unit` helper, while an instance-level read returns its unit string. `Box.unit is Box.__dict__["unit"]` is true because the explicit dictionary access retrieves the stored helper without invoking its getter. This direct access is useful while learning the protocol.

Descriptors can be inherited. Access through a subclass still finds the same helper if the subclass has not replaced it. The `owner` argument reflects the accessing class; the descriptor does not need to be recreated for each subclass.

The exercise's instance branch already returns a field label. Only the class-access branch is unfinished. Return the existing helper rather than constructing another one, returning its label, or returning the class. That preserves its identity and lets the supplied probe inspect the same configuration object.

## A small example

```python
class Unit:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "cm"

class Box:
    unit = Unit()

print(Box().unit)
print(Box.unit is Box.__dict__["unit"])
```

## Your Tasks

1. Complete the `instance is None` branch of `FieldLabel.__get__` so class access returns the descriptor itself, while instance access still returns its label.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
