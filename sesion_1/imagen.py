import numpy as np
import cv2 as cv

img = cv.imread('./Material/fruta.jpg')
cv.imshow('Fruta', img)

cv.waitKey(0)
cv.destroyAllWindows()