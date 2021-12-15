# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from photo.photo import photo
from convolutional_nnetwork import convolutional_nnetwork
from frame_process.segmentation import segmentation
import cv2 as cv
import os
import sys
import io
# import numpy as np

class Ui_MainWindow(object):
    
    videoExtension = [".mp4",".avi"]
    fotoExtension = [".jpeg",".jpg",".png"]
    FRAME_SIZE = (681,423)
    
    signals = {0: 'Velocidad maxima 20',1: 'Velocidad maxima 30', 2: 'Velocidad maxima 50', 3: 'Velocidad maxima 60', 4: 'Velocidad maxima 70', 
               5: 'Velocidad maxima 80', 6: 'Fin velocidad maxima 90', 7: 'Velocidad maxima 100', 8: 'Velocidad maxima 120', 9: 'Adelantamiento prohibido', 
               10: 'Adelantamiento prohibido camiones ', 11: 'Interseccion con prioridad', 12: 'Calzada con prioridad', 13: 'Ceda el paso', 14: 'Stop',
               15: 'Circulacion prohibida', 16: 'Prohibido el paso', 17: 'Otros peligros', 18: 'Curva peligrosa derecha',
               19: 'Curva peligrosa izquierda', 20: 'Curvas peligrosas izquierda', 21: 'Perfil irregular', 22: 'Pavimento deslizante', 23: 'Estrechamiento carril derecho',
               25: 'Obras', 26: 'Semaforo', 27: 'Paso peatones', 28: 'Niños', 29: 'Prohibido ciclos', 30: 'Hielo', 31: 'Paso animales en libertad', 32: 'Fin restricciones',
               33: 'Sentido obligatorio', 34: 'Unica dirección permitida', 35: 'Paso obligatorio', 36: 'Rotonda', 37: 'Fin adelantamiento prohibido', 
               38: 'Fin adelantamiento prohibido camiones', 39 :'Intersección prioridad sobre derecha', 40: 'Intersección prioridad sobre irquierda',
               41: 'Intersección prioridad incorporación derecha', 42: 'Intersección circulación giratoria', 43: 'Curvas peligrosas hacia derecha',
               44: 'Resalto', 45: 'Estrchamiento calzada', 46: 'Paso animales domesticos', 47: 'Giro derecha prohibido', 48: 'Giro izquierda prohibido',
               49: 'Media vuelta prohibida', 50: 'Velocidad maxima 40', 51: 'Obligación luces', 52: 'Prohibido peatones'}
    
    
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1644, 716)
        MainWindow.setMaximumSize(QtCore.QSize(4000, 4000))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(720, 110, 901, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(8, 30, 331, 21))
        self.label_5.setObjectName("label_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 60, 251, 181))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 249, 179))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_4)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 251, 181))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 530, 701, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layoutButtons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutButtons.setContentsMargins(0, 0, 0, 0)
        self.layoutButtons.setObjectName("layoutButtons")
        self.groupBoxButtons = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBoxButtons.setTitle("")
        self.groupBoxButtons.setObjectName("groupBoxButtons")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 97, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 10, 97, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.groupBoxButtons)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 681, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutButtons.addWidget(self.groupBoxButtons)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 99, 701, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutVideo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutVideo.setContentsMargins(0, 0, 0, 0)
        self.layoutVideo.setObjectName("layoutVideo")
        self.scrollAreaVideo = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollAreaVideo.setWidgetResizable(True)
        self.scrollAreaVideo.setObjectName("scrollAreaVideo")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 697, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setGeometry(QtCore.QRect(6, 10, 687, 411))
        self.graphicsView.setMaximumSize(QtCore.QSize(687, 429))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Panel)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView.setLineWidth(2)
        self.graphicsView.setObjectName("graphicsView")
        self.scrollAreaVideo.setWidget(self.scrollAreaWidgetContents)
        self.layoutVideo.addWidget(self.scrollAreaVideo)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(720, 360, 911, 291))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 911, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutSignal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutSignal.setContentsMargins(0, 0, 0, 0)
        self.layoutSignal.setObjectName("layoutSignal")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 110, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_4.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setObjectName("pushButton_4")
# =============================================================================
#         self.label_2 = QtWidgets.QLabel(self.groupBox_2)
#         self.label_2.setGeometry(QtCore.QRect(10, 150, 181, 31))
#         self.label_2.setText("")
#         self.label_2.setObjectName("label_2")
# =============================================================================
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(120, 20, 59, 23))
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 70, 59, 23))
        self.spinBox_2.setProperty("value", 60)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 109, 41))
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(200, 0, 701, 261))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 699, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(-7, 0, 711, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.layoutSignal.addWidget(self.groupBox_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1061, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutLoad = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutLoad.setContentsMargins(0, 0, 0, 0)
        self.layoutLoad.setObjectName("layoutLoad")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 60, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 40))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 40, 881, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutLoad.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1644, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.label_3.setEnabled(True)
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.progressBar.setEnabled(False)
        self.label_3.setText('Epochs')
        self.label_4.setText('step per epochs')
        
        self.pushButton.clicked.connect(self.open_video)
        self.pushButton_2.clicked.connect(self.play_video)
        self.pushButton_3.clicked.connect(self.stop_video)
        self.pushButton_4.clicked.connect(self.train_model)

        self.conv_nnetwork = convolutional_nnetwork()
        model = " Model: sequential \n \
        _________________________________________________________________ \n \
        Layer (type)             Output Shape                    Param #    \n \
        ================================================================  \n \
        conv2d_21 (Conv2D)       (None, 30, 30, 32)              896        \n \
        _________________________________________________________________ \n \
        max_pooling2d_14         (MaxPooling (None, 15, 15, 32)  0          \n \
        _________________________________________________________________ \n \
        dropout_14 (Dropout)     (None, 15, 15, 32)              0          \n \
        _________________________________________________________________ \n \
        conv2d_22 (Conv2D)       (None, 13, 13, 64)              18496      \n \
        _________________________________________________________________ \n \
        max_pooling2d_15         (MaxPooling (None, 6, 6, 64)    0          \n \
        _________________________________________________________________ \n \
        dropout_15 (Dropout)     (None, 6, 6, 64)                0          \n \
        _________________________________________________________________ \n \
        conv2d_23 (Conv2D)       (None, 4, 4, 64)                36928      \n \
        _________________________________________________________________ \n \
        flatten_7 (Flatten)      (None, 1024)                    0          \n \
        _________________________________________________________________ \n \
        dense_14 (Dense)         (None, 64)                      65600      \n \
        _________________________________________________________________ \n \
        dense_15 (Dense)         (None, 52)                      3380       \n \
        ================================================================ \n \
        Total params: 125,300 \n \
        Trainable params: 125,300 \n \
        Non-trainable params: 0 \n \
        _________________________________________________________________ "
        
        self.plainTextEdit.setPlainText(model)
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Detector"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Signal detected"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Neuronal Nettwork"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Train"))

    def train_model(self):
        
        self.pushButton.setEnabled(False)
        self.label_2.setText('In process.....')
        epochs = self.spinBox.text()
        step_per_epochs = self.spinBox_2.text()
        
        self.conv_nnetwork.fit_model(int(epochs), int(step_per_epochs))
        
        self.label_2.setText('Finished OK')
        self.pushButton.setEnabled(True)
        self.pushButton_4.setEnabled(False)

    def open_video(self):
        
        self.dialog = QtWidgets.QFileDialog.getOpenFileNames()
        nameFile = os.path.split(self.dialog[0][0])[-1]
        root, extension = os.path.splitext(nameFile)

        if extension.lower() in self.fotoExtension:
            frame = cv.imread(self.dialog[0][0])
            if frame is None:
                raise TypeError("No se ha podido abrir la imagen. Revisar la ruta y volver a probar")
                
            im = self.preprocessing_image(frame)

            self.view_video(im)            
            
            self.label.setText(str(self.dialog[0][0]))
            
            
        if extension.lower() in self.videoExtension:
            self.pushButton_2.setEnabled(True)
            self.label.setText(str(self.dialog[0][0]))
        
            self.cap = cv.VideoCapture(self.dialog[0][0])
            self.progressBar.setProperty("value", 1)
            ret, frame = self.cap.read()
            if ret == True:          
                im = cv.resize(frame,self.FRAME_SIZE,interpolation = cv.INTER_AREA)
                im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
                                          
                self.view_video(im)

                position = self.cap.get(1)
                self.progressBar.setEnabled(True)
                self.progressBar.setValue(int(position))
             
          
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
            
    def play_video(self):
        
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.fps = self.cap.get(5)
        self.timer = QtCore.QTimer()
        self.fps = 1000/self.fps 
        self.timer.start(self.fps)                
        self.timer.timeout.connect(self.nextFrame)
        self.progressBar.setMaximum(self.cap.get(7)-1)
        
    
    def nextFrame(self):
        ret, frame = self.cap.read()
        if ret == True:          
            frame = cv.resize(frame,self.FRAME_SIZE,interpolation = cv.INTER_AREA)
            
            im = self.preprocessing_image(frame)

            self.view_video(im)

            position = self.cap.get(0)/self.fps
            self.progressBar.setValue(position)


    def stop_video(self):
        
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)
        self.timer.stop()

    
    def view_video(self, image):
        
        h, w, ch = image.shape
        qt_image = QtGui.QImage(image.data, w, h,w * ch, QtGui.QImage.Format_RGB888)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap.fromImage(qt_image))
        self.graphicsView.setFixedWidth(w+10)
        self.graphicsView.setFixedHeight(h+10)
        self.graphicsView.setScene(scene)
    

    def view_signal(self, image_signal):
        
        image_signal = cv.cvtColor(image_signal,cv.COLOR_BGR2RGB)
        
        h, w, ch = image_signal.shape
        signal = QtGui.QImage(image_signal.data, w, h, w * ch, QtGui.QImage.Format_RGB888)
        scene_signal = QtWidgets.QGraphicsScene()
        scene_signal.addPixmap(QtGui.QPixmap.fromImage(signal))
        self.graphicsView_2.setScene(scene_signal)
        
      
    def preprocessing_image(self, image):
        
        image_seg = segmentation(image)
        image_preprocess, images_signals, size_images_signals = image_seg.preprocessing()
        
        image_preprocess = cv.cvtColor(image_preprocess,cv.COLOR_BGR2RGB)
        self.view_video(image_preprocess)
        
        for i in range(len(images_signals)):
            
            signal = self.conv_nnetwork.predict_image(images_signals[i])
            if signal in self.signals.keys():
                cv.rectangle(image_preprocess,(size_images_signals[i][0],size_images_signals[i][1]),
                              (size_images_signals[i][0]+size_images_signals[i][2],size_images_signals[i][1]+size_images_signals[i][3]),
                              (0,255,0),2)
            self.label_5.setText(self.signals[signal])  
        
            self.view_signal(images_signals[i])
        
        return image_preprocess


if __name__ == "__main__":
    # import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

