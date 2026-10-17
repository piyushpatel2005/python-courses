import pandas as pd
import matplotlib.pyplot as plt

def accessible_routes(frame):
    fig, ax = plt.subplots()
    ax.plot(frame['day'], frame['east'], marker='o', linestyle='-', color='#205c8a', label='East route')
    ax.plot(frame['day'], frame['west'], marker='s', linestyle='--', color='#a54f42', label='West route')
    ax.set(xlabel='Day', ylabel='Rides', title='Transit routes')
    ax.legend()
    return fig, ax

routes = pd.DataFrame({'day':['Mon','Tue','Wed'], 'east':[12,16,14], 'west':[8,11,13]})
fig, ax = accessible_routes(routes)
