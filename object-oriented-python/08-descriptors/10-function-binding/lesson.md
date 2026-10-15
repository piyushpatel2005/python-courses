---
title: Connect function binding to descriptors
slug: function-binding
order: 10
language: python
lesson_type: coding
summary: A player welcome function stored on a class becomes a bound method when read through a player instance. Use the function's descriptor hook explicitly to see which object supplies `self`.
seo_title: Connect function binding to descriptors | Object-oriented Python
seo_description: A player welcome function stored on a class becomes a bound method when read through a player instance. Use the function's descriptor hook explicitly to see which object supplies `self`.
seo_keywords:
  - Python
  - function binding
  - object-oriented programming
hints:
  - Call function.__get__ with the receiver and its class; return the result without calling it.
---

A player welcome function stored on a class becomes a bound method when read through a player instance. Use the function's descriptor hook explicitly to see which object supplies `self`.

Ordinary Python functions implement `__get__`, so they are non-data descriptors when stored on a class. Reading a function through an instance creates a bound method: calling it automatically supplies that instance as the first argument. Reading the function through the class leaves it unbound in normal class access.

For a function object `fn`, `fn.__get__(instance, type(instance))` creates a method bound to that instance. The returned method exposes `__self__`, the receiver, and `__func__`, the original function. These attributes help you inspect binding; most application code simply writes `object.method(...)` and lets Python do this work.

The example deliberately defines a function outside a class. Calling its descriptor hook can still bind it to an object with the data it needs. The function reads the receiver at call time, so changing an attribute before a later call affects the result. Binding does not copy the object's state.

Because functions are non-data descriptors, a same-named instance attribute can shadow a method found on the class. That is the same priority rule used for the overridable greeting in the previous lessons. A property behaves differently because it is a data descriptor.

Your helper should return the bound method, not call it immediately. The caller supplies the remaining arguments later. A lambda wrapper could imitate some outputs but would not be the actual bound method this exercise asks you to inspect.

## A small example

```python
def caption(self, suffix):
    return self.title + suffix

class Quest:
    title = "Lantern"

quest = Quest()
method = caption.__get__(quest, Quest)
print(method(" quest"))
print(method.__self__ is quest)
```

## Your Tasks

1. Implement `bind_to(function, instance)` by returning the actual bound method created with the function's `__get__` hook and the instance's type.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
