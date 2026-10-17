import matplotlib.pyplot as plt

def neighborhood_report(days, visits, riders, waits):
    fig, axes = plt.subplots(1, 3, figsize=(12, 3), constrained_layout=True)
    axes[0].plot(days, visits)
    axes[0].set_title("Visits over time")
    axes[1].bar(days, riders)
    axes[1].set_title("Boardings by day")
    axes[2].hist(waits, bins=3)
    axes[2].set_title("Wait distribution")
    fig.suptitle("Daily counts")
    return fig, axes

fig, axes = neighborhood_report([1, 2, 3], [24, 31, 27], [60, 72, 68], [4, 5, 7, 8, 10, 12])
