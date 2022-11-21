from gettext import npgettext
import skvideo.io
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu, threshold_local

# Read video
input_parameters = {}
output_parameters = {}
reader = skvideo.io.FFmpegReader('../Pics/horvada.mov',
    inputdict=input_parameters,
    outputdict=output_parameters)

num_frames, height, width, num_chanels = reader.getShape()
print(num_frames, height, width, num_chanels)

# Display 4 random frames
plt.figure(figsize=(20,10))
frame_list = np.random.choice(num_frames, 4)
frame_cnt, subplot_cnt = 0, 1
for frame in reader.nextFrame():
    if frame_cnt in frame_list:
        plt.subplot(2,2,subplot_cnt)
        plt.imshow(frame)
        plt.title("Frame {}".format(frame_cnt), size=20)
        plt.axis('off')
        subplot_cnt += 1
    frame_cnt += 1
plt.tight_layout()
plt.show()

def global_thresh():
    # Global Threshold to create binary images
    writer = skvideo.io.FFmpegWriter("../Pics/horvada_binary.mov",
        outputdict={})

    for frame in skvideo.io.vreader("../Pics/horvada.mov"):
        frame = rgb2gray(frame)
        thresh = threshold_otsu(frame)
        binary = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
        binary[..., 0] = binary[..., 1] = binary[..., 2] = 255*(frame > thresh).astype(np.uint8)
        writer.writeFrame(binary)
    writer.close()

def local_thresh():
    # Global Threshold to create binary images
    writer = skvideo.io.FFmpegWriter("../Pics/horvada_binary.mov",
        outputdict={})

    for frame in skvideo.io.vreader("../Pics/horvada.mov"):
        frame = rgb2gray(frame)
        block_size = 5
        thresh = threshold_local(frame, block_size, offset=10)
        # print(thresh)
        binary = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
        binary[..., 0] = binary[..., 1] = binary[..., 2] = 255*(frame > thresh).astype(np.uint8)
        writer.writeFrame(binary)
    writer.close()

global_thresh()
