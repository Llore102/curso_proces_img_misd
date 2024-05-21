import numpy as np
import cv2 as cv

cap = cv.VideoCapture('http://192.168.1.10:4747/video')

while (True):
    ret, frame = cap.read()
    cv.imshow('Video', frame)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()