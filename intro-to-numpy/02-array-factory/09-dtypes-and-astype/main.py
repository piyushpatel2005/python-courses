import numpy as np
# A sound-board level of zero means off. Change the middle level to 0.
levels = np.array([0, 2, 5])
flags = levels.astype(bool)
print(flags.tolist(), flags.dtype.kind)
print(levels.dtype.kind)
