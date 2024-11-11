import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# x = [1, 1, 2, 3, 5, 7, 3, 4, 2, 8, 20, 12, 3, 4]
# y = [15, 12, 3, 4, 4, 3, 1, 2, 6, 11, 1, 9, 8, 9]
# z = [3, 1, 3, 4, 2, 16, 11, 3, 2, 7, 4, 6, 4, 5]

# print(len(x), len(y),len(z))

# Load and format data
# dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
counties = pd.read_csv("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\uscounties.csv")
fname = cbook.get_sample_data("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\uscounties.csv", asfileobj=False)
# with cbook.get_sample_data("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\uscounties.csv") as file:
#     counties = pd.read_csv(file)
print('len of original counties data: ', len(counties))

continental = counties[(counties['state_id'] != 'HI')]

print('len of no hawaii data: ', len(continental))
# couldn't write an and statement that would process both queries at once so hacking it this way
continental = continental[(continental['state_id'] != 'AK')]
print('len of no alaska data: ', len(continental))

# sanity check
alaska = counties[(counties['state_id'] == 'AK')]
hawaii = counties[(counties['state_id'] == 'HI')]
print(f'alaska len: {len(alaska)}, hawaii len: {len(hawaii)}')
print(f'our data reduced the right number: {len(alaska) + len(hawaii) == len(counties) - len(continental)}')

total_continental_pop = sum(continental['population'])
print('continental us population: ', total_continental_pop)
# print(continental.tail()) # smallest county is Loving with 96
max_lat = max(continental['lat'])
min_lat = min(continental['lat'])
max_lng = max(continental['lng'])
min_lng = min(continental['lng'])
sum_lat = sum(continental['lat'])
sum_lng = sum(continental['lng'])
mean_lat = sum_lat / len(continental)
mean_lng = sum_lng / len(continental)
norm_lat_range = [min_lat - mean_lat, max_lat - mean_lat]
norm_lng_range = [min_lng - mean_lng, max_lng - mean_lng]
print(f'lat: [{min_lat}, {max_lat}] and lng: [{min_lng}, {max_lng}]')
print(f'norm lat: {norm_lat_range}, norm lng: {norm_lng_range}')
normalized_data = continental
normalized_data['lat'] = normalized_data['lat'] - mean_lat
normalized_data['lng'] = normalized_data['lng'] - mean_lng
print('normalized_data', normalized_data)
# for index, row in normalized_data.iterrows():
#     print('hi!', row['lat'], row['lng'])

# before norm, Los Angeles County was latlng 34.3219 -118.2247
# after normalization it is -3.959429 -26.566142  

# write normalized data to new csv file
# you can't write both of these at once, since the normalized data IS the continental data, it's a reference
# if you want to create the continental data just comment out lines 49-52 and swap these two
# continental.to_csv('C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-us-data.csv') 
# normalized_data.to_csv('C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-normalized.csv') 

# data_rate = 281 / 3144 # kb per 3144 csv entries
# z = counties['population']
# total_pop = sum(z)
# print('total pop: ', sum(z))
# print('pop div 50: ', total_pop//50)
# x = counties['lat']
# y = counties['lng']
# # nrows, ncols = z.shape
# # x = np.linspace(counties['lat'], counties['lat'], ncols)
# # y = np.linspace(counties['lng'], counties['lng'], nrows)
# print('x', x)
# print('y', y)
# print('z', z)
# # x, y = np.meshgrid(x, y)

# # region = np.s_[5:50, 5:50]
# # x, y, z = x[region], y[region], z[region]

# # # Set up plot
# # fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

# # ls = LightSource(270, 45)
# # # To use a custom hillshading mode, override the built-in shading and pass
# # # in the rgb colors of the shaded surface calculated from "shade".
# # rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
# # surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
# #                        linewidth=0, antialiased=False, shade=False)

# # plt.show()