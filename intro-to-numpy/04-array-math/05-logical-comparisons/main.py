import numpy as np
bands = np.array([2, 5, 8, 11])
usable = (bands >= 5) & (bands <= 7)  # Change upper bound to 10.
print(usable)
print(np.array_equal(usable, np.array([False, True, True, False])))
