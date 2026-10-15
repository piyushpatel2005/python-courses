---
title: Keep a rescue register
slug: rescue-register
order: 6
language: python
lesson_type: coding
summary: The individual records are ready. A register can now collect them in arrival order.
seo_title: Keep a rescue register | Object-oriented Python
seo_description: The individual records are ready. A register can now collect them in arrival
  order.
seo_keywords:
  - Python
  - Animal rescue project
  - rescue register
hints:
  - Append once, then ask the list for its length.
---

The individual records are ready. A register can now collect them in arrival order.

The supplied constructor gives each register its own empty `animals` list and stores a feeding service in `feeder` for the final report. This is composition: the register has a service. `add(animal)` stores the actual object, not a copied name or a new Animal. For this project, every call records an arrival, even when the same object is added twice.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `RescueRegister.add(animal)` to append the supplied object to `self.animals` and return the new integer count.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Registered: 1
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
