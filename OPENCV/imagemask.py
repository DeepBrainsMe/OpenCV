import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("./../April.jpg",1)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img,interpolation="bicubic")
print(img.shape)
plt.xticks(np.arange(0,375,step=75)),plt.yticks(np.arange(0,527,step=75))
plt.show()
