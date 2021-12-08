# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:13:57 2021

@author: eduardo.sanz
"""

import cv2 as cv
import numpy as np

class segmentation():
    
    image = None
    nnetwork = None
    
    def __init__(self, image):
        self.image = image          
    
    
    def get_histrogram(self, image):
        
        hist = cv.calcHist(image, [20], None, [256], (0,256), accumulate=False)
        values_hist=[]
        for i in range(1, 256):
            values_hist.append(int(hist[i]))
        
        return max(values_hist), min(values_hist)
    
    # def contrast(self, image_hsv):
        
    #     percentile = 1.0
    #     max_s = 255.0
        
    #     v_channel = image_hsv[:,:,2]
        
    #     low_auto_v = np.percentile(v_channel.ravel(), percentile, axis = 0)
    #     high_auto_v = np.percentile(v_channel.ravel(), 100.0-percentile, axis = 0)
    #     out_auto_v = max_s/(high_auto_v-low_auto_v)*(v_channel.ravel()-low_auto_v)
    #     out_auto_v = np.clip(out_auto_v, a_min = 0.0, a_max = 1.0)
    #     out_auto_v = np.reshape(out_auto_v,v_channel.shape)
    #     # out_auto_hsv = image_hsv.copy()
    #     image_hsv[:,:,2] = out_auto_v
    
    #     return image_hsv
    
    def get_mask(self):
        
        # image_blur = cv.medianBlur(self.image,7)       
        hsv = cv.cvtColor(self.image,cv.COLOR_BGR2HSV)
        hsv = cv.medianBlur(hsv,7)
        
        # hsv = self.contrast(hsv)
        # cv.imshow('hsv',hsv)
        
        # hist_s_max, hist_s_min = self.get_histrogram(hsv[:,:,2])
        # print(hist_s_max, hist_s_min)
        
        'para el color azul'
        lowerb = np.array([105,150,20], dtype=np.uint8)
        upperb = np.array([130,255,255], dtype=np.uint8)
        maskb = cv.inRange(hsv, lowerb, upperb) 
        
        # 'para el blanco'            
        # lowerw = np.array([0,0,0], dtype=np.uint8)
        # upperw = np.array([0,0,2555], dtype=np.uint8)
        # maskw = cv.inRange(hsv, lowerw, upperw)

        # 'para el amarillo'            
        # lowery = np.array([28,150,150], dtype=np.uint8)
        # uppery = np.array([31,255,255], dtype=np.uint8)
        # masky = cv.inRange(hsv, lowery, uppery)
            
        'para el color rojo'
        lowerr1 = np.array([0,100,75], dtype=np.uint8)
        upperr1 = np.array([10,255,255], dtype=np.uint8)
        maskr_low = cv.inRange(hsv, lowerr1, upperr1)
        
        lowerr2 = np.array([170,100,75], dtype=np.uint8)
        upperr2 = np.array([179,255,255], dtype=np.uint8)
        maskr_high = cv.inRange(hsv, lowerr2, upperr2)
        
        maskr = cv.add(maskr_low, maskr_high)

        mask = cv.bitwise_or(maskb, maskr)
        # mask = cv.bitwise_or(masky, mask)
        # mask = cv.bitwise_or(maskw, mask)

        cv.imshow('mask',mask)
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
        
        # cv.imshow('red',self.image[:,:,0])
        hist_s_max, hist_s_min = self.get_histrogram(self.image[:,:,2])
        print(hist_s_max, hist_s_min)
        
        mask = self.get_mask()   
        _,contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for c in contours:
            
            # area = cv.contourArea(c)
            # print('area:',area)
            # if area > 3:
            
            epsilon = 0.1*cv.arcLength(c,True)
            approx = cv.approxPolyDP(c,epsilon,True)
            
            if len(approx) >= 3 and len(approx) <= 4 :
                
                contour = cv.convexHull(c)
               
                x,y,w,h = cv.boundingRect(contour)
                x,y,w,h = self.check_dimension(x-10,y-10,w,h)
               
                img = self.image[y-10:y+h+10, x-10:x+w+10]

            
        return self.image, img, x,y,w,h
      
        
       
    
    
    
    
    