import matplotlib.pyplot as plt

def temperature_context(days, celsius, focus=(18, 22)):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    axes[0].set(title='Full range', xlabel='Day', ylabel='Temperature (°C)')
    axes[1].set(xlabel='Day', ylabel='Temperature (°C)')
    fig.tight_layout()
    return fig, axes

fig, axes = temperature_context(['Mon', 'Tue', 'Wed'], [19, 20, 21])
