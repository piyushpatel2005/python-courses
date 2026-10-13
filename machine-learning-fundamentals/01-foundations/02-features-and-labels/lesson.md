---
title: Features and labels
slug: features-and-labels
order: 2
language: python
lesson_type: informational
summary: Identify what a model receives and what it is asked to predict.
seo_title: Features and labels | Machine Learning Fundamentals
seo_description: Identify what a model receives and what it is asked to predict.
seo_keywords:
- machine learning
- features and labels
hints:
- Duration is the label; distance and queue length are features.
---

A **feature** is an input supplied to a model. A **label**, also called the target, is the answer a supervised model learns to predict. One row usually represents one example, such as one delivery.

| Record | Feature: distance (km) | Feature: queue at dispatch | Label: duration (minutes) |
| --- | ---: | ---: | ---: |
| A | 2 | 0 | 14 |
| B | 4 | 3 | 25 |
| C | 6 | 1 | 29 |

These are invented values for explaining the structure. The record identifier names a row; it is not automatically a useful feature. The duration column is a label because duration is the chosen prediction target.

**Supervised learning** uses examples with known targets. Targets may come from measurements, later events, or human judgments. They are not necessarily correct: an incorrectly stopped timer creates a misleading duration label.

Define the prediction moment as well as the target. Distance and the current queue may be available at dispatch. Actual arrival time is not available then and must not be used as an input to predict the same delivery's duration.

A column's role depends on the task. A measured duration could be an input for a later analysis, but it cannot be an input to an earlier prediction that requires knowing that duration in advance.

## Check your understanding

When predicting duration from distance and queue length, which value is the label?

**Answer:** Duration is the label; distance and queue length are features.
