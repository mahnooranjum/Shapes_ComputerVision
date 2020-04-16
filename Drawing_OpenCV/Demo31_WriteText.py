#==============================================================================
#   By: Mahnoor Anjum
#   Date: 5/04/2020
#   Codes inspired by:
#   Official Documentation
#==============================================================================
import cv2
import numpy as np

#==================================================================

#    FONT_HERSHEY_SIMPLEX 
#    FONT_HERSHEY_PLAIN 
#    FONT_HERSHEY_DUPLEX 
#    FONT_HERSHEY_COMPLEX 
#    FONT_HERSHEY_TRIPLEX 
#    FONT_HERSHEY_COMPLEX_SMALL 
#    FONT_HERSHEY_SCRIPT_SIMPLEX
#    FONT_HERSHEY_SCRIPT_COMPLEX 
#    FONT_ITALIC 

#TEXT
xy = (20,200)
stroke = 3
color = (100,170,0)
fontsize = 2
image = np.zeros((512,512,3),np.uint8)
cv2.putText(image,'Hello World', xy, cv2.FONT_HERSHEY_PLAIN,fontsize,color,stroke)
cv2.imshow('TEXT', image)

cv2.waitKey()
cv2.destroyAllWindows()