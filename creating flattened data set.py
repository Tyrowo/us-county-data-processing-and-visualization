import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from matplotlib import cbook, cm

print('starting')
# get the data
continental_us_data = pd.read_csv("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-normalized.csv")

flattened_data_list = []
# take every line of the counties, and break them apart
for index, row in continental_us_data.iterrows():
    county, pop, lat, lng = row['county'], row['population'], row['lat'], row['lng']
    rounded_pop = round(pop / 250) # data analysis led to a decision to round to nearest 250
    # breaking down each population into data points of 100 takes a long time, so need some logging
    print(f'breaking down population of county at i={index}, {county} : |', end = '')
    for i in range(rounded_pop):
        ten_percent = round(rounded_pop / 10)
        if ten_percent > 0 and i % ten_percent == 0:
            print(f' . ', end='')
        flattened_data_list.append([lat, lng])
        
    print(f'| added {rounded_pop} lines')

print(f'data has been flattened into a matrix of {len(flattened_data_list)} rows')
print(' ')
print('shuffling data')
random.shuffle(flattened_data_list)
print('second shuffle')
random.shuffle(flattened_data_list)
print(' ')
print('creating dataframe with matrix input. good luck!')
flat_df = pd.DataFrame(flattened_data_list, columns=['lat', 'lng'])
print('df created successfully')
print(' ')
# and write it to the output
print('writing. prayge')
flat_df.to_csv('C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-flattened.csv')
print('successfully wrote new dataset')