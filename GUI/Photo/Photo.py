# -*- coding: utf-8 -*-
"""

@author: eduardo.sanz
"""

#from skimage import io
#from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_peaks, corner_harris, plot_matches, BRIEF, ORB)
import cv2 as cv
#import PIL.Image as im

class Photo():

        photo_path = None    
        image = None
        gray = None
    
        def __init__(self, image):
            self.image = image
            self.gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            
        def getKeyPoints(self):
            'Función para obtener la lista de keypoints de la imagen'
            
            keypoints = corner_peaks(corner_harris(self.gray), min_distance=20)
            brief = BRIEF()
            brief.extract(self.gray,keypoints)
            keypoints = keypoints[brief.mask]
            descriptor = brief.descriptors
            
            #para comparar los descriptores de las imagenes
            #matchesDescriptors = match_descriptors(descriptor_photo, descriptor_imgGray)
            
            return descriptor
            
        """
        def newPhoto(self):
             
            self.image = cv.imread(self.photo_path, cv.IMREAD_GRAYSCALE)
            if self.image is None:
                raise TypeError("No se ha podido abrir la imagen. Revisar la ruta y volver a probar")
                
            self.image = cv.resize(self.image,(687,429),interpolation = cv.INTER_AREA)
            self.image = cv.cvtColor(self.image,cv.COLOR_BGR2RGB)
            
            return  self.image
        """ 
    
        def findContour(self):
            'Función para obtener los contornos de la imagen'
            
            'variable para guardar los pixeles donde esta la señal'
            cont = []
            
            _, threshold = cv.threshold(self.gray, 127, 255, cv.THRESH_BINARY)
            contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            i = 0
            for contour in contours:
                if i == 0: 
                    i = 1
                    continue
                
                approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True) 
                'Si approx es mayor de 3 y menor de 6 sabemos que pintamos el contorno'
                #if len(approx) <= 6 and len(approx) >= 3:
                if len(approx) == 3:
                    cont.append(contour)
                    cv.drawContours(self.image, [contour], 0,(0, 0, 255), 5)
                
            return self.image, cont
    