import matplotlib.pyplot as plt

def wait_views(waits, cutoff=20):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    for ax in axes:
        ax.set(xlabel='Wait (minutes)', ylabel='Observations')
    axes[0].set_title('All waits')
    fig.tight_layout()
    return fig, axes

fig, axes = wait_views([2, 3, 6, 7, 12, 39])
