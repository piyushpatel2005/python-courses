import numpy as np
readings = np.array([8, 24, 16, 31])
flagged = readings > 20
readings[flagged] = 0
print(readings)
