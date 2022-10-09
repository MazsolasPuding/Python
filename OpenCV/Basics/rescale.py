import cv2 as cv

# img = cv.imread('C:/Users/horva/Pictures/abstract_cool_4k_hd.jpg')
# cv.imshow('Background', img)

def rescaleFrame(frame, scale=0.75):
    """Rescalles all sorts of frames: (image, video, live video)"""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    """Only rescales live video stream."""
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('C:/Users/horva/Pictures/pexels-cottonbro-5532773.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)

