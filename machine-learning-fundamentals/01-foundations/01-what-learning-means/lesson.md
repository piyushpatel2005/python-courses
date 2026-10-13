---
title: What machine learning learns
slug: what-learning-means
order: 1
language: python
lesson_type: informational
summary: Distinguish a learned prediction rule from a rule written by hand.
seo_title: What machine learning learns | Machine Learning Fundamentals
seo_description: Distinguish a learned prediction rule from a rule written by hand.
seo_keywords:
- machine learning
- what machine learning learns
hints:
- No. The rule is already known and can be implemented directly.
---

Machine learning uses examples to build a **model**, a mathematical rule or system that produces an output from an input. Instead of writing every decision rule by hand, we use a learning algorithm to estimate useful patterns from data.

For example, a delivery-time model receives a distance and predicts a duration. Its training examples pair recorded distances with observed durations. A fixed rule such as “charge a delivery fee of 5” is different: the policy is already known and can be implemented directly.

The **learning algorithm** is the procedure used to build the model. The **fitted model** is the result of that procedure. Running the same algorithm on different examples can produce a different fitted model.

Learning does not choose a sensible goal, collect representative data, or establish that an observed relationship is causal. Those responsibilities remain part of the modeling process. A model can find a useful relationship in the records and still fail on unfamiliar inputs.

Use machine learning when examples contain patterns worth learning and performance can be checked on new cases. A fixed rule may be preferable when the rule is known, records are poor, or errors would be difficult to detect.

## Check your understanding

Does a fixed delivery fee set by policy require machine learning?

**Answer:** No. The rule is already known and can be implemented directly.
