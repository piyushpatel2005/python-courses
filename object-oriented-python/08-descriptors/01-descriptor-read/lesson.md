---
title: Intercept an attribute read
slug: descriptor-read
order: 1
language: python
lesson_type: coding
summary: Mosslight Studio wants Lantern Vale character stats to expose computed power through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.
seo_title: Intercept an attribute read | Object-oriented Python
seo_description: Mosslight Studio wants Lantern Vale character stats to expose computed power through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.
seo_keywords:
  - Python
  - descriptor read
  - object-oriented programming
hints:
  - Use the instance argument for the character data, not self.
---

Mosslight Studio wants Lantern Vale character stats to expose computed power through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.

A descriptor is an object whose type defines one or more descriptor methods, such as `__get__`. To activate normal descriptor lookup, put the descriptor object on the owner class. Storing it only in an instance dictionary does not make ordinary attribute access invoke the protocol.

For a read, `__get__(self, instance, owner)` receives three pieces of information. `self` is the descriptor object, `instance` is the object being read, and `owner` is the owner class used for the lookup. The descriptor is not the character. It is a helper shared through the character's class.

In the example, `TrainingDummy.power` is supplied by one `FixedPower` object. Reading `TrainingDummy().power` invokes its `__get__` and returns the number. No parentheses follow `power`, because the caller is requesting an attribute rather than calling an ordinary method.

A descriptor can compute a result from the particular instance. Your exercise reads an already supplied `base_power` attribute and scales it. Reading `instance.base_power` is safe here because it is a separate ordinary attribute. Reading the managed attribute from inside its own getter would invoke the getter again and could recurse indefinitely.

The starter includes a class-access guard: when `instance` is `None`, it returns the descriptor itself. Keep that branch; the next lesson explains it in detail. Your edit belongs only in the instance-read branch. Both probes use the same descriptor through different characters.

## A small example

```python
class FixedPower:
    def __get__(self, instance, owner):
        return 21

class TrainingDummy:
    power = FixedPower()

print(TrainingDummy().power)
```

## Your Tasks

1. Complete `ScaledPower.__get__` so reading a character's `power` returns its `base_power` value multiplied by ten; retain the supplied class-access branch.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
