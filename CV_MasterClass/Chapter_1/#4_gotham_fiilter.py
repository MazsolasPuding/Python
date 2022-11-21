from PIL import Image
import numpy as np
import matplotlib.pylab as plt

im = Image.open ('../Pics/winnie.jpeg') #  Assumed pixel values in [0, 255]
print(np.max(im))

# 1-d interpolatipon with numpy
