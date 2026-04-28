"""
Basic Image Enhancement
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load image
img_bgr = cv2.imread("New_Zealand_Lake.jpg",cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

# Plot the image
plt.imshow(img_gray,cmap='gray')

# Increase brightness
matrix = np.ones(img_gray.shape,dtype='uint8')*50

img_gray_brighter = cv2.add(img_gray,matrix)
img_gray_darker = cv2.subtract(img_gray,matrix)

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_gray_brighter,cmap='gray');plt.title("Brighter Image")
plt.subplot(132);plt.imshow(img_gray_darker,cmap='gray');plt.title("Darker Image")
plt.subplot(133);plt.imshow(img_gray,cmap='gray');plt.title("Original")


# Contrast Enhancement <=> Multiplication
matrix1 = np.ones(img_gray.shape,dtype='uint8')*1.8
matrix2 = np.ones(img_gray.shape,dtype='uint8')*0.2

img_contrast_high = np.uint8(np.clip(cv2.multiply(np.float64(img_gray),matrix1),0,255))
img_contrast_low =  np.uint8((cv2.multiply(np.float64(img_gray),matrix2)))

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_contrast_high,cmap='gray');plt.title("Brighter Image")
plt.subplot(132);plt.imshow(img_contrast_low,cmap='gray');plt.title("Darker Image")
plt.subplot(133);plt.imshow(img_gray,cmap='gray');plt.title("Original")


"""
Image Thresholding

Function syntax:
    retval,img_thres = cv2.threshold(img,thresh,maxval,type)
- thresh: threshold value
- maxval: maximum value the pixel is set after thresholing to use with the THRESH_BINARY and THRESH_BINARY_INV types
-
Function syntax:
    
    img_thres = cv2.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blockSize,C)

-> This function basically use operator to threshold an image. For example, an edge-operator to threshold edges
- maxValue: Non-zero value assigned to the pixels that satisfy the threshold condition
- thresholdType: must be either THRESH_BINARY or THRESH_BINARY_INV
- blockSize: 
"""

img_read = cv2.imread("building-windows.jpg",cv2.IMREAD_GRAYSCALE)
retval, img_thres = cv2.threshold(img_read,100,255,cv2.THRESH_BINARY)

plt.figure(figsize=[18,5])
plt.subplot(121);plt.imshow(img_read,cmap='gray');plt.title("Original")
plt.subplot(122);plt.imshow(img_thres,cmap='gray');plt.title("Binary")

img_piano = cv2.imread("Piano_Sheet_Music.png",cv2.IMREAD_GRAYSCALE)

retval,img_piano_thres50 = cv2.threshold(img_piano,50,255,cv2.THRESH_BINARY)
retval,img_piano_thres130 = cv2.threshold(img_piano,130,255,cv2.THRESH_BINARY)
img_piano_adaptThres = cv2.adaptiveThreshold(img_piano,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7)

plt.figure(figsize=[20,20])
plt.subplot(221);plt.imshow(img_piano,cmap='gray'); plt.title("Original")
plt.subplot(222);plt.imshow(img_piano_thres50,cmap='gray'); plt.title("Global Threshold - 50")
plt.subplot(223);plt.imshow(img_piano_thres130,cmap='gray'); plt.title("Global Threshold - 130")
plt.subplot(224);plt.imshow(img_piano_adaptThres,cmap='gray'); plt.title("Adaptive Threshold - Mean - 11x7")

"""
Bitwise Operator

The bitwise operator compare the content/area of two images. Depending on the operator
- cv2.bitwise_and(img1,img2,mask)
- cv2.bitwise_or(img1,img2,mask)
- cv2.bitwise_xor(img1,img2,mask)
the overlapping area can be thresholded differently.

The mask input specifies the area to compare
"""

img_circle = cv2.imread("circle.jpg",cv2.IMREAD_GRAYSCALE)
img_rectangle = cv2.imread("rectangle.jpg",cv2.IMREAD_GRAYSCALE)

img_overlap_and = cv2.bitwise_and(img_circle,img_rectangle,mask=None)
plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_circle,cmap='gray')
plt.subplot(132);plt.imshow(img_rectangle,cmap='gray')
plt.subplot(133);plt.imshow(img_overlap_and,cmap='gray')

img_overlap_or = cv2.bitwise_or(img_circle,img_rectangle,mask=None)
plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_circle,cmap='gray')
plt.subplot(132);plt.imshow(img_rectangle,cmap='gray')
plt.subplot(133);plt.imshow(img_overlap_or,cmap='gray')

img_overlap_xor = cv2.bitwise_xor(img_circle,img_rectangle,mask=None)
plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_circle,cmap='gray')
plt.subplot(132);plt.imshow(img_rectangle,cmap='gray')
plt.subplot(133);plt.imshow(img_overlap_xor,cmap='gray')


# Using biwise operator to foreground and background image

img_logo = cv2.imread("coca-cola-logo.png",cv2.IMREAD_COLOR)
img_logo_rgb = cv2.cvtColor(img_logo,cv2.COLOR_BGR2RGB)
plt.imshow(img_logo_rgb)
img_logo_gray = cv2.imread("coca-cola-logo.png",cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("checkerboard_color.png",cv2.IMREAD_COLOR)


plt.imshow(img_logo_gray,cmap='gray')

retval,img_logo_mask = cv2.threshold(img_logo_gray,200,255,cv2.THRESH_BINARY)
retval,img_logo_mask_inv = cv2.threshold(img_logo_gray,200,255,cv2.THRESH_BINARY_INV)
plt.imshow(img_logo_mask,cmap='gray')
plt.imshow(img_logo_mask_inv,cmap='gray')

logo_h,logo_w = img_logo_mask.shape
dim = [logo_h,logo_w]

img_color_rgb = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
img_color_resize = cv2.resize(img_color_rgb,dsize=dim,interpolation=cv2.INTER_AREA)


img_foreground_color = cv2.bitwise_and(img_color_resize,img_color_resize,mask=img_logo_mask)
plt.imshow(img_foreground_color)


img_background_color = cv2.bitwise_and(img_logo_rgb,img_logo_rgb,mask=img_logo_mask_inv)
plt.imshow(img_background_color)

img_result = cv2.add(img_background_color,img_foreground_color)
plt.imshow(img_result)


