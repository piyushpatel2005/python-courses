import matplotlib.pyplot as plt

def transit_ranking(stops, boardings):
    fig, ax = plt.subplots()
    ax.plot(boardings, stops, color="lightgray")
    # Replace the line with bars that run horizontally.
    return fig, ax

fig, ax = transit_ranking(["Harbor Terminal", "Elm Street"], [61, 38])
