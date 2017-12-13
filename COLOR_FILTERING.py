import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    #HUE SAT VALUE ,,,, LIMITS ARE 180 !!!!

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([30, 255, 255])

# IN RETURNS 0 or 1 , if its in the range, result is 1 (white) for the pixel, else it is 0 (black)
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((3,3), np.uint8)

#Mask bolgesinde "Kernel" seklinde Erozyon uygula

    erosion = cv2.erode(mask, kernel, iterations=1)

    dilation = cv2.dilate(mask, kernel, iterations=1)


    result_erosion = cv2.bitwise_and(frame,frame, mask = erosion)

    #APPLY MORPHOLOGY TO "MASK" with OPEN-CLOSE METHOD with KERNEL

    #OPEN IS THE DIFFERENCE BETWEEN INPUT IMAGE AND OPENING OF THE IMAGE

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('result_with_erosion', result_erosion)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()