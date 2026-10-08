import numpy as np

def typed_feeds(readings):
    values = np.array(readings)
    return (values.astype(bool), values.astype(str), values.astype(complex))

print(typed_feeds([0, 2]))
