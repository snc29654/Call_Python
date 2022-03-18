######　　2021.05．25　文字なしで空白を出力　######################################################
import tkinter
import json
import sqlite3
from contextlib import closing
dbname = '../ejdict.sqlite3'


root = tkinter.Tk()
def input_key(event):
    btn_click(event.keysym)

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)

textExample=tkinter.Text(root, height=10)
textExample.pack()
textExample.place(x=90, y=40)

# clickイベント
def btn_click(key):
    if key == "BackSpace":#最後の一文字
        get_data =txt.get()
        print(get_data[:-1])

        get_data =get_data[:-1]
    else:

        get_data =txt.get() + key
    match_word = get_data
    if match_word =="":
        textExample.delete("1.0",tkinter.END)
        return

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table items (item_id INTEGER PRIMARY KEY,word TEXT,mean TEXT,level INTEGER DEFAULT 0)'''
        try:
            c.execute(create_table)
        except:
            print("database already exist")

        #全レコード表示

        select_sql = 'select * from items where word = '+'"'+str(match_word)+'"'

        data=[]
        print (select_sql )
        try:

            for row in c.execute(select_sql):
                print(row)
                data.append(row)

            conn.commit()

        except:

            print("data not found")

    textExample.delete("1.0",tkinter.END)

    textExample.insert(tkinter.END,data)
# ボタン
btn = tkinter.Button(root, text='引く', command=btn_click)
btn.place(x=10, y=80)
# 画面サイズ
root.geometry('700x200')
# 画面タイトル
root.title('英和辞書')
# ラベル
lbl = tkinter.Label(text='英単語')
lbl.place(x=10, y=10)

lbl2 = tkinter.Label(text='意味')
lbl2.place(x=10, y=50)

# テキストボックス
txt = tkinter.Entry(width=20)
txt.place(x=90, y=10)
txt.insert(tkinter.END,"")

txt.pack()
txt.bind("<KeyPress>", input_key)
txt.focus_set()

# 表示
root.mainloop()
