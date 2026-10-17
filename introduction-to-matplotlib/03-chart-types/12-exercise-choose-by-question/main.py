import matplotlib.pyplot as plt

def neighborhood_view(question, names, values):
    fig, ax = plt.subplots()
    if question == "compare":
        ax.plot(values, names, color="lightgray")
    elif question == "distribution":
        ax.plot(values, [0] * len(values), marker="o", linestyle="")
    return fig, ax

fig, ax = neighborhood_view("compare", ["Central", "East", "West"], [45, 21, 37])
