import matplotlib.pyplot as plt

def route_compare(days, east, west):
    fig, ax = plt.subplots()
    ax.plot(days, east, color='#205c8a', marker='o', linestyle='-', label='East route')
    ax.plot(days, west, color='#a54f42', marker='s', linestyle='--', label='Series 2')
    ax.set(xlabel='Day', ylabel='Rides', title='Transit by route')
    ax.legend()
    return fig, ax

fig, ax = route_compare(['Mon', 'Tue', 'Wed'], [12, 16, 14], [8, 11, 13])
