import matplotlib.pyplot as plt

def hour_window(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts)
    ax.set_xticks(hours)
    ax.set_xlim(min(hours) - 1, max(hours) + 1)
    return fig

fig = hour_window([9, 12, 16], [11, 18, 7])
plt.show()
