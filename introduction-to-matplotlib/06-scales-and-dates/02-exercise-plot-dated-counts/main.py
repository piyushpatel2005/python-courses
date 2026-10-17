import pandas as pd
import matplotlib.pyplot as plt

def plot_dated_visits(frame):
    fig, ax = plt.subplots()
    return fig, ax

sample = pd.DataFrame({"day": ["2024-03-05", "2024-03-01"], "visits": [15, 8]})
fig, ax = plot_dated_visits(sample)
