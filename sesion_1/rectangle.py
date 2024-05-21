import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

img  = cv.rectangle(img, (200, 200), (400, 400), (0,255,0), 3)

cv.imshow('Cuadrado', img)

cv.waitKey()
cv.destroyAllWindows()