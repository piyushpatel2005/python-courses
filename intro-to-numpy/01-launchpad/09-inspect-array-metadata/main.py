import numpy as np
# Put this board inside a stack, then add a second 2-by-2 frame.
pads = np.array([[2, 4], [6, 8]])
print(pads.ndim, pads.shape, pads.size, len(pads))
