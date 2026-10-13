---
title: Precision and recall
slug: precision-and-recall
order: 5
language: python
lesson_type: informational
summary: Choose which classification mistakes deserve attention.
seo_title: Precision and recall | Machine Learning Fundamentals
seo_description: Choose which classification mistakes deserve attention.
seo_keywords:
- machine learning
- precision and recall
hints:
- Recall. Precision instead measures the fraction of issued warnings that are correct.
---

Use the previous lesson's late-trip counts: 6 correct warnings, 3 false alarms, and 2 missed late trips. Precision and recall answer different questions about the positive class.

$$
\begin{aligned}
\text{precision}&=\frac{\text{correct warnings}}{\text{all warnings}}\\
&=\frac{6}{6+3}\approx0.67
\end{aligned}
$$

Precision asks how often a warning is right. Here it is about 67%. The $\approx$ sign means approximately; the decimal is rounded.

$$
\begin{aligned}
\text{recall}&=\frac{\text{correct warnings}}{\text{all actual late trips}}\\
&=\frac{6}{6+2}=0.75
\end{aligned}
$$

Recall asks how many actual late trips we caught. Here it is 75%. A warning system can have high precision by warning only on a few obvious cases while missing many others.

For fixed scores, lowering a threshold flags more cases: recall cannot fall, but the extra warnings can reduce precision. Precision does not have to move monotonically in every finite dataset. Choose the threshold using validation data and the cost of missed cases versus false alarms.

Neither number is a universal quality score. If no warnings are made, precision has a zero denominator and is undefined under this formula; a reporting tool may adopt a convention. If there are no actual positives, recall has the analogous problem. Always inspect the counts behind a reported metric.

When positives are rare, also inspect how many examples support each fraction. Precision of 100% from one warning is much weaker evidence than the same proportion from many representative warnings. The metric describes the observed sample; it is not a guarantee for the next case.

## Check your understanding

Which metric directly measures the fraction of actual late deliveries that receive a warning?

**Answer:** Recall. Precision instead measures the fraction of issued warnings that are correct.
