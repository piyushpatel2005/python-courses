import matplotlib.pyplot as plt

def compare_branches(days, east, west):
    fig, ax = plt.subplots()
    ax.plot(days, east, label="East")
    # Add West and show the legend.
    return fig

fig = compare_branches([1, 2, 3], [8, 11, 14], [6, 10, 12])
plt.show()
