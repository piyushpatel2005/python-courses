import matplotlib.pyplot as plt
import numpy as np

def temperature_figure(hours, temperatures):
    fig, ax = plt.subplots()
    ax.plot(hours, temperatures)
    return fig

fig = temperature_figure(np.array([8, 10, 12]), np.array([15, 18, 22]))
plt.show()
