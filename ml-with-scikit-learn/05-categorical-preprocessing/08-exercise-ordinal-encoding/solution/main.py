import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def encode_sizes(training, incoming, levels):
    encoder = OrdinalEncoder(categories=[levels], handle_unknown="use_encoded_value", unknown_value=-1)
    encoder.fit(training)
    return encoder.transform(incoming)

training = np.array([["deep"], ["shallow"], ["standard"]])
incoming = np.array([["standard"], ["extra-deep"], ["deep"]])
levels = ["shallow", "standard", "deep"]

print("Encoded sizes:", encode_sizes(training, incoming, levels))
