import matplotlib.pyplot as plt

def marked_visits(hours, visits):
    fig, ax = plt.subplots()
    ax.plot(hours, visits, marker="D")
    return fig

fig = marked_visits([10, 12, 14], [8, 15, 11])
plt.show()
