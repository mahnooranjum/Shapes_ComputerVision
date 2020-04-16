#==============================================================================
#   Tutorial By: Mahnoor Anjum
#   Date: 30/03/2019
#   Codes inspired by:
#   Github.com/imvinod/
#   Official Documentation
#==============================================================================
import cv2
import numpy as np

#HOUGHLINES LINE DETECTION
image = cv2.imread('imgs/demo1.jpg')
cv2.imshow('Original', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170)  
rho_accuracy=1
theta_accuracy=np.pi/180
threshold=210
lines = cv2.HoughLines(edges, rho_accuracy, theta_accuracy, threshold)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image, (x1, y1), (x2, y2), (255, 255, 0), 2)
#cv2.imwrite('houghlines.jpg',image)
cv2.imshow('Hough Lines', image)

cv2.waitKey(0)
cv2.destroyAllWindows()