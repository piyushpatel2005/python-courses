---
title: "Substitute objects in a loop"
slug: "substitution-in-a-loop"
order: 6
language: "python"
lesson_type: "coding"
summary: "Call a shared method without branching on concrete class names."
seo_title: "Substitute objects in a loop | Object-oriented Python"
seo_description: "Call a shared method without branching on concrete class names. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "substitution in a loop", "object oriented programming"]
hints: ["Build a result list by calling the shared method; no class-name checks are needed."]
---

# Substitute objects in a loop

A dispatch board contains several kinds of delivery. It needs each delivery's message in order, not a separate branch for every delivery class. Write the board's collection function using their shared `dispatch()` interface.

Polymorphism means one operation can have different implementations. A caller asks each object for the same behavior, and method lookup selects the appropriate implementation. A base class can make that shared contract visible, while subclasses override the details. The loop should not need to know which subclass produced each message.

Substitution works when the implementations keep the caller's expectations. In this exercise every `dispatch()` takes no additional arguments and returns a string without changing the delivery. A subclass that required an extra destination argument would break this caller even if it inherited from the correct base. Relationships alone do not guarantee compatible behavior.

The example asks several built-in strings for uppercase text. It uses the same method name repeatedly instead of branching on each string's contents. Your function will use a similar loop with objects that implement their messages differently. Preserve input order and return a list; do not print inside the collecting function, because the board may need to format that list later.

Python also allows an unrelated object with a compatible method to participate. This is often called duck typing: the caller depends on supported behavior rather than a concrete class name. Submit includes such an object to ensure your function calls the interface instead of using `type` or `isinstance` branches.

The empty input should return an empty list. Repeated references should produce repeated messages, because this function represents board entries rather than unique objects. Keep the supplied classes unchanged; the only new behavior is the loop that collects their returned messages.

## A small example

```python
words = ["arrival", "departure"]
labels = []
for word in words:
    labels.append(word.upper())
print(labels)
```

## Your Tasks

1. Implement `dispatch_messages(deliveries)` to call each item's `dispatch()` once and return the messages in input order, including duplicates. Support an empty input and any compatible object without type-based branches.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
