import pandas as pd
import matplotlib.pyplot as plt

def daily_garden(frame):
    return frame.dropna(subset=['temp_c']).groupby('day', as_index=False)['temp_c'].mean().sort_values('day')

def garden_line(frame):
    daily = daily_garden(frame)
    fig, ax = plt.subplots()
    ax.plot(daily['day'], daily['temp_c'], marker='o', color='#347f9a')
    ax.set(title='Daily garden temperature', xlabel='Day', ylabel='Temperature (°C)')
    return fig, ax

garden = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02','2026-05-03'], 'temp_c':[18,20,None,21]})
fig, ax = garden_line(garden)
