---
title: Principal component analysis
slug: principal-components
order: 4
language: python
lesson_type: informational
summary: Understand a shorter representation that preserves large directions of variation.
seo_title: Principal component analysis | Machine Learning Fundamentals
seo_description: Understand a shorter representation that preserves large directions of variation.
seo_keywords:
- machine learning
- principal component analysis
hints:
- No. PCA does not ordinarily use fault labels, and a small-variation direction may carry the useful
  signal.
---

A parcel record might contain length, width, height, and several related measurements. **Dimensionality reduction** represents the record using fewer numbers. It can make a plot possible or reduce repeated information before another model uses the data.

**Principal component analysis**, or PCA, creates new features from weighted combinations of the original numerical features. It chooses directions along which the data varies most. The first component captures the largest available variation; later components capture additional variation in perpendicular directions.

If parcel length and width tend to rise together, one component might summarize an overall size direction. Keeping that component gives a compact description, but discards differences in other directions. The new value is not simply the old length column with a new name.

Large variation is not the same as useful prediction information. A small variation in a sensor reading might distinguish a rare fault, while a large variation in parcel size tells us little about faults. PCA ordinarily does not use target labels to decide what to preserve.

Units matter: a large numerical range can dominate the result. Fit scaling and PCA using training data only when they are part of a prediction pipeline, then apply the learned transformation unchanged to evaluation examples.

The first two components can provide a two-dimensional plot even when the source has many columns. The displayed axes are combinations of features, so points close in the plot may still differ in omitted directions. A tidy two-dimensional picture is therefore a partial view, not a complete account of the data.

## Check your understanding

Does retaining the directions of greatest variation guarantee retaining the best information for predicting faults?

**Answer:** No. PCA does not ordinarily use fault labels, and a small-variation direction may carry the useful signal.
