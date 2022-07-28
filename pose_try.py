import cv2
import numpy as np
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles

from pose_tranformer import FullBodyPoseEmbedder



cap = cv2.VideoCapture('Double_punch/dp_1.mp4')


with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=2) as pose:
 
    
    while cap.isOpened():
        ret,frame = cap.read()
        
        if ret:
            if int(cap.get(1))%2==0:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                results = pose.process(frame)
                
                mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                cv2.imshow("win",frame)
                cv2.waitKey(1)
        else:
            break

cv2.destroyAllWindows()
        