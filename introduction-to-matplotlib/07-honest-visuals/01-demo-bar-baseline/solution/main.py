import matplotlib.pyplot as plt

def draw_volunteers(counts):
    fig, ax = plt.subplots()
    ax.bar(['North', 'South'], counts, color='#347f9a')
    ax.set(title='Garden volunteers', ylabel='People')
    ax.set_ylim(bottom=0)
    return fig, ax

fig, ax = draw_volunteers([5, 8])
