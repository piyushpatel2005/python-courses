---
title: Carry useful exception details
slug: exception-details
order: 4
language: python
lesson_type: coding
summary: Store the requested and available quantities on an exception object.
seo_title: Carry useful exception details | Python OOP practice
seo_description: Store the requested and available quantities on an exception object.
seo_keywords:
  - Python
  - exception details
  - object oriented programming
hints:
  - Assign the details, then pass one formatted message to super().__init__.
---

# Carry useful exception details

Store the requested and available quantities on an exception object.

A message helps a person, but separate attributes let code decide what to do next without parsing that message. Set those attributes in `__init__`, then call `super().__init__(message)` so ordinary exception display still works. Here the constructor only records a shortage; deciding when to raise it belongs to the caller.

The two attributes are useful for a message such as "only two left" or for choosing a smaller request. Keep them as the original values rather than converting them to strings. Only the message needs formatting; the parent exception stores that message in its args tuple.

## A smaller example

The arrival error keeps a numeric detail as well as a human-readable message.

```python
class LateArrivalError(Exception):
    def __init__(self, minutes):
        self.minutes = minutes
        super().__init__(f"late by {minutes} minutes")
```

## Your Tasks

1. Implement `StockShortage.__init__(requested, available)` to store both arguments as same-named attributes and initialize the message as `"requested R; available A"`, with the actual values substituted.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `requested 6; available 2`. Press **Submit** to check the behavior with other inputs.
