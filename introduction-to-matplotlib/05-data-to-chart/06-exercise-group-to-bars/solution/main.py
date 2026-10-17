import pandas as pd
import matplotlib.pyplot as plt

def plot_route_means(frame):
    means = frame.groupby("route")["minutes"].mean()
    fig, ax = plt.subplots()
    ax.bar(means.index, means.to_numpy())
    ax.set(xlabel="Route", ylabel="Mean trip (minutes)")
    return fig, ax

sample = pd.DataFrame({"route": ["A", "B", "A"], "minutes": [8, 12, 14]})
fig, ax = plot_route_means(sample)
