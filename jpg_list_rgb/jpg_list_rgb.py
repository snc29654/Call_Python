### インポート
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
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

        



#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.save_flag = 0;

        self.index_before = 0
        self.sizerate=1.0
        self.raterate=1.0
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        
        button1 = Button(root_main, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=670, y=12) 

        button3= Button(root_main, text=u'ファイル   選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=670, y=42) 




        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')

        label4 = tkinter.Label(root_main, text="サイズ倍率", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=400, y=28) 


    def key_handler(self,e):
    
        print(e.keycode)
        if(e.keycode==38):
            self.sizeup()
        if(e.keycode==40):
            self.sizedown()

        print(e.keycode)
        if(e.keycode==39):
            self.rateup()
        if(e.keycode==37):
            self.ratedown()



    def button1_clicked(self):  
        self.sizerate =txt4.get()
        

        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        #filenames = []
        self.filenames = glob.glob('*.jpg')
        print(self.filenames)
        self.quit()

    def button3_clicked(self):  
        self.sizerate =txt4.get()
        


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(self.filenames)
        self.quit()


    def quit(self):
        root_main.destroy()

 
    def get_index(self,event):

        value = tkinter.StringVar()
 
        index = event.widget.curselection()
        if (self.index_before==index):
            self.angle += 90
        self.index_before=index

        n = event.widget.get(index)
        self.n_old = n
        value.set(n)
        self.select_one_rgb(n)
        print("get_index=" + n)


    def list_disp(self,sub):
    
        frame = tkinter.Frame(master=None)
        scrollbar = tkinter.Scrollbar(master=frame, orient="vertical")
        listbox = tkinter.Listbox(master=frame,  bg="white", height=25, yscrollcommand=scrollbar.set)
        for name in self.filenames:
            listbox.insert(tkinter.END, name)
        scrollbar.config(command=listbox.yview)
        frame.pack(side=RIGHT, anchor=NW)
        scrollbar.pack(side=tkinter.RIGHT, fill="y")
        listbox.pack(side=tk.LEFT)
        listbox.bind("<<ListboxSelect>>", self.get_index)


    def view_image(self):
        global item, canvas


        sub = tkinter.Tk()
        sub.title("画像回転するには同じファイルを押下してください")  
        sub.geometry("800x650")



        button9 = tk.Button(sub, text = '拡大（↑）', command=self.sizeup)
        button9.grid(row=0, column=1)  
        button9.place(x=700, y=480) 

        button10 = tk.Button(sub, text = '縮小（↓）', command=self.sizedown)
        button10.grid(row=0, column=1)  
        button10.place(x=700, y=510) 

        button11 = tk.Button(sub, text = '荒く（->）', command=self.rateup)
        button11.grid(row=0, column=1)  
        button11.place(x=700, y=540) 

        button12 = tk.Button(sub, text = '細かく（<-）', command=self.ratedown)
        button12.grid(row=0, column=1)  
        button12.place(x=700, y=570) 


        button13 = tk.Button(sub, text = 'ファイル保存', command=self.savefile)
        button13.grid(row=0, column=1)  
        button13.place(x=500, y=570) 






        self.list_disp(sub)



        sub.bind("<KeyPress>", self.key_handler)
        sub.mainloop()
 
 




 

    def sizeup(self):
        self.sizerate = float(self.sizerate) + 0.1
        self.select_one_rgb(self.n_old)


    def sizedown(self):
        self.sizerate = float(self.sizerate) - 0.1
        self.select_one_rgb(self.n_old)


    def rateup(self):
        print(self.raterate)
        self.raterate = float(self.raterate) + 1
        self.select_one_rgb(self.n_old)


    def ratedown(self):
        print(self.raterate)
        if(self.raterate >1 ):
            self.raterate = float(self.raterate) - 1
        self.select_one_rgb(self.n_old)


    def savefile(self):
        self.save_flag = 1;
        self.select_one_rgb(self.n_old)




    def select_one_rgb(self,n):
        root_one = tkinter.Tk()
        root_one.title("root_oneです")  
        root_one.geometry("1x1")

        txt2 = tk.Entry(width=50)
        txt2.place(x=20, y=600)
        img2 = Image.open(n)
        before_x, before_y = img2.size[0], img2.size[1]
        x = int(round(float(300 / float(before_y) * float(before_x))))
        y = 300
        img2.thumbnail((x*float(self.sizerate), y*float(self.sizerate)), Image.ANTIALIAS)

        img2 = img2.rotate(
            self.angle,
            expand=True
        )



        image2 = img2.convert('RGB')


        width, height = image2.size


        print(width)
        print(height)
        for x in range(width):
            for y in range(height):
                if((int(y/5))%self.raterate)==0:
                        r, g, b = image2.getpixel((x, y))
                else:
                    pass
                image2.putpixel((x, y), (r, g, b))
        if (self.save_flag==1):
            image2.save("modify.jpg")
            self.save_flag=0

        img2 = ImageTk.PhotoImage(image2)




        canvas = tkinter.Canvas(width=600, height=500)
        canvas.place(x=0, y=0)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)
        root_one.after(10, lambda: root_one.destroy())
        root_one.mainloop()



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("850x100") 


txt4 = tkinter.Entry(width=10)
txt4.place(x=330, y=30)
txt4.insert(tkinter.END,"1.0")



root_main.mainloop()


thread1 = threading.Thread(target=c.view_image)
thread1.start()


