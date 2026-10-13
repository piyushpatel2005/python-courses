import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def encode_categories(train, query):
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="error", drop=None).fit(train)
    return encoder, encoder.transform(query), encoder.get_feature_names_out(["category"])


# Supplied fixture and observation probe.
training = pd.read_json("categories.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
queries = pd.read_json("queries.json", orient="records", dtype={"category": "object"}, convert_dates=False).replace({None: np.nan})
train = training[["category"]].to_numpy(dtype=object)
query = queries[["category"]].to_numpy(dtype=object)

result = encode_categories(train, query)
if result is not None:
    encoder, values, names = result
    print("Output columns:", names)
    print("Encoded rows:\n", values)
else:
    print("Encode categories into named indicator columns.")
