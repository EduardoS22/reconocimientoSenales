# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:05:57 2021

@author: eduardo.sanz
"""

import tensorflow as tf
import numpy as np
import cv2 as cv
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split



class convolutional_nnetwork():
    
    HEIGHT = 32
    WIDTH = 32
    BASE_DIR = r'.\images\train'
    NUMBER_LABELS = 52
    
    model = tf.keras.models.Sequential()
    
    def __init__(self):
        self.model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(self.WIDTH,self.HEIGHT,3)))
        self.model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))
        self.model.add(tf.keras.layers.Dropout(rate=0.25))
        
        self.model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=(self.WIDTH,self.HEIGHT,3)))
        self.model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))
        self.model.add(tf.keras.layers.Dropout(rate=0.25))   
        
        self.model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'))

        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(64, activation='relu'))
        self.model.add(tf.keras.layers.Dense(self.NUMBER_LABELS, activation='sigmoid'))
        
        self.model.compile(loss='binary_crossentropy', optimizer=RMSprop(learning_rate=0.001), metrics=['accuracy'])
        
    def get_model(self):
        
        return self.model


    def get_data_train(self):
       
       images = list()
       labels = list()
       for label in range(self.NUMBER_LABELS):
           image_dir = os.path.join(self.BASE_DIR, str(label))
           for image in os.listdir(image_dir):
                img = load_img(os.path.join(image_dir, image), target_size=(self.WIDTH, self.HEIGHT))
                img_array = img_to_array(img)
                images.append(img_array)
                labels.append(label)
    
       labels = to_categorical(labels)
    
       return images, labels
    
    def fit_model(self, epochs=30, step_per_epochs=60):
        
        images, labels = self.get_data_train()
        
        x_train, x_test, y_train, y_test = train_test_split(np.array(images), labels, test_size=0.2)
        self.model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=epochs, steps_per_epoch=step_per_epochs)
        
        # return history
    
    def predict_image(self, image):
                   
        # class_signals = []
        # for image in images:
        image = cv.resize(image,(self.WIDTH,self.HEIGHT),interpolation = cv.INTER_AREA)
        image = tf.expand_dims(image, axis=0)
        
        predictions = self.model.predict(image)
        # class_signals.append(int(np.argmax(predictions)))
        class_signal = int(np.argmax(predictions))
        
        return class_signal