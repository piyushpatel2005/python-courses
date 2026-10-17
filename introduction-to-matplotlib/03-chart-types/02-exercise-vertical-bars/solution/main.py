import matplotlib.pyplot as plt

def library_bars(branches, visits):
    fig, ax = plt.subplots()
    ax.bar(branches, visits)
    ax.set_ylabel("Visits")
    return fig, ax

fig, ax = library_bars(["Central", "West", "South"], [42, 28, 33])
