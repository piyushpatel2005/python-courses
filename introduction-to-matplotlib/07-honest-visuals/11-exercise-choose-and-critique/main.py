import matplotlib.pyplot as plt

def review_charts(branches, visits, temperatures, visitors):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
    axes[0].set_title('Library branches')
    axes[1].set_title('Garden days and visitors')
    fig.tight_layout()
    return fig, axes

fig, axes = review_charts(['East','West'], [52,84], [17,20,23], [30,39,36])
