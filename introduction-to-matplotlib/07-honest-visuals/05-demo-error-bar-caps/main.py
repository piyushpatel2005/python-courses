import matplotlib.pyplot as plt

def plot_estimates(days, averages, margins):
    fig, ax = plt.subplots()
    ax.errorbar(days, averages, yerr=margins, fmt='o-', capsize=0, color='#347f9a')
    ax.set(title='Garden sensor estimates', ylabel='Temperature (°C)', xlabel='Day')
    return fig, ax

fig, ax = plot_estimates(['Mon', 'Tue', 'Wed'], [19, 20, 21], [0.5, 0.8, 0.4])
