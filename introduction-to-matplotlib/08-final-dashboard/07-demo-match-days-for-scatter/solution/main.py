import pandas as pd
import matplotlib.pyplot as plt

def paired_days(garden, library):
    return garden.merge(library, on='day', how='inner')

def paired_plot(garden, library):
    pairs = paired_days(garden, library)
    fig, ax = plt.subplots()
    ax.scatter(pairs['temp_c'], pairs['visits'], color='#347f9a')
    ax.set(title='Matched garden and library days', xlabel='Temperature (°C)', ylabel='Visits')
    return fig, ax

garden = pd.DataFrame({'day':['01','02','03'], 'temp_c':[18,20,22]})
library = pd.DataFrame({'day':['03','01','04'], 'visits':[42,30,99]})
fig, ax = paired_plot(garden, library)
