#==============================================================================
#   Tutorial By: Mahnoor Anjum
#   Date: 30/03/2019
#   Codes inspired by:
#   Github.com/imvinod/
#   Official Documentation
#==============================================================================
import cv2
import numpy as np

#BLOB DETECTION
image = cv2.imread("imgs/demo3.jpg", 0)
cv2.imshow("Original", image)

cv2.imshow("Keypoints", image)
is_v2 = cv2.__version__.startswith("2.")
# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 0;
params.maxThreshold = 255;
# Filter by Area.
params.filterByArea = True
params.minArea = 50
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.3
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5
# Filter by Inertia
params.filterByInertia =True
params.minInertiaRatio = 0.5
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
keypoints_image = cv2.drawKeypoints(image, keypoints, zeros, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", keypoints_image)



cv2.waitKey(0)
cv2.destroyAllWindows()