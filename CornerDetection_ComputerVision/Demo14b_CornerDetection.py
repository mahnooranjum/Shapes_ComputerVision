##==============================================================================
##   Demo By: Mahnoor Anjum
##   Date: 31/03/2019
##   Codes inspired by:
##   Github.com/imvinod/
##   Official Documentation
##==============================================================================

import cv2
import numpy as np
#PRE PROCESSING 
#image = cv2.imread('avengers.jpg')
#image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.Canny(image, 110, 255)
#image = cv2.medianBlur(image,5)
#ret,image = cv2.threshold(image,100,255,cv2.THRESH_BINARY)

#HARRIS CORNER DETECTION
image = cv2.imread('imgs\demo1.jpg')
#image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
image_h = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_h = np.float32(image_h)
blockSize=2
apertureSize=1
harris = cv2.cornerHarris(image_h,blockSize,apertureSize,0.05)
kernel = np.ones((3,3),np.uint8)
harris=cv2.dilate(harris,kernel,iterations=4)
image[harris > 0.05* harris.max()]=[255,127,255]
cv2.imshow('Harris Corners',image)


cv2.waitKey()
cv2.destroyAllWindows()

