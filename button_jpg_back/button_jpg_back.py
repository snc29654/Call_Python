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
        self.mono=0
# テキストボックス
        self.txt1 = tkinter.Entry(width=5)
        self.txt1.place(x=1000, y=150)
        self.txt1.insert(tkinter.END,"80")
        
        lbl1 = tkinter.Label(text='横数(x)')
        lbl1.place(x=950, y=150)
# テキストボックス
        self.txt2 = tkinter.Entry(width=5)
        self.txt2.place(x=1000, y=180)
        self.txt2.insert(tkinter.END,"100")

        lbl2 = tkinter.Label(text='縦数(y)')
        lbl2.place(x=950, y=180)





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
        

        button3= Button(root, text=u'ファイル選択', font=24,command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=950, y=30) 
        
    
        
        
        
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
            button4.place(x=950, y=300) 
 
            button5= Button(root, text=u'変換', font=24,command=self.button5_clicked,bg='#f0e68c')  
            button5.grid(row=0, column=1)  
            button5.place(x=1020, y=300) 

            button6= Button(root, text=u'白黒変換', font=24,command=self.button6_clicked,bg='#f0e68c')  
            button6.grid(row=0, column=1)  
            button6.place(x=950, y=350) 

            button7= Button(root, text=u'赤変換', font=24,command=self.button7_clicked,bg='#f0e68c')  
            button7.grid(row=0, column=1)  
            button7.place(x=950, y=400) 

            button8= Button(root, text=u'緑変換', font=24,command=self.button8_clicked,bg='#f0e68c')  
            button8.grid(row=0, column=1)  
            button8.place(x=950, y=450) 

            button9= Button(root, text=u'青変換', font=24,command=self.button9_clicked,bg='#f0e68c')  
            button9.grid(row=0, column=1)  
            button9.place(x=950, y=500) 

    def button4_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.button_disp=1
        self.mono=0
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button5_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.button_disp=0
        self.mono=0
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()


    def button6_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.mono=1
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button7_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.mono=2
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button8_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.mono=3
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def button9_clicked(self):  
        self.f = open(r"color_code.txt", "w")
        self.mono=4
        thread1 = threading.Thread(target=self.setnumber)
        thread1.start()
        thread2 = threading.Thread(target=self.update_counter)
        thread2.start()

    def show_selected(self, event):
        self.color = self.get()        
    def setnumber(self):
        
        column_max =int(self.txt1.get())
        row_max =int(self.txt2.get())
        for file in self.filenames:
            img2 = Image.open(file)
        image2 = img2.convert('RGB')
        width, height = image2.size

        column_step=int(width/column_max)        
        row_step=int(height/row_max)
        print(width, height)
        print(column_step,row_step)
                
        column = -1
        row = 0
        for i in range(column_max*row_max+1):
            self.counter=str(i)
            if i > 0:
                if i%column_max == 1:
                    row += 1 
                    column = -1
                column += 1


                self.r, self.g, self.b = image2.getpixel((column*column_step, row*row_step))

                text=f'{i}'
                if (self.button_disp == 1):
                    btn = tk.Button(root, text="    ")
                    btn.grid(column=column, row=row)
                    btn.config(command=self.collback(btn),bg=self.from_rgb_to_colorcode((self.r, self.g, self.b)))
                elif(self.mono==0):    
                    self.f.write(self.from_rgb_to_colorcode((self.r, self.g, self.b))+"\n")
                elif(self.mono==1):    
                    self.f.write(self.from_rgb_to_colorcode((self.r, self.r, self.r))+"\n")
                elif(self.mono==2):    
                    self.f.write(self.from_rgb_to_colorcode((self.r, 0, 0))+"\n")
                elif(self.mono==3):    
                    self.f.write(self.from_rgb_to_colorcode((0, self.g, 0))+"\n")
                else:
                    self.f.write(self.from_rgb_to_colorcode((0, 0, self.r))+"\n")
                    
        self.f.close()
        self.counter="end"
        self.end=1
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
            self.lable.place(x=950, y=210)
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
