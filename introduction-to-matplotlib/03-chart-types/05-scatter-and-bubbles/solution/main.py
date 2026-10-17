import matplotlib.pyplot as plt

def garden_bubbles(sunlight, harvest, areas):
    fig, ax = plt.subplots()
    ax.scatter(sunlight, harvest, s=areas, alpha=0.7)
    ax.set_xlabel("Sunlight (hours)")
    ax.set_ylabel("Harvest (kg)")
    return fig, ax

fig, ax = garden_bubbles([4, 6, 7], [3, 8, 10], [40, 90, 160])
