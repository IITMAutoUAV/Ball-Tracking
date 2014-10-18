import numpy as np
import cv2

cap = cv2.VideoCapture('sample.flv')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0) 
    cv2.imshow("Image", gray)
    thresh = cv2.adaptiveThreshold(blurred, 255,
                  cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
    edged = cv2.Canny(blurred, 20, 50)
    cv2.imshow("Edges",edged)
    cv2.imshow("thresh",thresh)

    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2 .CHAIN_APPROX_SIMPLE) 

    contoured=gray.copy()

    cv2.drawContours(contoured,cnts,-1,(255,0,0),1)
    cv2.imshow('frame',contoured)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#this is coming more dotted than good border
cap.release()
cv2.destroyAllWindows()
