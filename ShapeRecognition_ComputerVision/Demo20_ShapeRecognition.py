##==============================================================================
##   Demo By: Mahnoor Anjum
##   Date: 31/03/2019
##   Codes inspired by:
##   Official Documentation
##==============================================================================import cv2
import numpy as np
image = cv2.imread('imgs\operators.jpg')
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#cv2.imshow('Original', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Canny = cv2.Canny(gray, 100, 120)
_, contours, hierarchy = cv2.findContours(Canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  
contours = contours[::2]
cv2.drawContours(image, contours, -1, (0,255,0), 2)
#cv2.imshow('Contours', image)
for c in contours:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    print(len(approx))
    if(len(approx)==4):
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 2)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,"RECTANGLE", (cx+20, cy+40), cv2.FONT_HERSHEY_SIMPLEX, .5, (1, 1, 1), 2)
    elif(len(approx)==12):
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 2)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,"PLUS", (cx+50, cy+30), cv2.FONT_HERSHEY_SIMPLEX, .5, (1, 1, 1), 2)
    else:
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 2)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,"CIRCLE", (cx+20, cy+20), cv2.FONT_HERSHEY_SIMPLEX, .5, (1, 1, 1), 2)

    cv2.imshow('Shape Recognition', image)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
