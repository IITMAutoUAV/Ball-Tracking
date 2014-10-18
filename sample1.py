import numpy as np
import cv2
canvas1 = np.zeros((300,300,3),dtype="uint8")
canvas=cv2.bitwise_not(canvas1)
red=(0,0,255)
cv2.rectangle(canvas,(40,40),(70,80),red,-1)
cv2.circle(canvas,(200,250),15,(0,255,0),-1)
cv2.imshow("sample",canvas)
cv2.imwrite("C:\Python27\sample1.jpg",canvas)




cv2.waitKey(0)

            


