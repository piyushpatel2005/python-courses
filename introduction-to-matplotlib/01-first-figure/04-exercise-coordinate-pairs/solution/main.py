import matplotlib.pyplot as plt

def reading_room(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts)
    return fig

fig = reading_room([9, 11, 15], [4, 10, 6])
plt.show()
