---
title: Record a rescued bird
slug: bird-specialization
order: 2
language: python
lesson_type: coding
summary: A bird needs the same name and food record, plus a wingspan for the care team.
seo_title: Record a rescued bird | Object-oriented Python
seo_description: A bird needs the same name and food record, plus a wingspan for the care team.
seo_keywords:
  - Python
  - Animal rescue project
  - bird specialization
hints:
  - The parent needs two arguments; the bird keeps the third.
---

A bird needs the same name and food record, plus a wingspan for the care team.

`Bird` already inherits from `Animal`, and its supplied habitat is `"aviary"`. Its new constructor accepts `name`, `food`, and `wingspan_cm`, in that order. Call `super().__init__` to let Animal store the shared fields, then store the wingspan on the bird. Wingspans supplied here are nonnegative whole centimeters; no new validation is needed.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `Bird.__init__` using `super().__init__(name, food)` and store `wingspan_cm` on the instance.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Bird: Lark 24 aviary
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
