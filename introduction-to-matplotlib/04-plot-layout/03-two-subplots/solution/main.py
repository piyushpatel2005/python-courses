import matplotlib.pyplot as plt

def two_signals(days, visits, buses):
    fig, axes = plt.subplots(2, 1)
    axes[0].plot(days, visits)
    axes[0].set_title("Library visits")
    axes[1].plot(days, buses)
    axes[1].set_title("Bus boardings")
    return fig, axes

fig, axes = two_signals([1, 2, 3], [30, 41, 37], [65, 73, 68])
