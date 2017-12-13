import cv2
import numpy as np

img_bgr = cv2.imread('c:/FOTO/DotaFull.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('c:/FOTO/Venge.png', 0)

h , w = template.shape

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.345
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+ h, pt[1] + w) , (0,255,255) , 2)


cv2.imshow('Frame', img_bgr)
cv2.waitKey(0)