import numpy as np
# Arcade panel: make the blank panel three rows tall.
blank = np.zeros((2, 4))
on = np.ones((2, 4))
print(blank.shape, int(on.sum()))
