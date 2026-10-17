import pandas as pd
import matplotlib.pyplot as plt

def plot_rain_visitors(frame):
    complete = frame.dropna(subset=["rain_mm", "visitors"])
    fig, ax = plt.subplots()
    ax.scatter(complete["rain_mm"], complete["visitors"])
    ax.set(xlabel="Rainfall (mm)", ylabel="Visitors (people)")
    return fig, ax

sample = pd.DataFrame({"rain_mm": [0, None, 12], "visitors": [32, 21, 15]})
fig, ax = plot_rain_visitors(sample)
