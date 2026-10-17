import pandas as pd
import matplotlib.pyplot as plt

def plot_canopy_temperature(frame):
    fig, ax = plt.subplots()
    ax.scatter(frame["canopy_pct"], frame["temp_c"])
    ax.set(xlabel="Canopy (%)", ylabel="Temperature (°C)")
    return fig, ax

fig, ax = plot_canopy_temperature(pd.DataFrame({"canopy_pct": [30, 70], "temp_c": [29, 23]}))
