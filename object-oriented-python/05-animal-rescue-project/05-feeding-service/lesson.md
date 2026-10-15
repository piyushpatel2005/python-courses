---
title: Add a feeding service
slug: feeding-service
order: 5
language: python
lesson_type: coding
summary: The team needs meal labels for every animal. Put that formatting in a separate service
  that accepts an animal object.
seo_title: Add a feeding service | Object-oriented Python
seo_description: The team needs meal labels for every animal. Put that formatting in a separate
  service that accepts an animal object.
seo_keywords:
  - Python
  - Animal rescue project
  - feeding service
hints:
  - Read the two instance attributes each time the method is called.
---

The team needs meal labels for every animal. Put that formatting in a separate service that accepts an animal object.

`FeedingService` is not a kind of Animal, so it does not inherit from Animal. Its `meal(animal)` method reads the supplied object and returns a string in the exact form `name: food`, with one space after the colon. It must not change the record. A keeper can correct an animal’s food and the next call should reflect that correction.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `FeedingService.meal(animal)` to return the animal’s current name and food as `"name: food"` without changing either field.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Meal: Lark: seeds
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
