---
title: Name a fixed set of statuses
slug: named-statuses
order: 1
language: python
lesson_type: coding
summary: Mosslight Studio needs a small, agreed vocabulary for quests in Lantern Vale. An enum gives each allowed status a name that belongs to one particular type.
seo_title: Name a fixed set of statuses | Object-oriented Python
seo_description: Mosslight Studio needs a small, agreed vocabulary for quests in Lantern Vale. An enum gives each allowed status a name that belongs to one particular type.
seo_keywords:
  - Python
  - named statuses
  - object-oriented programming
hints:
  - Put both member assignments inside the supplied class body.
---

Mosslight Studio needs a small, agreed vocabulary for quests in Lantern Vale. An enum gives each allowed status a name that belongs to one particular type.

Import `Enum` from the standard library, then put it in the parentheses of a class definition. Assignments in that class body declare members. Uppercase member names are a convention for constants, not a syntax requirement. Unlike an ordinary class, an enum with declared members represents a fixed set of choices rather than a recipe for making arbitrary new records.

In the example, `Gate.OPEN` is a member object. Its `.name` is the string `"OPEN"`; its `.value` is the string `"open"`. These are three different things. Keep the member inside your program when you want a named choice, and use the value when communicating with a system that expects the raw code.

A misspelled member attribute does not silently create a new status: reading it raises `AttributeError`. This is one reason a set of named members can be easier to maintain than strings repeated throughout a program. It does not prevent every mistake, but it gives related choices a common type and a single definition.

The starter imports `Enum` and supplies an empty class. `pass` makes that unfinished class legal Python. Replace it with member assignments; you do not need an `__init__` method. The supplied probe catches missing-member errors until your definition is ready.

## A small example

```python
from enum import Enum

class Gate(Enum):
    OPEN = "open"
    CLOSED = "closed"

print(Gate.OPEN.name)
print(Gate.OPEN.value)
```

## Your Tasks

1. Define `QuestState` as an `Enum` with exactly `NEW = "new"` and `DONE = "done"`, in that order.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
