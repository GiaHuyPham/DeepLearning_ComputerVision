"""
Access Camera and Video Capturing
"""

import os
import sys
import cv2

s = 0 # default camera device index
if len(sys.argv) > 1:
    s = sys.argv[1] # check if 

# Access camera    
source = cv2.VideoCapture(s) # Camera object

# Create a display window
win_name = "Camera View"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: # Run until Esc key is pressed
    has_frame, frame = source.read()
    frame_flip = cv2.flip(frame,1)
    if not has_frame:
        break
    cv2.imshow(win_name,frame_flip)
    
source.release() # Delete camera object
cv2.destroyAllWindows()
