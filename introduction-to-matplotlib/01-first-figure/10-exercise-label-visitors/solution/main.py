import matplotlib.pyplot as plt

def labeled_visits(days, visits):
    fig, ax = plt.subplots()
    ax.plot(days, visits)
    ax.set_xlabel("Day")
    ax.set_ylabel("Visitors")
    return fig

fig = labeled_visits([1, 2, 3], [18, 23, 21])
plt.show()
