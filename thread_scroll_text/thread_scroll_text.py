### インポート
import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
import time
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
import tkinter.font as tkFont
        
from chardet import detect 


class main_class():  
    def __init__(self, main):
        print ("__init__")  
        button1= Button(root, text=u'終了', command=self.quit)  
        button1.grid(row=0, column=1)  
        button1.place(x=300, y=30) 
        self.textExample=ScrolledText(root, height=30,width=120, wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=90, y=70)

        button3= Button(root, text=u'ファイル   選択', command=self.button3_clicked) 
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=30) 

        button4= Button(root, text=u'中断', command=self.button4_clicked)  
        button4.grid(row=0, column=1)  
        button4.place(x=250, y=30) 


    def method0(self,message):  
        print ("method0")  
        self.textExample.insert(tkinter.END,message)

    def thread_method(self):
        while(1):
            if(self.kill==1):
                break
            self.textExample.delete("1.0",tkinter.END)

            for name in self.filenames:
                if(self.kill==1):
                    break
    
                with open(name, 'rb') as f:  # バイナリファイルとしてファイルをオープン
                    b = f.read()  # ファイルの内容を全て読み込む

                enc = detect(b)
                self.encode_type=enc['encoding']
                with open(name,encoding=self.encode_type) as f:
                    if(self.kill==1):
                        break


                    lines = f.readlines()
                    for line in lines:
                        if(self.kill==1):
                            break

                        print(line, end='')
                        self.textExample.insert(tkinter.END,str(line)+"\n")
                        time.sleep(0.5)
                        self.textExample.yview_moveto(1)

    def button3_clicked(self):  


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Text file", ".txt")], initialdir=iDir)
        print(self.filenames)
        self.kill = 0  

        thread1 = threading.Thread(target=self.thread_method)
        thread1.start()


    def button4_clicked(self):
        self.kill = 1  




    def quit(self):
        print ("quit")  
        root.destroy()

root= tkinter.Tk()  
c=main_class(root)  
root.title("テキストスクロール")  
root.geometry("1000x500") 


root.mainloop()

