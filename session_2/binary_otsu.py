import numpy as np
import cv2 as cv

img = cv.imread('../Material/person.jpg', 0)
blur = cv.GaussianBlur(img, (5, 5), 0)

ret, th = cv.threshold(blur,0,255, cv.THRESH_BINARY+cv.THRESH_OTSU )

cv.imshow('Umbral', img)
cv.imshow('Resultado', th)

cv.waitKey(0)
cv.destroyAllWindows()