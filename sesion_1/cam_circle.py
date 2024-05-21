import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while (True):
    ret, frame = cap.read()

    frame = cv.circle(frame, (200, 200), 98, (0,0,255), 5)
    cv.imshow('Video Cam', frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()