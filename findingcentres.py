import argparse
import cv2
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                                             help = "Path to the image") 
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blurred = cv2.GaussianBlur(gray, (11, 11), 0) 
cv2.imshow("Image", image)
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2 .CHAIN_APPROX_SIMPLE) 

contoured=image.copy()

cv2.drawContours(contoured,cnts,-1,(255,0,0),1)

cv2.imshow("wef",contoured)

(x, y, w, h) = cv2.boundingRect(cnts[1])
#cnts is a tuple so cnts[1/2/3] will give centre of diff bodies 
((centerX, centerY), radius) = cv2.minEnclosingCircle(cnts[0])

print ((centerX,centerY),radius)
print (x,y,w,h)

cv2.waitKey(0)
