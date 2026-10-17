import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4])
temperatures = np.array([22, 28, 30, 25])
threshold = 29
mask = temperatures > threshold
fig, ax = plt.subplots()
ax.plot(days[mask], temperatures[mask], marker="o")
ax.set(xlabel="Day", ylabel="Temperature (°C)", title="Hot garden days")
