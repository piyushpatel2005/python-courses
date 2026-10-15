---
title: Check the enum type at a boundary
slug: enum-type-checks
order: 9
language: python
lesson_type: coding
summary: A function accepts an internal quest state, not arbitrary text. Check the object's type before allowing it into the next part of the program.
seo_title: Check the enum type at a boundary | Object-oriented Python
seo_description: A function accepts an internal quest state, not arbitrary text. Check the object's type before allowing it into the next part of the program.
seo_keywords:
  - Python
  - enum type checks
  - object-oriented programming
hints:
  - Pass the object and the enum class to isinstance.
---

A function accepts an internal quest state, not arbitrary text. Check the object's type before allowing it into the next part of the program.

`isinstance(value, SomeEnum)` asks whether the object is a member of that enum type. It works with every member, so you do not need to enumerate all current choices in a chain of comparisons. It returns a Boolean rather than converting the input.

A member's raw value is not an instance of its plain enum. Neither is the enum class itself. A member from a different enum also fails the check, even if its name and stored value are identical. These distinctions matter at a boundary where data may arrive as a string, number, or already validated object.

To intentionally turn a raw value into a member, call the enum and handle `ValueError` for an unknown value. That operation is separate from this lesson's predicate. A predicate reports whether the input already satisfies a condition; it should not mutate it or substitute a different object.

For portability, use `isinstance` for this member-type question rather than raw-value containment. Python 3.12 changed how enum containment treats raw values, but the type check clearly expresses the intended contract. Checking `.name` alone would be weaker because unrelated objects can have that attribute too.

The supplied fixture includes both new and done members. Your helper should accept both, not just the one printed first. The checks also use an unrelated enum and ordinary Python values to make the boundary visible.

## A small example

```python
from enum import Enum

class AimMode(Enum):
    FREE = "free"
    LOCKED = "locked"

print(isinstance(AimMode.FREE, AimMode))
print(isinstance("free", AimMode))
```

## Your Tasks

1. Implement `is_quest_state(value)` to return whether `value` is an instance of the supplied `QuestState` enum.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
