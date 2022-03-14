import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
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
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font
from tkinter.scrolledtext import ScrolledText




class color_button(ttk.Combobox):
    def __init__(self, var, master=None):

        self.end=0
        self.button_disp=0

# テキストボックス
        self.txt1 = tkinter.Entry(width=5)
        self.txt1.place(x=1000, y=150)
        self.txt1.insert(tkinter.END,"20")
        
        lbl1 = tkinter.Label(text='横数(x)')
        lbl1.place(x=950, y=150)
# テキストボックス
        self.txt2 = tkinter.Entry(width=5)
        self.txt2.place(x=1000, y=180)
        self.txt2.insert(tkinter.END,"25")

        lbl2 = tkinter.Label(text='縦数(y)')
        lbl2.place(x=950, y=180)

        self.txt3 = tkinter.Entry(width=5)
        self.txt3.place(x=1000, y=210)
        self.txt3.insert(tkinter.END,"8")

        lbl3 = tkinter.Label(text='サイズ')
        lbl3.place(x=950, y=210)




        self.counter=0
        self.r=100
        self.g=100
        self.b=100
        self.color="Red"
        li = ['Red', 'Blue', 'Yellow','Green', 'Black', 'White',
              'Gray', 'ivory', 'pink','violet', 'lawngreen', 'gold',     
              'cyan', 'lightgray','brown']     
        super().__init__(master, values=li) 
        
        self.filenames ="WS000232.JPG"


        

        
        button10 = Button(root, text=u'フォルダー選択', command=self.button10_clicked)  
        button10.grid(row=0, column=1)  
        button10.place(x=950, y=370) 

        button13= Button(root, text=u'ファイル選択', command=self.button13_clicked)  
        button13.grid(row=0, column=1)  
        button13.place(x=950, y=400) 
        
        button11 = Button(root, text=u'停止', command=self.button11_clicked)  
        button11.grid(row=0, column=1)  
        button11.place(x=950, y=430) 
        
        self.var = var                      
        self.bind(                          
            '<<ComboboxSelected>>',
            self.show_selected
            )


    def button3_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)

        if(self.filenames != ""):
            button4= Button(root, text=u'表示', font=24,command=self.button4_clicked,bg='#f0e68c')  
            button4.grid(row=0, column=1)  
            button4.place(x=950, y=110) 
 
            button4= Button(root, text=u'変換', font=24,command=self.button5_clicked,bg='#f0e68c')  
            button4.grid(row=0, column=1)  
            button4.place(x=1000, y=110) 

    def button8_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames3 = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)

    def button9_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames4 = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)


    def button11_clicked(self):  
        self.end=1

    def button13_clicked(self):  


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)

        if(self.filenames != ""):
            button4= Button(root, text=u'表示', font=24,command=self.button4_clicked,bg='#f0e68c')  
            button4.grid(row=0, column=1)  
            button4.place(x=950, y=110) 

    def button10_clicked(self):  
        

        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        self.filenames = []
        self.filenames = glob.glob('*.jpg')
        print(self.filenames)

        if(self.filenames != ""):
            button4= Button(root, text=u'表示', font=24,command=self.button4_clicked,bg='#f0e68c')  
            button4.grid(row=0, column=1)  
            button4.place(x=950, y=110) 



    def button4_clicked(self):  
        self.button_disp=1
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button5_clicked(self):  
        self.f = open(r"C:\xampp\htdocs\xampp\shishu\color_code.txt", "w")
        self.button_disp=0
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button6_clicked(self):  
        exit (0)


    def show_selected(self, event):
        self.color = self.get()        
    def setnumber(self):
        
        font_size =int(self.txt3.get())

        column_max =int(self.txt1.get())
        row_max =int(self.txt2.get())
        btn=[0]*8100        
        first_flag=0
        for file in self.filenames:
            if(self.end==1):
                break

            first_flag += 1
            img10 = Image.open(file)
            image10 = img10.convert('RGB')
            width, height = image10.size

            column_step=int(width/column_max)        
            row_step=int(height/row_max)
            column = -1
            row = 0
            i=0
            for row in range(row_max):
                for column in range(column_max):
                    i=i+1
                    self.counter=str(i)


                    self.r, self.g, self.b = image10.getpixel((column*column_step, row*row_step))

                    text=f'{i}'
                    if (self.button_disp == 1):
                        if(first_flag==1):
                            btn[i] = tk.Button(root, text="  ",font=("", font_size))
                            btn[i].grid(column=column, row=row)
                            btn[i].config(command=self.collback(btn[i]),bg=self.from_rgb_to_colorcode((self.r, self.g, self.b)))

                        btn[i].grid(column=column, row=row)
                        btn[i].config(bg=self.from_rgb_to_colorcode((self.r, self.g, self.b)))





        if (self.button_disp == 0):
            self.f.close()
        self.counter="終了"
        self.end=1
        button6= Button(root, text=u'閉じる', font=8,command=self.button6_clicked)  
        button6.grid(row=0, column=1)  
        button6.place(x=950, y=500) 

    def collback(self,btn):
        def nothing():
            global color
            btn.config(bg=self.color)
        return nothing

    def from_rgb_to_colorcode(self,rgb):
        return "#%02x%02x%02x" % rgb
    
    def update_counter(self):
        while(1):
            self.lable = tkinter.Label(text=self.counter, width=8, height=2,font=('Helvetica', '20'), fg='white', bg='black')
            self.lable.place(x=950, y=300)
            if(self.end==1):
                break
            time.sleep(0.2)
                    
    
    
root = tk.Tk()
root.geometry('1100x750')
root.title("button color test")

var = tk.StringVar(master=root)
l = tk.Label(textvariable=var,font=48)
l.place(x=700,y=750)
c=color_button(master=root, var=var)
c.place(x=950,y=0)




root.mainloop()


