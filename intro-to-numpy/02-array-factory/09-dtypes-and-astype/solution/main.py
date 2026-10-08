import numpy as np
levels = np.array([0, 0, 5])
flags = levels.astype(bool)
print(flags.tolist(), flags.dtype.kind)
print(levels.dtype.kind)
