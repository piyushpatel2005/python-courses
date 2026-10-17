import matplotlib.pyplot as plt

def route_ranking(routes, riders):
    fig, ax = plt.subplots()
    ax.barh(routes, riders, color="steelblue")
    ax.set_xlabel("Trips")
    return fig, ax

fig, ax = route_ranking(["Cedar Station", "Market Square"], [34, 52])
