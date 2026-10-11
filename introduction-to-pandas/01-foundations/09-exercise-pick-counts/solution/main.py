import pandas as pd

def by_label(card, label):
    return card.loc[label]

def by_position(card, position):
    return card.iloc[position]

example = pd.Series([4, 9], index=["cider", "soap"])
print(by_label(example, "soap"), by_position(example, 0))
