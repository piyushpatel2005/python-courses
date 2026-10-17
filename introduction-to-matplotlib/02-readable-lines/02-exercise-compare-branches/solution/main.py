import matplotlib.pyplot as plt

def compare_branches(days, east, west):
    fig, ax = plt.subplots()
    ax.plot(days, east, label="East")
    ax.plot(days, west, label="West")
    ax.legend()
    return fig

fig = compare_branches([1, 2, 3], [8, 11, 14], [6, 10, 12])
plt.show()
