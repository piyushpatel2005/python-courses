import numpy as np
import matplotlib.pyplot as plt

def plot_loud_days(days, decibels, threshold):
    fig, ax = plt.subplots()
    days = np.asarray(days)
    decibels = np.asarray(decibels)
    mask = decibels > threshold
    ax.plot(days[mask], decibels[mask], marker="o")
    ax.set(xlabel="Day", ylabel="Noise (dB)")
    return fig, ax

fig, ax = plot_loud_days(np.array([1, 2, 3]), np.array([48, 65, 53]), 50)
