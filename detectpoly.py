import cv2
import numpy as np 
import sys
import os


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

if __name__=='__main__':

    folder = sys.argv[1]
    files = os.listdir(folder)

    for file in files:
        print(file)
        img = cv2.imread(f'{folder}/{file}')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 170, 255) 
        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY) 
        (contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        shapesCount = 0
        for cnt in contours:
            moment=cv2.moments(cnt) 
            cx = int(moment['m10'] / moment['m00']) 
            cy = int(moment['m01'] / moment['m00']) 
            shape, perimeter = detectShape(cnt) 
            print(f'{shape}, {perimeter}')
            '''
            if shape == 'circle':
                continue
            else:
                shapesCount = shapesCount + 1
            '''
            if perimeter >= 50:
                shapesCount = shapesCount + 1
                cv2.drawContours(img,[cnt],-1,(0,255,0),2)
            #cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
            
            outpath = os.path.join(os.getcwd(), 'polydetect', file)
            cv2.imwrite(outpath,img) 
        cv2.putText(img,str(shapesCount),(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        cv2.imwrite(outpath,img) 
    print('done')
'''
   
    
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
'''