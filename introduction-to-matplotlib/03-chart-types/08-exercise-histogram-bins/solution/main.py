import matplotlib.pyplot as plt

def wait_hist(waits, edges):
    fig, ax = plt.subplots()
    ax.hist(waits, bins=edges)
    ax.set_xlabel("Wait (minutes)")
    return fig, ax

fig, ax = wait_hist([2, 3, 7, 8, 9, 13], [0, 5, 10, 15])
