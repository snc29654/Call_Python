#!/usr/bin/python3
from tkinter.scrolledtext import ScrolledText
import tkinter
import tkinter as tk
import tkinter.simpledialog as sd
import sqlite3
from contextlib import closing
from tkinter import filedialog
from tkinter import filedialog as tkFileDialog
import os
from PIL import Image, ImageTk
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog as tkFileDialog
import tkinter as tk
import glob
import threading
import time


wf = 'C:\\jpg\\write.jpg' #書き込み画像ファイルパス

class main_window(tk.Frame):


    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.sizerate=1.0
        self.sizevalid=0
        self.label = tk.Label(master,text="sqlite3 jpg test")
        self.label.pack()
        
        button1 = tk.Button(root, text = 'DB読み出し', command=self.read_db)
        button1.pack() 
        button1.place(x=280, y=90)

        button7 = tk.Button(root, text = 'DB更新', command=self.update_db)
        button7.pack() 
        button7.place(x=360, y=90)

        button12 = tk.Button(root, text = '検索', command=self.srch_db)
        button12.pack() 
        button12.place(x=390, y=18)

        button13 = tk.Button(root, text = '検索', command=self.srch_db2)
        button13.pack() 
        button13.place(x=390, y=38)

        button14 = tk.Button(root, text = '検索', command=self.srch_db3)
        button14.pack() 
        button14.place(x=390, y=58)
        
        button2 = tk.Button(root, text = 'DB書き込み', command=self.write_db)
        button2.pack() 
        button2.place(x=200, y=90)


        #button11 = tk.Button(root, text = 'DB書き込み', command=self.write_db_folder)
        #button11.pack() 
        #button11.place(x=200, y=115)

        button3 = tk.Button(root, text = '表示クリア', command=self.text_clear)
        button3.pack() 
        button3.place(x=480, y=90)

        button4 = tk.Button(root, text = 'DB消去', command=self.clear_db)
        button4.pack() 
        button4.place(x=560, y=90)


        self.textExample=ScrolledText(root, height=10,width=75, wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=80, y=150)
        
        self.txt1= tkinter.Entry(width=50)
        self.txt1.place(x=80, y=20)
        self.txt1.insert(tkinter.END,"コメント1")

        self.txt2= tkinter.Entry(width=50)
        self.txt2.place(x=80, y=40)
        self.txt2.insert(tkinter.END,"コメント2")

        self.txt3= tkinter.Entry(width=50)
        self.txt3.place(x=80, y=60)
        self.txt3.insert(tkinter.END,"コメント3")

        self.txt4= tkinter.Entry(width=10)
        self.txt4.place(x=450, y=20)
        self.txt4.insert(tkinter.END,"検索キー")

        self.txt7= tkinter.Entry(width=20)
        self.txt7.place(x=530, y=20)
        self.txt7.insert(tkinter.END,"original.db")


        self.txt5= tkinter.Entry(width=10)
        self.txt5.place(x=450, y=40)
        self.txt5.insert(tkinter.END,"検索キー")

        self.txt6= tkinter.Entry(width=10)
        self.txt6.place(x=450, y=60)
        self.txt6.insert(tkinter.END,"検索キー")

        button5= tk.Button(root, text=u'jpgファイル選択', command=self.button5_clicked)  
        button5.pack() 
        button5.place(x=100, y=90) 


        button15= tk.Button(root, text=u'jpgプレビュー', command=self.button15_clicked)  
        button15.pack() 
        button15.place(x=100, y=120) 



        button9 = tk.Button(root, text = '拡大（↑）', command=self.sizeup)
        button9.pack()  
        button9.place(x=700, y=480) 

        button10 = tk.Button(root, text = '縮小（↓）', command=self.sizedown)
        button10.pack()  
        button10.place(x=700, y=510) 
        self.txt7.get()
        self.dbname = '../'+self.txt7.get()
        
        
        self.dir = 0

        self.frame = tkinter.Frame(master=None)
        scrollbar = tkinter.Scrollbar(master=self.frame, orient="vertical")
        self.listbox = tkinter.Listbox(master=self.frame,  bg="white", height=10, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.frame.pack(side=RIGHT, anchor=NW)
        scrollbar.pack(side=tkinter.RIGHT, fill="y")
        self.listbox.pack(side = tk.TOP)
        self.listbox.bind("<<ListboxSelect>>", self.get_index)

    def dbwrite(self):
        self.dbname = '../'+self.txt7.get()
        #DBコネクト​
        #データインサート​
        sql = 'insert into users (data1, data2, data3, path, data_jpg) values (?,?,?,?,?)'
        user = (self.data1, self.data2, self.data3, self.path, self.data_jpg)
        self.c.execute(sql, user)
        self.conn.commit()





    def dbclear(self):
     self.dbname = '../'+self.txt7.get()
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'delete from users'
        #user = (1, self.data1, self.data2, self.data3)
        c.execute(sql)
        conn.commit()
        conn.close()

        self.textExample.insert(tkinter.END,"\n")
        self.textExample.insert(tkinter.END,"DB消去しました")

    def delete_one(self):
     self.dbname = '../'+self.txt7.get()
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'delete from users where id ='+'"'+str(self.id)+'"'
        #user = (1, self.data1, self.data2, self.data3)
        c.execute(sql)
        conn.commit()
        conn.close()

        self.textExample.insert(tkinter.END,"\n")
        self.textExample.insert(tkinter.END,"1レコード消去しました")
        self.button6.destroy()


    def dbupdate(self):
     self.dbname = '../'+self.txt7.get()
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #データインサート​
        sql = 'update users set data1 = '+ '"'+str(self.data1)+'"'+ ' where id ='+' "'+str(self.id)+'";'
        c.execute(sql)
        conn.commit()
        sql = 'update users set data2 = '+ '"'+str(self.data2)+'"'+ ' where id ='+' "'+str(self.id)+'";'
        c.execute(sql)
        conn.commit()
        sql = 'update users set data3 = '+ '"'+str(self.data3)+'"'+ ' where id ='+' "'+str(self.id)+'";'
        c.execute(sql)
        conn.commit()
        conn.close()

        self.textExample.insert(tkinter.END,"\n")
        self.textExample.insert(tkinter.END,"更新しました")
        self.button6.destroy()


            
    def dbread(self):
     self.dbname = '../'+self.txt7.get()
     wf = 'C:\\jpg\\write.jpg' #書き込み画像ファイルパス
  
  
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        self.textExample.delete("1.0",tkinter.END)



        self.listbox.delete(0, tkinter.END)
        for row in c.execute('select id ,data1 ,data2, data3, path from users'):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)
            self.textExample.yview_moveto(1)


        for row in c.execute('select id ,data1 ,data2, data3, path from users'):
            self.listbox.insert(tkinter.END, row[0])


    def dbsrch(self):
     self.dbname = '../'+self.txt7.get()
     wf = 'C:\\jpg\\write.jpg' #書き込み画像ファイルパス
  
  
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        self.textExample.delete("1.0",tkinter.END)


        select_sql = 'select id ,data1 ,data2, data3, path  from users where data1 like '+'"%'+str(self.match_word)+'%"'

        self.listbox.delete(0, tkinter.END)
        for row in c.execute(select_sql):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)


        for row in c.execute(select_sql):
            self.listbox.insert(tkinter.END, row[0])

    def dbsrch2(self):
     self.dbname = '../'+self.txt7.get()
     wf = 'C:\\jpg\\write.jpg' #書き込み画像ファイルパス
  
  
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        self.textExample.delete("1.0",tkinter.END)


        select_sql = 'select id ,data1 ,data2, data3, path  from users where data2 like '+'"%'+str(self.match_word2)+'%"'

        self.listbox.delete(0, tkinter.END)
        for row in c.execute(select_sql):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)


        for row in c.execute(select_sql):
            self.listbox.insert(tkinter.END, row[0])


    def dbsrch3(self):
     self.dbname = '../'+self.txt7.get()
     wf = 'C:\\jpg\\write.jpg' #書き込み画像ファイルパス
  
  
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        self.textExample.delete("1.0",tkinter.END)


        select_sql = 'select id ,data1 ,data2, data3, path  from users where data3 like '+'"%'+str(self.match_word3)+'%"'

        self.listbox.delete(0, tkinter.END)
        for row in c.execute(select_sql):
            blob = row[0]
            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,row)


        for row in c.execute(select_sql):
            self.listbox.insert(tkinter.END, row[0])



    def jpgread(self):
     self.dbname = '../'+self.txt7.get()
        
     #self.id =self.txt4.get()
   
     self.sizevalid=1

  
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        #表示​
        #self.textExample.delete("1.0",tkinter.END)


        for row in c.execute('select * from users where id ='+'"'+str(self.id)+'"'):
            data1 = row[1]
            data2 = row[2]
            data3 = row[3]
            blob =  row[5]
        self.txt1.delete(0, tk.END)         
        self.txt1.insert(tkinter.END,data1)
        self.txt2.delete(0, tk.END)         
        self.txt2.insert(tkinter.END,data2)
        self.txt3.delete(0, tk.END)         
        self.txt3.insert(tkinter.END,data3)

        with open(wf, 'wb') as f:
            f.write(blob)

        self.select_one_image(wf)




    def write_db(self):
        self.dbname = '../'+self.txt7.get()
        global filenames

        if(self.dir==0):
            self.textExample.insert(tkinter.END,"jpgが未指定\n")
            return

        self.data1 =self.txt1.get()
        self.data2 =self.txt2.get()
        self.data3 =self.txt3.get()
        
        thread1 = threading.Thread(target=self.dbwrite_thread)
        thread1.start()

        
    def dbwrite_thread(self):
        
     self.dbname = '../'+self.txt7.get()
     #DBコネクト​
     with closing(sqlite3.connect(self.dbname)) as self.conn:
        self.c = self.conn.cursor()
        create_table = '''create table users (id integer primary key autoincrement, data1 varchar(64),
                      data2 varchar(64), data3 varchar(64),path varchar(64),data_jpg img)'''
        #テーブルクリエイト​
        try:
            self.c.execute(create_table)
        except:
            pass
        
        
        for file in self.filenames:
            file_c = file.replace('\\', '\\\\');

            self.path=file_c


            self.textExample.insert(tkinter.END,"\n")
            self.textExample.insert(tkinter.END,file_c)
            self.textExample.yview_moveto(1)
        
            with open(file_c, 'rb') as f:
                self.data_jpg = f.read()

            self.dbwrite()
 
        self.conn.close()
    
    def read_db(self):
        thread2 = threading.Thread(target=self.dbread)
        thread2.start()


    def srch_db(self):
        self.match_word =self.txt4.get()
        self.dbsrch()
    def srch_db2(self):
        self.match_word2 =self.txt5.get()
        self.dbsrch2()
    def srch_db3(self):
        self.match_word3 =self.txt6.get()
        self.dbsrch3()


    def read_jpg(self):
        self.jpgread()



    def clear_db(self):
        self.dbclear()

    def update_db(self):
        self.data1 =self.txt1.get()
        self.data2 =self.txt2.get()
        self.data3 =self.txt3.get()
        self.dbupdate()

    def text_clear(self):
        self.textExample.delete("1.0",tkinter.END)


    def select_one_image(self,n):

        img2 = Image.open(n)
        x = 300
        y = 300
        img2.thumbnail((x*float(self.sizerate), y*float(self.sizerate)), Image.ANTIALIAS)

        img2 = ImageTk.PhotoImage(img2)

        canvas = tkinter.Canvas(width=600, height=500)
        canvas.pack()
        canvas.place(x=100, y=300)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)

        self.button6 = tk.Button(root, text = '1レコード消去', command=self.delete_one)
        self.button6.pack() 
        self.button6.place(x=700, y=200)

        root.mainloop()


    def prev_image(self,n):
        self.sizevalid=0
    
        img2 = Image.open(n)
        x = 300
        y = 300
        img2.thumbnail((x, y), Image.ANTIALIAS)

        img2 = ImageTk.PhotoImage(img2)

        canvas = tkinter.Canvas(width=600, height=500)
        canvas.pack()
        canvas.place(x=100, y=300)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)


        root.mainloop()
        
    def change_image(self):

        self.sizevalid=0

        for n in filenames:
            img2 = Image.open(n)
            x = 300
            y = 300
            img2.thumbnail((x, y), Image.ANTIALIAS)
            img2 = ImageTk.PhotoImage(img2)
            canvas = tkinter.Canvas(width=600, height=500)
            canvas.place(x=100, y=300)
            item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
            canvas.itemconfig(item,image=img2)
            time.sleep(0.1) 
    def button10_clicked(self):  
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        #filenames = []
        self.dir = 1
        self.filenames = glob.glob('*.jpg')
        print(self.filenames)

    def button15_clicked(self):  
        if(self.dir==0):
            self.textExample.insert(tkinter.END,"jpgが未指定\n")
            return

        thread1 = threading.Thread(target=self.change_image)
        thread1.start()


    def button5_clicked(self):  
        global filenames


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)
        self.filenames=filenames
        self.dir = 1


        for file in self.filenames:
            file_c = file.replace('\\', '\\\\');
       
        self.prev_image(file_c)

        
        
    def get_index(self,event):
    
        value = tkinter.StringVar()
 
        item_index = self.listbox.curselection()
        # リストが１つ以上選択されている場合だけ処理
        if len(item_index) > 0:
 
            index = event.widget.curselection()

            n = event.widget.get(index)
            value.set(n)
            self.id=n
            self.jpgread()

    def sizeup(self):
        if(self.sizevalid==1):
            self.sizerate = float(self.sizerate) + 0.1
            self.select_one_image(wf)


    def sizedown(self):
        if(self.sizevalid==1):
            self.sizerate = float(self.sizerate) - 0.1
            self.select_one_image(wf)

   
#=================================================
# main function
#=================================================
if __name__  == '__main__':
    root = tk.Tk()
    mw = main_window(root)
    root.geometry("800x800")  
    root.mainloop();

