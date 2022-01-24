#BUSE AYYILDIZ 150170099

import math
import moviepy.video.io.VideoFileClip as mpy
import cv2
import moviepy.editor as mpy
import cv
import numpy as np


arr = []
#part1.1
vid = mpy.VideoFileClip('shapes_video.mp4')
frame_count = vid.reader.nframes
video_fps = vid.fps

for i in range(frame_count):
    frame = vid.get_frame(i*1.0/video_fps)
    median = cv2.medianBlur(frame, 5)
    arr.append(median)





clip = mpy.ImageSequenceClip(arr, fps=25)
clip.write_videofile('part1_video.mp4', codec='libx264')

#part1.2
