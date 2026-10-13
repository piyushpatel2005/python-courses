---
title: Monitoring and drift
slug: monitoring-and-drift
order: 2
language: python
lesson_type: informational
summary: Treat deployment as a monitored decision rather than a final score.
seo_title: Monitoring and drift | Machine Learning Fundamentals
seo_description: Treat deployment as a monitored decision rather than a final score.
seo_keywords:
- machine learning
- monitoring and drift
hints:
- No. It signals a change to investigate; actual outcomes are needed to establish the effect on performance.
---

A delivery-time model tested during quiet months may struggle after roadworks begin. **Data drift** means the distribution of inputs changes. **Concept drift** means the relationship between inputs and the target changes. Roadworks could change typical trip distances, travel times for the same distance, or both.

Monitor incoming features, missing values, prediction patterns, and actual outcomes when they become available. A change in features is a warning to investigate, not proof that prediction quality has fallen. Conversely, performance can change before a simple input monitor notices anything.

Outcomes may arrive late. A rising warning rate is observable immediately, but measuring false alarms and missed delays requires completed deliveries. Compare recent periods and relevant groups rather than relying only on a lifetime average.

Decide in advance who investigates, when a model is paused, and what fallback is used. A previous business rule may be a useful fallback. Retraining is one possible response, but it can reproduce faulty labels or reinforce a feedback loop if the model changes which outcomes get observed.

Keep records of model versions and evaluation conditions. A successful launch means the model was useful under tested conditions, not that it will remain useful indefinitely.

## Check your understanding

Does a change in average input distance prove that a model’s accuracy has fallen?

**Answer:** No. It signals a change to investigate; actual outcomes are needed to establish the effect on performance.
