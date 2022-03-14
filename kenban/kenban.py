import tkinter
import threading
from contextlib import closing
root = tkinter.Tk()
from winsound import Beep
from time import sleep
from tkinter import ttk
BASE = 300
m_index = 0
dlist = []
 

s = ttk.Style()
s.theme_use('classic')
s.configure('MyWidget.TButton', background='#ffffcc')


def Play_Hz(Hz):
    Beep(Hz, 400)
def Play_Hz_1000(Hz):
    Beep(Hz, 1000)
#ここからGUI
def btn_click1():
    set_m(0)
    Play_Hz(523)
    txt.insert(tkinter.END,u'ド')
def btn_click1u():
    set_m(1)
    Play_Hz(554)
    txt.insert(tkinter.END,u'ド#')

def btn_click2():
    set_m(2)
    Play_Hz(587)
    txt.insert(tkinter.END,u'レ')
def btn_click2u():
    set_m(3)
    Play_Hz(622)
    txt.insert(tkinter.END,u'レ#')
def btn_click3():
    set_m(4)
    Play_Hz(659)
    txt.insert(tkinter.END,u'ミ')
def btn_click4():
    set_m(5)
    Play_Hz(698)
    txt.insert(tkinter.END,u'ファ')
def btn_click4u():
    set_m(6)
    Play_Hz(740)
    txt.insert(tkinter.END,u'ファ#')
def btn_click5():
    set_m(7)
    Play_Hz(784)
    txt.insert(tkinter.END,u'ソ')
def btn_click5u():
    set_m(8)
    Play_Hz(831)
    txt.insert(tkinter.END,u'ソ#')
def btn_click6():
    set_m(9)
    Play_Hz(880)
    txt.insert(tkinter.END,u'ラ')
def btn_click6u():
    set_m(10)
    Play_Hz(932)
    txt.insert(tkinter.END,u'ラ#')
def btn_click7():
    set_m(11)
    Play_Hz(988)
    txt.insert(tkinter.END,u'シ')
def btn_click8():
    set_m(12)
    Play_Hz(1047)
    txt.insert(tkinter.END,u'ド')
def btn_click8u():
    set_m(13)
    Play_Hz(1109)
    txt.insert(tkinter.END,u'ド#')

def btn_click1_1000():
    set_m(14)
    Play_Hz_1000(523)
    txt.insert(tkinter.END,u'ド')
def btn_click1u_1000():
    set_m(15)
    Play_Hz_1000(554)
    txt.insert(tkinter.END,u'ド#')

def btn_click2_1000():
    set_m(16)
    Play_Hz_1000(587)
    txt.insert(tkinter.END,u'レ')
def btn_click2u_1000():
    set_m(17)
    Play_Hz_1000(622)
    txt.insert(tkinter.END,u'レ#')
def btn_click3_1000():
    set_m(18)
    Play_Hz_1000(659)
    txt.insert(tkinter.END,u'ミ')
def btn_click4_1000():
    set_m(19)
    Play_Hz_1000(698)
    txt.insert(tkinter.END,u'ファ')
def btn_click4u_1000():
    set_m(20)
    Play_Hz_1000(740)
    txt.insert(tkinter.END,u'ファ#')
def btn_click5_1000():
    set_m(21)
    Play_Hz_1000(784)
    txt.insert(tkinter.END,u'ソ')
def btn_click5u_1000():
    set_m(22)
    Play_Hz_1000(831)
    txt.insert(tkinter.END,u'ソ#')
def btn_click6_1000():
    set_m(23)
    Play_Hz_1000(880)
    txt.insert(tkinter.END,u'ラ')
def btn_click6u_1000():
    set_m(24)
    Play_Hz_1000(932)
    txt.insert(tkinter.END,u'ラ#')
def btn_click7_1000():
    set_m(25)
    Play_Hz_1000(988)
    txt.insert(tkinter.END,u'シ')
def btn_click8_1000():
    set_m(26)
    Play_Hz_1000(1047)
    txt.insert(tkinter.END,u'ド')
def btn_click8u_1000():
    set_m(27)
    Play_Hz_1000(1109)
    txt.insert(tkinter.END,u'ド#')



def set_m(mmm):
    global m_index
    dlist[m_index]=mmm
    m_index +=1
def btn_click9():
    thread1 = threading.Thread(target=replay,args=("one",))
    thread1.start()
def btn_click10():
    thread1 = threading.Thread(target=replay,args=("cont",))
    thread1.start()
def btn_click11():
    elise = [7,6,7,6,7,2,5,3,14,14]
    for i in range(10):
        dlist[i]=elise[i]
    global m_index
    m_index=10
    thread1 = threading.Thread(target=replay,args=("one",))
    thread1.start()
def btn_click12():
    elise = [0,2,18,2,0,0,2,4,2,0,16]
    for i in range(11):
        dlist[i]=elise[i]
    global m_index
    m_index=11
    thread1 = threading.Thread(target=replay,args=("one",))
    thread1.start()

def replay(param):
    global m_index
    key_count = 0;
    for v in dlist:
        key_count +=1
        #鍵盤を押下数でやめる
        print(v)
        if v == 0:
            Play_Hz(523)
            txt2.insert(tkinter.END,u'ド')
        if v == 1:
            Play_Hz(554)
            txt2.insert(tkinter.END,u'ド#')
        if v == 2:
            Play_Hz(587)
            txt2.insert(tkinter.END,u'レ')
        if v == 3:
            Play_Hz(622)
            txt2.insert(tkinter.END,u'レ#')
        if v == 4:
            Play_Hz(659)
            txt2.insert(tkinter.END,u'ミ')
        if v == 5:
            Play_Hz(698)
            txt2.insert(tkinter.END,u'ファ')
        if v == 6:
            Play_Hz(740)
            txt2.insert(tkinter.END,u'ファ#')
        if v == 7:
            Play_Hz(784)
            txt2.insert(tkinter.END,u'ソ')
        if v == 8:
            Play_Hz(831)
            txt2.insert(tkinter.END,u'ソ#')
        if v == 9:
            Play_Hz(880)
            txt2.insert(tkinter.END,u'ラ')
        if v == 10:
            Play_Hz(932)
            txt2.insert(tkinter.END,u'ラ#')
        if v == 11:
            Play_Hz(988)
            txt2.insert(tkinter.END,u'シ')
        if v == 12:
            Play_Hz(1047)
            txt2.insert(tkinter.END,u'ド')
        if v == 13:
            Play_Hz(1109)
            txt2.insert(tkinter.END,u'ド#')
        if v == 14:
            Play_Hz_1000(523)
            txt2.insert(tkinter.END,u'ド-')
        if v == 15:
            Play_Hz_1000(554)
            txt2.insert(tkinter.END,u'ド#-')
        if v == 16:
            Play_Hz_1000(587)
            txt2.insert(tkinter.END,u'レ-')
        if v == 17:
            Play_Hz_1000(622)
            txt2.insert(tkinter.END,u'レ#-')
        if v == 18:
            Play_Hz_1000(659)
            txt2.insert(tkinter.END,u'ミ-')
        if v == 19:
            Play_Hz_1000(698)
            txt2.insert(tkinter.END,u'ファ-')
        if v == 20:
            Play_Hz_1000(740)
            txt2.insert(tkinter.END,u'ファ-#')
        if v == 21:
            Play_Hz_1000(784)
            txt2.insert(tkinter.END,u'ソ-')
        if v == 22:
            Play_Hz_1000(831)
            txt2.insert(tkinter.END,u'ソ-#')
        if v == 23:
            Play_Hz_1000(880)
            txt2.insert(tkinter.END,u'ラ-')
        if v == 24:
            Play_Hz_1000(932)
            txt2.insert(tkinter.END,u'ラ#-')
        if v == 25:
            Play_Hz_1000(988)
            txt2.insert(tkinter.END,u'シ-')
        if v == 26:
            Play_Hz_1000(1047)
            txt2.insert(tkinter.END,u'ド-')
        if v == 27:
            Play_Hz_1000(1109)
            txt2.insert(tkinter.END,u'ド#-')
        if m_index == key_count:
            break
    if param == "cont":
        replay(param)    
#リストを100個で初期化            
dlist = [i for i in range(100)]
btn1 = ttk.Button(root, text='ド', command=btn_click1, width=2 ,style='MyWidget.TButton')
btn1.place(x=100, y=30)
btn2 = ttk.Button(root, text='レ', command=btn_click2, width=2 ,style='MyWidget.TButton')
btn2.place(x=150, y=30)
btn3 = ttk.Button(root, text='ミ', command=btn_click3, width=2 ,style='MyWidget.TButton')
btn3.place(x=200, y=30)
btn4 = ttk.Button(root, text='ファ', command=btn_click4, width=3 ,style='MyWidget.TButton')
btn4.place(x=250, y=30)
btn5 = ttk.Button(root, text='ソ', command=btn_click5, width=2 ,style='MyWidget.TButton')
btn5.place(x=300, y=30)
btn6 = ttk.Button(root, text='ラ', command=btn_click6, width=2 ,style='MyWidget.TButton')
btn6.place(x=350, y=30)
btn7 = ttk.Button(root, text='シ', command=btn_click7, width=2 ,style='MyWidget.TButton')
btn7.place(x=400, y=30)
btn8 = ttk.Button(root, text='ド', command=btn_click8, width=2 ,style='MyWidget.TButton')
btn8.place(x=450, y=30)

btn1u = tkinter.Button(root, text='ド#', command=btn_click1u, width=3)
btn1u.place(x=110, y=5)
btn2u = tkinter.Button(root, text='レ#', command=btn_click2u, width=3)
btn2u.place(x=160, y=5)
btn4u = tkinter.Button(root, text='ファ#', command=btn_click4u, width=3)
btn4u.place(x=260, y=5)
btn5u = tkinter.Button(root, text='ソ#', command=btn_click5u, width=3)
btn5u.place(x=310, y=5)
btn6u = tkinter.Button(root, text='ラ#', command=btn_click6u, width=3)
btn6u.place(x=360, y=5)
btn8u = tkinter.Button(root, text='ド#', command=btn_click8u, width=3)
btn8u.place(x=460, y=5)

btn1 = tkinter.Button(root, text='ド-', command=btn_click1_1000, width=3)
btn1.place(x=100, y=100)
btn2 = tkinter.Button(root, text='レ-', command=btn_click2_1000, width=3)
btn2.place(x=150, y=100)
btn3 = tkinter.Button(root, text='ミ-', command=btn_click3_1000, width=3)
btn3.place(x=200, y=100)
btn4 = tkinter.Button(root, text='ファ-', command=btn_click4_1000, width=3)
btn4.place(x=250, y=100)
btn5 = tkinter.Button(root, text='ソ-', command=btn_click5_1000, width=3)
btn5.place(x=300, y=100)
btn6 = tkinter.Button(root, text='ラ-', command=btn_click6_1000, width=3)
btn6.place(x=350, y=100)
btn7 = tkinter.Button(root, text='シ-', command=btn_click7_1000, width=3)
btn7.place(x=400, y=100)
btn8 = tkinter.Button(root, text='ド-', command=btn_click8_1000, width=3)
btn8.place(x=450, y=100)

btn1u = tkinter.Button(root, text='ド#-', command=btn_click1u_1000, width=3)
btn1u.place(x=110, y=75)
btn2u = tkinter.Button(root, text='レ#-', command=btn_click2u_1000, width=3)
btn2u.place(x=160, y=75)
btn4u = tkinter.Button(root, text='ファ#-', command=btn_click4u_1000, width=3)
btn4u.place(x=260, y=75)
btn5u = tkinter.Button(root, text='ソ#-', command=btn_click5u_1000, width=3)
btn5u.place(x=310, y=75)
btn6u = tkinter.Button(root, text='ラ#-', command=btn_click6u_1000, width=3)
btn6u.place(x=360, y=75)
btn8u = tkinter.Button(root, text='ド#-', command=btn_click8u_1000, width=3)
btn8u.place(x=460, y=75)




btn9 = tkinter.Button(root, text='再生', command=btn_click9, width=3)
btn9.place(x=500, y=10)

btn10 = tkinter.Button(root, text='繰り返し再生', command=btn_click10, width=10)
btn10.place(x=550, y=10)

btn11 = tkinter.Button(root, text='エリーゼ', command=btn_click11, width=10)
btn11.place(x=550, y=35)

btn12 = tkinter.Button(root, text='チャルメラ', command=btn_click12, width=10)
btn12.place(x=550, y=55)

txt = tkinter.Entry(width=80)
txt.place(x=90, y=160)
txt2 = tkinter.Entry(width=80)
txt2.place(x=90, y=180)
# 画面サイズ
root.geometry('650x220')
# 画面タイトル
root.title('鍵盤もどき')
# ラベル
#フレームの作成
frame1 = tkinter.Frame()
frame1.pack()
frame1.place(x=90, y=10)
# 表示
root.mainloop()

