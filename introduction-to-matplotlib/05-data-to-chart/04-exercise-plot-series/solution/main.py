import pandas as pd
import matplotlib.pyplot as plt

def plot_visits(visits):
    fig, ax = plt.subplots()
    ax.plot(visits.index, visits.to_numpy(), marker="o")
    ax.set(xlabel="Neighborhood", ylabel="Visits (people)")
    return fig, ax

fig, ax = plot_visits(pd.Series([21, 38], index=["North", "South"]))
