---
title: "Make repr useful for debugging"
slug: "developer-repr"
order: 2
language: "python"
lesson_type: "coding"
summary: "Write an unambiguous __repr__ with quoted string fields."
seo_title: "Make repr useful for debugging | Object-oriented Python"
seo_description: "Write an unambiguous __repr__ with quoted string fields. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "developer repr", "object oriented programming"]
hints: ["Use the !r conversion inside an f-string for each field."]
---

# Make repr useful for debugging

A debugging log needs more detail than a friendly label. A parcel code containing a quote or a newline should remain recognizable when you inspect a collection of parcels. Implement `__repr__` for that programmer-facing view.

Python calls `__repr__(self)` when you use `repr(value)`. Lists and other containers also use representations for their elements. Unlike the audience-facing `__str__`, a representation usually includes the class name and enough state to distinguish objects. It must return a string. A constructor-like form is helpful when practical, but a representation does not have to be executable Python.

Inside an f-string, the conversion `!r` requests `repr` for the embedded value. This matters for strings: quotes and escape sequences make boundaries visible. A code such as `A B` should not become indistinguishable from two separate arguments. Avoid manually surrounding an arbitrary string with single quotes; the string itself may already contain that quote character. Let Python choose a safe representation.

The example below describes a reading rather than a parcel. The class name supplies context, and the number needs no surrounding quotation marks. In your exercise, one field is text, so its representation requires the conversion just described. Tests include values that make careless quoting visible.

Keep representations free of mutations. Inspecting an object in a debugger must not alter its count or consume its contents. The supplied initializer is already complete; only the representation method is unfinished. If a class has `__repr__` but no custom `__str__`, its inherited string behavior can use the representation as a fallback. That convenience does not make the two audiences identical; choose the detail deliberately.

## A small example

```python
class Reading:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Reading(value={self.value!r})"

print([Reading(18)])
```

## Your Tasks

1. Implement `Parcel.__repr__` as `Parcel(code=<repr of code>, count=<repr of count>)`. Preserve quoting and escapes by representing the values rather than manually adding quotes.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
