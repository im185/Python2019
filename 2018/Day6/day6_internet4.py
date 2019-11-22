import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure
from scipy.spatial import distance
from scipy.ndimage.measurements import label


file = open("input.txt", "r")
lines = file.readlines()


# Cleaning function
def cleaning_line(line):
    line = list(map(int, line.split(",")))
    return line

# Get coordinates into a data frame
coordinates = []
for line in lines:
    line = cleaning_line(line)
    coordinates.append(line)

coordinates = pd.DataFrame(coordinates)
coordinates.index += 1
coordinates.columns = ["x_axis", "y_axis"]
coordinates.head()


# Places matrix
max_x = coordinates.x_axis.max()+1
max_y = coordinates.y_axis.max()+1
places = np.zeros((max_x, max_y))


# Function to get closest coordinate to a point using Manhattan distance 
def get_min_dist(incoming_coord):
    dist = {}
    for coordinate in coordinates.iterrows():
        coord = coordinate[0]
        x = coordinate[1][0]
        y = coordinate[1][1]
        dist[coord] = distance.cityblock(incoming_coord, (x,y))
    min_value = min(dist.values())
    min_keys = [k for k in dist if dist[k] == min_value]
    if len(min_keys)>1:
        return -1 # Location is equally far from two or more coordinates
    else: 
        return min_keys[0]


# Fill places matrix
for x in range(0,max_x):
    for y in range(0,max_y):
        coord = (x,y)
        places[x,y] = get_min_dist(coord)


# Let's see the places just for fun
figure(figsize=(7, 7))
plt.imshow(places, cmap="Greens")
plt.title("Places")
plt.show()


# Values that tend to infinity
edges = np.unique(list(places[0, :])+list(places[1:, -1])+list(places[-1, :-1])+list(places[1:-1, 0]))

largest_area = 0
frequencies = np.unique(places, return_counts=True)
for (coordinate, size) in zip(frequencies[0],frequencies[1]):
    if coordinate not in edges:
        if size>largest_area:
            largest_area=size
print('fin!', largest_area);

