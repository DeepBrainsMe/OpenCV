import numpy as np
import cv2

image=cv2.imread("./../si.jpg",1)
imageinfo = image.shape
height = imageinfo[0]
width = imageinfo[1]
matSrc = np.float32([[0,0],[0,height-1],[width-1,0]])
matDst = np.float32([[100,50],[300,height+100],[width+300,300]])
matAffine = cv2.getAffineTransform(matSrc,matDst)
print(matAffine)
dst = cv2.warpAffine(image,matAffine,(2000,2000))
cv2.imshow('dst',dst)
cv2.imshow("src",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
