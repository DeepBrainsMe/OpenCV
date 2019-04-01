import cv2 as cv


def nothing(x):
    pass


source  = cv.imread("./../sheep.jpg")
a = 2
b = 2
width ,height ,channl = source.shape

cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
switch = "Alpha"
cv.createTrackbar(switch,"image",0,4,nothing)
cv.createTrackbar("parameterA","image",0,2,nothing)
cv.createTrackbar("parameterB","image",0,2,nothing)
while(1):

    k = cv.waitKey(1)
    if k == ord('q'):
        break
    s = cv.getTrackbarPos(switch,"image")
    a = cv.getTrackbarPos("parameterA", "image")+1
    b = cv.getTrackbarPos("parameterB", "image")+1

    if s == 0:
        cv.imshow("image", source)
    elif s == 1:
        result1 = cv.cvtColor(source,cv.COLOR_BGR2RGB)
        result11 = cv.resize(result1,None,fx=a,fy=b,interpolation=cv.INTER_LINEAR)
        cv.imshow("image",result11)
    elif s == 2:
        result2 = cv.cvtColor(source,cv.COLOR_BGR2HSV)
        result22 = cv.resize(result2,None,fx=a,fy=b , interpolation=cv.INTER_LINEAR)
        cv.imshow('image',result22)
    elif s == 3:
        result3 = cv.cvtColor(source,cv.COLOR_BGR2HLS)
        result33 = cv.resize(result3,None,fx=a,fy=b , interpolation=cv.INTER_LINEAR)
        cv.imshow('image',result33)
    else:
        result4 = cv.cvtColor(source,cv.COLOR_BGR2YUV)
        result44 = cv.resize(result4,None,fx=a,fy=b , interpolation=cv.INTER_LINEAR)
        cv.imshow('image',result44)

cv.destroyAllWindows()

