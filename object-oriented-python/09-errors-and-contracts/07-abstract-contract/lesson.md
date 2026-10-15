---
title: Declare an abstract contract
slug: abstract-contract
order: 7
language: python
lesson_type: coding
summary: Prevent unfinished delivery policies from being instantiated.
seo_title: Declare an abstract contract | Python OOP practice
seo_description: Prevent unfinished delivery policies from being instantiated.
seo_keywords:
  - Python
  - abstract contract
  - object oriented programming
hints:
  - Both the ABC base and the abstractmethod decorator are needed.
---

# Declare an abstract contract

Prevent unfinished delivery policies from being instantiated.

Duck typing lets compatible objects work without a shared base class. An abstract base class adds an earlier check: Python refuses to instantiate it while abstract methods remain unimplemented. Import `ABC` and `abstractmethod` from `abc`, inherit from `ABC`, and decorate the required method. This checks that a concrete override exists; it does not prove the override calculates a sensible result.

The pass body is not what makes a method abstract. The decorator records that requirement on the class, and ABC makes Python enforce it during construction. A subclass that does nothing remains abstract; a regular override clears the requirement for that method.

## A smaller example

The sound source names an operation but deliberately leaves its body unfinished.

```python
from abc import ABC, abstractmethod

class SoundSource(ABC):
    @abstractmethod
    def sound(self):
        pass
```

## Your Tasks

1. Make `DeliveryPolicy` inherit from `ABC` and mark its supplied `fee_cents(self, subtotal_cents)` method with `@abstractmethod`. Both this class and a subclass that omits the method must reject instantiation with `TypeError`.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe reports `TypeError`, which is the intended protection in this lesson. Press **Submit** to check the behavior with other inputs.
