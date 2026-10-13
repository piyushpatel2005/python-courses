---
title: Comparing models for a decision
slug: model-comparison
order: 3
language: python
lesson_type: informational
summary: Combine evaluation, error costs, and operating limits in a model comparison.
seo_title: Comparing models for a decision | Machine Learning Fundamentals
seo_description: Combine evaluation, error costs, and operating limits in a model comparison.
seo_keywords:
- machine learning
- model comparison
- error costs
hints:
- No. Review capacity, error costs, and performance in relevant conditions are still needed.
---

Model comparison requires a defined decision, not just a ranked score. Consider a binary classification task: issue a warning at dispatch when a delivery is likely to arrive after its promised time. Every warning requires review, so missed late deliveries and unnecessary warnings both matter.

The available features include planned distance and the queue at dispatch. An eventual refund amount is also present in the historical records, but it was recorded after arrival. It must be excluded from this prediction because it is not available at dispatch.

For a future-delivery task, use earlier records for training and later records for validation, preserving a final later period for testing. Fit data preparation on training rows only. Compare candidate models against an always-on-time baseline and an existing decision rule, if one is available.

The following invented validation results describe the same examples. The letters identify candidates, not particular algorithms.

| Candidate | Correct warnings | False alarms | Missed late deliveries |
| --- | ---: | ---: | ---: |
| A | 6 | 3 | 2 |
| B | 7 | 7 | 1 |

A produces 9 warnings and catches 6 of the 8 late deliveries. B produces 14 warnings and catches 7 of the same 8. B therefore adds five reviews to catch one additional late delivery, including four extra false alarms. Neither row proves a universal winner.

Choose a candidate and threshold using validation evidence, review capacity, and the costs of each error. Check whether important groups have adequate data and acceptable errors. Then evaluate the fixed choice on the untouched test period. If the results lead to another round of selection, obtain fresh final evaluation evidence.

Record the chosen model's limits and a monitoring and fallback plan. A justified conclusion can be to use a simpler method or not deploy yet. The point is to support the intended decision, not to select the most elaborate algorithm.

## Check your understanding

Can the table alone establish that B should replace A?

**Answer:** No. Review capacity, error costs, and performance in relevant conditions are still needed.
