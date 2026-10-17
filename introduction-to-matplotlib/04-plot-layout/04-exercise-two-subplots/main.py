import matplotlib.pyplot as plt

def garden_and_library(days, temps, visits):
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(days, temps)
    # Add the library series to the empty panel.
    return fig, axes

fig, axes = garden_and_library([1, 2, 3], [17, 22, 19], [25, 40, 32])
