#フォルダー選択後インターバル時間間隔で表示
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
import random

interval = 1.0
sizerate = 1.0
filenames =[]


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("Image Viewer")  
        self.root.geometry("850x300") 


        self.txt2 = tkinter.Entry(width=10)
        self.txt2.place(x=10, y=30)
        self.txt2.insert(tkinter.END,"1.0")
        self.txt3 = tkinter.Entry(width=80)
        self.txt3.place(x=10, y=60)
        self.txt3.insert(tkinter.END,"")

        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=330, y=30)
        self.txt4.insert(tkinter.END,"1.0")




        button1 = Button(self.root, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=670, y=12) 



        button2 = tk.Button(self.root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=770, y=12) 

        button2 = tk.Button(self.root, text = '実行シャッフル', command=self.quitsh)
        button2.grid(row=0, column=1)  
        button2.place(x=770, y=42) 



        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')
        label2 = tkinter.Label(self.root, text="インターバル(秒）", fg="red", bg="white", font=font1)
        label2.pack(side="top")
        label2.place(x=100, y=28) 

        label4 = tkinter.Label(self.root, text="サイズ倍率", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=400, y=28) 

        self.root.mainloop() 

    def check_value(self):

        global interval

        self.txt3.delete(0, tk.END)      


        interval =self.txt2.get()
        global sizerate
        sizerate =self.txt4.get()
        
        if interval=="":
            self.txt3.insert(tkinter.END,str(interval)+"インターバルが未設定です。")
        else:
            self.txt3.insert(tkinter.END,str(interval)+"秒 に設定しています。" )

        if sizerate=="":
            self.txt3.insert(tkinter.END,str(sizerate)+"倍率が未設定です。")
        else:
            self.txt3.insert(tkinter.END,str(sizerate)+"倍に設定しています。" )

    def button1_clicked(self):  

        self.check_value()

        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        filenames = []
        filenames = glob.glob('*.jpg')
        print(filenames)


    def button3_clicked(self):  
        global filenames

        self.check_value()



        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)


    def quit(self):
        self.root.destroy()

    def quitsh(self):
        random.shuffle(filenames)
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

    def initial(self):
        #jpgの変更処理
        thread3 = threading.Thread(target=self.change_image)
        thread3.start()



    def view_image(self):
        global item, canvas
 
        self.root = tkinter.Tk()
        self.root.title('jpg viewer')
        self.root.geometry("1000x700")

        button4 = tk.Button(self.root, text = '停止', command=self.suspend)
        button4.grid(row=0, column=1)  
        button4.place(x=930, y=50) 

        button5 = tk.Button(self.root, text = '再開', command=self.resume)
        button5.grid(row=0, column=1)  
        button5.place(x=930, y=80) 

        button6 = tk.Button(self.root, text = '終了', command=self.quit)
        button6.grid(row=0, column=1)  
        button6.place(x=930, y=110) 

        button7 = tk.Button(self.root, text = '加速(->)', command=self.speedup)
        button7.grid(row=0, column=1)  
        button7.place(x=930, y=140) 

        button8 = tk.Button(self.root, text = '減速(<-)', command=self.speeddown)
        button8.grid(row=0, column=1)  
        button8.place(x=930, y=170) 

        button9 = tk.Button(self.root, text = '拡大(↑）', command=self.sizeup)
        button9.grid(row=0, column=1)  
        button9.place(x=930, y=200) 

        button10 = tk.Button(self.root, text = '縮小(↓)', command=self.sizedown)
        button10.grid(row=0, column=1)  
        button10.place(x=930, y=230) 

        button11 = tk.Button(self.root, text = '最初から', command=self.initial)
        button11.grid(row=0, column=1)  
        button11.place(x=930, y=260) 

        self.root.bind("<KeyPress>", self.key_handler)

        self.root.mainloop()
 
 
    def change_image(self):
        while(1):
            no=0
            for n in filenames:
                if(no%4==0):
                    if self.suspend_flag == 1:
                        while(1):
                            time.sleep(1)
                            if self.suspend_flag == 0:
                                break
                    img2 = Image.open(n)
                    before_x, before_y = img2.size[0], img2.size[1]
                    x = int(round(float(300 / float(before_y) * float(before_x))))
                    y = 300
                    img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
                    #img2 = img2.resize((900,600),Image.ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img2)
                    canvas = tkinter.Canvas(bg = "white", width=400, height=300)
                    canvas.place(x=0, y=0)
                    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                    print("size")
                    print(sizerate)
                    print("int")
                    print(interval)
                    int_interval=float(interval)
                    time.sleep(int_interval) 
                    canvas.itemconfig(item,image=img2)
                no=no+1






    def change_image2(self):
        while(1):
            no=0
            for n in filenames:
                if(no%4==1):
                    if self.suspend_flag == 1:
                        while(1):
                            time.sleep(1)
                            if self.suspend_flag == 0:
                                break
                    img2 = Image.open(n)
                    before_x, before_y = img2.size[0], img2.size[1]
                    x = int(round(float(300 / float(before_y) * float(before_x))))
                    y = 300
                    img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
                    #img2 = img2.resize((900,600),Image.ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img2)
                    canvas = tkinter.Canvas(bg = "white", width=400, height=300)
                    canvas.place(x=500, y=0)
                    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                    print("size")
                    print(sizerate)
                    print("int")
                    print(interval)
                    int_interval=float(interval)
                    time.sleep(int_interval) 
                    canvas.itemconfig(item,image=img2)
                no=no+1


    def change_image3(self):
        while(1):
            no=0
            for n in filenames:
                if(no%4==2):
                    if self.suspend_flag == 1:
                        while(1):
                            time.sleep(1)
                            if self.suspend_flag == 0:
                                break
                    img2 = Image.open(n)
                    before_x, before_y = img2.size[0], img2.size[1]
                    x = int(round(float(300 / float(before_y) * float(before_x))))
                    y = 300
                    img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
                    #img2 = img2.resize((900,600),Image.ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img2)
                    canvas = tkinter.Canvas(bg = "white", width=400, height=300)
                    canvas.place(x=0, y=300)
                    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                    print("size")
                    print(sizerate)
                    print("int")
                    print(interval)
                    int_interval=float(interval)
                    time.sleep(int_interval) 
                    canvas.itemconfig(item,image=img2)
                no=no+1


    def change_image4(self):
        while(1):
            no=0
            for n in filenames:
                if(no%4==3):
                    if self.suspend_flag == 1:
                        while(1):
                            time.sleep(1)
                            if self.suspend_flag == 0:
                                break
                    img2 = Image.open(n)
                    before_x, before_y = img2.size[0], img2.size[1]
                    x = int(round(float(300 / float(before_y) * float(before_x))))
                    y = 300
                    img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
                    #img2 = img2.resize((900,600),Image.ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img2)
                    canvas = tkinter.Canvas(bg = "white", width=400, height=300)
                    canvas.place(x=500, y=300)
                    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                    print("size")
                    print(sizerate)
                    print("int")
                    print(interval)
                    int_interval=float(interval)
                    time.sleep(int_interval) 
                    canvas.itemconfig(item,image=img2)
                no=no+1




    def quit(self):
        self.root.destroy()

image_gui()  

s=sub_gui()




#jpg表示画面を表示
thread1 = threading.Thread(target=s.view_image)
thread1.start()

thread3 = threading.Thread(target=s.change_image2)
thread3.start()

thread4 = threading.Thread(target=s.change_image3)
thread4.start()

thread5 = threading.Thread(target=s.change_image4)
thread5.start()


#jpgの変更処理
thread2 = threading.Thread(target=s.change_image)
thread2.start()
