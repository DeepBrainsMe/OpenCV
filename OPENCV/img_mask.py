import cv2 as cv
import numpy as np


sheep = cv.imread("./../sheep.jpg")
ground_sheep = cv.imread("./../sheep.png")
e1 = cv.getTickCount()
result = cv.addWeighted(src1=sheep ,alpha=0.9,src2=ground_sheep,beta=1, gamma=0,dtype=-1)
# result = cv.bitwise_xor(src1=sheep,src2=ground_sheep,)
cv.imwrite("./../sheepmask.jpg" ,result)
cv.imshow("result",result)
cv.imshow("src1",sheep)
cv.imshow("groundtruth",ground_sheep)
e2 = cv.getTickCount()
time = ((e2-e1)/cv.getTickFrequency())
print(time)
cv.waitKey(0)
cv.destroyAllWindows()


