---
title: The property function
slug: property-function
order: 6
language: python
lesson_type: coding
summary: Inside `GameItem`, define `label` with `property(get_label)` so reading `item.label` invokes the supplied getter each
  time.
seo_title: The property function | Python OOP practice
seo_description: Inside `GameItem`, define `label` with `property(get_label)` so reading `item.label` invokes the supplied getter
  each time.
seo_keywords:
- Python OOP
- the property function
- coding practice
---

# The property function

The inventory displays an uppercase item label. Let callers read `item.label` while a getter computes the text from the current name. Start with `property(...)` so the connection between the getter and the public attribute is visible.

## Calling a getter through attribute access

```python
class QuestRoute:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_heading(self):
        return f"{self.start} to {self.end}"

    heading = property(get_heading)
```

`get_heading` is a normal method definition. The last line runs in the class body and passes that function, without calling it, to `property`. The result is stored as the class attribute `heading`.

When you read `quest_route.heading` from a `QuestRoute` instance, Python invokes the getter with that instance as `self` and returns its result. The caller does not write parentheses after `heading`. `quest_route.heading()` would first obtain the string and then try to call the string, which is not what you want.

The property is computed when read. It does not store a second, permanently synchronized copy of the displayed text. If the underlying start or end changes, the next read uses those current values. That makes a property useful for a small derived value that callers naturally think of as an attribute.

For this task, the getter is already supplied and returns the item name in uppercase. You only need to connect it to the public name `label` in the class body. Pass the function itself to `property`; adding parentheses would try to call it before there is an instance to supply as `self`.

The probe reads the label, changes the item's name, and reads again. Both readings should work with dot access alone. This lesson adds a read interface; setting properties is a separate topic later in the module.

## Your Tasks

1. Inside `GameItem`, define `label` with `property(get_label)` so reading `item.label` invokes the supplied getter each time.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `LANTERN` followed by `SHIELD`.
