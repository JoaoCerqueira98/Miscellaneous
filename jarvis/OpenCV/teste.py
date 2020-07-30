import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.imread('messi_face.jpg', 0)

res = cv2.matchTemplate(gray, face, cv2.TM_CCOEFF_NORMED, )
print(res)
thresh = 0.8
loc = np.where(res >= thresh)
print(loc)


cv2.imshow('Messi', img)



cv2.waitKey(0)
cv2.destroyAllWindows()
