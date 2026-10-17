import pandas as pd
import matplotlib.pyplot as plt

def transit_line(frame):
    daily = frame.groupby('day')['rides'].sum().sort_index()
    fig, ax = plt.subplots()
    ax.plot(daily.index, daily.values, marker='o', color='#7662a8')
    ax.set(title='Daily transit rides', xlabel='Day', ylabel='Rides')
    return fig, ax

transit = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02'], 'rides':[55,31,64]})
fig, ax = transit_line(transit)
