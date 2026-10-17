import matplotlib.pyplot as plt

def garden_canvas(days, temperature):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(days, temperature)
    return fig, ax

fig, ax = garden_canvas([1, 2, 3], [17, 21, 19])
