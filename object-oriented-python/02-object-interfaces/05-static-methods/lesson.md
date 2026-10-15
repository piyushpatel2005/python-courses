---
title: Static methods
slug: static-methods
order: 5
language: python
lesson_type: coding
summary: Add `GameItem.normalize_code(text)` as a `@staticmethod` that returns `text` with leading/trailing whitespace removed
  and letters uppercased, preserving interior spaces.
seo_title: Static methods | Python OOP practice
seo_description: Add `GameItem.normalize_code(text)` as a `@staticmethod` that returns `text` with leading/trailing whitespace
  removed and letters uppercased, preserving interior spaces.
seo_keywords:
- Python OOP
- static methods
- coding practice
---

# Static methods

Item codes should use a consistent spelling before the inventory stores them. Remove whitespace at the ends and uppercase the letters. This helper fits on `GameItem`, but needs neither an existing item nor the class as an argument.

## No automatic receiver

You have seen an instance method receive `self` and a class method receive `cls`. The `@staticmethod` decorator tells Python to supply neither. Write only the parameters the caller should pass.

```python
class LevelCode:
    @staticmethod
    def compact(text):
        return text.replace(" ", "")

print(LevelCode.compact("AB 12"))  # AB12
```

The decorator line belongs immediately above `def`, at the same indentation. `text` receives the caller's string directly; there is no hidden level-code object in front of it. This is still an ordinary function body, so string methods and returns behave as usual.

A static method can also be accessed through an instance, without receiving that instance as an extra parameter. Calling it through the class often makes its independence from instance state clearer. Choose an instance method when the calculation needs stored instance data, and a class method when it needs the receiving class, such as constructing an alternative input format.

A module-level function would also be reasonable for this normalization rule. Use a static method when keeping the helper in the class's public interface makes it easier to find; there is no need to move every utility into a class.

In this exercise, `strip()` removes whitespace at the ends and `upper()` returns an uppercase string. Both return strings rather than mutating the original string, so you can chain the calls. Interior spaces must remain unchanged. The probe includes leading and trailing whitespace to make the normalization visible, and the tests also use empty text and calls through an instance.

## Your Tasks

1. Add `GameItem.normalize_code(text)` as a `@staticmethod` that returns `text` with leading/trailing whitespace removed and letters uppercased, preserving interior spaces.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Normalized code: AB-7`.
