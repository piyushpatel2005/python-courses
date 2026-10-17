import matplotlib.pyplot as plt

def plot_rack_use(hours, bikes, capacity):
    fig, ax = plt.subplots()
    ax.plot(hours, bikes, marker="o")
    ax.set_ylim(0, capacity)
    ax.set(xlabel="Hour of day", ylabel="Bikes (count)")
    return fig, ax

fig, ax = plot_rack_use([8, 9, 10], [2, 5, 4], 12)
