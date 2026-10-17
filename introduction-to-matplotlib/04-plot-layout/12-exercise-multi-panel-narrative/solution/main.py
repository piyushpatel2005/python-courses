import matplotlib.pyplot as plt

def weekly_story(days, garden, library, transit):
    fig, axes = plt.subplots(1, 3, figsize=(12, 3), constrained_layout=True)
    axes[0].plot(days, garden)
    axes[0].set_title("Garden temperature")
    axes[1].plot(days, library)
    axes[1].set_title("Library visits")
    axes[2].bar(days, transit)
    axes[2].set_title("Transit boardings")
    fig.suptitle("Neighborhood week")
    return fig, axes

fig, axes = weekly_story([1, 2, 3], [18, 20, 19], [30, 38, 35], [62, 70, 65])
