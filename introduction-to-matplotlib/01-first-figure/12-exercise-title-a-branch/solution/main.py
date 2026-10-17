import matplotlib.pyplot as plt

def branch_figure(branch, days, visits):
    fig, ax = plt.subplots()
    ax.plot(days, visits)
    ax.set_xlabel("Day")
    ax.set_ylabel("Visitors")
    ax.set_title(f"{branch} visitors")
    return fig

fig = branch_figure("North", [1, 2, 3], [20, 27, 24])
plt.show()
