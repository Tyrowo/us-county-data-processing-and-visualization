
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# need to use the not normalized data so the latlng isn't bunched so hard
continental_us_data = pd.read_csv("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-us-data.csv")

# display 
# # ax = plt.axes(projection="3d")
# x and y ened to be reversed, lat is flat but the measurement of latitude is the height of the position
y = continental_us_data['lat'].to_list()
x = continental_us_data['lng'].to_list()
z = continental_us_data['population'].to_list()
X, Y = np.meshgrid(x, y)
Z = np.array(z)
# print('x - lng', x)
# print('y - lat', y)
# print('z - pop', z)
# z[0] = z[1] # testing what it looks like without LA County, since it has twice the population of anyone else
# for i in range(0, 25): # testing what it looks like with the biggest 5 counties reduced (bringing down to 320k maxpop)
    # z[i] = z[25]
# after testing 1, 5, 25, 50, I think 25 is the best. after 50 it becomes a bunch of spikes

# from normalization, we found lat and lng min and maxes:
# lat: [25.3192, 48.8259] and lng: [-124.1568, -67.6287]
lat_dist = 48.8259 - 25.3192
lng_dist = 124.1568 - 67.6287
# print('distances: ', lat_dist, lng_dist)

fig = plt.figure(figsize=(lng_dist, lat_dist))
# plt.gca().set_aspect('equal') 
ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z)
# plt.tight_layout()
# plt.axes(projection='3d')
# plt.scatter(x, y, marker='.')
# ax.scatter(X, Y, Z, marker='.')
# instead of scatter we want a trisurface, trisurface is when you have 3 lists
# as opposed to meshgrid which uses two vectors as a meshgrid and a z function
# #56a0d3 = carolina blue, #000080 = navy, alpha is transparency, linewidths should be small because there's a lot
ax.plot_trisurf(x,y,z, color='#56a0d3', edgecolors='#000080', alpha=0.4, linewidths=0.05)
# ax.scatter(x,y,z, c='white', alpha = 0.05, marker='.')
# Add labels and title
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
ax.set_zlabel('population')
# plt.plot(x, y, markersize=2, linestyle='None')
plt.show() 