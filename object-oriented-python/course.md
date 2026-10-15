---
slug: object-oriented-python
title: Object Oriented Programming with Python
description: Learn Python object-oriented programming through game-studio examples, then apply the same ideas in animal rescue, banking, and console shop projects.
language: python
summary: Build useful Python objects through 112 coding lessons, with focused tasks, tests, reference solutions, and three staged projects.
seo_title: Object Oriented Programming with Python
seo_description: Practice Python classes, properties, inheritance, special methods, enums, descriptors, and exceptions in 112 coding lessons and three projects.
seo_keywords:
  - Python OOP
  - Python classes
  - inheritance
  - Python descriptors
  - object oriented programming exercises
modules:
  - slug: classes-and-objects
    title: Classes and objects
    sort_order: 1
  - slug: object-interfaces
    title: Object interfaces
    sort_order: 2
  - slug: python-protocols
    title: Python protocols
    sort_order: 3
  - slug: inheritance
    title: Inheritance and composition
    sort_order: 4
  - slug: animal-rescue-project
    title: Project — Animal rescue register
    sort_order: 5
  - slug: banking-project
    title: Project — Banking model
    sort_order: 6
  - slug: enums-and-records
    title: Enums and records
    sort_order: 7
  - slug: descriptors
    title: Descriptors
    sort_order: 8
  - slug: errors-and-contracts
    title: Errors and contracts
    sort_order: 9
  - slug: ecommerce-project
    title: Project — Console shop
    sort_order: 10
---

# Object Oriented Programming with Python

Mosslight Studio is building Lantern Vale, a small exploration game. An item needs to remember how often it has been used. A player needs an inventory that belongs to them alone. A quest needs a clear state, and a character's stats need rules that keep invalid values out. You will build these kinds of objects while learning Python OOP.

The studio and game are fictional. You do not need to know a game engine or write graphics code: the exercises use small Python objects and console output so you can see exactly what changes.

You will write code in every lesson. Start with a simple game item, give objects data and behavior, then connect them through clear interfaces. The explanations introduce the syntax beside the editor; the starter leaves the new behavior for you to implement. The projects deliberately try other settings, including a rescue register, a banking model, and an e-commerce shop. Those changes of setting let you use the same OOP ideas without relying on familiar game names.

## Before you start

You should already be comfortable with Python variables, strings, numbers, lists, dictionaries, loops, functions, imports, and basic `try`/`except`. You do not need previous experience with classes. If writing a function that loops through a list still takes most of your attention, complete Python basics first.

## How to work through a lesson

Read the explanation and the numbered task, then edit `main.py`. Supplied checks in the code let you inspect the result with Run. Submit runs the lesson's tests, including inputs beyond the visible example. A reference solution is available when you need to compare approaches, but try writing your version first.

Each lesson is self-contained. In a project, the next starter includes the preceding stage's completed behavior so that you can focus on the next addition. You do not need to copy files between lessons. A quiz follows each section.

## What you will build

- An animal rescue register with `Animal`, `Bird`, and `Fish` classes, feeding behavior, and a daily care report.
- A banking model with a base account, savings and current accounts, a fixed deposit, and a separate interest calculator. Its integer-money rules are deliberately simplified for programming practice; it is not production banking software.
- A console shop that lists products, manages a cart, records orders, and prints an itemized invoice. You will pass scripted commands to a `main.py` entrypoint rather than wait for keyboard input. The project runs locally in the lesson workspace and does not process payments or contact a service.

## Course route

Classes and object state come first: two game items can share a class without sharing their changing data. Properties, factories, and methods give the studio a consistent way to work with those objects. Special methods let game values participate in ordinary Python operations such as addition, comparison, formatting, and length.

Inheritance and composition show two different ways to reuse behavior. You will practice them with game objects before applying them to the animal and banking projects. Each project supplies the earlier completed stages, so the change of setting does not require starting from an empty file.

Back at the studio, enums name the states an object can be in, and dataclasses describe small game records. Descriptors explain managed attributes, including properties and bound methods. Exceptions and abstract contracts help you make failures and expectations explicit. The final console shop brings these ideas together in an e-commerce setting.

The course has 112 coding lessons across ten sections. Some lessons ask for only one method; later project stages ask you to connect behavior you have already built. The aim is to make each new responsibility small enough to reason about and test.
