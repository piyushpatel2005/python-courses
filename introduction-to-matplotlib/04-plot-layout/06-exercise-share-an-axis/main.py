import matplotlib.pyplot as plt

def shared_garden(days, temperature, moisture):
    fig, axes = plt.subplots(2, 1)
    axes[0].plot(days, temperature)
    axes[1].plot(days, moisture)
    # Link the day axes while keeping separate vertical scales.
    return fig, axes

fig, axes = shared_garden([1, 2, 3], [18, 22, 20], [48, 41, 45])
