import matplotlib.pyplot as plt

def plot_event_range(labels, counts):
    if any(value <= 0 for value in counts):
        raise ValueError("A logarithmic scale needs strictly positive counts")
    fig, ax = plt.subplots()
    ax.bar(labels, counts)
    ax.set_yscale("log")
    return fig, ax

fig, ax = plot_event_range(["Walk", "Fair", "Parade"], [4, 40, 400])
