import pandas as pd
import matplotlib.pyplot as plt

def daily_transit(frame):
    return frame.dropna(subset=['day','route','rides']).groupby('day', as_index=False)['rides'].sum().sort_values('day')

def plot_transit(frame):
    daily = daily_transit(frame)
    fig, ax = plt.subplots()
    ax.plot(daily['day'], daily['rides'], marker='o', color='#7662a8')
    ax.set(title='Daily transit use', xlabel='Day', ylabel='Rides')
    return fig, ax

transit = pd.DataFrame({'day':['01','01','02','02'], 'route':['A','B','A','B'], 'rides':[55,31,64,None]})
fig, ax = plot_transit(transit)
