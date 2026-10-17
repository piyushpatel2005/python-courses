import matplotlib.pyplot as plt

def sized_figure(days, visits):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(days, visits)
    return fig, ax

fig, ax = sized_figure(["Mon", "Tue", "Wed"], [24, 33, 29])
