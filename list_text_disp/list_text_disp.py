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
        



#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.index_before = 0
        self.sizerate=10
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

        label4 = tkinter.Label(root_main, text="Fontサイズ", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=400, y=28) 


    def key_handler(self,e):
    
        print(e.keycode)
        if(e.keycode==38):
            pass
        if(e.keycode==40):
            pass

    def button1_clicked(self):  
        
        self.sizerate = txt4.get();

        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        #filenames = []
        self.filenames = glob.glob('*.txt')
        print(self.filenames)
        self.quit()

    def button3_clicked(self):  
        
        self.sizerate = txt4.get();


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Text file", ".txt")], initialdir=iDir)
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
        self.select_one_image(n)
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
        sub.title("テキストファイルの表示")  
        sub.geometry("1200x600")



        button9 = tk.Button(sub, text = 'ファイル書き込み', command=self.sizeup)
        button9.grid(row=0, column=1)  
        button9.place(x=700, y=480) 

        #button10 = tk.Button(sub, text = 'フォント小', command=self.sizedown)
        #button10.grid(row=0, column=1)  
        #button10.place(x=700, y=510) 








        self.list_disp(sub)



        sub.bind("<KeyPress>", self.key_handler)



        sub.mainloop()
 
 


    def select_one_image(self,n):


        root_one = tkinter.Tk()
        root_one.title("root_oneです")  
        root_one.geometry("1x1")

        frame2 = ttk.Frame(root_one, padding=10)
        frame2.grid()



        self.txt2 = tk.Entry(width=50)
        self.txt2.place(x=20, y=500)




        self.txt2.delete(0, tk.END)
        self.txt2.insert(tk.END,n)

        txt3 = tk.Entry(width=50)
        txt3.place(x=20, y=20)

        self.text_box = tk.Text(bg="#000", fg="#fff", insertbackground="#fff",
                   height=10)
        self.text_box.pack()
        self.text_box.place(x=20, y=20)
        fontExample = tkFont.Font(family="Courier", size=self.sizerate, weight="normal", slant="roman")

        self.text_box.configure(font=fontExample)


        #f = open(n, encoding="utf-8")
        #text_data = f.read()

        with open(n,encoding="utf-8") as f:


            lines = f.readlines()
            for line in lines:
                print(line, end='')
                self.text_box.insert(END, line)


        root_one.after(10, lambda: root_one.destroy())
        root_one.mainloop()


 

    def sizeup(self):
        get_data=self.text_box.get("1.0", "end")
        print(get_data)
        
        out_file=self.txt2.get()
        fout_utf = open(out_file, 'w', encoding='utf-8')
 
        for row in get_data:
            fout_utf.write(row)
 
        fout_utf.close()

    def sizedown(self):
        self.sizerate = self.sizerate - 1
        self.select_one_image(self.n_old)



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("850x300") 


txt4 = tkinter.Entry(width=10)
txt4.place(x=330, y=30)
txt4.insert(tkinter.END,"10")


root_main.mainloop()


thread1 = threading.Thread(target=c.view_image)
thread1.start()

    
