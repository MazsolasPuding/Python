import cv2
import matplotlib.pyplot as plt

vc = cv2.VideoCapture(0)
plt.ion()
if vc.isOpened():  # Try to get the first frame
    is_capturing, frame = vc.read()
    webcam_preview = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
else:
    is_capturing = False

frame_indx = 1
while is_capturing:
    if frame_indx > 10: break
    is_capturing, frame = vc.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    webcam_preview.set_data(image)
    plt.title('Frame {0:d} '.format(frame_indx))
    plt.draw()
    frame_indx += 1

try:  # Avoid NotImplementedError caused by 'plt.pause'
    plt.pause(5)
except Exception:
    pass
vc.release()


# Why does it show a still frame?
# Write out the captured video!
# plt.draw?
