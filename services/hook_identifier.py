
import cv2
from typing import List
import os
import sys
import numpy as np
import uuid



class PerimContour:
    def __init__(self, perimeter, contour) -> None:
        self.perimeter = perimeter
        self.contour = contour




def sortByPerimeter(item: PerimContour):
    return item.perimeter


def detectShape(cnt):          #Function to determine type of polygon on basis of number of sides
       shape = 'unknown' 
       peri=cv2.arcLength(cnt,False) 
       vertices = cv2.approxPolyDP(cnt, 0.02 * peri, False)
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




def checkForHook(files: List) -> bool:
    filename = ''
    isHook = True
    for file in files:
        #print(file)
        filename = os.path.basename(file)
        img = cv2.imread(file)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 170, 255) 
        
        (contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        shapesCount = 0
        contourList = []
        imagesStack = []
        imageCntMap = {}
        for cnt in contours:
            moment = cv2.moments(cnt) 
           
            if moment['m00'] > 0:
                cx = int(moment['m10'] / moment['m00']) 
                cy = int(moment['m01'] / moment['m00']) 
                shape, perimeter = detectShape(cnt) 
                
                if perimeter >= 80:
                    #print(shape, perimeter)
                    shapesCount = shapesCount + 1
                    isConvex = cv2.isContourConvex(cnt)
                    cv2.drawContours(img,[cnt],-1,(0,255,0),2)
                    cv2.putText(img,f'{perimeter} = {isConvex}',(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    item = PerimContour(perimeter=perimeter, contour=cnt)
                    contourList.append(item)
                
                elif perimeter >= 50 and perimeter < 80:
                    shapesCount = shapesCount + 1
                    isConvex = cv2.isContourConvex(cnt)
                    cv2.drawContours(img,[cnt],-1,(0,255,0),2)
                    cv2.putText(img,f'{perimeter} = {isConvex}',(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    item = PerimContour(perimeter=perimeter, contour=cnt)
                    contourList.append(item)
                
                #outpath = os.path.join(os.getcwd(), 'hull', filename)
                #cv2.imwrite(outpath,img) 
        '''
        if shapesCount >= 2:
            contourList.sort(reverse=True, key=sortByPerimeter)
            first = contourList[0]
            second = contourList[1]

            cv2.drawContours(img,[first.contour, second.contour],-1,(0,255,0),2)
        elif shapesCount == 1:
            first = contourList[0]
            cv2.drawContours(img,[first.contour],-1,(0,255,0),2)
        '''

        cv2.putText(img,str(shapesCount),(40,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        outpath = os.path.join(os.getcwd(), 'hull', filename)
        cv2.imwrite(outpath,img)
        if shapesCount > 10 or shapesCount == 0:
            isHook = False
        print(f'{filename} = {shapesCount}, isHook = {isHook}')


    return isHook