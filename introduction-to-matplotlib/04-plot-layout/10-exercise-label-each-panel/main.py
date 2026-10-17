import matplotlib.pyplot as plt

def community_panels(days, beds, visits):
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(days, beds)
    axes[1].plot(days, visits)
    # Give each panel its own title and vertical unit label.
    return fig, axes

fig, axes = community_panels([1, 2, 3], [4, 6, 5], [32, 41, 36])
