import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def encode_sizes(training, incoming, levels):
    return None

training = np.array([["deep"], ["shallow"], ["standard"]])
incoming = np.array([["standard"], ["extra-deep"], ["deep"]])
levels = ["shallow", "standard", "deep"]

print("Encoded sizes:", encode_sizes(training, incoming, levels))
