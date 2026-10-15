---
title: Give each animal a movement
slug: species-behavior
order: 4
language: python
lesson_type: coding
summary: A care report should ask each animal how it moves. The caller should not have to check
  whether it received a bird or a fish.
seo_title: Give each animal a movement | Object-oriented Python
seo_description: A care report should ask each animal how it moves. The caller should not have
  to check whether it received a bird or a fish.
seo_keywords:
  - Python
  - Animal rescue project
  - species behavior
hints:
  - Each body needs only a return; the caller supplies no extra argument.
---

A care report should ask each animal how it moves. The caller should not have to check whether it received a bird or a fish.

Add the same method name to all three classes. Animal provides the default; Bird and Fish override it. Calling `animal.move()` in a mixed list then selects the method on that particular object. Return a lowercase word rather than printing it, so a later report can reuse the result.

The starter includes the completed previous stage. Only the new TODO bodies are unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `move()` to return `"walk"` for Animal, `"fly"` for Bird, and `"swim"` for Fish.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Movements: ['walk', 'fly', 'swim']
```

The probe is supplied; finish the three move methods. Submit checks a different mixed list as well.
