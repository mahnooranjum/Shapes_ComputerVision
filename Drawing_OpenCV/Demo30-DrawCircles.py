#==============================================================================
#   By: Mahnoor Anjum
#   Date: 5/04/2020
#   Codes inspired by:
#   Official Documentation
#==============================================================================

import cv2
import numpy as np

#CREATING A CIRCLE
#cv2.circle(image,center,radius,color,fill)
x0 = 100
y0 = 200
radius = 20
color=(250,150,50)
stroke=10
image =  np.zeros((512,512,3),np.uint8)
cv2.circle(image,(x0,y0),radius,color,stroke)
cv2.imshow("Circle",image)

#CREATING A FILLED CIRCLE
x0 = 100
y0 = 200
radius = 20
color=(250,150,250)
stroke=-1
image =  np.zeros((512,512,3),np.uint8)
cv2.circle(image,(x0,y0),radius,color,stroke)
cv2.imshow("Circle Filled",image)

cv2.waitKey()
cv2.destroyAllWindows()