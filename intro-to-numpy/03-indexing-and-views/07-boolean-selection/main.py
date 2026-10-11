import numpy as np
readings = np.array([8, 24, 16, 31])
flagged = readings > 20
readings[flagged] = -1  # Change -1 to 0.
print(readings)
