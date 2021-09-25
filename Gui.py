# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:17:31 2021

@author: eduardo.sanz
"""
import tkinter as tk
from tkinter import filedialog as fl
from PIL import ImageTk
import PIL.Image as im
from tkinter import * 
import cv2 as cv
#import imutils


"""
def open_doc():
    
    pic = fl.askopenfilename(initialdir="C:/Users/eduardo.sanz/Desktop/ficha y CV/UNIR/TFM")
    photo = PhotoImage(file=pic)
    img = Label(gui, image=photo)
    img.pack(side=LEFT)
    
    can = Canvas(gui)
    can.pack(fill=BOTH)
    can.create_image(400, 400, image=photo, anchor=NW)
     
    
    

gui = tk.Tk()
gui.title("Detección de señales")
gui.geometry("568x516")
menuBar = Menu(gui)
gui.config(menu=menuBar)
fileMenu = Menu(menuBar)
menuBar.add_cascade(label="Archivo", menu=fileMenu)
fileMenu.add_command(label="Abrir fichero", command=open_doc)
fileMenu.add_command(label="Salir", command=gui.destroy)

#se puede configurar el tamaño tambien : frame.config(width=400,height=300)
frame = Frame(gui, width=400, height=400)
frame.config(bd=4)
frame.config(cursor="")
frame.config(relief="sunken")
frame.pack(side=LEFT)



botonOpen = Button(gui, text="open", command=open_doc)
botonOpen.pack(side=RIGHT)

#(photo = PhotoImage(file='./setosa.png')
#img = Label(gui, image=photo)
#img.pack(side=TOP)


#img = fl.askopenfile(mode="r",initialdir="/")
#img = Image.open(pic)
#print(img)
#im = Image.open('minion.jpg')
#img = ImageTk.PhotoImage(im)
#label = Label(gui,image=img).place(x=0,y=0)
#label.pack()

gui.mainloop()
"""

class Window:
    'Clase para crear el interfaz de usuraio'
    
    cap = None 
    stop = False
    #paa saber si hemos apretado el botón de pause
    pause = False
    #directorio del video
    video_pat = ""
    
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.title("Detección de señales")
        self.gui.geometry("980x620")
        menuBar = tk.Menu(self.gui)
        self.gui.config(menu=menuBar)
        fileMenu = tk.Menu(menuBar)
        menuBar.add_cascade(label="Archivo", menu=fileMenu)
        fileMenu.add_command(label="Abrir Imagen", command=self.open_img)
        fileMenu.add_command(label="Abrir Video", command=self.open_video)
        fileMenu.add_separator()
        fileMenu.add_command(label="Salir", command=self.gui.destroy)
        
        #texto para la imagen principal
        mainLabel= tk.Label(self.gui, text="Video/Imagen a reproducir")
        mainLabel.grid(row=1, column=0, padx=5, pady=5, columnspan=3)      
        
        #se puede configurar el tamaño tambien : frame.config(width=400,height=300)
        #frame para la imagen o video que se quiere reproducir
        self.mainFrame = tk.Frame(self.gui, width=600, height=500)
        self.mainFrame.config(bd=4)
        self.mainFrame.config(cursor="")
        self.mainFrame.config(relief="sunken")
        self.mainFrame.grid(row=2,column=0, padx=5,pady=5, rowspan=4, columnspan=3)
        
        botonOpenImg = tk.Button(self.gui, text="Abrir Imagen", command=self.open_img)
        botonOpenImg.grid(row=2,column=3)
        botonOpenVideo = tk.Button(self.gui, text="Abrir Video", command=self.open_video)
        botonOpenVideo.grid(row=2,column=4)
        
        #frame para la imagen de la señal que se ve en el video o imagen
        self.originalFrame = tk.Frame(self.gui, width=200, height=200)
        self.originalFrame.config(bd=4)
        self.originalFrame.config(relief="sunken")
        self.originalFrame.grid(row=4,column=3,columnspan=2)
        
        #texto para la imagen original
        originLabel= tk.Label(self.gui, text="Imagen de señal encontrada")
        originLabel.grid(row=3, column=3, columnspan=2)
        
        #texto para la escibir lo que se quieran debajo de la imagen original
        originLabel= tk.Label(self.gui, text="Nombre de la señal encontrada")
        originLabel.grid(row=5, column=3, columnspan=2)
        
        #botones para el video
        botonPlay = tk.Button(self.gui, text="Play", command=self.play_video)
        botonPlay.grid(row=6,column=0)
        botonStop = tk.Button(self.gui, text="Stop", command=self.stop_video)
        botonStop.grid(row=6,column=1)
        botonPause = tk.Button(self.gui, text="Pause", command=self.pause_video)
        botonPause.grid(row=6,column=2)
        
        self.gui.mainloop()        
    
    def open_img(self):
    
        pic = fl.askopenfilename(initialdir="C:/Users/eduardo.sanz/Desktop/ficha y CV/UNIR/TFM")
        photo = ImageTk.PhotoImage(file=pic)
        label = tk.Label(self.mainFrame, image=photo, width=600, height=500)
        label.grid(row=0,column=0)
   
        self.gui.mainloop()
    
    def open_video(self):
        
        self.video_path = fl.askopenfilename(initialdir="C:/Users/eduardo.sanz/Desktop/ficha y CV/UNIR/TFM", 
                                             filetypes=[("all video format",".mp4"),
                                            ("all video format",".avi")])
        self.cap = cv.VideoCapture(self.video_path)
        ret, frame = self.cap.read()
        if ret == True:
            frame = cv.resize(frame,(600,500),interpolation = cv.INTER_AREA)
            frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            imFrame = im.fromarray(frame)
            img = ImageTk.PhotoImage(image=imFrame)
            
            label = tk.Label(self.mainFrame, image=img)
            label.grid(row=0,column=0)
                
        self.gui.mainloop()

    def play_video(self):
            
        if self.pause == False and self.stop == False:
            ret, frame = self.cap.read()
            if ret == True:
                frame = cv.resize(frame,(600,500),interpolation = cv.INTER_AREA)
                frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                imFrame = im.fromarray(frame)
                img = ImageTk.PhotoImage(image=imFrame)               
                label = tk.Label(self.mainFrame, image=img)
                label.grid(row=0,column=0)
                label.configure(image=img)
                label.image = img
                label.after(10, self.play_video)  
        else:
             #comprobamos que botón se ha pulsado
             if self.pause == True and self.stop == False:
                 self.pause = False
             elif self.stop == True and self.pause == False:
                 self.stop = False
             else:
                 self.pause = False
                 self.stop = False
             self.play_video        
            
        self.gui.mainloop()
        
    def stop_video(self):
               
        self.cap.release()
        if self.stop == False:
            self.stop = True
            
            self.cap = cv.VideoCapture(self.video_path)
            ret, frame = self.cap.read()
            if ret == True:
                frame = cv.resize(frame,(600,500),interpolation = cv.INTER_AREA)
                frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                imFrame = im.fromarray(frame)
                img = ImageTk.PhotoImage(image=imFrame)
                label = tk.Label(self.mainFrame, image=img)
                label.grid(row=0,column=0)
        
        self.gui.mainloop()
                
    def pause_video(self):
        
        if self.pause == False:
            self.pause = True          
            
        self.gui.mainloop()
