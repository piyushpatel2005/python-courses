import pandas as pd
import matplotlib.pyplot as plt

def plot_parcels(frame):
    ordered = frame.sort_values("day")
    fig, ax = plt.subplots()
    ax.plot(ordered["day"], ordered["parcels"], marker="o")
    ax.set(xlabel="Day", ylabel="Parcels (boxes)")
    return fig, ax

fig, ax = plot_parcels(pd.DataFrame({"day": [3, 1, 2], "parcels": [8, 2, 5]}))
