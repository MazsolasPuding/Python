from skimage.io import imread
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def plot_3d(x, y, z, cmap='Reds', title=''):
    """
    This function plots 3D visualization of a channel.
    It displays (x,y,f(x,y)) for all x,y values.
    """
    # Setup
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(projection='3d')

    surf = ax.plot_surface(x, y, z, cmap=cmap, linewidth=0, 
        antialiased=False, rstride=2, cstride=2, alpha=0.5)
    ax.xaxis.set_major_locator(LinearLocator(10))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.view_init(elev=10., azim=5)
    ax.set_title(title, size=20)
    plt.show()

im = imread('~/Pictures/small.jpg')

Y = np.arange(im.shape[0])
X = np.arange(im.shape[1])
X, Y = np.meshgrid(X, Y)

Z1 = im[..., 0]
Z2 = im[..., 1]
Z3 = im[..., 2]

# plot 3D visualizations of the R, G, B channels of the image respectively
# Book Solution
# plot_3d(Z1, X, im.shape[1]-Y, cmap='Reds', title='3D plot of the red channel')
# plot_3d(Z2, X, im.shape[1]-Y, cmap='Greens', title='3D plot of the green channel')
# plot_3d(Z3, X, im.shape[1]-Y, cmap='Blues', title='3D plot of the blue channel')

plot_3d(X, im.shape[1]-Y, Z1, cmap='Reds_r', title='3D plot of the red channel')
plot_3d(X, im.shape[1]-Y, Z2, cmap='Greens_r', title='3D plot of the green channel')
plot_3d(X, im.shape[1]-Y, Z3, cmap='Blues_r', title='3D plot of the blue channel')