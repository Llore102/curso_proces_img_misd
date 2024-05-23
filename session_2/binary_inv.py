import numpy as pn
import cv2 as cv

gray = cv.imread('../Material/tornos.png', cv.IMREAD_GRAYSCALE)
t,dst = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)

cv.imshow('Umbral', gray)
cv.imshow('Resultado', dst)

cv.waitKey(0)
cv.destroyAllWindows()