import matplotlib.pyplot as plt

def labeled_visits(days, visits):
    fig, ax = plt.subplots()
    ax.plot(days, visits)
    # Give each axis its own label.
    return fig

fig = labeled_visits([1, 2, 3], [18, 23, 21])
plt.show()
