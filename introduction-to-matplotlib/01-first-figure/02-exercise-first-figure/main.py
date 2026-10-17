import matplotlib.pyplot as plt

def arrival_figure(counts):
    fig, ax = plt.subplots()
    # Plot counts against 1, 2, 3, ... and return the figure.
    return fig

fig = arrival_figure([5, 9, 7])
plt.show()
