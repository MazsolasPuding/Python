import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# 1. Paint the pixels to one color
blank[:] = 0,255,0
# cv.imshow('green', blank)
blank[:] = 0,0,255
# cv.imshow('red', blank) # BGR
blank[:] = 0,0,0
blank[100:150, 200:300] = 123,222,12
blank[200:400, 150:350] = 123,112,200
blank[150:250, 225:275] = 230,112,130
cv.imshow('Rectangles', blank)

# 2. Draw Rectangles
blank[:] = 0,0,0


cv.waitKey(0)
