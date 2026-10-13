---
title: Reinforcement learning
slug: reinforcement-learning
order: 8
language: python
lesson_type: informational
summary: Distinguish learning from action outcomes from predicting a supplied label.
seo_title: Reinforcement learning | Machine Learning Fundamentals
seo_description: Distinguish learning from action outcomes from predicting a supplied label.
seo_keywords:
- machine learning
- reinforcement learning
hints:
- Route actions affect later states and rewards; the image classifier ordinarily predicts from a
  fixed input.
---

**Reinforcement learning** studies how an agent learns behavior through actions and rewards. Unlike a standard supervised prediction task, an action can change the next situation and the observations available later.

The agent observes a state, chooses an action, and receives a reward and a new situation from its environment. A **policy** is the rule for choosing actions. The objective usually concerns accumulated reward over time rather than only the next immediate reward.

Route selection is one example: taking a turn changes the location from which the next route decision must be made. A reward might depend on reaching the destination efficiently. This differs from classifying a stored image, where the prediction usually does not alter the image or create a sequence of new states.

**Exploration** tries actions to gather information. **Exploitation** uses actions that already appear effective. An unfamiliar action may reveal a better option but can also have a cost. Rewards can be delayed, making it difficult to determine which earlier actions helped or hurt.

A reward is not normally a correct-action label for every state. Optimizing an incomplete reward can produce unwanted behavior; rewarding speed alone does not establish safe operation. Real-world systems need constraints and evaluation beyond success in a simulation. If a known planning rule solves the problem well, reinforcement learning may add unnecessary complexity.

## Check your understanding

What makes a route-choice sequence different from classifying a stored image?

**Answer:** Route actions affect later states and rewards; the image classifier ordinarily predicts from a fixed input.
