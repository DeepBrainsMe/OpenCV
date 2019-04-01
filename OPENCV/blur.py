import cv2 as cv
import numpy as np
def nothing(x):
    pass
img = cv.imread("./../sheep.jpg")
cv.namedWindow('image')
cv.createTrackbar("parameterA","image",0,20,nothing)
cv.createTrackbar("parameterB","image",0,100,nothing)
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
        # result = cv.blur(img,(a+1,b+1),dst=None,anchor=None,borderType=cv.BORDER_REFLECT101)
        # result = cv.GaussianBlur(img,(2*a+1,2*a+1),b,borderType=cv.BORDER_REFLECT101)
        # result = cv.medianBlur(img,2*a+1)
        result = cv.bilateralFilter(src=img,d = a,sigmaColor=b,sigmaSpace=b,borderType=cv.BORDER_REFLECT101)
        cv.imshow("image",result)
cv.destroyAllWindows()
