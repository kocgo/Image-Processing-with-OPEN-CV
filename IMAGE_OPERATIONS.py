import numpy as np
import cv2

img = cv2.imread('c:\FOTO\KEE.jpg', cv2.IMREAD_COLOR)

# RESIZE
img_resized = cv2.resize(img,(0,0), fx=0.1,fy=0.1)
px = img[50,50]


# and this will resize the image to have 100 cols (width) and 50 rows (height):
#
# resized_image = cv2.resize(image, (100, 50))


# REGION OF IMAGE

roi = img_resized[100:150, 100:150] = [255,255,255]


# RESIZING SHOW WINDOW
# cv2.namedWindow('image',WINDOW_NORMAL)
# cv2.resizeWindow('image', 600,600)

cv2.imshow('GOSTER', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()