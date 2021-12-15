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
    

# =============================================================================
#     def min_max_histrogram(self, image):
#         
#         hist = cv.calcHist(image, [20], None, [256], (0,256), accumulate=False)
#         values_hist=[]
#         for i in range(1, 256):
#             values_hist.append(int(hist[i]))
#         
#         value_max = [values_hist[j] for j in range(len(values_hist)) if values_hist[j] > 0]
#         value_min = [values_hist[z] for z in range(len(values_hist)) if values_hist[z] > 0]
#         print(value_max,value_min)
#         
#         return max(value_max), min(value_min)
# =============================================================================

    

# =============================================================================
#     # def contrast(self, image_hsv):
#         
#     #     percentile = 1.0
#     #     max_s = 255.0
#         
#     #     v_channel = image_hsv[:,:,2]
#         
#     #     low_auto_v = np.percentile(v_channel.ravel(), percentile, axis = 0)
#     #     high_auto_v = np.percentile(v_channel.ravel(), 100.0-percentile, axis = 0)
#     #     out_auto_v = max_s/(high_auto_v-low_auto_v)*(v_channel.ravel()-low_auto_v)
#     #     out_auto_v = np.clip(out_auto_v, a_min = 0.0, a_max = 1.0)
#     #     out_auto_v = np.reshape(out_auto_v,v_channel.shape)
#     #     # out_auto_hsv = image_hsv.copy()
#     #     image_hsv[:,:,2] = out_auto_v
#     
#     #     return image_hsv
# =============================================================================
# =============================================================================
#     def find_contours_gray(self, image):
#         '''
#         Función que recupera los contornos con el algoritmo de OTSU
# 
#         Parameters
#         ----------
#         image : array
#             Se recuperan los contornos de una imagen con el algoritmo de OTSU.
# 
#         Returns
#         -------
#         None.
# 
#         '''
#         
#         gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# # =============================================================================
# #         hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# #         hls = cv.cvtColor(image, cv.COLOR_BGR2HLS)
# #         luv = cv.cvtColor(image, cv.COLOR_BGR2LUV)
# # =============================================================================
#         gray = cv.medianBlur(gray, 3)
#         
#         'Con algoritmo de OTSU obtenemos los contonos de la imagen en saturación'
#         # ret,th = cv.threshold(hsv[:,:,1],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#         th = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 1)
#          
#         # circles = cv.HoughCircles(th, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# # =============================================================================
# #         circles = cv.HoughCircles(th, cv.HOUGH_GRADIENT, 1.2, 75)
# #         for i in circles[0,:]:
# #             cv.circle(th,(i[0],i[1]),i[2],(0,255,0),2)
# # =============================================================================
#         # ret, th = cv.threshold(gray, 175, 255, cv.THRESH_BINARY)
#         _, contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#         cv.drawContours(th, contours, -1, (0,0,255),2)
#         cv.imshow('Imagen adaptive', th)
#         for contour in contours:
#             cv.fillPoly(th, pts=[contour], color = (255,255,255))
# # =============================================================================
# #         cv.drawContours(self.image, contours, -1, (255,255,0),3)
# # =============================================================================
#         
# # =============================================================================
# #         cv.imshow('Imagen hsv', hsv)
# #         cv.imshow('Imagen hls', hls)
# #         cv.imshow('Imagen luv', luv)
# # =============================================================================
#         cv.imshow('Imagen adaptive fillpoly', th)        
#         return contours    
# =============================================================================


        

    def find_contours_mask(self, image):
        '''
        Función que recupera los contornos con el algoritmo de OTSU

        Parameters
        ----------
        image : array
            Se recuperan los contornos de una imagen con el algoritmo de OTSU.

        Returns
        -------
        None.

        '''
      
        ret,th = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        _, contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        return contours

    
    def get_mask(self, image):
        '''
        Función que busca las posibles señales dentro de nuestra imagen, self.image

        Returns
        -------
        None.

        '''
        
        kernel = np.ones((3, 3), np.uint8)
        
        # image_blur = cv.medianBlur(self.image,7)       
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        hsv = cv.medianBlur(hsv,5)
        
        # hsv = self.contrast(hsv)
        # cv.imshow('hsv',hsv)
        
# =============================================================================
#         'hue'
#         hist_h_max, hist_h_min = self.min_max_histrogram(hsv[:,:,0])
#         'saturacion'
#         hist_s_max, hist_s_min = self.min_max_histrogram(hsv[:,:,1])
#         'valor'
#         hist_s_max, hist_s_min = self.min_max_histrogram(hsv[:,:,1])
# =============================================================================
        
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
# =============================================================================
#         mask_canny = cv.Canny(mask, 225, 255)
# =============================================================================
        # mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
        
# =============================================================================
#         cv.imshow('mask canny', mask_canny)
#         conts = self.find_contours(mask_canny)
#         cv.drawContours(self.image, conts, -1, (0,0,255),3)
#         for cont in conts:
#             
#             epsilon = 0.1*cv.arcLength(cont,True)
#             approx = cv.approxPolyDP(cont,epsilon,True)
#             cv.drawContours(self.image, approx, -1, (0,255,0),3)
# =============================================================================
        
        return mask

    def find_contours_image(self, image):
        '''
        Función para obtener los bordes de la imagen recortada

        Parameters
        ----------
        image : numpy array
            Imagen recortada de la original para obtener sus bordes.

        Returns
        -------
        None.

        '''
            
        image = cv.medianBlur(image, 5)
        # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # gray = cv.medianBlur(gray, 5)
        # cv.imshow('gray image', gray)
            
        mask = self.get_mask(image)
# =============================================================================
#         contours_mask = self.find_contours(mask)
#         cv.fillPoly(mask, pts=contours_mask, color = (255,255,255))
#         cv.imshow('mask image', mask)
#             
#         canny = cv.Canny(mask, 0, 255)
#             
#         contours_canny = self.find_contours(canny)
#         cv.imshow('canny image', canny)
# =============================================================================
            
    
        th = cv.adaptiveThreshold(mask, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
        _, contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # cv.imshow('th image', th)
            
        return contours

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
        # cv.imshow('mascara', mask)
        # image = cv.bitwise_or(mask, self.image)
        contours = self.find_contours_mask(mask)
        # cv.drawContours(self.image, ini_contours, -1, (255,0,0),3)
        # i = 0
        for contour in contours:        
   
            x,y,w,h = cv.boundingRect(contour)
            'Calculamos si al recortar la imagen sobrepasa el tamaño de la imagen'
            x,y,w,h = self.check_dimension(x-10,y-10,w+20,h+20)
            img = self.image[y:y+h, x:x+w]
            # cv.imshow('i', img)
            # i += 1
            image_contours = self.find_contours_image(img)
            
            
            for image_contour in image_contours:  
                
                area = cv.contourArea(image_contour)
                if area > 2000.0:                   
                    print('area: ', area)
                    print('tamaño borde imagen: ', len(image_contour))
                    
                    # cv.drawContours(img, [canny_border], 0, (255,0,0),3)
                # cv.fillPoly(mask, pts=[contour], color = (255,255,255))         
                
                # contour_convex= cv.convexHull(contour)   
                    epsilon = 0.1*cv.arcLength(image_contour,True)
                    approx = cv.approxPolyDP(image_contour,epsilon,True)
                    
                        
                    # if (len(approx) >= 3 and len(approx) <= 4 and len(canny_border) > 100) or (len(approx) >= 3 and len(approx) <= 4 and (len(canny_border) >= 40 and len(canny_border) <= 50)):                
                    if len(approx) >= 3 and len(approx) <= 4:
                        print('tamaño aproximación: ', len(approx))
                        # contour = cv.convexHull(ini_contour)
                        # cv.drawContours(self.image, [canny_border], 0, (255,0,0),3)
                        # cv.drawContours(self.image, approx, -1, (0,255,0),3)
                       
                        # x,y,w,h = cv.boundingRect(contour)
                        # 'Calculamos si al recortar la imagen sobrepasa el tamaño de la imagen'
                        # x,y,w,h = self.check_dimension(x-10,y-10,w+20,h+20)
                       
                        # img = self.image[y:y+h, x:x+w]
                        # mask_img = self.get_mask(img)
                        images_signals.append(img)
                        size_images_signals.append(np.array([x,y,w,h]))
        
                        # cv.imshow('Imagen recortada', img)
                        # cv.rectangle(self.image,(x,y),(x+w,y+h),(0,255,0),2)
            

        
# =============================================================================
#         # gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
#         # gray = cv.medianBlur(gray, 3)
#         contours_image_hsv = self.find_contours_gray(self.image)
#         
#         for contour_image_hsv in contours_image_hsv:
#             
# # =============================================================================
# #             area = cv.contourArea(contour_image_hsv)
# #             cv.fillPoly(self.image, pts=[contour_image_hsv], color = (255,255,255))
# #             print(area)
# # =============================================================================
#             
#             contour_image_hsv_convex= cv.convexHull(contour_image_hsv)   
#             epsilon_hsv = 0.1*cv.arcLength(contour_image_hsv_convex,True)
#             approx_hsv = cv.approxPolyDP(contour_image_hsv_convex,epsilon_hsv,True)
#             print(len(approx_hsv))
#             if len(approx_hsv) == 4 :                
# 
#                 # contour = cv.convexHull(ini_contour)
#                 # cv.drawContours(self.image, [contour_image_hsv], 0, (255,0,0),3)
#                 cv.drawContours(self.image, [approx_hsv], 0, (255,255,255),3)
#                
#                 x_hsv,y_hsv,w_hsv,h_hsv = cv.boundingRect(contour_image_hsv)
#                 'Calculamos si al recortar la imagen sobrepasa el tamaño de la imagen'
#                 x_hsv,y_hsv,w_hsv,h_hsv = self.check_dimension(x_hsv-10,y_hsv-10,w_hsv+20,h_hsv+20)
#                
# # =============================================================================
# #                 img_hsv = self.image[y_hsv:y_hsv+h_hsv, x_hsv:x_hsv+w_hsv]
# #                 images_signals.append(img_hsv)
# # 
# #                 cv.imshow('Imagen recortada', img_hsv)
# # =============================================================================
#                 cv.rectangle(self.image,(x_hsv,y_hsv),(x_hsv+w_hsv,y_hsv+h_hsv),(0,0,255),2)
# =============================================================================
                
    
        return self.image, images_signals, size_images_signals
      
 
    
    
    
    