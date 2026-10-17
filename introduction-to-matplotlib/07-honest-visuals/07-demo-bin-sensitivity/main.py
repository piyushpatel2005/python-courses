import matplotlib.pyplot as plt

def wait_histogram(waits):
    fig, ax = plt.subplots()
    ax.hist(waits, bins=3, range=(0, 20), color='#347f9a', edgecolor='white')
    ax.set(title='Transit waits', xlabel='Minutes', ylabel='Observations')
    return fig, ax

fig, ax = wait_histogram([2, 3, 3, 5, 8, 9, 12, 17])
