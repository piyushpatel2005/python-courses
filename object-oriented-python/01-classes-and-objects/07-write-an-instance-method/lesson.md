---
title: Write an instance method
slug: write-an-instance-method
order: 7
language: python
lesson_type: coding
summary: Add `GameItem.record_use(self)`, an instance method that increases the receiving item's existing `uses` count by one.
seo_title: Write an instance method | Python OOP practice
seo_description: Add `GameItem.record_use(self)`, an instance method that increases the receiving item's existing `uses` count
  by one.
seo_keywords:
- Python OOP
- write an instance method
- coding practice
---

# Write an instance method

An item activation should increase that item's `uses` count. Put this operation inside `GameItem` as a method, so callers can ask an item to record its own use rather than pass it to a separate function.

## A function in a class

A **method** is an operation accessed through a class or an instance. Write an ordinary `def` inside the class body, with another level of indentation for its statements.

```python
class Beacon:
    def activate(self):
        self.on = True

beacon = Beacon()
beacon.activate()
print(beacon.on)  # True
```

The first parameter, conventionally named `self`, refers to the instance receiving the call. In `beacon.activate()`, Python supplies `beacon` for `self`. The caller does not write it inside the parentheses.

`self` is a parameter name, not a keyword. Use the conventional name so other Python readers recognize it. Each call can supply a different instance, which is why a method should use `self` instead of a global name such as `beacon` or `lantern`.

A local assignment like `on = True` creates a local variable inside the method. It does not attach state to the object. The dot in `self.on` is what makes the assignment an attribute update.

The supplied item factory gives each item a starting `uses` count. Your method should add one to that count each time it is called. Its definition needs `self`, but a call such as `item.record_use()` needs no explicit argument.

Leave the factory in place. It supplies setup you already understand, allowing this lesson to focus on method syntax. The probe calls the same method twice so you can see state survive between calls; the method must read the current count rather than assume every item starts at zero.

## Your Tasks

1. Add `GameItem.record_use(self)`, an instance method that increases the receiving item's existing `uses` count by one.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Uses after two calls: 7`.
