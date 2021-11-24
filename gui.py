# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from photo.photo import photo
# from cnn.cnn import cnn
from image.image import image
import cv2 as cv
import os
import sys

class Ui_MainWindow(object):
    
    videoExtension = [".mp4",".avi"]
    fotoExtension = [".jpeg",".jpg",".png"]
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 749)
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(710, 100, 441, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutSignal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutSignal.setContentsMargins(0, 0, 0, 0)
        self.layoutSignal.setObjectName("layoutSignal")
        self.signal = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.signal.setMaximumSize(QtCore.QSize(400, 25))
        self.signal.setText("")
        self.signal.setObjectName("signal")
        self.layoutSignal.addWidget(self.signal)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(710, 200, 441, 471))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layoutViewSignal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layoutViewSignal.setContentsMargins(0, 0, 0, 0)
        self.layoutViewSignal.setObjectName("layoutViewSignal")
        self.scrollArea = QtWidgets.QScrollArea(self.horizontalLayoutWidget_2)
        self.scrollArea.setMaximumSize(QtCore.QSize(250, 250))
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 246, 246))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.layoutViewSignal.addWidget(self.scrollArea)
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
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))


    def open_video(self):
        
        self.dialog = QtWidgets.QFileDialog.getOpenFileNames()
        nameFile = os.path.split(self.dialog[0][0])[-1]
        root, extension = os.path.splitext(nameFile)

        if extension.lower() in self.fotoExtension:
            frame = cv.imread(self.dialog[0][0])
            if frame is None:
                raise TypeError("No se ha podido abrir la imagen. Revisar la ruta y volver a probar")
                
            img = image(frame)
            image_contours = img.preprocessing()
            im = cv.cvtColor(image_contours,cv.COLOR_BGR2RGB)

            h, w, ch = im.shape
            qt_image = QtGui.QImage(im.data, w, h,w * ch, QtGui.QImage.Format_RGB888)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap.fromImage(qt_image))
            self.graphicsView.setScene(scene)
            
            self.label.setText(str(self.dialog[0][0]))
                      
        if extension.lower() in self.videoExtension:
            self.pushButton_2.setEnabled(True)
            self.label.setText(str(self.dialog[0][0]))
        
            self.cap = cv.VideoCapture(self.dialog[0][0])
            self.progressBar.setProperty("value", 1)
            ret, frame = self.cap.read()
            if ret == True:          
                im = cv.resize(frame,(687,429),interpolation = cv.INTER_AREA)
                
                img = image(frame)
                image_contours = img.preprocessing()
                im = cv.cvtColor(image_contours,cv.COLOR_BGR2RGB)
                                          
                h, w, ch = im.shape
                img = QtGui.QImage(im.data, w, h, w * ch, QtGui.QImage.Format_RGB888)
                scene = QtWidgets.QGraphicsScene()
                scene.addPixmap(QtGui.QPixmap.fromImage(img))
                self.graphicsView.setScene(scene)
                position = self.cap.get(1)
                self.progressBar.setValue(int(position))
             
            
            
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
            
            img = image(frame)
            image_contours = img.preprocessing()
            im = cv.cvtColor(image_contours,cv.COLOR_BGR2RGB)
        
            h, w, ch = im.shape
            img = QtGui.QImage(im.data, w, h, w * ch, QtGui.QImage.Format_RGB888)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap.fromImage(img))
            self.graphicsView.setScene(scene)
            position = self.cap.get(0)/self.fps
            self.progressBar.setValue(position)


    def stop_video(self):
        
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)
        self.timer.stop()


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

