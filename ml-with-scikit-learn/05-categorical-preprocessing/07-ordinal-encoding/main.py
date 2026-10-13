import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def encode_sizes(training, incoming, levels):
    encoder = OrdinalEncoder(categories=[list(reversed(levels))], handle_unknown="use_encoded_value", unknown_value=-1)
    encoder.fit(training)
    return encoder.transform(incoming)

training = np.array([["small"], ["large"], ["medium"]])
incoming = np.array([["large"], ["sample"], ["small"]])
levels = ["small", "medium", "large"]

print("Encoded sizes:", encode_sizes(training, incoming, levels))
