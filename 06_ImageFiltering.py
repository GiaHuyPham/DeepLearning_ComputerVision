"""
Image Filtering
"""

import cv2
import os
import sys
import numpy as np

PREVIEW = 0 # No filter
BLUR = 1 # 
EDGE = 2
CORNER = 3

# Define parameters for corners detection
feature_params = dict(maxCorners = 500,
                      qualityLevel = 0.2, # threshold value for a pixel to be a corner. thres_val = max_pixel*qualityLevel
                      minDistance = 15,
                      blockSize = 9)

"""Live Video Recording with Filter"""
# Create camera object
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

cam = cv2.VideoCapture(s)

# Create window display
window_name = "Camera Recording Display"
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)

image_filter = PREVIEW
live = True
while live:
    has_frame,frame = cam.read()
    frame_flip = cv2.flip(frame,1)
    if image_filter == PREVIEW:
        img_display = frame_flip
    elif image_filter == BLUR:
        img_display = cv2.blur(frame_flip,(25,25))
    elif image_filter == EDGE:
        img_display = cv2.Canny(frame_flip,threshold1=50,threshold2=150)
    elif image_filter == CORNER:
        img_display = frame_flip
        frame_gray = cv2.cvtColor(frame_flip,cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray,**feature_params)
        if corners is not None:
            for x,y in np.float32(corners).reshape(-1,2):
                cv2.circle(img_display,center=(int(x), int(y)),radius=10,color=(0,255,0),thickness=2)
    
    cv2.imshow(window_name,img_display)
    
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        live = False
    elif key == ord('B') or key == ord('b'):
        image_filter = BLUR
    elif key == ord('E') or key == ord('e'):
        image_filter = EDGE
    elif key == ord('C') or key == ord('c'):
        image_filter = CORNER
    elif key == ord('P') or key == ord('p'):
        image_filter = PREVIEW
        
        
cam.release()
cv2.destroyAllWindows()

