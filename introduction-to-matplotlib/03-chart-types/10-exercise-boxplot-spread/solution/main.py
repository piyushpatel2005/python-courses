import matplotlib.pyplot as plt

def trip_boxplot(minutes):
    fig, ax = plt.subplots()
    ax.boxplot(minutes, patch_artist=True)
    ax.set_ylabel("Trip (minutes)")
    return fig, ax

fig, ax = trip_boxplot([12, 14, 15, 18, 23, 31])
