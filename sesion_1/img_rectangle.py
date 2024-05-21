import numpy as np
import cv2 as cv

img = cv.imread('./Material/fruta.jpg')
img = cv.rectangle(img, (480, 180), (690, 400), (0,225,0), 3)
cv.imshow('Fruta', img)

cv.waitKey(0)
cv.destroyAllWindows()