import numpy as np
import cv2 as cv

img1 = cv.imread('./Material/retrato_1.png')
img2 = cv.imread('./Material/retrato_2.png')

img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
img3 = cv.absdiff(img1, img2)

print(img1[200,250])
print(img2[200,250])
print(img3[200,250])

cv.imshow('Resultado1', img1)
cv.imshow('Resultado2', img2)
cv.imshow('Resultado3', img3)

cv.waitKey(0)
cv.destroyAllWindows()