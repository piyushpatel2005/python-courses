---
title: Carry useful exception details
slug: exception-details
order: 4
language: python
lesson_type: coding
summary: Record requested and available inventory quantities on an exception object.
seo_title: Carry useful exception details | Python OOP practice
seo_description: Record requested and available inventory quantities on an exception object.
seo_keywords:
  - Python
  - exception details
  - object oriented programming
hints:
  - Assign the details, then pass one formatted message to super().__init__.
---

# Carry useful exception details

A player tries to use six glowstones, but the inventory holds only two. An `InventoryShortage` should carry both counts so the game can explain the failure or offer a smaller quantity.

A message helps a person, but separate attributes let code decide what to do next without parsing that message. Set those attributes in `__init__`, then call `super().__init__(message)` so ordinary exception display still works. Here the constructor only records a shortage; deciding when to raise it belongs to the caller.

The two attributes are useful for a message such as "only two left" or for choosing a smaller request. Keep them as the original values rather than converting them to strings. Only the message needs formatting; the parent exception stores that message in its args tuple.

## A smaller example

A cooldown error keeps the remaining seconds as data, alongside its message.

```python
class CooldownError(Exception):
    def __init__(self, seconds):
        self.seconds = seconds
        super().__init__(f"wait {seconds} seconds")
```

## Your Tasks

1. Implement `InventoryShortage.__init__(requested, available)` to store both arguments as same-named attributes and initialize the message as `"inventory requested R; available A"`, with the actual values substituted.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `inventory requested 6; available 2`. Press **Submit** to check the behavior with other inputs.
