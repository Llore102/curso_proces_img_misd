import numpy as np
import cv2 as cv

img = cv.imread('./Material/vision.jpeg')

font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img, 'Vision Artifical', (20, 160), font, 1 ,(255,255,255), 2, cv.LINE_AA )
cv.imshow('Texto', img)

cv.waitKey()
cv.destroyAllWindows()