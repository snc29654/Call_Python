import tkinter as tk
from tkinter import ttk
from tkinter import font
import threading
import time
import datetime
class top_app(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.master.geometry("300x300")
        self.master.title("Tkinterで秒タイマー")
        self.font_chu = font.Font( family="Meiryo UI", size=15, weight="bold" )
        self.font_sho = font.Font( family="Meiryo UI", size=12, weight="normal" )
        self.make_frame()
        self.started = threading.Event() 
        self.alive = True 
        self._kaishi_th_top()
    def make_frame(self):
        # テキストボックス
        #ウイジット作成　部品のこと
        self.txt = tk.Entry(width=5)
        #場所決め
        self.txt.place(x=100, y=5)
        #文字初期値挿入
        self.txt.insert(tk.END,"10")
        self.lbl = tk.Label(text='タイマー秒')
        self.lbl.place(x=20, y=5)

        self.main_frame = tk.LabelFrame( self.master, text='', font=self.font_sho )
        self.main_frame.place( x=25, y=25 )
        self.main_frame.configure( height=250, width=250 )
        self.main_frame.grid_propagate( 0 )
        self.main_frame.grid_columnconfigure( 0, weight=1 )
        self.btn_Start = ttk.Button(self.main_frame)
        self.btn_Start.configure(text ='開始')
        self.btn_Start.configure(command = self._kaishi)
        self.btn_Start.grid(column = 0, row = 0, padx=10, pady = 10,sticky='NESW' )
        self.btn_Stop = ttk.Button(self.main_frame)
        self.btn_Stop.configure(text = '停止')
        self.btn_Stop.configure(command = self._teishi)
        self.btn_Stop.grid(column = 0, row = 1, padx=10, pady = 10,sticky='NESW')
        self.lable_st = ttk.Label(self.main_frame)
        self.lable_st.configure(text = '開始で時刻が表示')
        self.lable_st.grid(column = 0, row = 2, padx= 30, pady=10,sticky='NESW')
        self.btn_Kill = ttk.Button(self.main_frame)
        self.btn_Kill.configure(text = '終了')
        self.btn_Kill.configure(command = self._end_th)
        self.btn_Kill.grid(column=0, row=3, padx = 10, pady=20,sticky='NESW')
    def _kaishi(self):
        self.stop = 0
        self.get_data =self.txt.get()
        self.started.set()
    def _teishi(self):
        self.stop = 1
        self.started.clear()
    def _kaishi_th_top(self):
        self.thread_main = threading.Thread(target=self._main_func)
        self.thread_main.start()
        #2020.11.14  beep音追加
    def _end_th(self):
        if self.started.is_set() == False:
            self.started.set()
            self.alive = False
            self.thread_main.join()
        else:
            self._teishi()
            self.started.set()
            self.alive = False
    def _main_func(self):
        self.started.wait()
        jikan = 0
        while self.alive:
            if jikan != int(self.get_data):
                print(self.get_data)
                jikan=jikan + 1
                print(jikan)
                time.sleep(1)
                print( "{}\r".format(jikan), end="" )
                self.lable_st.configure( text=jikan ,font = self.font_sho)
            else:
                #self.lable_st.configure( text= '停止しました' ,font = self.font_chu)
                while(1):
                    if self.stop == 1:
                        jikan = 0
                        break
                    print("\007")
                    time.sleep(1)
                self.started.wait()
        pass
def main():
    root = tk.Tk()
    app = top_app(master=root)
    app.mainloop()
if __name__ == "__main__":
    main()
