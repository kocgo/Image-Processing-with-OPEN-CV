import cv2
import numpy as np
import keyboard

canny_trackbar1pos = 0
canny_trackbar2pos = 0

def nothing(x):
    pass

cv2.namedWindow('Threshold',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('Threshold_Bar1', 'Threshold', 150, 600, nothing )
cv2.createTrackbar('Threshold_Bar2', 'Threshold', 200, 600, nothing )

cap = cv2.VideoCapture(0)



while True:
    _, frame = cap.read()

    canny_trackbar1pos = cv2.getTrackbarPos('Threshold_Bar1', 'Threshold')
    canny_trackbar2pos = cv2.getTrackbarPos('Threshold_Bar2', 'Threshold')

#SECOND PARAMETER IS DEPTH
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0 , ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    edges = cv2.Canny(frame, canny_trackbar1pos, canny_trackbar2pos)

    # cv2.imshow('Frame', frame)
    # cv2.imshow('Laplacion', laplacian)
    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('sobely', sobely)
    cv2.imshow('Threshold', edges)


    cv2.waitKey(1)
    if keyboard.is_pressed('Esc'):
        break



cv2.destroyAllWindows()
cap.release()






