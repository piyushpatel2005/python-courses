---
title: A class method factory
slug: class-method-factory
order: 4
language: python
lesson_type: coding
summary: Add `GameItem.from_text(cls, text)` decorated with `@classmethod`; parse valid `"name:uses"` text, convert `uses` to
  an integer, and return a new instance by calling `cls(name, uses)`.
seo_title: A class method factory | Python OOP practice
seo_description: Add `GameItem.from_text(cls, text)` decorated with `@classmethod`; parse valid `"name:uses"` text, convert `uses`
  to an integer, and return a new instance by calling `cls(name, uses)`.
seo_keywords:
- Python OOP
- a class method factory
- coding practice
---

# A class method factory

A saved item record may arrive as text such as `lantern:8`. Add a named constructor for that format while keeping the ordinary initializer for separate values. No item exists yet, so the new method receives the class instead of an instance.

## The first decorator

A **decorator** is written as an `@` line immediately before a function definition. Python applies it when defining the function and binds the name to the decorated result. You do not put parentheses around the following `def`, and you do not call the decorator each time you call the method.

`@classmethod` changes how Python supplies the first argument: it passes the class rather than an instance. That parameter is conventionally named `cls`.

```python
class MapPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_pair(cls, text):
        x, y = text.split(",")
        return cls(int(x), int(y))
```

Call `MapPosition.from_pair("3,5")`. Python supplies `MapPosition` for `cls`; your string becomes `text`. The method splits the string, converts the pieces to integers, and calls the class to build a new instance. Unlike `__init__`, this method must return the created object.

Place the decorator at the same indentation as `def`, inside the class. The body still needs another level of indentation. `cls(...)` is an ordinary call through the class parameter, like calling a factory argument in the previous lesson.

For this saved-item format, assume the input contains one colon, a nonempty name, and a nonnegative integer count. You do not need error handling yet. Use the existing initializer rather than manually attaching attributes in the factory. The two entry points should lead to the same kind of ready-to-use object; only their input formats differ.

## Your Tasks

1. Add `GameItem.from_text(cls, text)` decorated with `@classmethod`; parse valid `"name:uses"` text, convert `uses` to an integer, and return a new instance by calling `cls(name, uses)`.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe shows the parsed name and count, then confirms an integer count.
