"""
Basic Image Manipulation:

- Access and manipulate pixel
- Resizing image
- Cropping
- Flipping
"""

import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("checkerboard_18x18.png",0)
# Access pixel through matrix indexing
print(cb_img[0,0])
print(cb_img[0,6])

# Manipulate pixel value
cb_img[2,2] = 200
cb_img[2,3] = 200
cb_img[3,2] = 200
cb_img[3,3] = 200

plt.imshow(cb_img,cmap='gray')

# Cropping image <=> Matrix slicing
img_cropped = cb_img[6:11,6:11]
plt.imshow(img_cropped,cmap='gray')

"""
Image Resizing

Function syntax:
    dsize = cv2.resize(img,method)
- Method 1: scaling
    dsize = cv2.resize(img,none,fx=a,fy=b)
- Method 2: passing desired size
    dsize = cv2.resize(img,dsize=dim,interpolation=cv2.INTER_AREA)
- Method 3: resize with aspect ration

"""
# Method 1
img_cropped_scale = cv2.resize(img_cropped,dsize=None,fx=2,fy=2)
plt.imshow(img_cropped_scale,cmap='gray')

# Method 2
dwidth = 100
dheight = 200
dim = [dheight,dwidth]
img_cropped_res = cv2.resize(img_cropped,dsize=dim)
plt.imshow(img_cropped_res,cmap='gray')

# Method 3
dwidth = 100
ratio = img_cropped.shape[0]/img_cropped.shape[1];print(ratio)
dheight_ratio = int(ratio*dwidth); print(dheight_ratio)
dim_ratio = [dwidth,dheight_ratio];print(dim_ratio)
img_cropped_res_ratio = cv2.resize(img_cropped,dsize=dim_ratio)
plt.imshow(img_cropped_res_ratio,cmap='gray')

"""
Flip image

Function syntax: 
    cv2.flip(img,flipFlag)
- flipFlag = 0 : flip around x-axis
- flipFlag = 1 : flip aroung y-axis
- flipFlag = -1 : flip around both axes
"""
