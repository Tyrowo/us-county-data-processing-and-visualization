from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cbook import get_sample_data
from matplotlib.image import imread
fn = get_sample_data("C:\\Users\\tycre\\Desktop\\00. pics of me\\profpic_2024-05-13.jpg", asfileobj=False)
img = imread(fn)
x, y = ogrid[0:img.shape[0], 0:img.shape[1]]
ax = gca()
ax.plot_surface(x, y, 10, rstride=5, cstride=5, facecolors=img)
show()