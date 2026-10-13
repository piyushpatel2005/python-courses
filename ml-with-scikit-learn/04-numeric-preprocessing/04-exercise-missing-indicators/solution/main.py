import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd


def fill_with_flags(train, query):
    imputer = SimpleImputer(strategy="median", add_indicator=True, keep_empty_features=True)
    imputer.fit(train)
    return imputer, imputer.transform(query)


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['width_cm', 'volume_l']].to_numpy()
query = queries[['width_cm', 'volume_l']].to_numpy()

result = fill_with_flags(train, query)
if result is not None:
    imputer, values = result
    print("Output shape:", values.shape)
    print("Values and appended flags:\n", values)
    if imputer.indicator_ is not None:
        print("Flagged training columns:", imputer.indicator_.features_)
else:
    print("Append flags for columns missing during training.")
