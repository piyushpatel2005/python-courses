import matplotlib.pyplot as plt
import numpy as np

hours = np.array([7, 9, 11])
wind = np.array([3, 6, 10])
fig, ax = plt.subplots()
ax.plot(hours, wind)
plt.show()
