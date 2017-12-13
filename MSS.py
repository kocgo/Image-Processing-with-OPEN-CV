import time
import cv2
import mss
import numpy as np
import keyboard

monitor = {'top': 40, 'left': 0, 'width': 600, 'height': 400}

for i in list(range(2))[::-1]:
    print(i+1)
    time.sleep(1)




while True:
    sct = mss.mss()
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array(sct.grab(monitor))


    keyboard.press('W')



    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=600)

    vertices = np.array([[10, 400], [10, 300], [175, 200], [460, 200], [640, 300], [640, 400]])

    mask = np.zeros_like(processed_img)
    cv2.fillPoly(mask, [vertices], 255)
    processed_img = cv2.bitwise_and(processed_img, mask)

#                      EDGES

    lines = cv2.HoughLinesP(processed_img,1)



    cv2.imshow('OpenCV/Numpy normal', processed_img)

    print('fps: {0}'.format(1 / (time.time()-last_time)))

    if (cv2.waitKey(25) & 0xFF == ord('q') or keyboard.is_pressed('q') == True):

        keyboard.release('W')
        cv2.destroyAllWindows()
        break