import numpy as pn
import cv2 as cv

img = cv.imread('../Material/person.jpg', 0 )
res = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Umbral', img)
cv.imshow('Resultado', res)

cv.waitKey(0)
cv.destroyAllWindows()