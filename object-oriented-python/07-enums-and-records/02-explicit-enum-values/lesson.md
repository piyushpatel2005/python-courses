---
title: Choose explicit enum values
slug: explicit-enum-values
order: 2
language: python
lesson_type: coding
summary: Lantern Vale sends numeric quest codes to its save-data reader. Those codes belong in an explicit enum definition, where inserting a new member cannot renumber existing codes.
seo_title: Choose explicit enum values | Object-oriented Python
seo_description: Lantern Vale sends numeric quest codes to its save-data reader. Those codes belong in an explicit enum definition, where inserting a new member cannot renumber existing codes.
seo_keywords:
  - Python
  - explicit enum values
  - object-oriented programming
hints:
  - Change the right-hand sides of the two existing member assignments.
---

Lantern Vale sends numeric quest codes to its save-data reader. Those codes belong in an explicit enum definition, where inserting a new member cannot renumber existing codes.

Write the required code on the right side of each assignment. Python does not require consecutive integers. A value can also be a string, tuple, or another object. For example, a tuple can group a unit label and a conversion factor. The member remains an enum member even when its value contains several pieces of data.

The two lookup forms answer different questions. `Encounter["PATROL"]` looks up a member by its name; `Encounter(12)` looks up a member by its value. Calling the enum this way retrieves an existing member rather than creating a new one. A missing name raises `KeyError`, whereas an unknown value raises `ValueError`.

The example's values are deliberately spaced apart. A persisted code should keep its meaning even if you rearrange the source. Use automatically generated values only when the actual codes do not form an external contract; that is the next lesson.

Structured values are allowed, but a mutable list or dictionary is a poor choice for a fixed specification if later code can change it. Prefer immutable values when possible. This exercise uses integers so the relationship between a member and its external code stays easy to inspect.

The starter already has both names. Your edit changes their codes, not the probe or the enum's base class.

## A small example

```python
from enum import Enum

class Encounter(Enum):
    PATROL = 12
    AMBUSH = 48

print(Encounter(48).name)
print(Encounter["PATROL"].value)
```

## Picture the behavior

The diagram illustrates `QuestState.DONE` with the string code `"done"`; the exercise below uses a separate `QuestCode` enum with numeric codes. The member, its name, and its stored value remain distinct.

![QuestState.DONE has name DONE and stored value done; QuestState("done") retrieves the member.](enum-member-and-value.svg)

## Your Tasks

1. Change `QuestCode` so `ACCEPTED` has value `202` and `MISSING` has value `404`.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
