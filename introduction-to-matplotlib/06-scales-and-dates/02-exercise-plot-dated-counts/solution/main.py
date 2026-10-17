import pandas as pd
import matplotlib.pyplot as plt

def plot_dated_visits(frame):
    ordered = frame.assign(day=pd.to_datetime(frame["day"])).sort_values("day")
    fig, ax = plt.subplots()
    ax.plot(ordered["day"], ordered["visits"], marker="o")
    ax.set(xlabel="Date", ylabel="Visits (people)")
    return fig, ax

sample = pd.DataFrame({"day": ["2024-03-05", "2024-03-01"], "visits": [15, 8]})
fig, ax = plot_dated_visits(sample)
