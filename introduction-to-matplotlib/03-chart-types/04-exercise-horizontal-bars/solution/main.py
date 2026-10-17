import matplotlib.pyplot as plt

def transit_ranking(stops, boardings):
    fig, ax = plt.subplots()
    ax.barh(stops, boardings)
    ax.set_xlabel("Boardings")
    return fig, ax

fig, ax = transit_ranking(["Harbor Terminal", "Elm Street"], [61, 38])
