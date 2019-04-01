import cv2


image = cv2.imread("./boxing-fisheye/00000.jpg",1)
imagegt = cv2.imread("./boxing-fisheye/00000.png",1)
imageinfo = image.shape
imagegtinfo = imagegt.shape
print("imageinfo:",imageinfo)
print("imageftinfo:",imagegtinfo)
height = imageinfo[0]
width = imageinfo[1]
channel = imageinfo[2]
dstheight = int(height*0.5)
dstwidth = int(width*0.5)
dst = cv2.resize(image,(dstwidth,dstheight))
cv2.imshow("image", image)
cv2.imshow("GroundTruth", imagegt)
cv2.imshow("resize",dst)

cv2.waitKey(0)
