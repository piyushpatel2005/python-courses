import matplotlib.pyplot as plt

def hour_window(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts)
    # Set ticks and an x window based on hours.
    return fig

fig = hour_window([9, 12, 16], [11, 18, 7])
plt.show()
