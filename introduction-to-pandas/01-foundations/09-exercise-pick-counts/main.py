import pandas as pd

def by_label(card, label):
    return None

def by_position(card, position):
    return None

example = pd.Series([4, 9], index=["cider", "soap"])
print(by_label(example, "soap"), by_position(example, 0))
