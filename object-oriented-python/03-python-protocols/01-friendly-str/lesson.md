---
title: "Give objects a friendly string"
slug: "friendly-str"
order: 1
language: "python"
lesson_type: "coding"
summary: "Implement __str__ so a map marker prints a useful label."
seo_title: "Give objects a friendly string | Object-oriented Python"
seo_description: "Implement __str__ so a map marker prints a useful label."
seo_keywords: ["python", "friendly str", "object oriented programming"]
hints: ["Return text; leave printing to the supplied probe."]
---

# Give objects a friendly string

Mosslight Studio needs readable map markers for Lantern Vale. The previous section gave objects explicit interfaces; now you will let Python operations such as `str()` use those interfaces. Give `MapMarker` a label showing its destination and distance.

A protocol is an agreement about behavior. Python recognizes certain method names and uses them for familiar operations. These names have two underscores on each side; programmers often call them dunder methods. `__str__(self)` is the protocol method for a friendly text representation. Calling `str(marker)` asks the object for that text, and `print(marker)` uses it too. The result must be a string, even when some stored attributes are numbers.

Do not print inside `__str__`. Printing is a side effect; returning a string lets the caller decide whether to print it, put it in a message, or save it for later. A missing return produces `None`, which is not a valid result for this protocol. An f-string is convenient because it converts embedded values to text while keeping the surrounding label readable.

The small example uses a kitchen timer. Notice that the method reads the current instance rather than a global variable. Two timers can therefore produce different descriptions with the same method definition. Your map markers need the same independence, but a different output format.

Special methods belong on the class, alongside `__init__`, rather than being assigned to a single instance. Keep the supplied initializer unchanged. After implementing the method, also try changing a marker's distance and printing it again: a useful description reflects the current data instead of caching the first label.

## A small example

```python
class Timer:
    def __init__(self, minutes):
        self.minutes = minutes

    def __str__(self):
        return f"Timer: {self.minutes} min"

print(Timer(7))
```

## Your Tasks

1. Implement `MapMarker.__str__` to return `<destination>: <km> km`, using the current attributes. For example, the supplied marker should print `Lake: 4 km`.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
