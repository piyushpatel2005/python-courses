---
title: Iterate over canonical members
slug: iterate-members
order: 6
language: python
lesson_type: coding
summary: A small settings panel needs one menu row for each real choice. Build its rows from the enum rather than maintaining a second list of names.
seo_title: Iterate over canonical members | Object-oriented Python
seo_description: A small settings panel needs one menu row for each real choice. Build its rows from the enum rather than maintaining a second list of names.
seo_keywords:
  - Python
  - iterate members
  - object-oriented programming
hints:
  - Iterate over the enum_type argument itself, not over its __members__ mapping.
---

A small settings panel needs one menu row for each real choice. Build its rows from the enum rather than maintaining a second list of names.

An enum class is iterable. In `for member in SomeEnum`, each item is a member object, not its string name or raw value. Use `.name` and `.value` inside the loop to select the information you need. Definition order determines iteration order; Python does not sort the names alphabetically.

Aliases explain an important difference between iteration and `__members__`. Ordinary iteration visits each canonical member once. The `__members__` mapping contains every declared name, including aliases. Use that mapping when you need to inspect spellings, and ordinary iteration when you need one entry per choice.

The example includes an older name for one color. Both names still resolve, but the printed list has only two entries. This avoids duplicate menu options when an application keeps an alias for compatibility. The canonical name is the first name declared for a particular value.

Your helper receives the enum class as an argument. That makes it reusable: it should not refer to the supplied `Theme` fixture by name inside the implementation. Build a fresh list on each call and append a `(name, value)` tuple for each member. A comprehension is also suitable if you prefer it.

The probe shows one input; the checks supply other enums, including an empty enum. An empty iterable should naturally produce an empty list, without a special hardcoded answer.

## A small example

```python
from enum import Enum

class Ink(Enum):
    BLACK = "k"
    CHARCOAL = "k"
    WHITE = "w"

print([member.name for member in Ink])
```

## Your Tasks

1. Implement `member_rows(enum_type)` to return a list of `(member.name, member.value)` tuples in iteration order, omitting aliases.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
