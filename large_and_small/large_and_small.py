### インポート
import pygame
from pygame.locals import *
import time
import threading


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

interval = 1.0
sizerate = 1.0
filenames =[]


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("Image Viewer")  
        self.root.geometry("300x100") 






        button3= Button(self.root, text=u'ファイル選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=10) 


        button2 = tk.Button(self.root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=200, y=10) 



        self.root.mainloop() 

    def check_value(self):

        global interval



        

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
        self.root.geometry("1000x650")

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
            for n in filenames:
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
                canvas = tkinter.Canvas(bg = "white", width=900, height=600)
                canvas.place(x=0, y=0)
                item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                print("size")
                print(sizerate)
                print("int")
                print(interval)
                int_interval=float(interval)
                time.sleep(int_interval) 
                canvas.itemconfig(item,image=img2)

    def quit(self):
        self.root.destroy()

image_gui()  





### 定数
WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ
RATE   = 1.01        # 倍率
#####################
### 写真表示関数
#####################
def test_thread():
    global scale
    while(1):
        while(scale >0.1):
            scale /= RATE
            time.sleep(0.01)
        while(scale < 0.4):
            scale *= RATE
            time.sleep(0.01)
def image_view():
    ### 画面初期化
    surface.fill((0,0,0))
    ### サイズ変更
    img = pygame.transform.rotozoom(img_org, 0, scale)
    ### 写真表示
    surface.blit(img, (int((WIDTH-img.get_width())/2), 
    int((HEIGHT-img.get_height())/2)))
    ### 画面更新
    pygame.display.update()




def view_image():
    ### モジュール初期化
    ### 画面設定
    ### 写真表示
    image_view()
    thread1 = threading.Thread(target=test_thread) 
    thread1.start()
    ### 無限ループ
    while True:
        image_view()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:   # 終了
                    break
        else:
            continue
        ### whileループ終了
        break
    ### 終了処理
    pygame.quit()
    
    
pygame.init()
for n in filenames:
    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    ### 写真読み込み
    img_org = pygame.image.load(n)
    ### 初期スケール設定
    scale = HEIGHT/img_org.get_height()
    view_image()    
