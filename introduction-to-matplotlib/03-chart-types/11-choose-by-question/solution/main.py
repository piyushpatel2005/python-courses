import matplotlib.pyplot as plt

def choose_view(question, names, values):
    fig, ax = plt.subplots()
    if question == "compare":
        ax.bar(names, values)
    elif question == "distribution":
        ax.hist(values, bins=3)
    return fig, ax

fig, ax = choose_view("distribution", ["North", "South", "East"], [3, 8, 5])
