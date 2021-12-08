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
# import numpy as np

class Ui_MainWindow(object):
    
    videoExtension = [".mp4",".avi"]
    fotoExtension = [".jpeg",".jpg",".png"]
    
    signals = {0: 'Velocidad maxima 20',1: 'Velocidad maxima 30', 2: 'Velocidad maxima 50', 3: 'Velocidad maxima 60', 4: 'Velocidad maxima 70', 
               5: 'Velocidad maxima 80', 6: 'Fin velocidad maxima 80', 7: 'Velocidad maxima 100', 8: 'Velocidad maxima 120', 9: 'Adelantamiento prohibido', 
               10: 'Adelantamiento prohibido camiones ', 11: 'Interseccion con prioridad', 12: '', 13: 'Ceda el paso', 14: 'Stop',
               15: 'Circulacion prohibida', 16: '', 17: 'Prohibido el paso', 18: 'Otros peligros', 19: 'Curva peligrosa hacia izquierda',
               20: 'Curva peligrosa hacia derecha', 21: 'Curvas peligrosa hacia izquierda', 22: 'Perfil irregular', 23: 'Pavimento deslizante', 24: 'Estrechamiento carril derecho',
               25: 'Obras', 26: 'Semaforo', 27: 'Paso peatones', 28: 'Niños', 29: 'Bicicletas', 30: 'Hielo', 31: 'Paso animales en libertad', 32: 'Fin restricciones',
               33: 'Sentido obligatorio derecha', 34: 'Sentido obligatorio izquierda', 35: 'Sentido obligatorio', 36: 'Unica dirección permitida', 37: 'Unica dirección permitida',
               38: 'Paso obligatorio', 39: 'Paso obligatorio', 40: 'Rotonda', 41: 'Fin adelantamiento prohibido', 42: 'Fin adelantamiento prohibido camiones'}
    
    def setupUi(self, MainWindow):      
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 749)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1141, 91))
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 530, 701, 141))
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
        self.pushButton_2.setEnabled(False)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 10, 97, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.progressBar = QtWidgets.QProgressBar(self.groupBoxButtons)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 681, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutButtons.addWidget(self.groupBoxButtons)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(720, 100, 431, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutSignal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutSignal.setContentsMargins(0, 0, 0, 0)
        self.layoutSignal.setObjectName("layoutSignal")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 140, 100, 30))
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
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, -1, 111, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setEnabled(True)
        self.label_3.setText("Epochs")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(110, 0, 321, 61))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit.setMaximumSize(QtCore.QSize(220, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit.setText('30')
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 60, 111, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Step per epochs")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(110, 60, 311, 61))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(220, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('60')
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(128, 139, 211, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutSignal.addWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(730, 310, 421, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layoutViewSignal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layoutViewSignal.setContentsMargins(0, 0, 0, 0)
        self.layoutViewSignal.setObjectName("layoutViewSignal")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.layoutViewSignal.addWidget(self.label_5)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(770, 370, 341, 241))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.verticalLayoutWidget_8)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_6.addWidget(self.graphicsView_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.pushButton.clicked.connect(self.open_video)
        self.pushButton_2.clicked.connect(self.play_video)
        self.pushButton_3.clicked.connect(self.stop_video)
        self.pushButton_4.clicked.connect(self.train_model)

        self.conv_nnetwork = convolutional_nnetwork()         
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Train"))

    def train_model(self):
        
        self.label_2.setText('Training neuronal network')
        epochs = self.lineEdit.text()
        step_per_epochs = self.lineEdit_2.text()
        
        self.conv_nnetwork.fit_model(int(epochs), int(step_per_epochs))
        self.label_2.setText('Training finished OK')

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
                im = cv.resize(frame,(687,429),interpolation = cv.INTER_AREA)
                im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
                                          
                self.view_video(im)

                position = self.cap.get(1)
                self.progressBar.setValue(int(position))
             
          
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
            
    def play_video(self):
        
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.fps = self.cap.get(5)
        self.timer = QtCore.QTimer()
        self.fps = 1000/self.fps #(int(self.cap.get(7))/int(fps)) * 1000
        self.timer.start(self.fps)                
        self.timer.timeout.connect(self.nextFrame)
        self.progressBar.setMaximum(self.cap.get(7)-1)
        
    
    def nextFrame(self):
        ret, frame = self.cap.read()
        if ret == True:          
            frame = cv.resize(frame,(687,429),interpolation = cv.INTER_AREA)
            
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
        self.graphicsView.setScene(scene)
    

    def view_signal(self, image_signal):
        
        image_signal = cv.cvtColor(image_signal,cv.COLOR_BGR2RGB)
        
        h, w, ch = image_signal.shape
        signal = QtGui.QImage(image_signal.data, w, h, w * ch, QtGui.QImage.Format_RGB888)
        scene_signal = QtWidgets.QGraphicsScene()
        scene_signal.addPixmap(QtGui.QPixmap.fromImage(signal))
        self.graphicsView_2.setFixedWidth(w+10)
        self.graphicsView_2.setFixedHeight(h+10)
        self.graphicsView_2.setScene(scene_signal)
        
      
    def preprocessing_image(self, image):
        
        img = segmentation(image)
        img, image_signal, x,y,w,h = img.preprocessing()
            
        signal = self.conv_nnetwork.predict_image(image_signal)
            
        cv.rectangle(img,(x-10,y-10),(x+w+10,y+h+10),(0,255,0),2)
        self.label_5.setText(self.signals[signal])  
        
        im = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        
        self.view_signal(image_signal)
        
        return im


if __name__ == "__main__":
    # import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

