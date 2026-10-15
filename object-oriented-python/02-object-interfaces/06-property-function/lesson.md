---
title: The property function
slug: property-function
order: 6
language: python
lesson_type: coding
summary: Inside `Tool`, define `label` with `property(get_label)` so reading `tool.label` invokes the supplied getter each
  time.
seo_title: The property function | Python OOP practice
seo_description: Inside `Tool`, define `label` with `property(get_label)` so reading `tool.label` invokes the supplied getter
  each time.
seo_keywords:
- Python OOP
- the property function
- coding practice
---

# The property function

A tool's displayed name should be readable as `tool.label`, even though it needs a little computation. A property lets attribute access run a method. Start with the explicit `property(...)` function so you can see what the decorator in the next lesson will abbreviate.

## Calling a getter through attribute access

```python
class Route:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_heading(self):
        return f"{self.start} to {self.end}"

    heading = property(get_heading)
```

`get_heading` is a normal method definition. The last line runs in the class body and passes that function, without calling it, to `property`. The result is stored as the class attribute `heading`.

When you read `route.heading` from a `Route` instance, Python invokes the getter with that instance as `self` and returns its result. The caller does not write parentheses after `heading`. `route.heading()` would first obtain the string and then try to call the string, which is not what you want.

The property is computed when read. It does not store a second, permanently synchronized copy of the displayed text. If the underlying start or end changes, the next read uses those current values. That makes a property useful for a small derived value that callers naturally think of as an attribute.

For this task, the getter is already supplied and returns the tool name in uppercase. You only need to connect it to the public name `label` in the class body. Pass the function itself to `property`; adding parentheses would try to call it before there is an instance to supply as `self`.

The probe reads the label, changes the tool's name, and reads again. Both readings should work with dot access alone. This lesson adds a read interface; setting properties is a separate topic later in the module.

## Your Tasks

1. Inside `Tool`, define `label` with `property(get_label)` so reading `tool.label` invokes the supplied getter each time.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `DRILL` followed by `SAW`.
