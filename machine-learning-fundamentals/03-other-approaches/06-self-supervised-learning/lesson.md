---
title: Self-supervised learning
slug: self-supervised-learning
order: 6
language: python
lesson_type: informational
summary: See how a learning task can obtain targets from the data itself.
seo_title: Self-supervised learning | Machine Learning Fundamentals
seo_description: See how a learning task can obtain targets from the data itself.
seo_keywords:
- machine learning
- self-supervised learning
hints:
- From the part of the original image that was hidden, not from a person supplying a category label.
---

A collection of unlabeled images still contains information that a model can learn from. In **self-supervised learning**, the training procedure constructs a task whose targets come from the data itself rather than from a person labeling every example.

For example, hide part of an image and train a model to predict the missing content from the visible part. The original image supplies the answer. This is only one possible self-supervised task; the broader idea is to create a useful learning signal from available data.

The result can be a representation that helps a later task. A model trained on many images might provide useful features for a smaller labeled image-classification dataset. The next lesson considers reuse more generally.

Self-supervision differs from clustering: it defines a prediction objective rather than necessarily trying to group examples. It also differs from reinforcement learning, where actions influence later observations and rewards.

Removing manual labels does not remove human choices or data problems. The examples can still exclude important situations, include private information, or encourage shortcuts that do not help the eventual application. Success at reconstructing hidden content is not proof of reliable performance on another task.

## Check your understanding

In the hidden-image example, where does the training target come from?

**Answer:** From the part of the original image that was hidden, not from a person supplying a category label.
