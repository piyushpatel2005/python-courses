import matplotlib.pyplot as plt

def garden_pair(days, sunshine, rain):
    fig, axes = plt.subplots(1, 2, constrained_layout=True)
    axes[0].plot(days, sunshine)
    axes[1].plot(days, rain)
    return fig, axes

fig, axes = garden_pair([1, 2, 3], [5, 7, 4], [3, 0, 8])
