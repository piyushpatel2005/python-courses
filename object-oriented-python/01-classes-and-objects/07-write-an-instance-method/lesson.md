---
title: Write an instance method
slug: write-an-instance-method
order: 7
language: python
lesson_type: coding
summary: Add `Tool.record_use(self)`, an instance method that increases the receiving tool's existing `uses` count by one.
seo_title: Write an instance method | Python OOP practice
seo_description: Add `Tool.record_use(self)`, an instance method that increases the receiving tool's existing `uses` count
  by one.
seo_keywords:
- Python OOP
- write an instance method
- coding practice
---

# Write an instance method

The workshop has been passing tools to ordinary functions. Now put an operation inside the class so a tool can update its own usage count. This keeps the operation beside the kind of data it uses.

## A function in a class

A **method** is an operation accessed through a class or an instance. Write an ordinary `def` inside the class body, with another level of indentation for its statements.

```python
class Lamp:
    def switch_on(self):
        self.on = True

lamp = Lamp()
lamp.switch_on()
print(lamp.on)  # True
```

The first parameter, conventionally named `self`, refers to the instance receiving the call. In `lamp.switch_on()`, Python supplies `lamp` for `self`. The caller does not write it inside the parentheses.

`self` is a parameter name, not a keyword. Use the conventional name so other Python readers recognize it. Each call can supply a different instance, which is why a method should use `self` instead of a global name such as `lamp` or `drill`.

A local assignment like `on = True` creates a local variable inside the method. It does not attach state to the object. The dot in `self.on` is what makes the assignment an attribute update.

The supplied tool factory gives each tool a starting `uses` count. Your method should add one to that count each time it is called. Its definition needs `self`, but a call such as `tool.record_use()` needs no explicit argument.

Leave the factory in place. It supplies setup you already understand, allowing this lesson to focus on method syntax. The probe calls the same method twice so you can see state survive between calls; the method must read the current count rather than assume every tool starts at zero.

## Your Tasks

1. Add `Tool.record_use(self)`, an instance method that increases the receiving tool's existing `uses` count by one.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Uses after two calls: 7`.
