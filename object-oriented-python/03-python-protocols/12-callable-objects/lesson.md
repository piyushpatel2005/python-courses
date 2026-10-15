---
title: "Make an instance callable"
slug: "callable-objects"
order: 12
language: "python"
lesson_type: "coding"
summary: "Implement __call__ for an object that retains a conversion setting."
seo_title: "Make an instance callable | Object-oriented Python"
seo_description: "Implement __call__ for an object that retains a conversion setting. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "callable objects", "object oriented programming"]
hints: ["Treat __call__ like a regular method that returns a calculation."]
---

# Make an instance callable

A drawing tool repeatedly converts grid units to pixels. Instead of passing the scale into every function call, a `Scaler` object can remember it. Calling that object will apply its stored scale to a new value.

You have already called classes to construct instances. A callable instance is a separate idea: after construction, parentheses on the instance ask its class for `__call__`. A class does not need to be a function to support function-call syntax. The method still receives `self`, followed by the arguments from the call, just like an ordinary bound method.

In this exercise `Scaler(factor)` constructs the object, and a later `scaler(value)` converts a number. Keep those two moments distinct. The initializer stores configuration; `__call__` uses it. You should not overwrite the factor with the latest input or accumulate results, because each conversion is independent.

The small example is a normal function that adds punctuation. It shows the caller's familiar parentheses syntax and a returned result. Your class will keep the same convenience while also carrying per-instance data. Two scalers can coexist with different factors without sharing mutable configuration.

Callable objects are useful when a callback needs settings or state. They are not automatically better than functions: if there is no state to keep, a function may be simpler. Here the stored factor is the reason for the object. The required operation is multiplication, not printing, so the result can feed another calculation.

The probe calls one scaler more than once and also creates a second scaler. Observe that repeated calls do not change either object's factor. Submit varies the values and factors, including zero, so the implementation must calculate from its arguments rather than return a sample result.

## A small example

```python
def add_period(text):
    return text + "."

formatter = add_period
print(formatter("Doors open"))
```

## Your Tasks

1. Implement `Scaler.__call__(value)` to return `value` multiplied by the instance factor, leaving the factor unchanged across repeated calls.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
