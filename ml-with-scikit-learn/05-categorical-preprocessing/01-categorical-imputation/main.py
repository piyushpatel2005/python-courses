import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd


def fill_categories(train, query):
    imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent", keep_empty_features=True)
    imputer.fit(train)
    return imputer, imputer.transform(query)


# Supplied fixture and observation probe.
training = pd.read_json("categories.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
queries = pd.read_json("queries.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
train = training[["category"]].to_numpy(dtype=object)
query = queries[["category"]].to_numpy(dtype=object)

result = fill_categories(train, query)
if result is not None:
    imputer, values = result
    print("Replacement:", imputer.statistics_)
    print("Filled categories:\n", values)
else:
    print("Replace missing markers with a declared category sentinel.")
