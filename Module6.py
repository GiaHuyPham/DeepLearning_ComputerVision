"""
Read Video
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

source = "race_car.mp4"

vid = cv2.VideoCapture(source)

# Read and display one frame
has_frame,frame = vid.read()
frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(frame_rgb)

# Display a wholde video
window_name = "Video Display"
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
fps = vid.get(cv2.CAP_PROP_FPS)
print(f"The video frame rate is {fps} Hz")

vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

while has_frame:
    cv2.imshow(window_name,frame)
    
    # waitkey is required to update frame
    key = cv2.waitKey(np.uint8(1/fps * 10**3))
    
    # Press esc to exit
    if key == 27:
        break
    
    has_frame,frame = vid.read()
    


""" Writing a video

Function syntax:
    object = cv2.VideoWriter(filename, fourcc, fps, frameSize)

- fourcc: 4-character code used to compress the frames
- fps: Framerate of the converted video 
- frameSize: Output size of the video
"""
# Get properties BEFORE any release

frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output paths
out_put_avi_path = "race_car_saved.avi"
out_put_mp4_path = "race_car_saved.mp4"

# Initialize writers only if files don't exist
out_avi = None
out_mp4 = None

if not os.path.exists(out_put_avi_path):
    out_avi = cv2.VideoWriter(
        out_put_avi_path,
        cv2.VideoWriter_fourcc(*'MJPG'),
        fps,
        (frame_width, frame_height)
    )
else:
    print("AVI file already exists")

if not os.path.exists(out_put_mp4_path):
    out_mp4 = cv2.VideoWriter(
        out_put_mp4_path,
        cv2.VideoWriter_fourcc(*'avc1'),
        30.0,
        (frame_width, frame_height)
    )
else:
    print("MP4 file already exists")

# Display + write loop
window_name = "Video Display"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

delay = np.uint8(1/fps * 10**3)
vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

while True:
    has_frame, frame = vid.read()
    if has_frame:
        out_mp4.write(frame)
        cv2.imshow(window_name,frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Cleanup
vid.release()
if out_avi is not None:
    out_avi.release()
if out_mp4 is not None:
    out_mp4.release()

cv2.destroyAllWindows()

print("Video processing finished.")