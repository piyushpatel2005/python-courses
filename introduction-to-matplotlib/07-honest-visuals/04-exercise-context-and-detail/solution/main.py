import matplotlib.pyplot as plt

def temperature_context(days, celsius, focus=(18, 22)):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    for ax in axes:
        ax.plot(days, celsius, marker='o', color='#347f9a')
        ax.set(xlabel='Day', ylabel='Temperature (°C)')
    axes[0].set(title='Full range')
    axes[0].set_ylim(bottom=0)
    axes[1].set(title='Detail view')
    axes[1].set_ylim(*focus)
    fig.tight_layout()
    return fig, axes

fig, axes = temperature_context(['Mon', 'Tue', 'Wed'], [19, 20, 21])
