import numpy as np
import cv2 as cv
import datetime

def nothing(x):
    print(x)

def blue(x):
    print(f'Blue: {x}')

def green(x):
    print(f'Green: {x}')

def red(x):
    print(f'Red: {x}')

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('Drawing/lena.jpg')

    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 2, (255,0,0))

    k = cv.waitKey(1)
    if k == 27:
        break
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image', img)

cv2.destroyAllWindows()