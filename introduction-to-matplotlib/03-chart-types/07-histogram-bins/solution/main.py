import matplotlib.pyplot as plt

def temperature_hist(readings):
    fig, ax = plt.subplots()
    ax.hist(readings, bins=[10, 15, 20, 25], color="tomato")
    ax.set_xlabel("Temperature (°C)")
    return fig, ax

fig, ax = temperature_hist([11, 12, 14, 16, 19, 21, 24])
