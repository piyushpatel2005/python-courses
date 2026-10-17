import pandas as pd
import matplotlib.pyplot as plt


def prepare_signals(garden, library, transit):
    garden_daily = garden.dropna(subset=['day','temp_c']).groupby('day', as_index=False)['temp_c'].mean().sort_values('day')
    valid_library = library.dropna(subset=['day','branch','visits'])
    branch_totals = valid_library.groupby('branch')['visits'].sum().sort_index()
    library_daily = valid_library.groupby('day', as_index=False)['visits'].sum()
    transit_daily = transit.dropna(subset=['day','route','rides']).groupby('day')['rides'].sum().sort_index()
    matched = garden_daily.merge(library_daily, on='day', how='inner')
    return garden_daily, branch_totals, transit_daily, matched

def build_dashboard(garden, library, transit):
    garden_daily, branches, rides, matched = prepare_signals(garden, library, transit)
    fig, axes = plt.subplots(2, 2, figsize=(11, 7))
    axes[0,0].plot(garden_daily['day'], garden_daily['temp_c'], marker='o', color='#347f9a', label='Daily mean')
    axes[0,0].set(title='Garden temperature', xlabel='Day', ylabel='Temperature (°C)')
    axes[0,0].legend()
    axes[0,1].bar(branches.index, branches.values, color='#e6a45c')
    axes[0,1].set(title='Library by branch', ylabel='Visits')
    axes[0,1].set_ylim(bottom=0)
    axes[1,0].plot(rides.index, rides.values, marker='s', color='#7662a8', label='Daily rides')
    axes[1,0].set(title='Transit rides', xlabel='Day', ylabel='Rides')
    axes[1,0].legend()
    axes[1,1].scatter(matched['temp_c'], matched['visits'], color='#347f9a', label='Shared days')
    axes[1,1].set(title='Garden and library on shared days', xlabel='Temperature (°C)', ylabel='Visits')
    axes[1,1].legend()
    fig.suptitle('Neighborhood Signals')
    fig.tight_layout()
    return fig, axes

garden = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02','2026-05-03','2026-05-04'], 'temp_c':[18,20,21,None,23]})
library = pd.DataFrame({'day':['2026-05-01','2026-05-02','2026-05-02','2026-05-04'], 'branch':['East','East','West','West'], 'visits':[38,40,31,47]})
transit = pd.DataFrame({'day':['2026-05-01','2026-05-01','2026-05-02','2026-05-04'], 'route':['A','B','A','B'], 'rides':[55,32,70,61]})
fig, axes = build_dashboard(garden, library, transit)
