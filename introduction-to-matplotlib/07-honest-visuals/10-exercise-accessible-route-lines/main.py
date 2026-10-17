import pandas as pd
import matplotlib.pyplot as plt

def accessible_routes(frame):
    fig, ax = plt.subplots()
    ax.set(xlabel='Day', ylabel='Rides', title='Transit routes')
    return fig, ax

routes = pd.DataFrame({'day':['Mon','Tue','Wed'], 'east':[12,16,14], 'west':[8,11,13]})
fig, ax = accessible_routes(routes)
