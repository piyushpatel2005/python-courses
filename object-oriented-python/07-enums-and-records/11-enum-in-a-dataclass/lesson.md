---
title: Store an enum member in a dataclass
slug: enum-in-a-dataclass
order: 11
language: python
lesson_type: coding
summary: A support record has both free-form text and a status chosen from a fixed set. Use a dataclass for the record and an enum for its status field.
seo_title: Store an enum member in a dataclass | Object-oriented Python
seo_description: A support record has both free-form text and a status chosen from a fixed set. Use a dataclass for the record and an enum for its status field.
seo_keywords:
  - Python
  - enum in a dataclass
  - object-oriented programming
hints:
  - The default should be the member, not its name or raw value.
---

A support record has both free-form text and a status chosen from a fixed set. Use a dataclass for the record and an enum for its status field.

An enum and a dataclass answer different questions. An enum names a fixed collection of choices. A dataclass represents individual records whose field values can vary. Combine them by annotating a field with the enum type and assigning a member as its default.

The example's `Card` is an ordinary dataclass. Its `side` field holds a `Side` member, so callers can inspect `card.side.name` or compare it with `Side.BACK`. The annotation is documentation for tools and readers; it does not itself enforce the field type. You would need explicit validation to reject a caller who passes a raw string.

Apply `@dataclass` to the record, not directly to the enum class. Decorating an `Enum` subclass as a dataclass is not the pattern taught here and can produce broken member comparison behavior. Keeping the types separate also makes their roles easier to read.

A member is a suitable shared default because every record can intentionally begin with the same named status. Reassigning one record's field to a different member does not change another record's field, nor does it mutate the member itself. Do not confuse shared choices with a shared mutable list of record data.

The exercise supplies the enum and the rest of the dataclass. Replace the placeholder field declaration with a typed member default. Existing generated initialization will then accept an explicit status when a caller wants a different starting state.

## A small example

```python
from dataclasses import dataclass
from enum import Enum

class Side(Enum):
    FRONT = "front"
    BACK = "back"

@dataclass
class Card:
    caption: str
    side: Side = Side.FRONT

print(Card("Trail map").side.name)
```

## Your Tasks

1. Change `SupportCase.state` to an annotated `CaseState` field whose default is `CaseState.OPEN`; callers must still be able to pass `CaseState.CLOSED` explicitly.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
