import matplotlib.pyplot as plt

def guided_counts(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts)
    ax.grid(axis="y")
    return fig

fig = guided_counts([9, 11, 13], [14, 20, 18])
plt.show()
