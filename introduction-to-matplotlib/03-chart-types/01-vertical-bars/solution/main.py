import matplotlib.pyplot as plt

def garden_bars(beds, harvests):
    fig, ax = plt.subplots()
    ax.bar(beds, harvests, color="seagreen")
    ax.set_ylabel("Harvest (kg)")
    return fig, ax

fig, ax = garden_bars(["North", "South", "East"], [8, 5, 11])
