import cv2
import numpy as np
import os
import sys

def detectShape(c):          #Function to determine type of polygon on basis of number of sides
       shape = 'unknown' 
       peri=cv2.arcLength(cnt,True) 
       vertices = cv2.approxPolyDP(cnt, 0.02 * peri, True)
       sides = len(vertices) 
       if (sides == 3): 
            shape='triangle' 
       elif(sides==4): 
             x,y,w,h=cv2.boundingRect(cnt)
             aspectratio=float(w)/h 
             if (aspectratio==1):
                   shape='square'
             else:
                   shape="rectangle" 
       elif(sides==5):
            shape='pentagon' 
       elif(sides==6):
            shape='hexagon' 
       elif(sides==8): 
            shape='octagon' 
       elif(sides==10): 
            shape='star'
       else:
           shape='circle' 
       return shape, peri




image = 'IRIS03-SymmetryMoon-AlODroplet-Sub/T1_20210126_PJ0187062916_1225_X_map_xy_A.png'
img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 170, 255) 
ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY) 
(contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

prevx = 0
prevy = 0
for cnt in contours:
    moment=cv2.moments(cnt) 
    if moment['m00'] > 0:
     cx = int(moment['m10'] / moment['m00']) 
     cy = int(moment['m01'] / moment['m00'])
     shape, perimeter = detectShape(cnt) 
     print(f'{shape}, {perimeter}')
     if perimeter > 36:
          cv2.drawContours(img,[cnt],-1,(0,255,0),2)
          if prevx > 0 and prevy > 0:
               cv2.line(img, (prevx, prevy), (cx, cy), (255, 0, 0), 2)
          prevx, prevy = cx, cy
     outpath = os.path.join(os.getcwd(), 'moondetect', os.path.basename(image))
     cv2.imwrite(outpath,img) 

print('done')