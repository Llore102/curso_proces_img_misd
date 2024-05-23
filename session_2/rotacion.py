import cv2 as cv
import numpy as np

img = cv.imread('../Material/arbol.jpg')
rows, cols = img.shape[:2]
M = cv.getRotationMatrix2D((cols/2, rows/2), 80, 1 )
res = cv.warpAffine(img,M, (cols, rows))

cv.imshow('Resultados', res)

cv.waitKey(0)
cv.destroyAllWindows()

