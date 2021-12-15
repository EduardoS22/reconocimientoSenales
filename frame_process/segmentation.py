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
    WIDTH = 681
    HEIGTH = 423
    
    def __init__(self, image):
        self.image = image  
        self.image = cv.resize(self.image,(self.WIDTH, self.HEIGTH),interpolation = cv.INTER_AREA)        
    
    
    
    def find_contours(self, image, adaptive=True):
        '''
        Función para obtener los contornos de una imagen. Si adaptive es igual a True
        se ejecutará la función de openCV adaptiveThreshold. Si es Flase será threshold el que se ejecute

        Parameters
        ----------
        image : numoy array
            DESCRIPTION.
        adaptive : Boolean, optional
            Variable para saber si se ejecuta adaptiveThreshold o threshold.

        Returns
        -------
        contours: numpy array
            Contornos de la imagen.

        '''
        
        if adaptive == False:
            ret,th = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
            _, contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            
        else:
# =============================================================================
#             image = cv.medianBlur(image, 5)     
#             mask = self.get_mask(image)
# =============================================================================

            th = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
            _, contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
        
        return contours

    
    def get_mask(self, image):
        '''
        Función que busca las posibles señales dentro de nuestra imagen, self.image

        Returns
        -------
        mask: mascara de la imagen.

        '''
        
        kernel = np.ones((3, 3), np.uint8)
            
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        hsv = cv.medianBlur(hsv,5)
        
        'para el color azul'
        lowerb = np.array([105,150,20], dtype=np.uint8)
        upperb = np.array([130,255,255], dtype=np.uint8)
        maskb = cv.inRange(hsv, lowerb, upperb) 
        

        'para el amarillo'            
        lowery = np.array([28,150,150], dtype=np.uint8)
        uppery = np.array([31,255,255], dtype=np.uint8)
        masky = cv.inRange(hsv, lowery, uppery)
            
        'para el color rojo'
        lowerr1 = np.array([0,100,75], dtype=np.uint8)
        upperr1 = np.array([10,255,255], dtype=np.uint8)
        maskr_low = cv.inRange(hsv, lowerr1, upperr1)
        
        lowerr2 = np.array([165,100,75], dtype=np.uint8)
        upperr2 = np.array([179,255,255], dtype=np.uint8)
        maskr_high = cv.inRange(hsv, lowerr2, upperr2)
        
        maskr = cv.add(maskr_low, maskr_high)

        mask = cv.bitwise_or(maskb, maskr)
        mask = cv.bitwise_or(masky, mask)

        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        
        
        return mask


    def check_dimension(self, x, y, w, h):
        '''
        Parameters
        ----------
        x : int 
            Coordenada del eje x más pequeña.
        y : int
            Coordenada del eje y más pequeña.
        w : int
            Ancho de la imagen a capturar.
        h : int
            Alto de la imagen a capturar.

        Returns
        -------
        x : int 
            Coordenada del eje x más pequeña.
        y : int
            Coordenada del eje y más pequeña.
        w : int
            Ancho de la imagen a capturar.
        h : int
            Alto de la imagen a capturar.

        '''
        
        dimension=[self.WIDTH, self.HEIGTH]
        
        x = (0 if (x - 10) < 0 else x)
        y = (0 if (y - 10) < 0 else y)
        w = (dimension[0] if (x + w) > dimension[0] else w)
        h = (dimension[1] if (y + h) > dimension[1] else h)
        
        return x,y,w,h 
        
    
    def preprocessing(self):
        '''
        Función para orquestar el proceso de pre-procesado de la imagen

        Returns
        -------
        self.image : Imagen original señalando las señales
        images_signals : las imagenes de las señales encontradas.

        '''
        
        images_signals = []
        size_images_signals = []
        'Se buscan señales por sus colores'
        mask = self.get_mask(self.image)  

        contours = self.find_contours(mask, adaptive=False)
        for contour in contours:        
   
            x,y,w,h = cv.boundingRect(contour)
            'Calculamos si al recortar la imagen sobrepasa el tamaño de la imagen'
            x,y,w,h = self.check_dimension(x-10,y-10,w+20,h+20)
            image = self.image[y:y+h, x:x+w]
            image_mask = mask[y:y+h, x:x+w]

            image_contours = self.find_contours(image_mask)
            
            for image_contour in image_contours:  
                
                area = cv.contourArea(image_contour)
                if area > 2000.0:                      
                    epsilon = 0.1*cv.arcLength(image_contour,True)
                    approx = cv.approxPolyDP(image_contour,epsilon,True)
                    
                    if len(approx) >= 3 and len(approx) <= 4:
                        images_signals.append(image)
                        size_images_signals.append(np.array([x,y,w,h]))               
    
        return self.image, images_signals, size_images_signals
      
 
    
    
    
    