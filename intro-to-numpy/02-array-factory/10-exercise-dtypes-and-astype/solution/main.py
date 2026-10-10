import numpy as np

def typed_feeds(readings):
    values = np.array(readings)
    flags = values.astype(bool)
    labels = values.astype(str)
    complex_values = values.astype(complex)
    return flags, labels, complex_values

print(typed_feeds([0, 2]))
