import pandas as pd
import matplotlib.pyplot as plt

def plot_visits(visits):
    fig, ax = plt.subplots()
    return fig, ax

fig, ax = plot_visits(pd.Series([21, 38], index=["North", "South"]))
