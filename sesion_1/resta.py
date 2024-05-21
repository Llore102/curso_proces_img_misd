import numpy as np
import cv2 as cv

img = np.zeros((360, 810, 3), np.uint8)
img = cv.circle(img, (530, 210), 145, (255,255,255), -1)
cv.imshow('Resultado', img)


img1 = cv.imread('./Material/pelota_b.jpg')
img1 = cv.resize(img1, (810, 360))


img3 = cv.subtract(img, img1)

print(img1[0,0])
print(img3[0,0])

cv.imshow('Resultado2', img3)

cv.waitKey(0)
cv.destroyAllWindows()