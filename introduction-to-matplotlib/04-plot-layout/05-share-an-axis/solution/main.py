import matplotlib.pyplot as plt

def shared_timeline(days, riders, waits):
    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].plot(days, riders)
    axes[1].plot(days, waits)
    return fig, axes

fig, axes = shared_timeline([1, 2, 3], [38, 46, 41], [9, 6, 11])
