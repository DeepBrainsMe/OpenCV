import cv2
import numpy as np
image = cv2.imread("./../SI.jpg",1)
cv2.imshow("src",image)
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()