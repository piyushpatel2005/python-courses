import matplotlib.pyplot as plt

def garden_pair(days, sunshine, rain):
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(days, sunshine)
    axes[1].plot(days, rain)
    # Give the already plotted panels room for labels.
    return fig, axes

fig, axes = garden_pair([1, 2, 3], [5, 7, 4], [3, 0, 8])
