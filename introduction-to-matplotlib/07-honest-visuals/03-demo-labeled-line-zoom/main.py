import matplotlib.pyplot as plt

def temperature_detail(days, celsius):
    fig, ax = plt.subplots()
    ax.plot(days, celsius, marker='o', color='#347f9a')
    ax.set_ylim(18, 22)
    ax.set(title='Garden temperature', xlabel='Day', ylabel='Temperature (°C)')
    return fig, ax

fig, ax = temperature_detail(['Mon', 'Tue', 'Wed'], [19.2, 20.0, 20.4])
