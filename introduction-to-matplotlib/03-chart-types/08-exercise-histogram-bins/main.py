import matplotlib.pyplot as plt

def wait_hist(waits, edges):
    fig, ax = plt.subplots()
    ax.plot(waits, [0] * len(waits), marker="o", linestyle="")
    # Replace the dot strip with counts in the supplied intervals.
    return fig, ax

fig, ax = wait_hist([2, 3, 7, 8, 9, 13], [0, 5, 10, 15])
