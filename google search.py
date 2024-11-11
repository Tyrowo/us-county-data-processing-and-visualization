import matplotlib.pyplot as plt
import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D

# Load the image
image = cv2.imread('C:\\Users\\tycre\\Desktop\\00. pics of me\\profpic_2024-05-13.jpg')

# Create 3D data (replace with your own data)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D data
ax.scatter(x, y, z, c='r', marker='o')

# Display the image as a background
ax.imshow(image, aspect='auto', extent=[x.min(), x.max(), y.min(), y.max()], zorder=0)

# Set the title
ax.set_title('3D Data Overlay')

# Show the plot
plt.show()