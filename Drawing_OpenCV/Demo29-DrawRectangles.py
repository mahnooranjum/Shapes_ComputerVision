#==============================================================================
#   By: Mahnoor Anjum
#   Date: 5/04/2020
#   Codes inspired by:
#   Official Documentation
#==============================================================================

import cv2
import numpy as np

#CREATING A RECTANGLE
x0 = 200
y0 = 100
width = 200
height = 100
stroke = 10
color = (200,50,200)
image = np.zeros((512,512,3),np.uint8)
cv2.rectangle(image, (x0,y0),(x0+width,y0+height),color,stroke)
cv2.imshow("Rectange",image)

#CREATING A FILLED RECTANGLE
x0 = 100
y0 = 200
width = 200
height = 100
stroke = -1
color = (250,250,250)
image = np.zeros((512,512,3),np.uint8)
cv2.rectangle(image, (x0,y0),(x0+width,y0+height),color,stroke)
cv2.imshow("Rectange Filled",image)


#CREATE A POLYGON
closed = True
stroke = 2
color=(250,150,250)
image = np.zeros((512,512,3),np.uint8)
pts = np.array([[100,150],[400,250],[90,200],[500,500]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],closed,color,stroke)
cv2.imshow("Polygon", image)


cv2.waitKey()
cv2.destroyAllWindows()