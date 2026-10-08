import numpy as np

def choose_pair(readings):
    return readings[[-1, 1]]

print(choose_pair(np.array([4, 9, 6, 2])))
