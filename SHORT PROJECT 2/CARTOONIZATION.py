import cv2
import numpy as np

num_down = 2           #number of times downsampling happens
num_bilateral = 7      #number of bilaterlal filtering steps

img_rgb = cv2.imread("dog.jpg")

print(img_rgb.shape)    #dimensions of the picture

img_rgb = cv2.resize(img_rgb, (800, 500))  #resizing the image for optimal result
#downsampling
img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)
#applying small bilateral filter repeatedly instead of one large one
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

#upscaling to original size
for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

#convert back to color
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)

#display
stack = np.hstack([img_rgb, img_cartoon])
cv2.imshow('Stacked Images', stack)
