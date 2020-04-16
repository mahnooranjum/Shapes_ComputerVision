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

#GOOD FEATURES TO TRACK
image = cv2.imread('imgs\demo1.jpg')
#image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
image_c = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
numberofcorners=100
minimumdist=12
quality=0.001
corners = cv2.goodFeaturesToTrack(image_c, numberofcorners, quality, minimumdist)
for corner in corners:
    x,y = corner[0]
    x = int(x)
    y = int(y)
    cv2.circle(image,(x,y),6,(255,100,255),2)
cv2.imshow('Corners by Good Features',image)   


cv2.waitKey()
cv2.destroyAllWindows()

