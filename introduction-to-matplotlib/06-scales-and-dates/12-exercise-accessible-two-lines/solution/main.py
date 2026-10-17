import matplotlib.pyplot as plt

def plot_school_routes(days, walkers, riders):
    with plt.style.context("ggplot"):
        fig, ax = plt.subplots(constrained_layout=True)
        ax.plot(days, walkers, label="Walkers", color="#0072B2", linestyle="-")
        ax.plot(days, riders, label="Riders", color="#D55E00", linestyle="--")
        ax.set(xlabel="Day", ylabel="Travelers (people)")
        ax.legend()
    return fig, ax

fig, ax = plot_school_routes([1, 2, 3], [14, 18, 21], [11, 13, 17])
