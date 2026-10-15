---
title: Print the daily care report
slug: daily-care-report
order: 8
language: python
lesson_type: coding
summary: Finish the rescue program by turning its current register into a readable care report.
seo_title: Print the daily care report | Object-oriented Python
seo_description: Finish the rescue program by turning its current register into a readable care
  report.
seo_keywords:
  - Python
  - Animal rescue project
  - daily care report
hints:
  - Build a list of care lines, then join it with a newline.
---

Finish the rescue program by turning its current register into a readable care report.

For each arrival, call the stored feeding service’s `meal(animal)` and the animal’s `move()`. Join the returned meal, habitat, and movement with `" | "`. Join those lines with a newline, preserving arrival order and leaving off a trailing newline. Return `"No animals registered."` when the register is empty. The method returns text; the supplied Console probe prints it. Reading a report must not add or remove arrivals.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `RescueRegister.daily_report()` using `self.feeder.meal(animal)` and `animal.move()` to return the care report described above.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Daily care:
Moss: hay | land | walk
Lark: seeds | aviary | fly
Ripple: flakes | tank | swim
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.

The finished program records animals, groups their habitats, and prepares care lines from their own behavior and the shared feeding service.
