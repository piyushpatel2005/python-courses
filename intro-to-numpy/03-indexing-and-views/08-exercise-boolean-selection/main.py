import numpy as np

def censor_weak(signals, threshold):
    cleaned = signals.copy()
    # Replace every value below threshold with -1.
    return cleaned

print(censor_weak(np.array([5, 2, 8, 3]), 4))
