##==============================================================================
##   Demo By: Mahnoor Anjum
##   Date: 31/03/2019
##   Codes inspired by:
##   Official Documentation
##==============================================================================


import cv2
import numpy as np
image = cv2.imread("imgs/demo6.png", 0)
#image = cv2.imread("imgs/demo6a.jpg", 0)

cv2.imshow("Keypoints", image)
#ret,image = cv2.threshold(image,1,255,cv2.THRESH_BINARY_INV)
image = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
cv2.imshow("image", image)

image = abs(255-image)
is_v2 = cv2.__version__.startswith("2.")
# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()
## Change thresholds
#params.minThreshold = 0;
#params.maxThreshold = 255;
## Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.9
## Filter by Convexity
#params.filterByConvexity = True
#params.minConvexity = 1
## Filter by Inertia
#params.filterByInertia = True
#params.minInertiaRatio = 0.9

if is_v2:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)
zeros= np.zeros((1,1))
keypoints = detector.detect(image)
#cv2.DRAW_MATCHES_FLAGS_DEFAULT
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
#cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTING
#cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
keypoints_image = cv2.drawKeypoints(image, keypoints, zeros, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
blobs = (len(keypoints))
text = "Total blobs " + str(blobs)
cv2.putText(keypoints_image, text,(20,200),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)
cv2.imshow("Keypoints", keypoints_image)

cv2.waitKey(0)
cv2.destroyAllWindows()