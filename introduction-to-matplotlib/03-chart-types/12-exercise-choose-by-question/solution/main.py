import matplotlib.pyplot as plt

def neighborhood_view(question, names, values):
    fig, ax = plt.subplots()
    if question == "compare":
        ax.barh(names, values)
    elif question == "distribution":
        ax.hist(values, bins=3)
    return fig, ax

fig, ax = neighborhood_view("compare", ["Central", "East", "West"], [45, 21, 37])
