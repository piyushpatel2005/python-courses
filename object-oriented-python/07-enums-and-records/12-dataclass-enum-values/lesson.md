---
title: Use dataclass objects as enum values
slug: dataclass-enum-values
order: 12
language: python
lesson_type: coding
summary: A paper catalog has named formats, each with two measurements. Store a small record as each member's value instead of hiding the measurements in positional tuples.
seo_title: Use dataclass objects as enum values | Object-oriented Python
seo_description: A paper catalog has named formats, each with two measurements. Store a small record as each member's value instead of hiding the measurements in positional tuples.
seo_keywords:
  - Python
  - dataclass enum values
  - object-oriented programming
hints:
  - Construct a Dimensions record for each member value.
---

A paper catalog has named formats, each with two measurements. Store a small record as each member's value instead of hiding the measurements in positional tuples.

An enum value can be an arbitrary object, including an instance of a dataclass. Define the record class first, then construct record objects on the right side of the enum's member assignments. The resulting member has its usual `.name`; its `.value` is the record, whose fields you read with a second attribute access.

The example therefore reads `Badge.SMALL.value.height`, not `Badge.SMALL.height`. The member and its stored record are separate objects with separate responsibilities. A method on the enum could later provide a shorter public interface, but this lesson keeps the two layers visible.

The record uses `@dataclass(frozen=True)`. That option blocks ordinary reassignment of its fields, which is useful for a fixed specification shared by every caller of an enum member. It is not deep immutability: a mutable object stored inside a frozen record could still be changed. Our fields are integers, so that complication does not arise here.

Dataclass equality also affects enum construction. Equal record values become aliases, just as equal strings or integers do. Give genuinely different choices different records, or use `@unique` if duplicate specifications should be rejected. Do not apply `@dataclass` directly to the enum; only the value-record class receives that decorator.

The exercise supplies the frozen record and asks you to fill the catalog. The probe follows the two attribute layers and computes an area from the stored measurements.

## A small example

```python
from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Bounds:
    width: int
    height: int

class Badge(Enum):
    SMALL = Bounds(3, 2)
    LARGE = Bounds(8, 5)

print(Badge.SMALL.value.height)
```

## Your Tasks

1. Define `PaperSize.CARD` with value `Dimensions(10, 15)` and `PaperSize.POSTER` with value `Dimensions(30, 40)`, in that order.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
