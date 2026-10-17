import matplotlib.pyplot as plt

def garden_canvas(days, temperature):
    fig, ax = plt.subplots()
    ax.plot(days, temperature)
    # Give the already plotted trend more room.
    return fig, ax

fig, ax = garden_canvas([1, 2, 3], [17, 21, 19])
