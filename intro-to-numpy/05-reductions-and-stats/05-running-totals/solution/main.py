import numpy as np

sightings = np.array([3, 1, 4, 2])
running = np.cumsum(sightings)
print(running)
