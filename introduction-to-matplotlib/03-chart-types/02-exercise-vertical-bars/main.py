import matplotlib.pyplot as plt

def library_bars(branches, visits):
    fig, ax = plt.subplots()
    ax.plot(branches, visits, color="lightgray")
    # Replace this line with bars and label their values axis.
    return fig, ax

fig, ax = library_bars(["Central", "West", "South"], [42, 28, 33])
