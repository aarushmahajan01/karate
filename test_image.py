''''
This fiel takes in the video as generates the two classes of images 
ie that is the start and the stop of a particular action
But the frame vlaues are hard coded
'''

import cv2
import numpy
from tqdm import tqdm
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles
import os

from pose_tranformer import FullBodyPoseEmbedder




cap = cv2.VideoCapture("Double_Punch/dp_1.mp4")
# print(cap.get(7))   # gets the number of frames in float
num_frame = int(cap.get(7))

if cap.isOpened():
    # for the punch start phase
    cap.set(1,38)
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    cv2.waitKey(0)



cap.release()

