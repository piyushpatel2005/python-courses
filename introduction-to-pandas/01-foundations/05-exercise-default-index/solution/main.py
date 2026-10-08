import pandas as pd

def arrival_labels(counts):
    return pd.Series(counts).index

print(arrival_labels([6, 2, 5]))
