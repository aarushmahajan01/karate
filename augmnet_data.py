import cv2
import numpy


def get_fourcc(cap):
    ''' 
        This function takes in a video capture object and return the 
        fourcc code of the video
    '''
    h = int(828601953.0)
    fourcc = chr(h&0xff) + chr((h>>8)&0xff) + chr((h>>16)&0xff) + chr((h>>24)&0xff) 
    print(fourcc)
    return fourcc


# 4 6 8 10
cap = cv2.VideoCapture('left_hand_block/lhb_1.mp4')
# fourcc = get_fourcc(cap)
fps = cap.get(5)# get the fps of the video
# out = cv2.VideoWriter('dp_1.mp4',cv2.VideoWriter_fourcc(*"mp4v"), fps, (480,640))

print(cap.get(7))   # gets the number of frames in float

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        frame = cv2.flip(frame,1)
        cv2.imshow('Frame',frame)

        # out.write(frame)
        
        print(cap.get(0),cap.get(1)) # get the current position in ms and the frame count in float

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
# out.release()

cv2.destroyAllWindows()