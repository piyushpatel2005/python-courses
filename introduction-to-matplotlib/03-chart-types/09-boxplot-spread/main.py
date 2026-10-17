import matplotlib.pyplot as plt

def soil_boxplot(readings):
    fig, ax = plt.subplots()
    ax.boxplot(readings, showmeans=False)
    ax.set_ylabel("Soil moisture (%)")
    return fig, ax

fig, ax = soil_boxplot([24, 28, 29, 30, 38, 42, 70])
