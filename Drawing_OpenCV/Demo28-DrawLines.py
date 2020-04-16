#==============================================================================
#   By: Mahnoor Anjum
#   Date: 5/04/2020
#   Codes inspired by:
#   Official Documentation
#==============================================================================

import cv2
import numpy as np

#INTRODUCTION TO DRAWING VIA CODE
#CREATING A BLACK IMAGE
image = np.zeros((512,512,3), dtype = "uint8")
bw = np.zeros((512,512),dtype = "uint8")
cv2.imshow("Black image (color) 3 channels",image)
cv2.imshow("Black image (B&W) 1 channel",bw)
cv2.waitKey()

#CREATING A LINE
image = np.zeros((512,512,3),np.uint8)
cv2.line(image,(0,0),(512,512),(255,255,0),10)
cv2.imshow("Line",image)
cv2.waitKey()

#CREATING A CROSS
image = np.zeros((512,512,3),np.uint8)
cv2.line(image,(0,0),(512,512),(255,255,0),10)
cv2.line(image,(0,512),(512,0),(0,255,255),10)
cv2.imshow("Cross",image)

#CREATE A LINE
x0 = 100
y0 = 100
x=400
y=300
stroke = 10
color = (0,255,255)
image = np.zeros((512,512,3),np.uint8)
cv2.line(image,(x0,y0),(x0+x,y0+y),color,stroke)
cv2.imshow("Line",image)

cv2.waitKey()
cv2.destroyAllWindows()