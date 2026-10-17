import matplotlib.pyplot as plt

def roomy_panels(days, boardings, waits):
    fig, axes = plt.subplots(1, 2, constrained_layout=True)
    axes[0].plot(days, boardings)
    axes[0].set_title("Daily boardings")
    axes[1].plot(days, waits)
    axes[1].set_title("Average wait")
    return fig, axes

fig, axes = roomy_panels([1, 2, 3], [60, 74, 68], [7, 5, 9])
