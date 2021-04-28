
import cv2
import sys
import os

img = cv2.imread(sys.argv[1])
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray_img)
#cv2.waitKey(0)

ret,thresh = cv2.threshold(gray_img,127,255,0)
#cv2.imshow('ret', thresh)
#cv2.waitKey(0)

M = cv2.moments(thresh)

cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

print(cX, cY)

cv2.circle(img, (cX, cY), 5, (255, 0, 255), 3)

cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
