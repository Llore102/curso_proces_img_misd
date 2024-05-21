import numpy as np
import cv2 as cv

img = cv.imread('./Material/pelota.jpeg')
img = cv.circle(img, (530, 500), 338, (0,0,255), 5)
cv.imshow('Futbol', img)

cv.waitKey()
cv.destroyAllWindows()