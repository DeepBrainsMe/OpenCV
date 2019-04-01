import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt
a = 4
source = cv.imread("./../sheep.jpg",cv.IMREAD_UNCHANGED)
source = cv.cvtColor(source ,cv.COLOR_BGR2RGB)
kenel = np.ones((a,a),np.float32)/(a*a)
dst = cv.filter2D(src=source,ddepth=-1,kernel=kenel)
plt.subplot(1,2,1),plt.imshow(source),plt.title("source")
plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(dst),plt.title("result")
plt.xticks([]),plt.yticks([])
plt.show()