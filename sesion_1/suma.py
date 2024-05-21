import numpy as np
import cv2 as cv

img1 = cv.imread('./Material/cuadrado.jpg')
img2 = cv.imread('./Material/estrella.jpg')
img3 = cv.add(img1, img2)

cv.imshow('Cuadrado',img1)
cv.imshow('Estrella',img2)
cv.imshow('Resultado',img3)

cv.waitKey(0)
cv.destroyAllWindows()

