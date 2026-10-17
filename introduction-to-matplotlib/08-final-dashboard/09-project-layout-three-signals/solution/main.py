import pandas as pd
import matplotlib.pyplot as plt


def build_dashboard(garden, library, transit):
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0,0].plot(garden['day'], garden['temp_c'], marker='o', color='#347f9a')
    axes[0,0].set(title='Garden temperature', xlabel='Day', ylabel='Temperature (°C)')
    branches = library.groupby('branch')['visits'].sum().sort_index()
    axes[0,1].bar(branches.index, branches.values, color='#e6a45c')
    axes[0,1].set(title='Library by branch', ylabel='Visits')
    axes[0,1].set_ylim(bottom=0)
    rides = transit.groupby('day')['rides'].sum().sort_index()
    axes[1,0].plot(rides.index, rides.values, marker='s', color='#7662a8')
    axes[1,0].set(title='Transit rides', xlabel='Day', ylabel='Rides')
    axes[1,1].set(title='Shared-day signals')
    fig.suptitle('Neighborhood Signals')
    fig.tight_layout()
    return fig, axes

garden = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02','2026-05-03','2026-05-04'], 'temp_c':[18,20,21,None,23]})
library = pd.DataFrame({'day':['2026-05-01','2026-05-02','2026-05-02','2026-05-04'], 'branch':['East','East','West','West'], 'visits':[38,40,31,47]})
transit = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02','2026-05-04'], 'route':['A','B','A','B'], 'rides':[55,32,70,61]})
fig, axes = build_dashboard(garden, library, transit)
