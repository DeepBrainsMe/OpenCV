import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

source = cv.imread("./../sheep.jpg",0)
ret, thresh1 = cv.threshold(source, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(source, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(source, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(source, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(source, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['original image','Binary','binary-inv','trunc','tozero','tozero-inv']
images = [source,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()