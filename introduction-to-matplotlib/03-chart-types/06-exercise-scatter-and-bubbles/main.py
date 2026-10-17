import matplotlib.pyplot as plt

def reading_bubbles(hours, visits, events):
    fig, ax = plt.subplots()
    ax.plot(hours, visits, marker="o", color="lightgray")
    # Replace the connected points with bubbles sized by events.
    return fig, ax

fig, ax = reading_bubbles([5, 7, 9], [28, 40, 54], [30, 90, 150])
