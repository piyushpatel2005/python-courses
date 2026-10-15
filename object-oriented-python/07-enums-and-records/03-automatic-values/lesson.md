---
title: Generate internal values with auto
slug: automatic-values
order: 3
language: python
lesson_type: coding
summary: A multiplayer match needs named phases, but no external system cares which integers represent them. Let Python assign those internal values.
seo_title: Generate internal values with auto | Object-oriented Python
seo_description: A multiplayer match needs named phases, but no external system cares which integers represent them. Let Python assign those internal values.
seo_keywords:
  - Python
  - automatic values
  - object-oriented programming
hints:
  - Each member needs its own call to the imported auto function.
---

A multiplayer match needs named phases, but no external system cares which integers represent them. Let Python assign those internal values.

Import `auto` alongside `Enum`. In a plain enum, each assignment such as `PREPARE = auto()` requests a generated value. For an enum consisting only of these calls and using the default behavior, values start at one and increase by one in definition order.

The parentheses matter: `auto()` creates the placeholder that the enum machinery replaces. Writing the bare name `auto` assigns something else. You can still inspect `.value` after the class exists; the placeholder itself is not the finished value.

Automatic numbers are convenient for internal choices, but they are not stable storage codes. Inserting a member near the beginning changes the numbers of later members. If a file or network message depends on the exact number, use an explicit value instead. Avoid mixing automatic and manually chosen values here; the simple all-automatic case makes the rule clear across Python versions.

Notice that the example does not define an initializer or increment a counter. The enum builds its members while the class is created. Your exercise uses a different sequence and asks for that same creation mechanism, not merely integers that happen to equal today's generated result.

The starter imports everything needed and gives the phases temporary strings. Replace the values with calls while keeping their names and order. Run will print the resulting numbers; Submit also checks that the definition actually uses `auto()` for each phase.

## A small example

```python
from enum import Enum, auto

class TurnPhase(Enum):
    AIM = auto()
    RESOLVE = auto()

print(TurnPhase.AIM.value, TurnPhase.RESOLVE.value)
```

## Your Tasks

1. Use `auto()` for all three `MatchPhase` members, keeping the order `LOBBY`, `PLAY`, `RESULTS`.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
