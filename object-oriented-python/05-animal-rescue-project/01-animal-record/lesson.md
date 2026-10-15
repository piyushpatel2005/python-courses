---
title: Start an animal record
slug: animal-record
order: 1
language: python
lesson_type: coding
summary: The rescue team needs a small record for each animal. Begin with a name and a food; later
  stages will use the same objects to prepare care reports.
seo_title: Start an animal record | Object-oriented Python
seo_description: The rescue team needs a small record for each animal. Begin with a name and a
  food; later stages will use the same objects to prepare care reports.
seo_keywords:
  - Python
  - Animal rescue project
  - animal record
hints:
  - Assign each argument through self; the class habitat is already supplied.
---

The rescue team needs a small record for each animal. Begin with a name and a food; later stages will use the same objects to prepare care reports.

You have practiced inheritance with lockers, tickets, and other small classes. This project uses those skills to build an Animal, Bird, and Fish hierarchy for the rescue team. The supplied class attribute `habitat = "land"` is the default for an ordinary Animal. Store the constructor arguments as instance attributes so changing one animal does not rename another. Both arguments are strings; this stage does not validate their contents.

## Your Tasks

1. Complete `Animal.__init__(self, name, food)` so each new animal stores its own `name` and `food` unchanged.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe should print:

```text
Record: Moss hay
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
