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

files = os.scandir("dynamic_block")

total_count_start = 1
total_count_stop = 1


for file in tqdm(files):
    # name = file.name()
    
    cap = cv2.VideoCapture("dynamic_block/"+file.name)
    # print(cap.get(7))   # gets the number of frames in float
    num_frame = int(cap.get(7))
    
    if cap.isOpened():
        # for the punch start phase
        cap.set(1,0)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_start/block_start"+str(total_count_start)+".jpg",frame)
        total_count_start = total_count_start+1
        cap.set(1,1)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_start/block_start"+str(total_count_start)+".jpg",frame)
        total_count_start = total_count_start+1
        cap.set(1,2)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_start/block_start"+str(total_count_start)+".jpg",frame)
        total_count_start = total_count_start+1
        
        
        # for the punch stop phase
        cap.set(1,num_frame-4-1)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_stop/block_stop"+str(total_count_stop)+".jpg",frame)
        total_count_stop = total_count_stop+1
        cap.set(1,num_frame-4-2)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_stop/block_stop"+str(total_count_stop)+".jpg",frame)
        total_count_stop = total_count_stop+1
        cap.set(1,num_frame-4-3)
        ret, frame = cap.read()
        cv2.imwrite("dynamic_block_stop/block_stop"+str(total_count_stop)+".jpg",frame)
        total_count_stop = total_count_stop+1
            
            


    cap.release()

