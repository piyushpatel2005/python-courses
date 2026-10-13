---
title: Bias and limits
slug: bias-and-limits
order: 1
language: python
lesson_type: informational
summary: Look for uneven errors and unsupported interpretations.
seo_title: Bias and limits | Machine Learning Fundamentals
seo_description: Look for uneven errors and unsupported interpretations.
seo_keywords:
- machine learning
- bias and limits
hints:
- No. Other features can act as proxies, and labels or sampling can still reflect unequal conditions.
---

A model can score well overall while working poorly for some people or conditions. If almost all training trips come from city streets, an aggregate result may conceal poor estimates for rural routes.

**Sampling bias** occurs when the collected examples do not adequately represent the intended setting. Labels can also reflect unequal treatment: a customer complaint record measures who complained and whose complaint was recorded, not simply whether service was poor.

Inspect errors in meaningful groups and conditions, while protecting privacy and considering small sample sizes. Removing a sensitive column alone does not ensure fair behavior. Other features may act as proxies, and the target itself may encode an unfair process. Different fairness goals can also conflict; an accuracy score does not choose among them.

Prediction does not establish causation. If rainy days have more late trips, a model may predict the association, but it cannot establish the effect of a specific intervention without further evidence.

Document the intended use and who it affects, the cases it should not handle, and who can review an error. Collect only necessary data with appropriate permission. For consequential decisions, a sensible process may require human review, an appeal route, or deciding not to automate at all.

## Check your understanding

Does removing a neighborhood field guarantee that a model cannot reproduce neighborhood-related disparities?

**Answer:** No. Other features can act as proxies, and labels or sampling can still reflect unequal conditions.
