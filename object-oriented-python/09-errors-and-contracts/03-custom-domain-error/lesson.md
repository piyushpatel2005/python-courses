---
title: Name a domain error
slug: custom-domain-error
order: 3
language: python
lesson_type: coding
summary: Give callers a specific error type when a lobby has no free slots.
seo_title: Name a domain error | Python OOP practice
seo_description: Give callers a specific error type when a lobby has no free slots.
seo_keywords:
  - Python
  - custom domain error
  - object oriented programming
hints:
  - The base class goes in parentheses after the class name.
---

# Name a domain error

A player can join a Lantern Vale lobby only while a slot remains. Give that failure its own exception type so the join screen can handle it without catching every error.

A custom exception is an ordinary class that inherits from `Exception` or one of its subclasses. A meaningful name lets callers catch a game condition separately from unrelated invalid values. The supplied `join_lobby` function already raises `LobbyFullError`; your work is to make that name an exception class. It needs no new methods because its base already stores the message.

The starter deliberately defines the right name with the wrong base. Calling it with a message currently fails before it can act as an exception. Change the class declaration, not `join_lobby`; callers should then be able to distinguish a full lobby by catching the new type.

## A smaller example

The gate exception inherits message handling without adding an initializer.

```python
class GateClosedError(Exception):
    pass

problem = GateClosedError("west gate")
print(str(problem))
```

## Your Tasks

1. Define `LobbyFullError` as a subclass of `Exception` so the supplied `join_lobby(remaining)` raises a catchable domain error when no slots remain.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. After completion the guarded probe reports `LobbyFullError`, rather than `TypeError`. Press **Submit** to check the behavior with other inputs.
