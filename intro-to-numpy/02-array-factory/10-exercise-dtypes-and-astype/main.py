import numpy as np

def typed_feeds(readings):
    values = np.array(readings)
    flags = None
    labels = None
    complex_values = None
    return flags, labels, complex_values

print(typed_feeds([0, 2]))
