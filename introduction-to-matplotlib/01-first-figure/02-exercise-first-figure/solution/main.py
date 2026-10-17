import matplotlib.pyplot as plt

def arrival_figure(counts):
    fig, ax = plt.subplots()
    ax.plot(range(1, len(counts) + 1), counts)
    return fig

fig = arrival_figure([5, 9, 7])
plt.show()
