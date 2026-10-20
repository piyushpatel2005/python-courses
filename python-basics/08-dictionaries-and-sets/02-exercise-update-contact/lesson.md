---
title: "Exercise: Update a contact"
slug: exercise-update-contact
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: "Read, edit, and safely look up contact details."
seo_title: "Exercise: Update a contact | Python Basics"
seo_description: "Read, edit, and safely look up contact details."
seo_keywords: [python basics, python collections, beginner python]
---

A contact record has named fields rather than numbered positions. The starter stores a person's name and phone number. Read the name with brackets; assign a new phone number under the existing `"phone"` key. The email address is optional, so use `get()` with a fallback when `"email"` is absent.

Edit `main.py`. **Run** to inspect the name, updated contact, and email; **Submit** to check each step.

## Your Tasks

1. Set `name` from `contact["name"]`.
2. Update `contact["phone"]` to `555-0130`.
3. Set `email` using `contact.get("email", "not provided")`.
