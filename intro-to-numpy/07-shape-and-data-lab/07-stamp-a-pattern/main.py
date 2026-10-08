import numpy as np

exposures = np.array([2, 5])
held = np.repeat(exposures, 2)  # Change this repeat count.
cycled = np.tile(exposures, 2)
print("held:", held)
print("cycled:", cycled)
