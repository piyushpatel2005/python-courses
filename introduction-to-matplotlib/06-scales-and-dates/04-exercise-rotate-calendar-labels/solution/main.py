import pandas as pd
import matplotlib.pyplot as plt

def plot_collection_dates(frame):
    fig, ax = plt.subplots()
    ax.plot(pd.to_datetime(frame["day"]), frame["bags"], marker="o")
    ax.tick_params(axis="x", labelrotation=40)
    ax.set(xlabel="Date", ylabel="Collected bags (count)")
    return fig, ax

sample = pd.DataFrame({"day": ["2024-05-01", "2024-05-04"], "bags": [7, 11]})
fig, ax = plot_collection_dates(sample)
