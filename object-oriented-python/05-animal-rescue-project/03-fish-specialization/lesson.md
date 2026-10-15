---
title: Record a rescued fish
slug: fish-specialization
order: 3
language: python
lesson_type: coding
summary: Fish records need a water type rather than a wingspan. Add the second specialized record
  without changing Bird.
seo_title: Record a rescued fish | Object-oriented Python
seo_description: Fish records need a water type rather than a wingspan. Add the second specialized
  record without changing Bird.
seo_keywords:
  - Python
  - Animal rescue project
  - fish specialization
hints:
  - Reuse Animal for name and food instead of assigning those fields again.
---

Fish records need a water type rather than a wingspan. Add the second specialized record without changing Bird.

Use the same constructor pattern as the bird stage. `Fish(name, food, water_type)` receives three strings; `water_type` may be `"fresh"`, `"salt"`, or another supplied description. Store it unchanged. The class already supplies `habitat = "tank"`; water type describes conditions inside that habitat, not a different grouping key.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `Fish.__init__` by calling `super().__init__(name, food)` and storing `water_type` on the instance.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Fish: Ripple fresh tank
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
