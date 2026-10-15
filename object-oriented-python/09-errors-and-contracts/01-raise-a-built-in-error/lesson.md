---
title: Reject an invalid reservation
slug: raise-a-built-in-error
order: 1
language: python
lesson_type: coding
summary: Protect a reservation object from a zero or negative seat count.
seo_title: Reject an invalid reservation | Python OOP practice
seo_description: Protect a reservation object from a zero or negative seat count.
seo_keywords:
  - Python
  - raise a built in error
  - object oriented programming
hints:
  - Put the guard before the assignment to self.seats.
---

# Reject an invalid reservation

Protect a reservation object from a zero or negative seat count.

An exception ends the current operation and gives its caller a reason it could not finish. `ValueError` fits a value that has the expected kind but is outside the allowed range. Check before assigning the attribute: a failed update must leave the old count intact. For this exercise, callers supply integers; type validation is outside this method's contract.

Try a valid update first, then an invalid one on the same object. If you assign before checking, the error can appear correct even though the object now holds a bad seat count. A caller should be able to catch the error and continue using the reservation.

## A smaller example

The temperature check raises before it returns a usable value.

```python
def set_temperature(value):
    if value < -273:
        raise ValueError("below the allowed minimum")
    return value
```

## Your Tasks

1. Implement `Reservation.set_seats(count)`: raise `ValueError("seats must be positive")` when `count <= 0`; otherwise store `count` in `self.seats`. Leave the old value unchanged on rejection.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. A finished method prints `Seats: 4`. Press **Submit** to check the behavior with other inputs.
