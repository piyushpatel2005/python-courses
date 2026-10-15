---
title: Return a value
slug: return-a-value
order: 8
language: python
lesson_type: coding
summary: 'Implement `Tool.summary(self)` to return `"<name>: <uses> uses"` from the receiving tool''s current attributes,
  without printing or changing them.'
seo_title: Return a value | Python OOP practice
seo_description: 'Implement `Tool.summary(self)` to return `"<name>: <uses> uses"` from the receiving tool''s current attributes,
  without printing or changing them.'
seo_keywords:
- Python OOP
- return a value
- coding practice
---

# Return a value

A workshop screen needs a short description of a tool. Let the tool compute that text, but let the caller decide whether to print it, save it, or put it into a longer message. A return value makes those choices possible.

## Return versus print

Methods return values in the same way ordinary functions do:

```python
class Seat:
    def label(self):
        return f"Row {self.row}"

seat = Seat()
seat.row = "C"
text = seat.label()
print(text.upper())  # ROW C
```

The `return` expression becomes the result of the method call. Here the caller receives a string and can call a string method on it. Printing inside `label` would show some text, but without a `return` the call's result would be `None`. That would not support `text.upper()`.

The `f` before a string allows expressions inside braces. `self.row` reads data from the receiving object at call time. The method is not storing a permanent snapshot of the row; if the row changes, the next call reads the new value.

Keep observation separate from mutation in this exercise. A description method only reads the tool's attributes. Asking for a description should not record another use or change the tool's name.

The supplied factory already attaches `name` and `uses`. Complete the supplied method inside `Tool`. Its output format is part of the interface: other code can rely on the colon, spaces, and word `uses`. We use the same word even when the count is one, so you do not need a pluralization branch.

The probe prints the returned string, then changes the count and prints again. If you see `None` after your description, check whether your method printed instead of returning. Keep printing in the supplied probe, outside the method.

## Your Tasks

1. Implement `Tool.summary(self)` to return `"<name>: <uses> uses"` from the receiving tool's current attributes, without printing or changing them.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints two descriptions with counts `2` and `3`.
