import cv2 as cv

img = cv.imread('C:/Users/horva/Pictures/canvas.png')

cv.imshow('Cat', img)

capture = cv.VideoCapture('C:/Users/horva/Pictures/pexels-cottonbro-5532773.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)