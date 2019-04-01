import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import scipy.ndimage as sci
source = cv.imread("./../sheep.jpg")
# cols,rows = img.shape[:2]
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# #行，列，通道数
def elastic_transform(image, alpha, sigma, alpha_affine, random_state=None):
    """Elastic deformation of images as described in [Simard2003]_ (with modifications).
    .. [Simard2003] Simard, Steinkraus and Platt, "Best Practices for
         Convolutional Neural Networks applied to Visual Document Analysis", in
         Proc. of the International Conference on Document Analysis and
         Recognition, 2003.

     Based on https://gist.github.com/erniejunior/601cdf56d2b424757de5
    """
    if random_state is None:
        random_state = np.random.RandomState(None)

    shape = image.shape
    shape_size = shape[:2]

    # Random affine
    center_square = np.float32(shape_size) // 2
    square_size = min(shape_size) // 3
    pts1 = np.float32([center_square + square_size, [center_square[0] + square_size, center_square[1] - square_size],
                       center_square - square_size])
    pts2 = pts1 + random_state.uniform(-alpha_affine, alpha_affine, size=pts1.shape).astype(np.float32)
    M = cv.getAffineTransform(pts1, pts2)
    image = cv.warpAffine(image, M, shape_size[::-1], borderMode=cv.BORDER_REFLECT_101)

    dx = sci.gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dy = sci.gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dz = np.zeros_like(dx)

    x, y, z = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
    indices = np.reshape(y + dy, (-1, 1)), np.reshape(x + dx, (-1, 1)), np.reshape(z, (-1, 1))

    return sci.map_coordinates(image, indices, order=1, mode='reflect').reshape(shape)
dst = elastic_transform(image=source,alpha=0.5,sigma=0.7,alpha_affine=cv.MOTION_AFFINE)
cv.imshow("dst",dst)
cv.imshow("source",source)
cv.waitKey(0)
cv.destroyAllWindows()













plt.subplot(121 ,plt.imshow(source),plt.title("input"))
plt.subplot(122 ,plt.imshow(dst),plt.title("output"))
plt.show()
