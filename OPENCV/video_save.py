import numpy as np
import cv2 as cv
cap = cv.VideoCapture("./../blackswan.mp4")
fourcc = cv.VideoWriter_fourcc(*"MJPG")
out = cv.VideoWriter("./../grayswan.MP4",fourcc,20.0,(1920,1080))
while(cap.isOpened()):
    ret ,frame = cap.read()
    if ret == True:
        fanzhuan = cv.flip(frame,180)
        # print(frame.shape)
        # grayswan = cv.cvtColor(fanzhuan,cv.COLOR_BGR2GRAY)
        out.write(fanzhuan)
        cv.imshow("grayswan",fanzhuan)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
