import numpy as np
import cv2 as cv

img = np.zeros((360, 810, 3), np.uint8)
img = cv.circle(img, (530, 210), 145, (255,255,255), -1)
img1 = cv.imread('./Material/pelota_b.jpg')

img1 = cv.resize(img1, (img.shape[1], img.shape[0]))
img2 = cv.bitwise_and(img1, img)

print(img1[0,0])
print(img[0,0])

cv.imshow('Resultado1', img1)
cv.imshow('Resultado2', img2)

cv.waitKey(0)
cv.destroyAllWindows()