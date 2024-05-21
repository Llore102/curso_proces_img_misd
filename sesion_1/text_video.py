import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while (True):
    ret, frame = cap.read()

    font = cv.FONT_HERSHEY_SIMPLEX

    cv.putText(frame, 'Vision Artifical', (20, 256), font, 2 ,(255,255,255), 2, cv.LINE_AA )

    cv.imshow('Video Cam', frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()