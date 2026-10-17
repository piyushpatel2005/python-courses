import pandas as pd
import matplotlib.pyplot as plt

def garden_preview(garden, library, transit):
    fig, ax = plt.subplots()
    ax.plot(garden['day'], garden['temp_c'], marker='o', color='#347f9a')
    ax.set(title='Garden readings', xlabel='Day', ylabel='Temperature (°C)')
    return fig, ax

garden = pd.DataFrame({'day':['Mon','Tue','Wed'], 'temp_c':[18,20,19]})
library = pd.DataFrame({'day':['Mon','Tue','Wed'], 'branch':['East','West','East'], 'visits':[32,45,39]})
transit = pd.DataFrame({'day':['Mon','Tue','Wed'], 'route':['A','B','A'], 'rides':[81,74,89]})
fig, ax = garden_preview(garden, library, transit)
