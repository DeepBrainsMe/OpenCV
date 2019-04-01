import cv2
import numpy as np
image = cv2.imread("si.jpg",1)
imginfo = image.shape
height = imginfo[0]
width = imginfo[1]
dstheight = int(height/2)
dstwidth = int(width/2)
dstImage = np.zeros((dstheight,dstwidth,3),np.uint8)
for i in range(0,dstheight):
    for j in range(0,dstwidth):
        iNew = int(i*(height*1.0/dstheight))
        jNew = int(j*(height*1.0/dstheight))
        dstImage[i,j]=image[iNew,jNew]
cv2.imshow("dst",dstImage)
cv2.imwrite("April.jpg ",dstImage)