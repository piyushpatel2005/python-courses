import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def plot_large_visits(frame):
    fig, ax = plt.subplots()
    ax.bar(frame["site"], frame["visits"])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, pos: f"{value:,.0f}"))
    return fig, ax

fig, ax = plot_large_visits(pd.DataFrame({"site": ["Square", "Pier"], "visits": [1200, 3500]}))
