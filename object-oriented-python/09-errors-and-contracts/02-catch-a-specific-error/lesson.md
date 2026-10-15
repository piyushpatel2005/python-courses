---
title: Catch only the expected lookup error
slug: catch-a-specific-error
order: 2
language: python
lesson_type: coding
summary: Handle a missing player ID without hiding a broken lookup.
seo_title: Catch only the expected lookup error | Python OOP practice
seo_description: Handle a missing player ID without hiding a broken lookup.
seo_keywords:
  - Python
  - catch a specific error
  - object oriented programming
hints:
  - Catch KeyError, not Exception.
---

# Catch only the expected lookup error

The lobby screen looks up player names by ID. An unknown ID should show a fallback label; a broken player directory should still report its error.

A `try` block surrounds the operation that may fail. `except KeyError` handles a missing dictionary key, while a different exception still reaches the caller. Keep the block small so a programming mistake elsewhere is not mistaken for missing data. The supplied directory may be any object that supports square-bracket lookup.

Do not test the looked-up value with an if statement. An empty string can be a legitimate label, and the contract says to return it unchanged. The fallback is about an exception during lookup, not about whether the result is truthy.

## A smaller example

The map uses a default marker for a location without one. Other lookup failures still reach the caller.

```python
def find_marker(markers, location):
    try:
        return markers[location]
    except KeyError:
        return "unmarked"
```

## Your Tasks

1. Implement `player_label(directory, player_id)` to return `directory[player_id]`, or `"Unknown player"` only when lookup raises `KeyError`. Let other exceptions propagate.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Unknown player`. Press **Submit** to check the behavior with other inputs.
