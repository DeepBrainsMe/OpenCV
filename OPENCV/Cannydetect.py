import cv2 as cv
import numpy as np
def nothing(x):
    pass
img = cv.imread("./../sheep.jpg")
cv.namedWindow('image')
cv.createTrackbar("parameterA","image",100,255,nothing)
cv.createTrackbar("parameterB","image",200,300,nothing)
switch = "0:OFF\n1:ON"
cv.createTrackbar(switch,"image",0,1,nothing)

while(1):
    k = cv.waitKey(1)
    if k == ord('q'):
        break

    a = cv.getTrackbarPos("parameterA","image")
    b = cv.getTrackbarPos("parameterB","image")
    s = cv.getTrackbarPos(switch,"image")
    if s == 0:
        cv.imshow("image",img)
    else:
        result = cv.Canny(img,a,b)
        cv.imshow("image",result)
cv.destroyAllWindows()