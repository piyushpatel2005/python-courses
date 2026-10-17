import matplotlib.pyplot as plt

def trip_boxplot(minutes):
    fig, ax = plt.subplots()
    ax.plot([1] * len(minutes), minutes, marker="o", linestyle="")
    # Replace the dot strip with a filled boxplot.
    return fig, ax

fig, ax = trip_boxplot([12, 14, 15, 18, 23, 31])
