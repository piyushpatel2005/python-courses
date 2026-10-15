---
title: Intercept an attribute read
slug: descriptor-read
order: 1
language: python
lesson_type: coding
summary: A sensor should expose a computed reading through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.
seo_title: Intercept an attribute read | Object-oriented Python
seo_description: A sensor should expose a computed reading through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.
seo_keywords:
  - Python
  - descriptor read
  - object-oriented programming
hints:
  - Use the instance argument for the sensor data, not self.
---

A sensor should expose a computed reading through ordinary attribute syntax. A descriptor lets a reusable helper control what that attribute returns.

A descriptor is an object whose type defines one or more descriptor methods, such as `__get__`. To activate normal descriptor lookup, put the descriptor object on the owner class. Storing it only in an instance dictionary does not make ordinary attribute access invoke the protocol.

For a read, `__get__(self, instance, owner)` receives three pieces of information. `self` is the descriptor object, `instance` is the object being read, and `owner` is the owner class used for the lookup. The descriptor is not the sensor. It is a helper shared through the sensor's class.

In the example, `Gauge.reading` is supplied by one `FixedReading` object. Reading `Gauge().reading` invokes its `__get__` and returns the number. No parentheses follow `reading`, because the caller is requesting an attribute rather than calling an ordinary method.

A descriptor can compute a result from the particular instance. Your exercise reads an already supplied `raw` attribute and scales it. Reading `instance.raw` is safe here because it is a separate ordinary attribute. Reading the managed attribute from inside its own getter would invoke the getter again and could recurse indefinitely.

The starter includes a class-access guard: when `instance` is `None`, it returns the descriptor itself. Keep that branch; the next lesson explains it in detail. Your edit belongs only in the instance-read branch. Both probes use the same descriptor through different sensors.

## A small example

```python
class FixedReading:
    def __get__(self, instance, owner):
        return 21

class Gauge:
    reading = FixedReading()

print(Gauge().reading)
```

## Your Tasks

1. Complete `ScaledReading.__get__` so reading a sensor's `reading` returns its `raw` value multiplied by ten; retain the supplied class-access branch.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
