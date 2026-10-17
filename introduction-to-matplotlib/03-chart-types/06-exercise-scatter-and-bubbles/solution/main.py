import matplotlib.pyplot as plt

def reading_bubbles(hours, visits, events):
    fig, ax = plt.subplots()
    ax.scatter(hours, visits, s=events)
    ax.set_xlabel("Open hours")
    return fig, ax

fig, ax = reading_bubbles([5, 7, 9], [28, 40, 54], [30, 90, 150])
