---
title: The property decorator
slug: property-decorator
order: 7
language: python
lesson_type: coding
summary: Decorate the supplied `Member.display_name` getter with `@property` so attribute access returns the current full
  name without parentheses.
seo_title: The property decorator | Python OOP practice
seo_description: Decorate the supplied `Member.display_name` getter with `@property` so attribute access returns the current
  full name without parentheses.
seo_keywords:
- Python OOP
- the property decorator
- coding practice
---

# The property decorator

You have connected a getter using `label = property(get_label)`. Python also offers a decorator form that keeps the public attribute name beside the getter's implementation. You will use it to expose a member's display name.

## Same property, different spelling

A decorator applies to the function defined immediately below it. With `@property`, the function name becomes the public property name:

```python
class Package:
    def __init__(self, grams):
        self.grams = grams

    @property
    def kilograms(self):
        return self.grams / 1000
```

The decorator line is inside the class, at the same indentation as `def`. This is equivalent to defining the method and then writing `kilograms = property(kilograms)` in the class body. The result stored under `kilograms` is a property rather than an ordinary method.

The getter still needs `self` because it reads a particular package's data. The caller writes `package.kilograms`, without parentheses. Python runs the getter automatically for that attribute read. Adding `@property` changes the access interface, not the arithmetic in the body.

Keep the getter short and predictable. An attribute-looking read should not unexpectedly perform a slow operation or alter unrelated state. Computing text from two stored names is a good fit; sending an email would be better expressed as an explicit method call.

The editor already has a working `display_name` method for a `Member`. Your change is to decorate it so callers read `member.display_name` as text. Do not call the method in the initializer and store its result; that would become stale when a member's name changes.

Notice the difference from `@classmethod` and `@staticmethod`: those alter which automatic argument a method call receives. `@property` gives callers attribute-style access to a getter. All three use the same decorator syntax, but their effects differ. The probe reads before and after changing the surname so you can confirm the getter still runs on each read.

## Your Tasks

1. Decorate the supplied `Member.display_name` getter with `@property` so attribute access returns the current full name without parentheses.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints strings, not bound-method representations.
