---
title: Catch only the expected lookup error
slug: catch-a-specific-error
order: 2
language: python
lesson_type: coding
summary: Turn a missing locker number into a useful message without hiding unrelated
  failures.
seo_title: Catch only the expected lookup error | Python OOP practice
seo_description: Turn a missing locker number into a useful message without hiding
  unrelated failures.
seo_keywords:
  - Python
  - catch a specific error
  - object oriented programming
hints:
  - Catch KeyError, not Exception.
---

# Catch only the expected lookup error

Turn a missing locker number into a useful message without hiding unrelated failures.

A `try` block surrounds the operation that may fail. `except KeyError` handles a missing dictionary key, while a different exception still reaches the caller. Keep the block small so a programming mistake elsewhere is not mistaken for missing data. The supplied directory may be any object that supports square-bracket lookup.

Do not test the looked-up value with an if statement. An empty string can be a legitimate label, and the contract says to return it unchanged. The fallback is about an exception during lookup, not about whether the result is truthy.

## A smaller example

A missing paint label has a normal fallback; a broken palette should still fail visibly.

```python
def find_color(palette, label):
    try:
        return palette[label]
    except KeyError:
        return "unpainted"
```

## Your Tasks

1. Implement `locker_label(directory, number)` to return `directory[number]`, or `"Unknown locker"` only when lookup raises `KeyError`. Let other exceptions propagate.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints `Unknown locker`. Press **Submit** to check the behavior with other inputs.
