import numpy as np

def calibrate(record):
    view = record[1:3]
    snapshot = record[1:3].copy()
    view[0] = 50
    snapshot[0] = -5
    return view, snapshot

sample = np.array([2, 4, 6, 8])
print(calibrate(sample), sample)
