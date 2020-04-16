#==============================================================================
#   Tutorial By: Mahnoor Anjum
#   Date: 30/03/2019
#   Codes inspired by:
#   Github.com/imvinod/
#   Official Documentation
#==============================================================================
import cv2
import numpy as np

#CIRCLE DETECTION
image = cv2.imread('imgs/demo2.jpg')
cv2.imshow('circles', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT,1, 1)
for i in circles[0,:]:
       cv2.circle(image,(i[0], i[1]), i[2], (255, 0, 0), 3)
       cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)
cv2.imshow('detected circles', image)

cv2.waitKey(0)
cv2.destroyAllWindows()