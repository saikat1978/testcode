import cv2
import os
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)

ret1, thresh1 = cv2.threshold(img1,240,255,cv2.THRESH_BINARY) 
ret2, thresh2 = cv2.threshold(img2,240,255,cv2.THRESH_BINARY) 


d1 = cv2.matchShapes(img1,img2,cv2.CONTOURS_MATCH_I1,0) 
d2 = cv2.matchShapes(img1,img2,cv2.CONTOURS_MATCH_I2,0) 
d3 = cv2.matchShapes(img1,img2,cv2.CONTOURS_MATCH_I3,0)

print(d2)

if d2 > 0.0:
    print('mismatch')
