import pandas as pd
import matplotlib.pyplot as plt

def match_signals(garden, library):
    return garden[['day','temp_c']].copy()

def signal_scatter(garden, library):
    fig, ax = plt.subplots()
    ax.set(title='Garden and library', xlabel='Temperature (°C)', ylabel='Visits')
    return fig, ax

garden = pd.DataFrame({'day':['01','02','03'], 'temp_c':[18,20,22]})
library = pd.DataFrame({'day':['02','01','02'], 'visits':[31,24,12]})
fig, ax = signal_scatter(garden, library)
