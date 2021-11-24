# -*- coding: utf-8 -*-
"""

@author: eduardo.sanz
"""

import cv2 as cv
import numpy as np

class image():
    
    image = None
    
    def __init__(self, image):
        self.image = image
            
    
    
    def get_mask(self):
        
        image_blur = cv.medianBlur(self.image,7)
        
        hsv = cv.cvtColor(image_blur,cv.COLOR_BGR2HSV)
        
        'para el color azul'
        lowerb = np.array([105,150,80])
        upperb = np.array([130,255,255])
        maskb = cv.inRange(hsv, lowerb, upperb) 

        'para el amarillo'            
        # lowery = np.array([15,100,20])
        # uppery = np.array([45,255,255])
        # masky = cv.inRange(hsv, lowery, uppery)
            
        'para el color rojo'
        lowerr1 = np.array([0,100,20])
        upperr1 = np.array([10,255,255])
        maskr_low = cv.inRange(hsv, lowerr1, upperr1)
        
        lowerr2 = np.array([160,100,20])
        upperr2 = np.array([180,255,255])
        maskr_high = cv.inRange(hsv, lowerr2, upperr2)
        
        maskr = cv.add(maskr_low, maskr_high)

            
        mask = cv.bitwise_or(maskb, maskr)
        # mask = cv.bitwise_or(mask, masky)
        
        # contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # cv.fillPoly(mask, pts = contours, color =(255,255,255)) 
        
        return mask

    def check_dimension(self,x, y, w, h):
        
        dimension=[687,429]
        
        if (x + w) > dimension[0]:
            w = x + dimension[0]
        
        elif (x - w) < 0:
            w = x - 0
            
        if (y + h) > dimension[1]:
            h = y + dimension[1]
        
        elif (y - h) < 0:
            h = y - 0
        
        return x,y,w,h    


    
    def preprocessing(self):
        
        self.image = cv.resize(self.image,(687,429),interpolation = cv.INTER_AREA)
        # self.image = cv.cvtColor(self.image,cv.COLOR_BGR2HSV)
        
        mask = self.get_mask()
        
        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for c in contours:
            
            area = cv.contourArea(c)
            if area > 3:
            
                area = cv.contourArea(c)
                print(area)
                'para comprobar si esta lejos o no'
                if area > 3:    
            
                    contour = cv.convexHull(c)
                   
                    #if len(contour) >= 9 and len(contour) <= 50:
                    x,y,w,h = cv.boundingRect(contour)
                    print(x,y,w,h)
                    x,y,w,h = self.check_dimension(x,y,w,h)
                    
                    # x,y,w,h = find_contours(mask)
                   
                    img = self.image[y-10:y+h+10, x-10:x+w+10]
                    # img = image[(x-20):(x+w+20), (y-20):(y+h+20)]
                    # cv.imshow('img'+str(i),img)
                    # i = i + 1
            
                    # contour = cv.convexHull(c) 

                    # x,y,w,h = cv.boundingRect(contour)
                   
                    # img = image[x-20:x+w+20, y-20:y+h+20]
                    # cv.imshow(' ',img)
                    
                    # cv.drawContours(self.image, c, 0, (0,255,0), 3)
                    cv.rectangle(self.image,(x,y),(x+w,y+h),(0,255,0),2)
                    cv.putText(self.image,'{},{}'.format(x, y),(x+10,y),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1,cv.LINE_AA)
                    # # cv.imshow('Image',self.image)
           
        return self.image
      
        
       
    
    
    
    
    