import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def encode_new(train, query):
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore", drop=None).fit(train)
    return encoder, encoder.transform(query)


# Supplied fixture and observation probe.
training = pd.read_json("categories.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
queries = pd.read_json("queries.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
train = training[["category"]].to_numpy(dtype=object)
query = queries[["category"]].to_numpy(dtype=object)

result = encode_new(train, query)
if result is not None:
    encoder, values = result
    print("Frozen vocabulary:", encoder.categories_[0])
    print("Query indicators:\n", values)
else:
    print("Transform new categories without growing the vocabulary.")
