import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
img  = cv.circle(img, (200, 200), 100, (0,0,255), -1)
cv.imshow('Circulo', img)

cv.waitKey()
cv.destroyAllWindows()