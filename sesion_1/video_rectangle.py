import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while (True):
    ret, frame = cap.read()

    frame = cv.rectangle(frame, (200, 100), (400, 300 ), (0,255,0), 3)
    cv.imshow('Video Cam', frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()