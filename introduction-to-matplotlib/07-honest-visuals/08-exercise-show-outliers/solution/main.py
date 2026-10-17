import matplotlib.pyplot as plt

def wait_views(waits, cutoff=20):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    axes[0].hist(waits, bins=5, color='#347f9a', edgecolor='white')
    nearby = [w for w in waits if w <= cutoff]
    axes[1].hist(nearby, bins=5, color='#347f9a', edgecolor='white')
    for ax in axes:
        ax.set(xlabel='Wait (minutes)', ylabel='Observations')
    axes[0].set_title('All waits')
    axes[1].set_title(f'Detail ≤ {cutoff} min; {len(waits)-len(nearby)} excluded')
    fig.tight_layout()
    return fig, axes

fig, axes = wait_views([2, 3, 6, 7, 12, 39])
