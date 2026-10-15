---
slug: object-oriented-python
title: Object Oriented Programming with Python
description: Learn Python object-oriented programming by writing classes, implementing protocols, and building animal rescue, banking, and console shop projects.
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

A rescue register needs to remember each animal's needs. A bank account needs to protect its balance. A shopping cart needs to keep an order accurate even after the cart changes. These are the kinds of problems you will work on here.

You will write the code in every lesson. Start with a small class, then give objects data and behavior, choose clear interfaces, and connect several objects into a working program. The explanations introduce the syntax beside the editor; the starter leaves the lesson's new behavior for you to implement.

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

Classes and object state come first. Properties, factories, and methods help you design a usable interface. Special methods connect your objects to Python operations such as addition, comparison, formatting, and length.

Inheritance comes before the animal project so you can build its hierarchy with tools you have already practiced. Composition provides an alternative when an object needs a helper rather than a parent. The banking project puts both ideas to work.

Enums give a fixed set of states names. Dataclasses reduce repetitive record code. Descriptors explain how managed attributes work, including properties and bound methods. Exceptions and abstract contracts prepare you to make errors and expectations explicit in the final shop project.

The course has 112 coding lessons across ten sections. Some lessons ask for only one method; later project stages ask you to connect behavior you have already built. The aim is to make each new responsibility small enough to reason about and test.
