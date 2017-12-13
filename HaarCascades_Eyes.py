import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\dasar_haartrain\myhaar.xml')

cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    eyes = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in eyes:
        img = cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('Gri', gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

