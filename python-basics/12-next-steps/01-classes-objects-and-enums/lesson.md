---
title: "Classes, objects, and enums: a first look"
slug: classes-objects-and-enums
order: 1
language: python
lesson_type: informational
runtime: pyodide
summary: Recognize classes, objects, attributes, methods, and enums in Python code.
seo_title: "Python Class, Object, and Enum Vocabulary | Python Basics"
seo_description: Learn what Python classes, objects, attributes, methods, and enum choices mean before studying them in depth.
seo_keywords: [python class, object, attribute, method, enum]
---

You have used objects throughout this course, even though you have not written a class. A class describes a kind of value; an object is one particular value of that kind. For instance, `"pottery"` is a string object. Its `.upper()` method returns `"POTTERY"`.

An attribute is data attached to an object. In a program that defines a `Workshop` class, `workshop.name` could read one workshop object's name, while `workshop.remaining_seats()` could call a method to calculate its open seats. That class is only an illustration; you do not need to implement it in the final project. You can keep the workshop capacities in a dictionary instead.

An enum names a fixed set of choices, such as `OPEN` and `FULL` for registration status. Python uses class syntax to define custom enums. For now, it is enough to recognize the term; the next lesson uses ordinary strings for status messages.
