import cv2 as cv
import numpy as np
def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')
cv.createTrackbar("parameterA","image",0,20,nothing)
cv.createTrackbar("parameterB","image",0,20,nothing)
cv.createTrackbar("parameterC","image",0,20,nothing)
switch = "0:OFF\n1:ON"
cv.createTrackbar(switch,"image",0,1,nothing)
while(1):
    cv.imshow("image",img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

    a = cv.getTrackbarPos("parameterA","image")
    b = cv.getTrackbarPos("parameterB","image")
    c = cv.getTrackbarPos("parameterC","image")
    s = cv.getTrackbarPos(switch,"image")
    if s == 0:
        img[:]=0
    else:
        img[:]=[a*12,b*12,c*12]
cv.destroyAllWindows()
