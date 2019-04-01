import numpy as np
import cv2 as cv
img = np.zeros((512,1024,3),np.uint8)
# cv.line(img,(0,0),(512,512),color=(0,255,255),thickness=5,lineType=cv.LINE_4)  #line
# cv.rectangle(img,(128,128),(256,256),color=(0,0,255),thickness=3,lineType=cv.LINE_AA)# rectangle
# cv.circle(img,(255,255),128,color=(0,255,0),thickness=2,lineType=cv.LINE_AA)

# pts = np.array([[128,128],[360,128],[128,360],[400,400]],np.int32)
# pts = pts.reshape(-1,1,2)
# cv.polylines(img,[pts],isClosed=False,color=(0,0,255),thickness=3,lineType=cv.LINE_AA)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"hello cv",(128,360),font,4,color=(0,255,0),thickness=2,lineType=cv.LINE_AA)
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.resizeWindow("image",1000,1000)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()
