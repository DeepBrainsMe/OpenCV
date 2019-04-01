import numpy as np
import cv2 as cv
cap = cv.VideoCapture("./../blackswan.mp4")
i = 0
while(True):
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("frame",frame)
    print(cap.get(propId=i))
    i= i+1
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
