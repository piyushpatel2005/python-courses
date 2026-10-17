import matplotlib.pyplot as plt

def review_charts(branches, visits, temperatures, visitors):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
    axes[0].bar(branches, visits, color='#347f9a')
    axes[0].set(title='Library branches', ylabel='Visits')
    axes[0].set_ylim(bottom=0)
    axes[1].scatter(temperatures, visitors, color='#a54f42')
    axes[1].set(title='Garden days and visitors', xlabel='Temperature (°C)', ylabel='Visitors')
    fig.tight_layout()
    return fig, axes

fig, axes = review_charts(['East','West'], [52,84], [17,20,23], [30,39,36])
