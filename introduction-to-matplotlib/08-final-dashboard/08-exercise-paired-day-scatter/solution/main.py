import pandas as pd
import matplotlib.pyplot as plt

def match_signals(garden, library):
    totals = library.groupby('day', as_index=False)['visits'].sum()
    return garden[['day','temp_c']].merge(totals, on='day', how='inner')

def signal_scatter(garden, library):
    pairs = match_signals(garden, library)
    fig, ax = plt.subplots()
    ax.scatter(pairs['temp_c'], pairs['visits'], color='#347f9a')
    ax.set(title='Matched garden and library days', xlabel='Temperature (°C)', ylabel='Visits')
    return fig, ax

garden = pd.DataFrame({'day':['01','02','03'], 'temp_c':[18,20,22]})
library = pd.DataFrame({'day':['02','01','02'], 'visits':[31,24,12]})
fig, ax = signal_scatter(garden, library)
