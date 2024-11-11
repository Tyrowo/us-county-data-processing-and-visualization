import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

continental_us_data = pd.read_csv("C:\\Users\\tycre\Desktop\\10.python\\ml project\\data vis\\continental-normalized.csv")

# need to perform some data analysis on this dataset

# population impact of rounding up 10,000, 5,000, and 2,500 - how much population have we "created" by rounding up to one data point
impact_10k = 0
impact_5k = 0
impact_2p5k = 0
n_10 = 0
n_5 = 0
n_25 = 0
e_10 = 0
e_5 = 0
e_25 = 0
excl_pop_10 = 0
excl_pop_5 = 0
excl_pop_25 = 0
map_10 = {}
map_5 = {}
map_25 = {}

# prefix sum
prefix = []
cur_pop = 0

for index, row in continental_us_data.iterrows():
    county, state, pop, lat, lng = row['county'], row['state_name'], row['population'], row['lat'], row['lng']
    cur_pop += pop
    prefix.append(cur_pop)
    if pop < 1000:
        impact_10k += 1000 - pop
        map_10[state] = 1000 - pop + map_10.get(state, 0)
        n_10 += 1
    if pop < 500:
        impact_5k += 500 - pop
        map_5[state] = 500 - pop + map_5.get(state, 0)
        n_5 += 1
        e_10 += 1
        excl_pop_10 += pop
    if pop < 250:
        impact_2p5k += 250 - pop
        map_25[state] = 250 - pop + map_25.get(state, 0)
        n_25 += 1
        e_5 += 1
        excl_pop_5 += pop
    if pop < 125:
        e_25 += 1
        excl_pop_25 += pop

# need a suffix sum just for the data visuals
n = len(prefix)
suffix = [0] * n
cur_pop = 0

for index, row in continental_us_data.iterrows():
    county, pop, lat, lng = row['county'], row['population'], row['lat'], row['lng']
    cur_pop += pop
    suffix[n - 1 - index] = cur_pop
for i in range(n -1, 0, -1):
    suffix[i] = prefix[n - 1] - prefix[i - 1] # formula for pop should be total pop - pop of everything before this

# calulate equal point from prefix sum [top x pop == bottom x pop]
# returns array where array[i] = the number of smallest counties that it takes to add up to the top i+1 cities
# i.e. the point where the suffix sum adds up to the prefix 
# two pointer will be easy enough to solve this
breakpoints = [0] * n
right = n - 1
def binary_search(l, r, target):
    while l <= r:
        mid = (r - l)//2 + l
        if suffix[mid] == target:
            return mid
        elif suffix[mid] < target:
            # if less than the target then we need to add more so move the right pointer
            r = mid - 1
        else:
            l = mid + 1
    return l - 1
for left in range(n):
    if right < left:
        break
    if right > 0 and suffix[right] < prefix[left]:
        # saving a little time with binary search so it doesn't take thousands of iterations to get through the first couple
        # right -= 1
        # print('hi', suffix[right], prefix[left])
        right = binary_search(left, right, prefix[left])
    breakpoints[left] = n - right


# boolean - does the equal point support going for 10,000 (assumed too much) 5,000, or 2,500
# which equal point? let's look at it real quick
print('pre', prefix[0:20])
print('suf', suffix[0:20])
print('breakpoints', breakpoints[0:20])

print(' ')
print(f'total pop is {suffix[0]}')
print(f'pop impacts : ( 10k, {impact_10k} people invented in {n_10} counties, {round(impact_10k/suffix[0] * 100, 4)}% of pop), ( 5k, {impact_5k} people invented in {n_5} counties, {round(impact_5k/suffix[0] * 100, 4)}% of pop), ( 2.5k, {impact_2p5k} people invented in {n_25} counties, {round(impact_2p5k/suffix[0] * 100, 4)}% of pop)')
# print(f'exclusions: rounding down would exclude x counties for [10k: {e_10}], [5k: {e_5}], [2.5k: {e_25}]')
print(f'excl impacts:  ( 10k, {excl_pop_10} people excluded in {e_10} counties, {round(excl_pop_10/suffix[0] * 100, 4)}% of pop), ( 5k, {excl_pop_5} people excluded in {e_5} counties, {round(excl_pop_5/suffix[0] * 100, 4)}% of pop), ( 2.5k, {excl_pop_25} people excluded in {e_25} counties, {round(excl_pop_25/suffix[0] * 100, 4)}% of pop)')
print('num counties = ', n)
print('')
print('total data:')
print(f'10k: {suffix[0] // 1000}, 5k: {suffix[0] // 500}, 2500: {suffix[0] // 250}, 100: {suffix[0] // 100}')

# breakpoint examples
print(' ')
print(f'the top 10 counties in population have more people than the smallest {breakpoints[9]} counties combined')
print(f'LA has more people than the smallest {breakpoints[0]} counties combined')
# print(' ')
# print(len(map_10), 'states impacted at 10k')
# print(map_10)
# print(len(map_5), 'states impacted at 5k')
# print(map_5)
# print(len(map_25), 'states impacted at 2.5k')
# print(map_25)


""" output:
pre [9936690, 15162057, 19888234, 24319105, 27608806, 30784033, 33472270, 36151890, 38755943, 41185430, 43546256, 45812182, 48066553, 50247116, 52360970, 54375029, 56315936, 58232767, 60014408, 61678231]
suf [328912183, 318975493, 313750126, 309023949, 304593078, 301303377, 298128150, 295439913, 292760293, 290156240, 287726753, 285365927, 283100001, 280845630, 278665067, 276551213, 274537154, 272596247, 270679416, 268897775]
breakpoints [1159, 1423, 1611, 1759, 1853, 1937, 2001, 2061, 2116, 2163, 2206, 2245, 2281, 2314, 2345, 2373, 2398, 2422, 2443, 2461]

total pop is 328912183
pop impacts : ( 10k, 3230781 people invented in 714 counties, 0.9823% of pop), ( 5k, 688926 people invented in 305 counties, 0.2095% of pop), ( 2.5k, 127139 people invented in 137 counties, 0.0387% of pop)
excl impacts:  ( 10k, 836074 people excluded in 305 counties, 0.2542% of pop), ( 5k, 215361 people excluded in 137 counties, 0.0655% of pop), ( 2.5k, 32282 people excluded in 42 counties, 0.0098% of pop)
num counties =  3109

total data:
10k: 32891, 5k: 65782, 2500: 131564, 100: 3289121

round 2, divide by 10
pop impacts : ( 1k, 10886 people invented in 33 counties, 0.0033% of pop), ( 500, 1331 people invented in 7 counties, 0.0004% of pop), ( 250, 322 people invented in 3 counties, 0.0001% of pop)
excl impacts:  ( 1k, 2169 people excluded in 7 counties, 0.0007% of pop), ( 500, 428 people excluded in 3 counties, 0.0001% of pop), ( 250, 212 people excluded in 2 counties, 0.0001% of pop)
num counties =  3109

total data:
1k: 328912, 500: 657824, 250: 1315648, 100: 3289121

the top 10 counties in population have more people than the smallest 2163 counties combined
LA has more people than the smallest 1159 counties combined

I believe that what I want to do is use the 250 per data set because it creates 1,315,648.
that's 1,000,000 data points to go into the model, and 15% of that that can go testing and 15% that can go into validation
it's about 59MB, too many data points to open in excel lol
but github will let you upload 59mb files as long as you do it from the command line so I'll figure that out.

we'll see if it's wieldy. might need to tone down to the 500 per model if it runs a little too slowly since we have to do
clustering models for 1 to 3109 counties
but idk something in me says having a million data points to represent the 300 million people in the country is right.

"""
