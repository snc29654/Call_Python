import cv2
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font


class image_gui():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("mp4 to jpg")  
        self.root.geometry("400x100") 







        button3= Button(self.root, text=u'ファイル選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=42) 


        button2 = tk.Button(self.root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=100, y=12) 



        self.root.mainloop() 


    def button1_clicked(self):  


        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        filenames = []
        filenames = glob.glob('*.mp4')
        print(filenames)


    def button3_clicked(self):  
        global filenames


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("mpeg", ".mp4") ], initialdir=iDir)
        print(filenames)


    def quit(self):
        self.root.destroy()

class sub_gui():
    def __init__(self):
        self.suspend_flag = 0

    def key_handler(self,e):
        
        print(e.keycode)

        if(e.keycode==38):
            self.sizeup()
        if(e.keycode==40):
            self.sizedown()

        if(e.keycode==37):
            self.speeddown()
        if(e.keycode==39):
            self.speedup()



    def suspend(self):
        self.suspend_flag = 1
    def resume(self):
        self.suspend_flag = 0

    def speedup(self):
        global interval
        if(float(interval) > 0.1):
            interval = float(interval) - 0.1

    def speeddown(self):
        global interval
        interval = float(interval) + 0.1


    def sizeup(self):
        global sizerate
        sizerate = float(sizerate) + 0.1

    def sizedown(self):
        global sizerate
        sizerate = float(sizerate) - 0.1




 
 

    def quit(self):
        self.root.destroy()

image_gui()  

s=sub_gui()



def convert():
    global filenames

    file_list = glob.glob("../mp4jpg/*jpg")
 
    for file in file_list:
        print("remove：{0}".format(file))
        os.remove(file)

  
    
    for n in filenames:
        path_name = n
    movie_name = os.path.basename(path_name)
    print(movie_name)
    cap = cv2.VideoCapture(path_name)

    # 幅
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print('width : {:.0f} px'.format(width))
    # 高さ
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('height : {:.0f} px'.format(height))
    # 総フレーム数
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('number of frames : {:.0f}'.format(num_frame))
    # fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('fps : {:f}'.format(fps))

    count = 0
    while True:
        ret, frame = cap.read()
        if ret == True:
            count += 1
            # 画像を生成
            cv2.imwrite('../mp4jpg/{:s}_{:06d}.jpg'.format(movie_name, count), frame)
        else:
            break
        
convert()
