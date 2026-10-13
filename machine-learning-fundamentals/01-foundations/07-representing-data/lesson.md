---
title: Representing data
slug: representing-data
order: 7
language: python
lesson_type: informational
summary: See why useful features require consistent, meaningful measurements.
seo_title: Representing data | Machine Learning Fundamentals
seo_description: See why useful features require consistent, meaningful measurements.
seo_keywords:
- machine learning
- representing data
hints:
- Unknown and measured zero convey different information.
---

A model needs a consistent representation of its inputs. If one record expresses duration in minutes and another in hours, equal numbers no longer mean equal quantities. Check definitions and units before treating columns as comparable measurements.

Numerical features measure amounts. Categorical features name groups. Separate yes/no indicator columns can represent package types without pretending that one type is twice another. The appropriate encoding depends on the model and the meaning of the categories.

Missing is not the same as zero. A missing distance records an unknown value; zero is a specific measured distance. One possible policy fills missing values with a typical value learned from training data and adds an indicator for whether the original value was absent.

**Scaling** changes numerical ranges. A common approach subtracts a training-set average and divides by a training-set measure of spread. This does not make a feature more informative; it prevents units alone from dominating some algorithms.

Distance-based methods are particularly sensitive to scale. Changing kilometers to meters multiplies numerical differences by 1,000 without changing the actual deliveries. A tree asking threshold questions one feature at a time is usually less sensitive to this issue.

Fixed unit conversions can be defined in advance. Preparation that learns values from records must be fitted on training data only, then applied unchanged to evaluation data. Do not estimate replacement values or scaling statistics from the entire dataset before splitting it.

## Check your understanding

Why should an unknown distance not automatically become zero?

**Answer:** Unknown and measured zero convey different information.
