import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                 help = "Path to the image")
args = vars(ap.parse_args())
image1 = cv2.imread(args["image"])
image=image1
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, 
                                cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

cv2.imshow("Mean Thresh", thresh)
cv2.imshow("Image", image)

cv2.waitKey(0)
