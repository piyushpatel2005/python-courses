import pandas as pd
import matplotlib.pyplot as plt

def daily_transit(frame):
    return frame[['day','rides']].copy()

def plot_transit(frame):
    fig, ax = plt.subplots()
    ax.set(title='Daily transit use', xlabel='Day')
    return fig, ax

transit = pd.DataFrame({'day':['01','01','02','02'], 'route':['A','B','A','B'], 'rides':[55,31,64,None]})
fig, ax = plot_transit(transit)
