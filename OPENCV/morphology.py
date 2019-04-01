import cv2 as cv
import numpy as np
def nothing(x):
    pass
img = cv.imread("./../sheep.jpg")
cv.namedWindow('image',cv.WINDOW_FULLSCREEN)
cv.createTrackbar("parameterA","image",0,20,nothing)
cv.createTrackbar("parameterB","image",0,20,nothing)
switch = "Morphology"
cv.createTrackbar(switch,"image",0,8,nothing)

while(1):
    k = cv.waitKey(1)
    if k == ord('q'):
        break

    a = cv.getTrackbarPos("parameterA","image")
    b = cv.getTrackbarPos("parameterB","image")
    s = cv.getTrackbarPos(switch,"image")
    if s == 0:
        cv.imshow("image",img)
    elif s == 1:
        kernel = np.ones((a,a))
        # result = cv.dilate(img,kernel=kernel,iterations=b)  # 膨胀
        # result = cv.erode(img,kernel=kernel,iterations=b)  # 腐蚀
        result = cv.morphologyEx(img,cv.MORPH_OPEN,kernel,iterations=b)
        cv.imshow("image",result)
    elif s == 2:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=b)
        cv.imshow("image", result)
    elif s == 3:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel, iterations=b)
        cv.imshow("image", result)
    elif s == 4:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_CROSS, kernel, iterations=b)
        cv.imshow("image", result)
    elif s == 5:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_ELLIPSE, kernel, iterations=b)
        cv.imshow("image", result)
    elif s ==6:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel, iterations=b)
        cv.imshow("image", result)
    elif s == 7:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_HITMISS, kernel, iterations=b)
        cv.imshow("image", result)
    elif s == 8:
        kernel = np.ones((a, a))
        result = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel, iterations=b)
        cv.imshow("image", result)
cv.destroyAllWindows()