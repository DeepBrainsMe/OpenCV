import cv2  as  cv
import numpy as np

sheep = cv.imread("./../sheep.jpg")
ground_sheep = cv.imread("./../sheep.png")

result = cv.cvtColor(ground_sheep,cv.COLOR_BGR2HSV)
cv.imshow("result",result)
# cv.imshow("src1",sheep)
cv.imshow("groundtruth",ground_sheep)





cv.waitKey(0)
cv.destroyAllWindows()
