---
title: Class defaults
slug: class-defaults
order: 5
language: python
lesson_type: coding
summary: Give `Tool` a class attribute named `loan_days` with the value `7`. Instances should use that shared default rather
  than store their own copy.
seo_title: Class defaults | Python OOP practice
seo_description: Give `Tool` a class attribute named `loan_days` with the value `7`. Instances should use that shared default
  rather than store their own copy.
seo_keywords:
- Python OOP
- class defaults
- coding practice
---

# Class defaults

Most workshop tools have the same loan period. You could repeat that number on every object, but a class attribute can hold one shared default. You will add that default without writing an initializer.

## Data on the class

An assignment directly inside a class body belongs to the class. It is different from assigning through an instance name after construction.

```python
class LibraryCard:
    renewal_days = 30

card = LibraryCard()
print(LibraryCard.renewal_days)  # 30
print(card.renewal_days)         # 30
```

For the ordinary attributes in this module, Python checks the instance first. When the instance has no value named `renewal_days`, lookup continues on its class. The class value is available through the instance, but Python has not copied it into that instance.

That distinction becomes visible when the default changes:

```python
LibraryCard.renewal_days = 45
print(card.renewal_days)  # 45
```

The already-created card sees the updated default because it still has no individual override. A newly created card sees it too. This is useful for settings that truly describe the category rather than one particular item.

Keep individual names and usage counts on individual tools. If changing one tool's name changed every tool's name, the data would be stored at the wrong level. A shared integer default works well here; mutable collections such as lists need more care, which you will practice shortly.

The editor supplies an empty `Tool` class. Put the default assignment in its indented body, where `pass` currently stands. The probe reads the default through both the class and an instance. The tests also change the class default temporarily to check that new and existing tools consult the class instead of receiving a copied value.

## Your Tasks

1. Give `Tool` a class attribute named `loan_days` with the value `7`. Instances should use that shared default rather than store their own copy.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. Both completed readings should be `7`.
