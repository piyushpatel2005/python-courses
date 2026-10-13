import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd


def fill_missing(train, query):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['width_cm', 'volume_l']].to_numpy()
query = queries[['width_cm', 'volume_l']].to_numpy()

result = fill_missing(train, query)
if result is not None:
    imputer, values = result
    print("Training fill values:", imputer.statistics_)
    print("Filled query:\n", values)
else:
    print("Fit a median imputer and transform the query.")
