---
title: Register accounts by ID
slug: account-registry
order: 9
language: python
lesson_type: coding
summary: The simulation needs a way to keep several accounts without confusing their owners or
  balances. Use a dictionary keyed by account ID.
seo_title: Register accounts by ID | Object-oriented Python
seo_description: The simulation needs a way to keep several accounts without confusing their owners
  or balances. Use a dictionary keyed by account ID.
seo_keywords:
  - Python
  - Banking project
  - account registry
hints:
  - Check dictionary membership before assigning the new entry.
---

The simulation needs a way to keep several accounts without confusing their owners or balances. Use a dictionary keyed by account ID.

The supplied constructor creates a separate `accounts` dictionary for each registry. `add(account_id, account)` receives a nonempty string ID and an Account or one of its subclasses; those input types are assumed valid here. Store the same account object so later deposits are visible through the registry. Different IDs may refer to the same object.

An ID already in the dictionary must be rejected even if it refers to the same object. Raise `ValueError` before replacing anything; it tells the caller that the ID is unavailable. A successful addition returns the integer number of registered IDs.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Complete `AccountRegistry.add(account_id, account)` to reject duplicate IDs with `ValueError`, otherwise store the supplied object and return the new count.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Account count: 1
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.
