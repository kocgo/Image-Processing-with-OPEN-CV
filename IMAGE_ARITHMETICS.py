import cv2
import numpy as np


img1 = cv2.imread('c:\FOTO\D-Matplotlib.png')
img2 = cv2.imread('c:\FOTO\mainsvmimage.png')
img3 = cv2.imread('c:\FOTO\mainlogo.png')

rows,cols,channels = img3.shape

roi = img1[0:rows,0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# FIRST OUTPUT IS RET
# SECOND OUTPUT IS THRESHOLDED IMAGE
# IF IT PASSES 220 , IT TURNS INTO 255
# ELSE IT GOES 0
# LAST PARAMETER DOES THE REVERSE ACTION

ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3,img3, mask=mask)

dst = cv2.add(img1_bg,img3_fg)
img1[0:rows, 0:cols ] = dst



#add = img1 + img2
#add = cv2.add(img1,img2)

#WEIGHTING IMAGES - LAST PARAMETER IS GAMMA

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


#cv2.imshow('Masked', mask)
cv2.imshow('gray', img3gray)
cv2.imshow('MASK', mask)
cv2.imshow('MASKINV', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)
cv2.imshow('Adding', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()