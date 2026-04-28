import cv2
from IPython.display import Image
import numpy as np
import matplotlib.pyplot as plt


"""
Reading an image using imread function from cv2:

Function syntax: img = cv2.imread(fileName,Flags)

Flags = 0 <=> read a grayscale image
Flags = 1 (Default) <=> read a color image
Flags = -1 <=> read image as such including alpha channels

"""

# Read grayscale image
cb_image = cv2.imread("checkerboard_18x18.png",0)
print(cb_image)

# Extract image dimensions
numRows,numCols = cb_image.shape
print(f"Image has a size of {numRows}x{numCols}")

# Extract image type
img_type = cb_image.dtype
print(f"Image data type is {img_type}")

"""
Displaying Images:

Function syntax: plt.imshow(img,Options)

The function plt.imshow() will not plot an image with its original colomap.

For grayscale images, if we want to display it black&white, 
we must pass cmap='gray' 

The color image loaded by OpenCV will have a BGR channel configuration
, while matplotlib has a default RGB channel configuration expected for images.
Therefore, to display the image correctly, we must convert the image first

colorImg = cv2.imread("coca-cola-logo.png",1)
colorImg_corr = cv2.cvtColor(colorImg,cv2.COLOR_BGR2RGB)

Or we can load the image RGB directly

colorImg_rgb = cv2.imread(filename,cv2.IMREAD_COLOR_RGB)
"""

cb_img2 = cv2.imread("checkerboard_fuzzy_18x18.jpg",0)
numRows2,numCols2 = cb_img2.shape

# Display B&W images
plt.imshow(cb_image)
plt.imshow(cb_img2,cmap='gray')

# Dispaly color image
colorImg = cv2.imread("coca-cola-logo.png",1)
colorImg_corr = cv2.cvtColor(colorImg,cv2.COLOR_BGR2RGB)
numRows_cImg,numCols_cImg,numChannels = colorImg.shape
print(f"Coca-cola logo has a size of {numRows_cImg}x{numCols_cImg}x{numChannels}")

plt.figure(figsize=[50,50])
plt.subplot(121);plt.imshow(colorImg);plt.title(f"Uncorrected Color Image")
plt.subplot(122);plt.imshow(colorImg_corr);plt.title(f"Corrected Color Image")

""" 
Manipulating image channel/color:

Split the image into its channels:
    b,g,r, = cv2.split(img)
    
Merging the 3 channels into one image:
    img_merge = cv2.merge([b,g,r])
    



"""
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg",cv2.IMREAD_COLOR)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB);
b,g,r = cv2.split(img_NZ_bgr)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(b,cmap='gray');plt.title("Blue")
plt.subplot(142);plt.imshow(g,cmap='gray');plt.title("Green")
plt.subplot(143);plt.imshow(r,cmap='gray');plt.title("Red")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("RGB-Image")

# Merging 
img_merge = cv2.merge([b,g,r])
plt.imshow(img_merge);plt.imshow(img_merge)

"""
Saving image

Function syntax: 
    cv2.imwrite(filename,img)
    
"""



