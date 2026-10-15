---
title: Group animals by habitat
slug: habitat-groups
order: 7
language: python
lesson_type: coding
summary: The care team works one habitat at a time. Give it a grouped view without rearranging
  the arrival list.
seo_title: Group animals by habitat | Object-oriented Python
seo_description: The care team works one habitat at a time. Give it a grouped view without rearranging
  the arrival list.
seo_keywords:
  - Python
  - Animal rescue project
  - habitat groups
hints:
  - Create a list when you first encounter a habitat, then append to that list.
---

The care team works one habitat at a time. Give it a grouped view without rearranging the arrival list.

`habitat_groups()` returns a new dictionary whose keys are habitat strings and whose values are new lists of the original animal objects. Within a habitat, preserve arrival order and repeated arrivals. Include only habitats present in the register; an empty register returns `{}`. Read `animal.habitat` rather than making a list of known species, so a future subclass can supply its own habitat.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `RescueRegister.habitat_groups()` to return the habitat-to-animals dictionary without changing `self.animals`.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Habitats: {'aviary': ['Lark'], 'tank': ['Ripple']}
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
